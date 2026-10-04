## 2024-05-24 - Tesseract.js Worker Reuse Overhead
**Learning:** Tesseract.js's convenience wrapper `Tesseract.recognize()` is deprecated because it creates and destroys a WebWorker (redownloading/re-initializing WebAssembly and language packs) on every single call. This creates a massive performance bottleneck when performing multiple sequential OCR tasks.
**Action:** Always instantiate a reusable worker via `Tesseract.createWorker()` when performing OCR tasks in the browser, and initialize it as early as possible to hide the load time.
