"""AgroScan Universal Launcher.

Tự động nhận diện môi trường ảo .venv (nếu có) và thư mục src.
Chạy được trên mọi hệ điều hành (Windows, Linux, macOS) chỉ với 1 lệnh:
    python run.py
"""

import os
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

# 1. Tự động kiểm tra và ưu tiên sử dụng Python trong .venv nếu người dùng chưa kích hoạt
if os.name == "nt":
    venv_python = ROOT_DIR / ".venv" / "Scripts" / "python.exe"
else:
    venv_python = ROOT_DIR / ".venv" / "bin" / "python"

if venv_python.exists() and Path(sys.executable).resolve() != venv_python.resolve():
    # Tự động chuyển giao quyền chạy sang Python của .venv
    sys.exit(subprocess.call([str(venv_python), __file__] + sys.argv[1:]))

# 2. Đảm bảo thư mục src luôn có trong sys.path
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# 3. Khởi chạy ứng dụng AgroScan
from agroscan.main import main

if __name__ == "__main__":
    main()
