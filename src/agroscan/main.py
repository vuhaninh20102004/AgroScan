import sys
from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication
from agroscan.ui.main_window import MainWindow


def load_application_fonts():
    """Tải và kích hoạt font Inter chuẩn hoá quốc tế từ resources."""
    fonts_dir = Path(__file__).parent / "ui" / "resources" / "fonts"
    if fonts_dir.exists():
        for font_file in fonts_dir.glob("*.ttf"):
            QFontDatabase.addApplicationFont(str(font_file))


def main():
    app = QApplication(sys.argv)

    # Nạp font Inter vào hệ thống ứng dụng
    load_application_fonts()
    app.setFont(QFont("Inter", 10))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

