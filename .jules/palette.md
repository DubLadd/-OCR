## 2024-10-08 - Added aria-live to status bar
**Learning:** The dynamic status updates (idle, extracting, complete) were visually distinct but completely invisible to screen readers without aria-live regions.
**Action:** Always add aria-live="polite" and aria-atomic="true" to dynamic status indicators that update asynchronously.
