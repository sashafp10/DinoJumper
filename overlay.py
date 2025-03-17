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

#     # def closeEvent(self, event):
#     #     print("Closing...")
#     #     app.quit()  # Ensure the application quits when the overlay window is closed