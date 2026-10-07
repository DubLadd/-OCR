from playwright.sync_api import sync_playwright
import time
import os

def test_ocr():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        # Create a context with video recording
        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()

        # Go to the local server
        page.goto("http://localhost:8000")

        # Wait for Tesseract to initialize
        time.sleep(2)

        # Take a screenshot before upload
        page.screenshot(path="screenshot_before.png")

        # Upload the test image
        with page.expect_file_chooser() as fc_info:
            page.click("text=Select Image")
        file_chooser = fc_info.value
        file_chooser.set_files("test_image.png")

        # Wait for OCR to complete (status changes to COMPLETE or ERROR)
        # This might take a few seconds
        page.wait_for_selector("#status-msg:has-text('COMPLETE')", timeout=30000)

        # Take a screenshot after OCR
        page.screenshot(path="screenshot_after.png")

        # Close the browser context to save the video
        context.close()
        browser.close()

if __name__ == "__main__":
    test_ocr()
