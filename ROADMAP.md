# AGROSCAN — PROJECT HANDOVER & DEVELOPMENT ROADMAP

**Phiên bản tài liệu:** 1.0  
**Ngày cập nhật:** 11/10/2026  
**Trạng thái:** Đang xây dựng nền tảng Desktop UI  
**Mục tiêu sản phẩm:** `AgroScan.exe`

---

## 1. Tổng quan dự án

**Tên dự án:** AgroScan

**Tên đầy đủ:** AI-Powered Semi-Automated Multi-Category Goods Inspection System.

**Loại dự án:** Đồ án tốt nghiệp ngành Software Engineering, Duy Tan University.

**Mục tiêu:** Xây dựng phần mềm desktop hỗ trợ kiểm tra và đánh giá chất lượng hàng hóa tại cửa khẩu logistics bằng computer vision, AI và quy trình lấy mẫu thống kê.

AgroScan không phải hệ thống tự động thay thế hoàn toàn nhân viên kiểm định. Đây là hệ thống hỗ trợ ra quyết định: AI xử lý hình ảnh, phát hiện dấu hiệu bất thường, tổng hợp kết quả và chuyển các trường hợp cần thiết cho người kiểm tra xác nhận.

### Phạm vi MVP

Hai nhóm hàng được ưu tiên triển khai đầy đủ:

- Agricultural Goods — nông sản.
- Aquatic Goods — thủy sản.

Các nhóm hàng khác có thể được hỗ trợ về mặt kiến trúc trong tương lai, nhưng không nằm trong phạm vi model MVP hiện tại.

### Quy trình nghiệp vụ chính

Camera / Image Input  
→ Category Classification  
→ Object Detection & Counting  
→ Statistical Sampling  
→ Quality Assessment  
→ Human Review  
→ Phase 1 Decision  
→ Inspection Report.

**Nguyên tắc:** YOLO đảm nhiệm phát hiện, định vị và đếm vật thể; Quality Classifier đảm nhiệm phân loại chất lượng dựa trên hình ảnh. Kết quả AI có thể không chắc chắn và phải hỗ trợ chuyển sang kiểm tra thủ công.

Hình ảnh RGB chỉ hỗ trợ đánh giá dấu hiệu quan sát được, không tự chứng minh hàng hóa không có nhiễm bẩn vi sinh, hóa chất hoặc hư hỏng bên trong.

---

## 2. Các quyết định kiến trúc đã chốt

### 2.1. Công nghệ desktop

**Đã chốt: Python + PySide6 Widgets + QSS.**

- Python: ngôn ngữ chính.
- PySide6: xây dựng giao diện desktop Windows.
- QSS: tùy biến màu sắc, typography, khoảng cách, trạng thái widget và theme.
- PyInstaller: dự kiến dùng để đóng gói ứng dụng thành EXE.
- VS Code/Antigravity IDE: môi trường phát triển hiện tại.
- Git + GitHub Desktop: quản lý mã nguồn.

Không chuyển sang Flet, CustomTkinter, React/Tauri hoặc framework khác nếu chưa có lý do kỹ thuật rõ ràng.

### 2.2. Kiến trúc giai đoạn hiện tại

Toàn bộ ứng dụng được phát triển trong **một repository Python duy nhất**.

- Desktop UI.
- Application services.
- AI modules.
- Local data.
- Reports.

Chưa xây dựng FastAPI server, chưa triển khai kiến trúc client-server, chưa cần PostgreSQL hoặc MinIO.

### 2.3. Hướng mở rộng tương lai

Khi dự án phát triển, có thể tách AI backend thành FastAPI server chạy trên máy desktop có tài nguyên mạnh hơn.

Các máy khách vẫn sử dụng AgroScan Desktop và gọi AI server qua API.

Định hướng tương lai:

- Desktop client: PySide6.
- API server: FastAPI.
- AI: YOLO + Quality Classifier.
- Database tập trung: PostgreSQL khi cần nhiều máy.
- Image storage: MinIO hoặc giải pháp lưu trữ phù hợp khi cần.

**Không triển khai những thành phần này trong giai đoạn hiện tại.** Thiết kế module ngay từ đầu để có thể tách về sau, nhưng ưu tiên hoàn thiện ứng dụng chạy local trước.

### 2.4. Định hướng tối ưu tài nguyên

Ưu tiên theo thứ tự:

1. Nhẹ và tiết kiệm tài nguyên.
2. Hiệu suất.
3. Giao diện đẹp nhưng vẫn dễ sử dụng.

Không cài thư viện AI hoặc dịch vụ backend trước khi cần. Không tải model vào UI thread. Khi tích hợp AI, tác vụ nặng phải chạy trong worker để tránh treo giao diện.

---

## 3. Trạng thái môi trường phát triển

### Đã hoàn thành

- Python 3.13.5.
- Git 2.53.0.windows.2.
- GitHub Desktop đã cài.
- Antigravity IDE đang được sử dụng.
- Repository AgroScan đã tạo.
- Thư mục project: `D:\Github Clone\AgroScan`.
- Virtual environment `.venv` đã tạo và kích hoạt.
- PySide6 6.12.0 đã cài thành công.
- Đã chạy được cửa sổ desktop AgroScan đầu tiên.
- Lỗi `ModuleNotFoundError: No module named 'agroscan'` đã được khắc phục.

Lệnh chạy ứng dụng từng hoạt động thành công:

```powershell
$env:PYTHONPATH = "src"
python -m agroscan.main
```

Khi chạy, cửa sổ Windows riêng xuất hiện với tiêu đề `AgroScan` và nội dung `AgroScan - Inspection Workstation`.

### Cấu trúc source hiện tại

```text
AgroScan/
├── .venv/
├── src/
│   └── agroscan/
│       ├── __init__.py
│       ├── main.py
│       └── ui/
│           ├── __init__.py
│           ├── main_window.py
│           └── pages/
│               ├── __init__.py
│               └── dashboard.py
├── .gitattributes
├── .gitignore
└── README.md
```

Lưu ý: thư mục `__pycache__` có thể xuất hiện sau khi chạy Python; đây là bình thường.

---

## 4. Tiến độ UI chính xác tại thời điểm bàn giao

### Đã hoàn thành

**Bước 1 — Tạo môi trường và cài PySide6.**

**Bước 2 — Tạo `DashboardPage` trong `dashboard.py`.**

File đã được viết theo hướng:

- Có lớp `StatCard`.
- Có lớp `DashboardPage`.
- Hiển thị tiêu đề Dashboard.
- Có bốn thẻ thống kê:
  - Total Inspections.
  - Pending Review.
  - Completed.
  - Flagged Samples.
- Có nội dung `Demo data`.
- Dùng `QVBoxLayout`, `QGridLayout`, `QFrame` và `QLabel`.

Các số liệu hiện tại là dữ liệu giả lập, chưa lấy từ database hoặc AI thật.

### Chưa hoàn thành

Các nội dung sau mới được hướng dẫn, chưa xác nhận đã thực hiện:

- Thay `main_window.py` bằng phiên bản có sidebar và `QStackedWidget`.
- Tạo `styles/dark_theme.qss`.
- Tích hợp DashboardPage vào MainWindow mới.
- Chạy thử giao diện Dashboard hoàn chỉnh.
- Tạo và kiểm tra `requirements.txt`.
- Commit phiên bản đầu tiên bằng Git.
- Tạo trang New Inspection.
- Xây dựng điều hướng thực sự giữa các trang.
- Đóng gói EXE.

**Không được nhầm việc hoàn thành code `dashboard.py` với việc hoàn thành Dashboard tích hợp.** Ứng dụng hiện đã chạy được cửa sổ cơ bản; DashboardPage đã có code, nhưng bước tích hợp UI vẫn đang chờ.

---

## 5. Lộ trình triển khai tiếp theo

### Giai đoạn A — Hoàn thiện Desktop UI Foundation

**Đây là giai đoạn cần tiếp tục ngay.**

1. Kiểm tra lại `dashboard.py`.
2. Hoàn thiện `main_window.py`.
3. Tạo sidebar gồm:
   - Dashboard.
   - New Inspection.
   - Inspection History.
   - Quality Review.
   - Reports.
   - Settings.
4. Tạo header, vùng nội dung chính và `QStackedWidget`.
5. Tạo `styles/dark_theme.qss`.
6. Load QSS vào MainWindow.
7. Chạy lại ứng dụng và kiểm tra giao diện.
8. Sửa lỗi nếu có.
9. Tạo `requirements.txt` và commit phiên bản ổn định.

Mục tiêu nghiệm thu: ứng dụng mở được, Dashboard xuất hiện, sidebar hiển thị đúng, giao diện thống nhất và không có lỗi runtime.

### Giai đoạn B — Hoàn thiện luồng nghiệp vụ bằng dữ liệu giả

Triển khai lần lượt:

1. New Inspection.
2. Tạo phiên kiểm tra và nhập thông tin lô hàng.
3. Tải ảnh từ máy tính.
4. Hiển thị ảnh và trạng thái pipeline.
5. Màn hình detection mock.
6. Màn hình quality assessment mock.
7. Human Review.
8. Phase 1 Decision.
9. Inspection History.
10. Reports.

Dữ liệu giả phải được đánh dấu `DEMO MODE`. Không trình bày kết quả mock như kết quả AI thật.

Mục tiêu: có một luồng demo từ tạo phiên đến xem kết quả và xác nhận.

### Giai đoạn C — Nghiệp vụ và lưu trữ local

Khi UI ổn định:

- Tách nghiệp vụ khỏi giao diện.
- Xây inspection service.
- Xây sampling service.
- Xây report service.
- Dùng SQLite để lưu metadata và lịch sử local.
- Lưu ảnh trong thư mục riêng.
- Xuất PDF/Excel.
- Thêm logging, validation và xử lý lỗi.

Chưa cần FastAPI, PostgreSQL hoặc MinIO ở giai đoạn này.

### Giai đoạn D — AI Integration

Thứ tự triển khai:

1. Audit dataset.
2. Category Classifier.
3. YOLO detection/counting.
4. Statistical Sampling.
5. Quality Classifier.
6. Human Review.
7. Decision aggregation.
8. Benchmark và tích hợp pipeline.

YOLO và Quality Classifier là hai module riêng. Không dùng YOLO thay thế model đánh giá chất lượng.

Lựa chọn YOLO cuối cùng phải dựa trên dataset và benchmark thực tế; không mặc định model mới hơn sẽ tốt hơn trên dataset AgroScan.

### Giai đoạn E — Đóng gói và kiểm thử

- Build thử bằng PyInstaller sớm.
- Kiểm tra tài nguyên và model weights.
- Kiểm tra chạy trên máy chưa cài Python.
- Kiểm tra dung lượng bộ cài, RAM, CPU và thời gian khởi động.
- Hoàn thiện tài liệu người dùng và hướng dẫn cài đặt.
- Chuẩn bị bản demo tốt nghiệp.

### Giai đoạn F — Mở rộng server sau này

Chỉ thực hiện khi ứng dụng local đã ổn định và thực sự cần nhiều máy khách hoặc AI chạy trên máy riêng.

Khi đó mới tách FastAPI, PostgreSQL và image storage thành các dịch vụ riêng.

---

## 6. Quy tắc làm việc trong các session tiếp theo

1. Hướng dẫn từng bước, không đưa quá nhiều công việc cùng lúc.
2. Chỉ đánh dấu hoàn thành khi người dùng xác nhận hoặc có bằng chứng chạy thành công.
3. Trước khi yêu cầu tạo file, kiểm tra xem file đã tồn tại chưa.
4. Ưu tiên sửa file hiện có thay vì tạo project mới.
5. Khi gặp lỗi, chẩn đoán dựa trên thông báo và cấu trúc file thực tế.
6. Không tự ý đổi tên dự án, package hoặc framework.
7. Tên sản phẩm là `AgroScan`; tên package Python là `agroscan`; file phát hành cuối là `AgroScan.exe`.
8. Không triển khai server trước khi hoàn thiện ứng dụng desktop local.
9. Tách UI, nghiệp vụ và AI thành module riêng.
10. Mỗi giai đoạn cần có tiêu chí nghiệm thu và commit tương ứng.
