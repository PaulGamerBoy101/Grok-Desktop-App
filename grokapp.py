import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class GrokDesktopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grok")
        self.setGeometry(100, 100, 1200, 800)

        # Create and set up web view
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://grok.com"))
        self.setCentralWidget(self.web_view)

        # Minimal styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
        """)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Grok Desktop")
    window = GrokDesktopApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
