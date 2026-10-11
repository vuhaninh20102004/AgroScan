from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsDropShadowEffect,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class StatCard(QFrame):
    def __init__(self, title: str, value: str, note: str):
        super().__init__()
        self.setObjectName("StatCard")

        # Hiệu ứng đổ bóng (Drop shadow) giúp thẻ nổi bật và cao cấp hơn
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 6)
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        value_label = QLabel(value)
        value_label.setObjectName("CardValue")
        value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        note_label = QLabel(note)
        note_label.setObjectName("CardNote")
        note_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(note_label)
        layout.addStretch()


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("DashboardPage")

        root = QVBoxLayout(self)
        root.setContentsMargins(40, 40, 40, 40)
        root.setSpacing(40)

        # Header section
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)

        title = QLabel("Dashboard")
        title.setObjectName("PageTitle")

        subtitle = QLabel("Overview of goods inspection activities")
        subtitle.setObjectName("PageSubtitle")

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)

        root.addLayout(header_layout)

        # Grid section for cards
        grid = QGridLayout()
        grid.setSpacing(24)

        cards = [
            StatCard("TOTAL INSPECTIONS", "1,248", "↑ 12% vs last week"),
            StatCard("PENDING REVIEW", "32", "Needs attention"),
            StatCard("COMPLETED", "1,190", "All clear"),
            StatCard("FLAGGED SAMPLES", "26", "Action required"),
        ]

        for index, card in enumerate(cards):
            grid.addWidget(card, 0, index)

        root.addLayout(grid)
        root.addStretch()
