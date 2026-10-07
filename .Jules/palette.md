## 2024-10-07 - Interactive Dropzone Polish
**Learning:** Custom dropzones acting as input buttons need explicit cursor hints and keyboard accessibility, otherwise screen reader/keyboard users are left stranded since a standard `div` does not expose interactive behavior natively.
**Action:** Always pair `click` listeners on custom interactive `div`s with `role="button"`, `tabindex="0"`, `cursor: pointer`, focus states (`:focus-visible`), and keyboard (`Enter`/`Space`) activation listeners.
