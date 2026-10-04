## 2026-10-04 - CSP Configuration for Tesseract.js
**Vulnerability:** Missing Content-Security-Policy allowed potential XSS and data exfiltration in an OCR application.
**Learning:** Implementing CSP for Tesseract.js requires specific allowances: `'wasm-unsafe-eval'` for WebAssembly compilation, `worker-src 'self' blob:` for worker threads, and `connect-src` access to both the library CDN and `https://tessdata.projectnaptha.com` for downloading language models.
**Prevention:** When implementing OCR or heavy client-side processing libraries, proactively verify their network and execution requirements before applying restrictive security policies to avoid functional regressions.
