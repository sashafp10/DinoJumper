# import pyautogui
# import time

# def locate_and_click_dino_white():
#     try:
#         image_path = r"c:\D\patriot\src\py\DinoChromeGame\dinoJumper\resources\images\dino_white.png"
#         # Using confidence parameter for better matching accuracy (requires OpenCV)
#         location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=0.8)
#         if location:
#             print(f"Image found at: {location}")
#             center = pyautogui.center(location)
#             pyautogui.click(center)
#             return location
#             print(f"Dino clicked: {center}")
#         else:
#             print("White dino not found.")
#             return None
#     except pyautogui.ImageNotFoundException:
#         print("Image not found exception occurred.")
#         return None

# def main():
#     print("Hello, Dino!")
#     time.sleep(2)
#     dino_location = locate_and_click_dino_white()

# import pyautogui
# import cv2
# import numpy as np
# import time
# import keyboard
# import sys

# # Configuration
# game_window_active = False  # Set to True if you want the script to ensure the game window is active
# print("sdscddcsdcscsdc")
# run_duration = 60  # Run duration in seconds (can be set to your desired value)

# # Screenshot region (you may need to adjust these values)
# region = (0, 0, 800, 600)

# # Obstacles coordinates (you may need to fine-tune these values for optimal performance)
# dino_coords = (300, 530)
# jump_coords = (400, 330)
# duck_coords = (500, 330)

# # Variable to count Esc keys pressed
# esc_press_count = 0

# # Function to activate game window
# def activate_game_window():
#     print("Activating window...")
#     dino_screen = pyautogui.screenshot(region=region)
#     dino_screen_np = np.array(dino_screen)
#     dino_gray = cv2.cvtColor(dino_screen_np, cv2.COLOR_BGR2GRAY)
#     res = cv2.matchTemplate(dino_gray, dino_template, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     dino_start = max_loc
#     pyautogui.click(dino_start[0] + region[0], dino_start[1] + region[1])
#     game_window_active = True
#     time.sleep(0.1)
#     pyautogui.press('space')

# # Function to handle Esc key press
# def on_esc_press(event):
#     global esc_press_count
#     if event.name == 'esc':
#         print("Esc key pressed " + str(esc_press_count) + " times")
#         esc_press_count += 1
#         if esc_press_count >= 5:
#             print("Esc key pressed 5 times. Terminating.")
#             sys.exit()

# # Register the Esc key press event
# keyboard.on_press(on_esc_press)

# # Load dino template
# dino_image = cv2.imread(r"c:\D\patriot\src\py\DinoChromeGame\dinoJumper\resources\images\dino_white.png", 0)
# if dino_image is None:
#     print("Please take a screenshot of the dino in the game and save it as 'dino.png'")
#     sys.exit()

# dino_template = dino_image

# # Activate the window initially
# if game_window_active == False:
#     print("AAA") 
#     activate_game_window()

# # Main game loop
# start_time = time.time()  # Record the start time

# try:
#     while True:
#         print('.', end='')
#         # Ensure the game window is active
#         print("space 1: " + str(game_window_active))
#         if game_window_active == False:
#             print("FFF")
#             activate_game_window()
        
#         # Take a screenshot of the specified region
#         screen = pyautogui.screenshot(region=region)
#         screen_np = np.array(screen)
#         screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
#         # Detect obstacles
#         res = cv2.matchTemplate(screen_gray, dino_template, cv2.TM_CCOEFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
#         # Calculate obstacle coordinates
#         obstacle_location = (max_loc[0] + region[0], max_loc[1] + region[1])
        
#         # Perform jump based on obstacle coordinates
#         if obstacle_location[0] > dino_coords[0] and obstacle_location[0] < jump_coords[0]:
#             print("Hit space")
#             pyautogui.press('space')
        
#         time.sleep(0.05)

# except KeyboardInterrupt:
#     print("Bot stopped by user")

# finally:
#     keyboard.unhook_all()  # Remove all keyboard hooks when the script exits












# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QPainter, QColor, QPen

# class Overlay(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Get screen resolution
#         screen_resolution = QApplication.primaryScreen().size()
#         width, height = screen_resolution.width(), screen_resolution.height()

#         # Set position and size of the window
#         self.setGeometry(0, 0, width, height)
        
#         # Set window flags to create a transparent window
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#         # Set timer to close the window
#         QTimer.singleShot(2000, self.close)  # Close after 2 seconds

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         try:
#             # Set up pen
#             pen = QPen(QColor(255, 0, 0))
#             pen.setWidth(20)  # 10-pixel-wide border
#             painter.setPen(pen)

#             # Draw rectangle
#             rect_x, rect_y, rect_width, rect_height = 100, 100, 200, 200
#             print("Draw...")
#             painter.drawRect(rect_x, rect_y, rect_width, rect_height)
#             print("Drawn")
#         finally:
#             painter.end()

#     def closeEvent(self, event):
#         print("Closing...")
#         app.quit()  # Ensure the application quits when the overlay window is closed

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Create and show the overlay
#     overlay = Overlay()
#     overlay.show()

#     # Ensure the application terminates when the window is closed
#     app.exec_()  # Run the application's event loop
#     print("Overlay application closed.")
#     sys.exit()

# def is_cactus_present():
#     """
#     Check if a cactus is present in the game region.
#     Returns True if detected beyond the jump distance.
#     """
#     img = ImageGrab.grab(bbox=game_region)
#     pixels = img.load()
    
#     # Start checking from 'jump_distance' pixels from the right edge moving left
#     width = img.size[0]
#     for x in range(width - jump_distance, 0, -1):
#         # Check pixel at height where cactus base appears
#         # Adjust y based on the game's ground level (here, ~50% of image height)
#         y = int(img.size[1] * 0.5)
#         pixel = pixels[x, y]
#         if pixel == cactus_color:
#             return True
#     return False

# def play_game():
#     print("Starting Dino game bot. Press 'q' to quit.")
#     time.sleep(5)  # Time to switch to the game window
    
#     # Initial jump to start the game
#     pyautogui.press('space')
    
#     while True:
#         if keyboard.is_pressed('q'):
#             print("Bot stopped by user.")
#             break
#         if is_cactus_present():
#             pyautogui.press('space')
#         time.sleep(0.02)  # Adjust speed to prevent high CPU usage

# # if __name__ == "__main_ _":
# # Create and show the overlay
# #play_game()


# main.py
from datetime import datetime
import os
import shutil
import threading
import winsound
from PIL import Image

import cv2
import numpy as np
import pyautogui
from screenshot_utils import ScreenshotUtility
from keyboard_listener import KeyboardListener

import pyautogui
import cv2
import numpy as np
import time
import keyboard
import sys

import mss


import pygetwindow as gw  # For locating the window

# pyautogui.FAILSAFE = False

def make_beep():
    frequency = 1000  # Set Frequency To 1000 Hertz
    duration = 500  # Set Duration To 500 ms == 0.5 second
    winsound.Beep(frequency, duration)

def save_screenshot_to_file(image, prefix):
    # Create the logs/images directory if it doesn't exist
    save_path = os.path.join("logs", "images")
    os.makedirs(save_path, exist_ok=True)

    # Create the timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]  # Keep microseconds to 3 digits (milliseconds)
    filename = f"{timestamp}_{prefix}.png"
    full_path = os.path.join(save_path, filename)

    # Save the image file using Pillow
    image.save(full_path)
    print(f"    Screenshot saved to: {full_path}")

    
class MainApp:

    # Configuration
    game_window_active = False  # Set to True if you want the script to ensure the game window is active

    # Window region, updated on start
    region = (0, 0, 800, 600)

    # Dino coords will be updated in future. Height is const
    dino_coords = (300, 530)
    dino_height = 43;   # Real height is 52

    jump_coords = (400, 330)
    duck_coords = (500, 330)

    # Load dino template
    dino_image = cv2.imread(r"c:\D\patriot\src\py\DinoChromeGame\dinoJumper\resources\images\dino_white.png", 0)
    if dino_image is None:
        print("Please take a screenshot of the dino in the game and save it as 'dino.png'")
        sys.exit()

    dino_template = dino_image

    game_window_active = False

    screenshot_utility = ScreenshotUtility()

    def clear_logs_images(self):
        """
        Clears the logs/images directory.
        """
        save_path = os.path.join("logs", "images")
        if os.path.exists(save_path):
            for filename in os.listdir(save_path):
                file_path = os.path.join(save_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        else:
            os.makedirs(save_path, exist_ok=True)

        print(f"    Cleared files in directory: {save_path}")

    def locate_chrome_window(self):
        """
        Locate the window and save it's coords
        """
        print("    Locating Chrome window...")
        window_list = gw.getWindowsWithTitle("Chrome")  # Finds windows with "Chrome" in title
        if not window_list:
            raise Exception("Chrome window not found! Please open Chrome and ensure it is visible.")

        chrome_window = window_list[0]  # Assume first match is the desired one
        print(f"    Found Chrome window: {chrome_window.title}")

        # Store the region (x, y, width, height)
        x, y, width, height = chrome_window.left, chrome_window.top, chrome_window.width, chrome_window.height
        self.region = (x, y, width, height)  # Save as tuple
        print(f"Chrome window located at: {self.region}")

    def activate_game_window(self):
        if not self.region:
            raise Exception("Region for Chrome is not set! Please call locate_chrome_window() first.")
        
        print("    Activating game window with mss...")

        # Define the region for capturing
        region_dict = {
            "left": self.region[0],
            "top": self.region[1],
            "width": self.region[2],
            "height": self.region[3]
        }

        # Use mss to take a screenshot in the given region
        with mss.mss() as sct:
            screenshot = sct.grab(region_dict)  # Captures the specified region
            dino_screen_np = np.array(screenshot)  # Convert the mss capture to a NumPy array

        # Convert screenshot to grayscale and process it
        dino_gray = cv2.cvtColor(dino_screen_np, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(dino_gray, self.dino_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        dino_start = max_loc

        # Simulate clicking on the found location within the game region
        pyautogui.click(dino_start[0] + self.region[0], dino_start[1] + self.region[1])

        # Save the screenshot to a file for debugging/logging
        save_screenshot_to_file(Image.fromarray(cv2.cvtColor(dino_screen_np, cv2.COLOR_BGR2RGB)), "main")

        # Simulate a space bar press to start the game
        time.sleep(0.1)
        #pyautogui.press('space')

    def locate_and_click_dino_white(self):
        """
        Locate the white dino in the game window, store its coords and click on it.
        """
        try:
            image_path = r"resources\images\dino_white.png"
            print("    Attempting to locate dino...")

            # Load the template image (dino_white.png)
            dino_template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if dino_template is None:
                print(f"Error: Unable to read the template image from {image_path}")
                return None

            # Define the region for the screenshot (if set) or take a full-screen shot
            region_dict = None
            if self.region:
                region_dict = {
                    "left": self.region[0],
                    "top": self.region[1],
                    "width": self.region[2],
                    "height": self.region[3],
                }

            # Take a screenshot using mss
            with mss.mss() as sct:
                screenshot = sct.grab(region_dict) if region_dict else sct.grab(sct.monitors[0])
                screenshot_np = np.array(screenshot)  # Convert mss capture to NumPy array
                screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

            # Perform template matching
            result = cv2.matchTemplate(screen_gray, dino_template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Check if match confidence is above the threshold
            confidence_threshold = 0.8
            if max_val >= confidence_threshold:
                print(f"Dino template matched with confidence: {max_val}")

                # Calculate the center point of the matched location
                (template_height, template_width) = dino_template.shape[:2]
                target_x = max_loc[0] + (template_width // 2)
                target_y = max_loc[1] + (template_height // 2)

                self.dino_coords = (int(target_x - template_width / 2 + self.region[0]),
                                    int(target_y - self.dino_height / 2 + self.region[1]))
                
                screenshot_coords = (self.dino_coords[0],
                                     self.dino_coords[1],
                                     template_width,
                                     self.dino_height)
                self.screenshot_utility.capture_and_store(screenshot_coords, "dino")

                # Save the click position
                self.last_click_coords = (target_x + self.region[0], target_y + self.region[1])

                # Click the center of the matched location
                # pyautogui.click(self.last_click_coords[0], self.last_click_coords[1])
                self.screenshot_utility.click_and_screen(self.last_click_coords[0], self.last_click_coords[1])
                print(f"    Dino clicked at: {self.last_click_coords}")

                # Return location for further use
                return max_loc
            else:
                print("No match found for the white dino.")
                return None

        except Exception as e:
            print(f"An error occurred while locating the dino: {e}")
            return None
        
    def is_game_over(self):
        """
        Check if the game is over by looking for game over images.
        If detected, wait for 2 seconds and hit Ctrl+F5.
        """
        try:
            image_paths = [
                r"resources\images\gameover.png",
                r"resources\images\gameover_n.png"
            ]

            for image_path in image_paths:
                # Load the template image
                gameover_template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                if gameover_template is None:
                    print(f"Error: Unable to read the template image from {image_path}")
                    continue

                # Define the region for the screenshot (if set) or take a full-screen shot
                region_dict = None
                if self.region:
                    region_dict = {
                        "left": self.region[0],
                        "top": self.region[1],
                        "width": self.region[2],
                        "height": self.region[3],
                    }

                # Take a screenshot using mss
                with mss.mss() as sct:
                    screenshot = sct.grab(region_dict) if region_dict else sct.grab(sct.monitors[0])
                    screenshot_np = np.array(screenshot)  # Convert mss capture to NumPy array
                    screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

                # Perform template matching
                result = cv2.matchTemplate(screen_gray, gameover_template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                # Check if match confidence is above the threshold
                confidence_threshold = 0.8
                if max_val >= confidence_threshold:
                    print(f"GameOver template matched with confidence: {max_val}")
                    # Wait for 2 seconds
                    time.sleep(2)
                    # Hit Ctrl+F5
                    pyautogui.hotkey('ctrl', 'f5')
                    return True

            return False

        except Exception as e:
            print(f"An error occurred while checking for game over: {e}")
            return False
    
    def react_obsticle(self):
        """
        Make an action if an obstacle is detected in any predefined regions
        """
        #for obstacle_region in self.obstacle_regions:  # Iterate over the predefined coordinate sets
        if self.is_obstacle_detected(self.obstacle_regions[0]):  # Pass the region tuple directly
            # DEBUG
            # print("    Obstacle detected")
            self.jump()
            return
            
    def is_obstacle_detected(self, obstacle_region):
        """
        Detects if an obstacle is present in the specified region using the mss library.

        Arguments:
            obstacle_region (tuple): A tuple of (x, y, width, height) defining the region to check for obstacles.

        Returns:
            bool: True if an obstacle is detected; False otherwise.
        """
        # DEBUG
        # print(".", end="")

        # Convert obstacle_region into a dictionary compatible with mss
        region_dict = {
            "left": obstacle_region[0],
            "top": obstacle_region[1],
            "width": obstacle_region[2],
            "height": obstacle_region[3]
        }

        # Capture the screenshot for the specified region using mss
        with mss.mss() as sct:
            screenshot = sct.grab(region_dict)
            screenshot_np = np.array(screenshot)  # Convert mss screenshot to a NumPy array

        # self.move_mouse_to_coords(obstacle_region[0], obstacle_region[1])

        # Convert the screenshot to a Pillow Image and grayscale
        image = Image.fromarray(screenshot_np).convert('L')

        # Get the pixel intensity range (extrema)
        extrema = image.getextrema()
        res = extrema[0] == extrema[1]

        # DEBUG
        # if not res:
        #     self.save_screenshot(screenshot_np, "obstacle")

        # Check if all pixels have the same intensity (no obstacle detected)
        return not res 
    
    def save_screenshot(self, screenshot_np, prefix):
        """
        Saves the given screenshot (NumPy array) to a file with a timestamped filename.

        Arguments:
        - screenshot_np (np.array): The screenshot image to save.
        - prefix (str): The prefix for the screenshot filename.
        """
        # Convert the screenshot to a Pillow Image
        screenshot_image = Image.fromarray(screenshot_np)

        # Create the logs/images directory if it doesn't exist
        save_path = os.path.join("logs", "images")
        os.makedirs(save_path, exist_ok=True)

        # Create the timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]  # Keep milliseconds
        filename = f"{prefix}_{timestamp}.png"
        full_path = os.path.join(save_path, filename)

        # Save the image file
        screenshot_image.save(full_path)
        print(f"Screenshot saved to: {full_path}")

    def move_mouse_to_coords(self, x, y):
        """
        Moves the mouse pointer to the specified coordinates.

        Arguments:
        - x (int): The x-coordinate to move the mouse pointer to.
        - y (int): The y-coordinate to move the mouse pointer to.
        """
        pyautogui.moveTo(x, y)
        # print(f"Mouse moved to: ({x}, {y})")

    last_speed = 0;
    
    def measure_speed(self):
        """
        Measures the speed by taking two screenshots and finding the matching pattern.
        """
        while not self._exit_requested:
            # Take the first screenshot
            with mss.mss() as sct:
                screenshot1 = sct.grab(self.speed_coords)
                screenshot1_np = np.array(screenshot1)

            time_span = 0.1
            # Wait for 0.05 seconds
            time.sleep(time_span)

            # Take the second screenshot
            with mss.mss() as sct:
                screenshot2 = sct.grab(self.speed_coords)
                screenshot2_np = np.array(screenshot2)

            # Convert screenshots to grayscale
            screenshot1_gray = cv2.cvtColor(screenshot1_np, cv2.COLOR_BGR2GRAY)
            screenshot2_gray = cv2.cvtColor(screenshot2_np, cv2.COLOR_BGR2GRAY)

            # Define the region to match (30% of the end of the first image)
            height, width = screenshot1_gray.shape
            match_region = screenshot1_gray[:, int(width * 0.8):]

            # Perform template matching
            result = cv2.matchTemplate(screenshot2_gray, match_region, cv2.TM_CCOEFF_NORMED)
            _, _, _, max_loc = cv2.minMaxLoc(result)

            # Calculate the shift in pixels
            shift_in_pixels = self.speed_coords["width"] - max_loc[0]
            
            if self.last_speed == 0 and shift_in_pixels < self.speed_coords["width"]:
                self.last_speed = shift_in_pixels

            # # Calculate the speed (pixels per second)
            #speed = shift_in_pixels / time_span
            # print(f"Speed: {speed} pixels/second")

            # DEBUG
            #if self.speed_counter % 10 == 0:
            #print(f"Speed: {speed} pixels / second")

            coef_correction = 70
            # Update self.obstacle_regions[0] safely
            # if shift_in_pixels < self.speed_coords["width"]:
            #     with self.lock:
            #         correction = shift_in_pixels + coef_correction - self.x_correction
            #         # print(f"Corretion: {correction} pixels. Total: {self.x_correction}")
            #         if correction > 0:
            #             correction = int(max(correction ** 1.35, 0))
            #             self.x_correction += correction
            #             print(f"Corretion2: {correction} pixels. Total2: {self.x_correction}")
            #             self.obstacle_regions[0] = (self.dino_coords[0] + self.x_correction,
            #                                         self.dino_coords[1],
            #                                         40,
            #                                         self.dino_height - self.y_correction)
            #             self.move_mouse_to_coords(self.obstacle_regions[0][0], self.obstacle_regions[0][1])

            # # if shift_in_pixels < self.speed_coords["width"] and self.last_speed < shift_in_pixels:
            # #     with self.lock:
            # #         correction = int((shift_in_pixels - self.last_speed) * 1.2)
            # #         self.x_correction += correction
            # #         print(f"Corretion2: {correction} pixels. Total2: {self.x_correction}")
            # #         self.obstacle_regions[0] = (self.dino_coords[0] + self.x_correction,
            # #                                     self.dino_coords[1],
            # #                                     40,
            # #                                     self.dino_height - self.y_correction)
            # #         self.move_mouse_to_coords(self.obstacle_regions[0][0], self.obstacle_regions[0][1])
            # #         self.last_speed = shift_in_pixels

            if shift_in_pixels < self.speed_coords["width"] and self.last_speed < shift_in_pixels:
                with self.lock:
                    self.x_correction = max(int(coef_correction + shift_in_pixels + self.x_correction / 20), self.x_correction)
                    print(f"Corretion: {self.x_correction} pixels")
                    self.obstacle_regions[0] = (self.dino_coords[0] + self.x_correction,
                                                self.dino_coords[1],
                                                40,
                                                self.dino_height - self.y_correction)
                    self.move_mouse_to_coords(self.obstacle_regions[0][0], self.obstacle_regions[0][1])
                    self.last_speed = shift_in_pixels

            time.sleep(4)  # Simulate doing work in the loop



    def jump(self):
        current_time = time.time()
        time_since_last_jump = current_time - self.last_jump_time

        if time_since_last_jump < 0.15:
            time_to_wait = 0.15 - time_since_last_jump
            time.sleep(time_to_wait + 0.03)  # Add a small buffer

        # print("J", end="")
        # pyautogui.press('space')
        pyautogui.press('up')
        self.last_jump_time = time.time()
    
    def __init__(self):
        self._keyboard_listener = KeyboardListener()
        self._exit_requested = False

        # Start keyboard listener in a separate thread
        self._listener_thread = threading.Thread(target=self._keyboard_listener.start_listening)
        self._listener_thread.start()
                
        # Create a lock for thread-safe operations
        self.lock = threading.Lock()

    def run(self):
        # Start keyboard listener in a separate thread
        self._listener_thread = threading.Thread(target=self._keyboard_listener.start_listening)
        self._listener_thread.start()

        # Initialize the last jump time
        self.last_jump_time = 0

        self.clear_logs_images()
        
        self.locate_chrome_window()

        if self.game_window_active == False:
            self.activate_game_window()

        self.locate_and_click_dino_white()

        self.y_correction = 6;
        self.x_correction = 190
        obstacle_width = 30
        self.obstacle_regions = [
            (self.dino_coords[0] + self.x_correction,
             self.dino_coords[1],
             obstacle_width,
             self.dino_height - self.y_correction),
            # (self.dino_coords[0] + x_correction + obstacle_width, self.dino_coords[1], obstacle_width, self.dino_height - y_correction),
            # (self.dino_coords[0] + x_correction + obstacle_width * 2, self.dino_coords[1], obstacle_width, self.dino_height - y_correction),
            # (self.dino_coords[0] + x_correction + 3, self.dino_coords[1], 3, self.dino_height - y_correction),
            # (self.dino_coords[0] + x_correction + 4, self.dino_coords[1], 3, self.dino_height - y_correction),
        ]

        self. jump() 

        # Start the speed measurement in a separate thread
        self.speed_coords = {"left": self.dino_coords[0] + self.x_correction,
                              "top": self.dino_coords[1] + self.dino_height, 
                              "width": 300, "height": 10}  # Example coordinates
        self._speed_thread = threading.Thread(target=self.measure_speed)
        self._speed_thread.start()

        iteration_limit = 20000000  # Set the iteration limit
        iteration_count = 0
        # Main loop that runs until exit_requested is True
        while not self._keyboard_listener._exit_requested and iteration_count < iteration_limit:
            self.react_obsticle()

            # time.sleep(0.1)  # Simulate doing work in the loop
            iteration_count += 1
            # if self.is_game_over():
            #     print("Game over")
            #     break
            
        self._exit_requested = True
        print("ESC pressed. Exiting.")
    


if __name__ == '__main__':
    app = MainApp()
    app.run()