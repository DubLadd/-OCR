## 2024-10-08 - Content Security Policy (CSP) for Tesseract.js and WebAssembly
**Vulnerability:** Missing Content Security Policy (CSP) allowing any resources to be loaded, putting the application at risk of XSS and other injection attacks.
**Learning:** Adding a CSP for an application using Tesseract.js requires specific directives. It needs 'wasm-unsafe-eval' and 'unsafe-inline' in script-src for WebAssembly execution, 'https://tessdata.projectnaptha.com' in connect-src for language models, and 'blob:' for worker-src and img-src.
**Prevention:** When implementing OCR using Tesseract.js, always include these specific CSP directives to maintain security while allowing the necessary WebAssembly and web worker operations to function correctly.
