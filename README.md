## ☁️ Muốn deploy app lên cloud?

<details>
<summary>Nhấn vào đây</summary>

1. Tạo tài khoản Streamlit và kết nối với GitHub.

2. Tạo repo mới trên GitHub, dùng GitHub Desktop clone repo về máy.

3. Thêm file code Python và `requirements.txt` bao gồm các thư viện mà các file Python sử dụng vào folder của repo, commit lên GitHub
```
📁 your-repo/
├── app.py
├── requirements.txt
└── (and lots of other things)
```
  *Nếu không biết tên thư viện là gì thì dùng `pip list` để biết tên.*

4. Tại share.streamlit.io, chọn New App -> Vâng, tôi có app.
   
5. Chọn repo GitHub, branch và file khởi chạy ứng dụng Streamlit (thường là `app.py`), và chọn domain cho đẹp (không thì thôi).

> *https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app*

</details>

## 🚀 Muốn thêm Anaconda Prompt vào menu chuột phải để mở cho nhanh?

<details>
<summary>Nhấn vào đây</summary>

### 1. Lấy đường dẫn Anaconda Prompt

- Tìm Anaconda Prompt -> click chuột phải -> chọn Mở vị trí tệp (Open file location).
- Click chuột phải tại Anaconda Prompt (anaconda3) -> Thuộc tính (Properties) -> Đích (Target). Chỉ sao chép đoạn này:

```
cmd.exe /K C:\Users\[tên user của bạn]\anaconda3\Scripts\activate.bat
```

### 2. Thêm key vào registry

- Nhấn `Win + R`, gõ `regedit`.
- Tìm đến `HKEY_CLASSES_ROOT\Directory\Background\shell`.
- Click chuột phải vào shell và tạo key mới (`New > Key`) tên là Anaconda Prompt, set value data là Open in Anaconda Prompt (hoặc gì tuỳ bạn).
- Tạo một subkey trong Anaconda Prompt với tên là Command, set value data là thứ vừa sao chép ở bước 1 vào.

</details>
