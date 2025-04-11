import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                              QWidget, QLineEdit, QPushButton, QLabel)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QIcon

class GrokDesktopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grok - Desktop App")
        self.setGeometry(100, 100, 1200, 800)
        self.init_ui()

    def init_ui(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Toolbar
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(10, 5, 10, 5)

        # Navigation buttons
        back_btn = QPushButton("◄")
        back_btn.setFixedWidth(40)
        back_btn.clicked.connect(self.web_view.back)
        toolbar_layout.addWidget(back_btn)

        forward_btn = QPushButton("►")
        forward_btn.setFixedWidth(40)
        forward_btn.clicked.connect(self.web_view.forward)
        toolbar_layout.addWidget(forward_btn)

        refresh_btn = QPushButton("↻")
        refresh_btn.setFixedWidth(40)
        refresh_btn.clicked.connect(self.web_view.reload)
        toolbar_layout.addWidget(refresh_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setText("https://grok.com")
        self.url_bar.returnPressed.connect(self.load_url)
        self.url_bar.setStyleSheet("padding: 5px; border-radius: 5px;")
        toolbar_layout.addWidget(self.url_bar)

        # Fullscreen toggle
        fs_btn = QPushButton("⛶")
        fs_btn.setFixedWidth(40)
        fs_btn.clicked.connect(self.toggle_fullscreen)
        toolbar_layout.addWidget(fs_btn)

        main_layout.addWidget(toolbar)

        # Web view
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://grok.com"))
        self.web_view.loadFinished.connect(self.on_load_finished)
        self.web_view.urlChanged.connect(self.update_url_bar)
        main_layout.addWidget(self.web_view)

        # Status label for errors
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ff6347; padding: 5px;")
        main_layout.addWidget(self.status_label)

        # Styling
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1e1e1e;
            }
            QPushButton {
                background-color: #3c3c3c;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QLineEdit {
                background-color: #2b2b2b;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 5px;
            }
        """)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.web_view.setUrl(QUrl(url))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())

    def on_load_finished(self, ok):
        if ok:
            self.status_label.setText("")
        else:
            self.status_label.setText("Failed to load page. Check your connection or URL.")

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Grok Desktop")
    window = GrokDesktopApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
