# AgroScan 🌾🔍

> **AI-Powered Semi-Automated Multi-Category Goods Inspection System**  
> Hệ thống trạm làm việc (Workstation) hỗ trợ kiểm tra và đánh giá chất lượng hàng hóa nông sản tại cửa khẩu logistics bằng Computer Vision, AI và quy trình lấy mẫu thống kê.

---

## 📌 Tính năng nổi bật hiện tại

- 🖥️ **Desktop UI hiện đại:** Xây dựng bằng **PySide6** (Qt for Python), hỗ trợ Dark Theme phong cách Slate / Sky Blue cao cấp.
- 🔤 **Chuẩn hoá quốc tế:** Nhúng sẵn font chữ **Inter** đảm bảo hiển thị sắc nét, đồng nhất trên mọi màn hình và hệ điều hành.
- ⚡ **Chuyển cảnh nhạy bén:** Tối ưu hóa thời gian tải trang, đi kèm hiệu ứng Flash nhẹ mượt mà khi chuyển đổi giữa các module.
- 🚀 **Launcher vạn năng (`run.py`):** Tự động phát hiện môi trường ảo `.venv` và cấu hình đường dẫn `src`, chỉ cần **1 lệnh duy nhất** là chạy được ngay trên bất kỳ máy nào.

---

## ⚙️ Yêu cầu hệ thống

- **Hệ điều hành:** Windows 10/11, macOS, hoặc Linux
- **Python:** Phiên bản `>= 3.10` (khuyến nghị Python 3.11 - 3.13)
- **Git**

---

## 🚀 Hướng dẫn cài đặt

### Bước 1: Clone mã nguồn về máy

Mở Terminal / PowerShell và chạy:
```bash
git clone https://github.com/vuhaninh20102004/AgroScan.git
cd AgroScan
```

### Bước 2: Tạo và kích hoạt môi trường ảo (`.venv`)

**Trên Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
*(Nếu gặp chính sách cấm chạy script của PowerShell, chạy trước lệnh: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

**Trên macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Bước 3: Cài đặt các thư viện cần thiết

Cài đặt các gói phụ thuộc từ `requirements.txt`:
```bash
pip install -r requirements.txt
```

*(Tùy chọn: Bạn cũng có thể cài đặt theo chuẩn package hiện đại bằng lệnh `pip install -e .`)*

---

## 🎮 Hướng dẫn khởi chạy ứng dụng

Sau khi cài đặt xong, bạn có thể khởi chạy phần mềm bằng 1 trong các cách sau:

### Cách 1: Sử dụng Launcher tự động (Khuyên dùng — Tiện lợi nhất)
Chỉ cần gõ **đúng 1 lệnh duy nhất**:
```bash
python run.py
```
> 💡 *File `run.py` đã tích hợp sẵn cơ chế Auto-detect: kể cả khi bạn mở Terminal mới mà quên kích hoạt `.venv`, nó vẫn tự động tìm thấy `.venv` và khởi chạy chuẩn xác.*

### Cách 2: Chạy trực tiếp module Python
*(Yêu cầu đã kích hoạt môi trường ảo `.venv`)*:
```bash
python -m agroscan.main
```

---

## 📂 Cấu trúc thư mục dự án

```text
AgroScan/
├── src/
│   └── agroscan/
│       ├── __init__.py
│       ├── main.py                  # Entry point chính của ứng dụng
│       └── ui/
│           ├── main_window.py       # Cửa sổ chính (Sidebar, Header, Router)
│           ├── components/          # Các widget tái sử dụng (Loading, Spinner...)
│           ├── pages/               # Các trang giao diện (Dashboard, New Inspection...)
│           ├── resources/fonts/     # Font chữ Inter nhúng sẵn
│           └── styles/              # File dark_theme.qss giao diện tối
├── run.py                           # Launcher chạy nhanh đa nền tảng
├── pyproject.toml                   # Cấu hình đóng gói Package chuẩn PEP 621
├── requirements.txt                 # Danh sách thư viện phụ thuộc
├── ROADMAP.md                       # Kế hoạch phát triển chi tiết 6 giai đoạn
└── README.md                        # Tài liệu hướng dẫn này
```

---

## 🗺️ Lộ trình phát triển

Dự án được phân chia thành 6 giai đoạn phát triển rõ ràng. Chi tiết xem tại [ROADMAP.md](ROADMAP.md):
- [x] **Phase 1:** Desktop UI Foundation *(Hoàn thành)*
- [ ] **Phase 2:** New Inspection Flow & Mock AI
- [ ] **Phase 3:** YOLO Core Integration & Inference Worker
- [ ] **Phase 4:** Sampling Decision Engine & Defect Inspection
- [ ] **Phase 5:** Quality Review & Inspection History
- [ ] **Phase 6:** Packaging (`AgroScan.exe`) & Final Handover

---

## 📄 Bản quyền & Tác giả

- **Dự án:** Đồ án tốt nghiệp ngành Software Engineering — Trường Đại học Duy Tân (DTU).
- **Tác giả:** Vũ Hà Ninh ([@vuhaninh20102004](https://github.com/vuhaninh20102004))
