import os
import mss
import numpy as np
from datetime import datetime
from PIL import Image
import pyautogui


class ScreenshotUtility:
    def __init__(self):
        pass

    @staticmethod
    def save_screenshot_to_file(image, prefix, save_path="logs/images"):
        """
        Saves a given screenshot (Pillow Image) to a file with a timestamped filename.

        Arguments:
        - image (PIL.Image.Image): The screenshot image to save.
        - save_path (str): The directory where the screenshot will be stored (default is 'logs/images').
        """
        # Create the directory if it does not exist
        os.makedirs(save_path, exist_ok=True)

        # Create the timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]  # Keep milliseconds
        # filename = f"{timestamp}_{prefix}.png"
        filename = f"{prefix}_{timestamp}.png"
        full_path = os.path.join(save_path, filename)

        # Save the image file
        image.save(full_path)
        print(f"Screenshot saved to: {full_path}")

    def click_and_screen(self, x, y, tag = "click"):
        """
        Clicks the given coordinates and captures a screenshot for the region.

        Arguments:
        - coords (tuple): A tuple of (x, y, width, height) defining the region to capture.
        - prefix (str): The prefix for the screenshot filename.

        Returns:
        - None
        """
        x_offset = 30
        y_offset = 30

        coords_copy = (x - x_offset, y - y_offset, x_offset * 2, y_offset * 2)

        # Capture and store the screenshot
        self.capture_and_store(coords_copy, tag)

        # Click the coordinates
        pyautogui.click(x, y)
        print(f"Clicked at: ({x}, {y})")

    def capture_and_store(self, coords, prefix):
        """
        Accepts coordinates, captures a screenshot for the region, and saves it.

        Arguments:
        - coords (tuple): A tuple of (x, y, width, height) defining the region to capture.

        Returns:
        - None
        """
        print(f"Capturing screenshot for region: {coords}")

        # Ensure coordinates are provided
        if not isinstance(coords, tuple) or len(coords) != 4:
            raise ValueError("Coordinates must be a tuple with (x, y, width, height).")

        # Convert the coordinate tuple into an mss-compatible region dictionary
        region_dict = {
            "left": int(coords[0]),
            "top": int(coords[1]),
            "width": int(coords[2]),
            "height": int(coords[3])
        }

        # Capture the screenshot using mss
        with mss.mss() as sct:
            screenshot = sct.grab(region_dict)
            screenshot_np = np.array(screenshot)  # Convert the mss capture to NumPy array

            # Convert the screenshot back to a Pillow Image for saving
            screenshot_image = Image.fromarray(screenshot_np)

            # Save the screenshot using the existing save method
            self.save_screenshot_to_file(screenshot_image, prefix)