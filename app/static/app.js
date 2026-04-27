const form = document.getElementById("upload-form");
const input = document.getElementById("image-input");
const styleSelect = document.getElementById("style-select");
const originalImage = document.getElementById("original-image");
const resultImage = document.getElementById("result-image");
const clearButton = document.getElementById("clear-button");
const loadingOverlay = document.getElementById("loading-overlay");
const status = document.getElementById("status");
const submitButton = form.querySelector("button[type='submit']");

let currentOriginalUrl = null;
let currentResultUrl = null;

function setStatus(message, type = "info") {
  status.textContent = message;
  status.style.color = type === "error" ? "#fb7185" : "#9ca3af";
}

function setLoading(isLoading) {
  if (isLoading) {
    loadingOverlay.classList.remove("hidden");
    submitButton.disabled = true;
  } else {
    loadingOverlay.classList.add("hidden");
    submitButton.disabled = false;
  }
}

function clearResults() {
  input.value = "";

  if (currentOriginalUrl) {
    URL.revokeObjectURL(currentOriginalUrl);
    currentOriginalUrl = null;
  }

  if (currentResultUrl) {
    URL.revokeObjectURL(currentResultUrl);
    currentResultUrl = null;
  }

  originalImage.src = "";
  resultImage.src = "";

  setStatus("Results cleared. Upload a new photo to try again.");
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  console.log("Form submitted");

  if (!input.files?.length) {
    setStatus("Please choose an image file.", "error");
    return;
  }

  const file = input.files[0];

  // Validate file type
  if (!file.type.startsWith("image/")) {
    setStatus("Please upload a valid image file.", "error");
    return;
  }

  // Validate file size (max 5MB)
  const MAX_SIZE = 5 * 1024 * 1024;
  if (file.size > MAX_SIZE) {
    setStatus("Image too large. Please upload under 5MB.", "error");
    return;
  }

  console.log("File:", file.name, file.size);

  // Preview original image
  if (currentOriginalUrl) {
    URL.revokeObjectURL(currentOriginalUrl);
  }
  currentOriginalUrl = URL.createObjectURL(file);
  originalImage.src = currentOriginalUrl;

  // Reset result
  resultImage.src = "";
  if (currentResultUrl) {
    URL.revokeObjectURL(currentResultUrl);
    currentResultUrl = null;
  }

  setLoading(true);
  setStatus("Processing... this may take 1–3 minutes.");

  const style = styleSelect ? styleSelect.value : "natural";
  console.log("Selected style:", style);

  const formData = new FormData();
  formData.append("file", file);
  formData.append("style", style);

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 360000); // 3 min

    const url = new URL("/remove-people/", window.location.origin).toString();

    const response = await fetch(url, {
      method: "POST",
      body: formData,
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      let errorMsg = "Server error";
      try {
        const err = await response.json();
        errorMsg = err?.detail || errorMsg;
      } catch {
        errorMsg = await response.text();
      }
      throw new Error(errorMsg);
    }

    const blob = await response.blob();

    if (currentResultUrl) {
      URL.revokeObjectURL(currentResultUrl);
    }

    currentResultUrl = URL.createObjectURL(blob);
    resultImage.src = currentResultUrl;

    setStatus("Done! Compare the images.");
  } catch (error) {
    console.error(error);

    if (error.name === "AbortError") {
      setStatus("Request timed out. Try a smaller image.", "error");
    } else {
      setStatus(error.message || "Processing failed.", "error");
    }
  } finally {
    setLoading(false);
  }
});

clearButton.addEventListener("click", clearResults);

