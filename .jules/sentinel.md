## 2026-10-05 - Add Content Security Policy
**Vulnerability:** Missing Content Security Policy (CSP)
**Learning:** Web applications should always define a Content Security Policy to prevent XSS and data injection attacks. Given the reliance on Tesseract.js, it needed specific allowances for WebAssembly and external script loading.
**Prevention:** Ensure that a CSP is explicitly defined for any web application, especially those that include external scripts and execute WebAssembly.
