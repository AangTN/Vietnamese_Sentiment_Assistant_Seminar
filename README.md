# 🤖 TRỢ LÝ PHÂN LOẠI CẢM XÚC TIẾNG VIỆT (VIETNAMESE SENTIMENT ASSISTANT)

> **Đồ án môn học: Xử lý ngôn ngữ tự nhiên / Trí tuệ nhân tạo**
>
> - **Sinh viên:** Nguyễn Minh Tuấn
> - **Mã SV:** 3122560086

## 📖 Giới thiệu
Ứng dụng web sử dụng mô hình học sâu (Deep Learning) **PhoBERT** để phân tích cảm xúc của các câu văn tiếng Việt (Tích cực / Tiêu cực / Trung tính). Hệ thống hỗ trợ xử lý ngôn ngữ tự nhiên (NLP) cơ bản như chuẩn hóa teencode, viết tắt và lưu trữ lịch sử phân tích.

## 🚀 Tính năng nổi bật
- **Phân tích cảm xúc:** Nhận diện chính xác cảm xúc từ văn bản tiếng Việt.
- **Xử lý ngôn ngữ (NLP):** Tự động sửa lỗi chính tả, teencode phổ biến (vd: "ko" -> "không", "ok" -> "tốt").
- **Lịch sử hoạt động:** Lưu lại các câu đã phân tích vào cơ sở dữ liệu SQLite.
- **Giao diện thân thiện:** Xây dựng trên Streamlit, dễ sử dụng, hỗ trợ Dark Mode.

## 🛠️ Công nghệ sử dụng
- **Ngôn ngữ:** Python 3.8+
- **Giao diện:** Streamlit
- **AI Model:** HuggingFace Transformers (`wonrax/phobert-base-vietnamese-sentiment`)
- **Database:** SQLite
- **Thư viện khác:** Pandas, PyTorch

## ⚙️ Hướng dẫn cài đặt & Chạy
1. **Kích hoạt môi trường ảo (nếu có):**
   ```bash
   .\venv\Scripts\activate
   ```

2. **Cài đặt thư viện:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy ứng dụng:**
   ```bash
   streamlit run app.py
   ```

## 📂 Cấu trúc dự án
- `app.py`: Giao diện chính của ứng dụng.
- `classifier.py`: Module xử lý AI và load model.
- `database.py`: Module quản lý cơ sở dữ liệu.
- `utils.py`: Các hàm tiện ích (tiền xử lý văn bản).
