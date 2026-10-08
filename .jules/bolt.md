## 2024-05-24 - Tesseract.js Worker Reuse Overhead
**Learning:** Tesseract.js's convenience wrapper `Tesseract.recognize()` is deprecated because it creates and destroys a WebWorker (redownloading/re-initializing WebAssembly and language packs) on every single call. This creates a massive performance bottleneck when performing multiple sequential OCR tasks.
**Action:** Always instantiate a reusable worker via `Tesseract.createWorker()` when performing OCR tasks in the browser, and initialize it as early as possible to hide the load time.

## 2024-05-24 - FileReader vs URL.createObjectURL
**Learning:** `FileReader.readAsDataURL()` reads the entire file into memory as a base64 string, which is slow and blocks the main thread for large images. `URL.createObjectURL()` is instantaneous as it just creates a pointer. However, the object URL must not be revoked until Tesseract has completely finished recognizing it, because Tesseract fetches the URL asynchronously.
**Action:** Use `URL.createObjectURL` for file inputs instead of `FileReader`, and ensure `URL.revokeObjectURL` is called only after `Tesseract.recognize()` resolves or rejects.
