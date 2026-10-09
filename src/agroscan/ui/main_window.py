from PySide6.QtWidgets import QLabel, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AgroScan")
        self.resize(1200, 800)

        label = QLabel("AgroScan")
        label.setStyleSheet(
            "font-size: 24px; padding: 24px;"
        )

        self.setCentralWidget(label)
