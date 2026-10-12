from pathlib import Path

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsOpacityEffect,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from agroscan.ui.components.loading_screen import LoadingScreen
from agroscan.ui.pages.dashboard import DashboardPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AgroScan - Inspection Workstation")
        self.resize(1440, 900)
        self.setMinimumSize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)

        # Root layout chia màn hình thành 2 phần: Sidebar và Content
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ==================== SIDEBAR ====================
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(260)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(24, 32, 24, 24)
        sidebar_layout.setSpacing(12)

        # Tên thương hiệu
        brand = QLabel("AgroScan")
        brand.setObjectName("Brand")

        brand_subtitle = QLabel("INSPECTION WORKSTATION")
        brand_subtitle.setObjectName("BrandSubtitle")

        sidebar_layout.addWidget(brand)
        sidebar_layout.addWidget(brand_subtitle)
        sidebar_layout.addSpacing(32)

        # Menu điều hướng (Navigation)
        self.navigation = QListWidget()
        self.navigation.setObjectName("Navigation")
        self.navigation.setFocusPolicy(Qt.FocusPolicy.NoFocus) # Xóa viền chấm bi khi click

        pages = [
            "Dashboard",
            "New Inspection",
            "Inspection History",
            "Quality Review",
            "Reports",
            "Settings",
        ]

        for name in pages:
            item = QListWidgetItem(name)
            item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
            self.navigation.addItem(item)

        # Trỏ chuột biến thành hình bàn tay khi hover qua menu
        self.navigation.setCursor(Qt.CursorShape.PointingHandCursor)

        sidebar_layout.addWidget(self.navigation)
        sidebar_layout.addStretch()

        # Nhãn dưới cùng
        footer = QLabel("DEMO MODE")
        footer.setObjectName("DemoBadge")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(footer)

        # ==================== MAIN CONTENT ====================
        content = QWidget()
        content.setObjectName("Content")

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Header bar
        header = QFrame()
        header.setObjectName("Header")
        header.setFixedHeight(72)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(32, 0, 32, 0)

        self.breadcrumb = QLabel("AgroScan  /  Dashboard")
        self.breadcrumb.setObjectName("Breadcrumb")

        user_label = QLabel("Inspector User")
        user_label.setObjectName("UserLabel")
        user_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(self.breadcrumb)
        header_layout.addStretch()
        header_layout.addWidget(user_label)

        # Vùng chứa các trang (Stacked Widget)
        self.pages = QStackedWidget()
        
        # Trang 1: Dashboard
        self.dashboard_page = DashboardPage()
        self.pages.addWidget(self.dashboard_page)

        # Trang 2: Placeholder cho các trang chưa làm
        self.placeholder_page = QWidget()
        self.placeholder_page.setObjectName("DashboardPage")
        placeholder_layout = QVBoxLayout(self.placeholder_page)
        placeholder_layout.setContentsMargins(40, 40, 40, 40)
        placeholder_layout.setSpacing(12)
        placeholder_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.placeholder_title = QLabel("Page Under Construction")
        self.placeholder_title.setObjectName("PageTitle")
        self.placeholder_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.placeholder_subtitle = QLabel("This module will be developed in the upcoming phase.")
        self.placeholder_subtitle.setObjectName("PageSubtitle")
        self.placeholder_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        placeholder_layout.addWidget(self.placeholder_title)
        placeholder_layout.addWidget(self.placeholder_subtitle)
        self.pages.addWidget(self.placeholder_page)

        # Trang 3: Loading Screen chuyển trang
        self.loading_screen = LoadingScreen()
        self.pages.addWidget(self.loading_screen)

        content_layout.addWidget(header)
        content_layout.addWidget(self.pages)

        # Thêm Sidebar và Content vào Root
        root.addWidget(sidebar)
        root.addWidget(content)

        # Trạng thái điều hướng
        self._current_index = 0
        self._pending_target_index = 0
        self._is_loading = False

        # Xử lý sự kiện click menu
        self.navigation.currentRowChanged.connect(self.change_page)
        
        # Tải giao diện QSS
        self.load_stylesheet()
        
        # Chọn mặc định mục đầu tiên
        self.navigation.setCurrentRow(0)

    def change_page(self, index: int):
        if index < 0:
            return

        # 1. Nếu không đang loading và click vào chính trang đang xem -> bỏ qua
        if not self._is_loading and index == self._current_index:
            return

        # 2. Nếu đang loading trang X và người dùng click lại chính trang X đang load -> bỏ qua (tránh reset)
        if self._is_loading and index == self._pending_target_index:
            return

        # 3. Nếu đang loading nhưng người dùng đổi ý bấm quay lại trang hiện tại đang mở:
        if self._is_loading and index == self._current_index:
            self.loading_screen.stop()
            self._is_loading = False
            self._pending_target_index = self._current_index
            item = self.navigation.item(self._current_index)
            cur_name = item.text().strip() if item else "Dashboard"
            self.breadcrumb.setText(f"AgroScan  /  {cur_name}")
            target_w = self.dashboard_page if self._current_index == 0 else self.placeholder_page
            self._switch_to_page_with_transition(target_w)
            return

        # Dừng ngay tiến trình loading cũ nếu có
        self.loading_screen.stop()

        item = self.navigation.item(index)
        page_name = item.text().strip() if item else "Page"

        # 4. Phân loại: Trang nặng (cần tải dữ liệu/mô hình AI) vs Trang nhẹ (mở tức thì)
        # Trang nhẹ như Settings, Dashboard: chuyển tức thì không cần chờ!
        heavy_pages = {
            "New Inspection": 2000,
            "Inspection History": 2200,
            "Quality Review": 2000,
            "Reports": 2400,
        }

        # Nếu là trang KHÔNG CẦN LOADING (ví dụ: Settings, Dashboard khi quay về):
        if page_name not in heavy_pages:
            self._is_loading = False
            self._current_index = index
            self._pending_target_index = index
            self.breadcrumb.setText(f"AgroScan  /  {page_name}")

            # Đồng bộ highlight trên Sidebar
            self.navigation.blockSignals(True)
            self.navigation.setCurrentRow(index)
            self.navigation.blockSignals(False)

            if index == 0:
                self._switch_to_page_with_transition(self.dashboard_page)
            else:
                self.placeholder_title.setText(page_name)
                self.placeholder_subtitle.setText(f"{page_name} preferences and configurations.")
                self._switch_to_page_with_transition(self.placeholder_page)
            return

        # 5. Nếu là trang NẶNG (CẦN LOADING 2s):
        self._pending_target_index = index
        self._is_loading = True

        # Cập nhật breadcrumb thông báo trạng thái
        self.breadcrumb.setText(f"AgroScan  /  Loading {page_name}...")

        # Chuyển sang màn hình Loading
        self.pages.setCurrentWidget(self.loading_screen)

        est_ms = heavy_pages.get(page_name, 2000)

        # Chuyển trang nhanh gọn với hiệu ứng flash nhẹ (bỏ cd 2s, estimate thực tế giữ nguyên)
        self.loading_screen.start(
            page_name=page_name,
            on_complete=lambda: self._finish_loading(index, page_name),
            estimated_ms=est_ms,
            transition_ms=280,
        )

    def _finish_loading(self, target_index: int, page_name: str):
        # Đảm bảo chỉ hoàn tất nếu trang này vẫn là trang mục tiêu cuối cùng người dùng chọn
        if target_index != self._pending_target_index:
            return

        self._is_loading = False
        self._current_index = target_index

        # Cập nhật Breadcrumb hoàn tất
        self.breadcrumb.setText(f"AgroScan  /  {page_name}")

        # Đồng bộ highlight trên thanh Sidebar đúng theo trang đích
        self.navigation.blockSignals(True)
        self.navigation.setCurrentRow(target_index)
        self.navigation.blockSignals(False)

        # Chuyển trang thực tế với hiệu ứng flash fade-in mượt mà
        if target_index == 0:
            self._switch_to_page_with_transition(self.dashboard_page)
        else:
            self.placeholder_title.setText(page_name)
            self.placeholder_subtitle.setText(f"{page_name} module is scheduled for development in Phase C/D.")
            self._switch_to_page_with_transition(self.placeholder_page)

    def _switch_to_page_with_transition(self, target_widget: QWidget):
        """Chuyển sang trang đích với hiệu ứng flash fade-in mượt mà."""
        self.pages.setCurrentWidget(target_widget)

        effect = QGraphicsOpacityEffect(target_widget)
        target_widget.setGraphicsEffect(effect)

        anim = QPropertyAnimation(effect, b"opacity", self)
        anim.setDuration(240)
        anim.setStartValue(0.15)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        anim.finished.connect(lambda: target_widget.setGraphicsEffect(None))
        anim.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)
        self._page_transition_anim = anim

    def load_stylesheet(self):
        # Đảm bảo nạp font Inter nếu chạy độc lập
        fonts_dir = Path(__file__).parent / "resources" / "fonts"
        if fonts_dir.exists():
            for font_file in fonts_dir.glob("*.ttf"):
                QFontDatabase.addApplicationFont(str(font_file))

        style_path = Path(__file__).parent / "styles" / "dark_theme.qss"
        if style_path.exists():
            self.setStyleSheet(style_path.read_text(encoding="utf-8"))
