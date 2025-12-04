import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="Vietnamese Sentiment Assistant", page_icon="🤖", layout="wide")

# Load model ngay khi vào app để người dùng không phải chờ lâu ở lần chạy đầu tiên
with st.spinner("Đang khởi động hệ thống và tải mô hình AI... Vui lòng chờ giây lát!"):
    import classifier  # Import module AI
    import database    # Import module DB
    classifier.load_model()

st.title("🤖 Trợ Lý Phân Loại Cảm Xúc Tiếng Việt")
st.markdown("---")

col1, col2 = st.columns([1, 1])

# --- CỘT TRÁI: NHẬP LIỆU ---
with col1:
    st.subheader("📝 Nhập văn bản")
    with st.form("nlp_form"):
        user_input = st.text_area("Nhập câu (hỗ trợ không dấu/viết tắt):", height=150,
                                placeholder="Ví dụ: Rat vui hom nay...")
        submitted = st.form_submit_button("Phân tích", type="primary")

    if submitted:
        if not user_input or len(user_input.strip()) < 5:
            st.error("⚠️ Câu quá ngắn! Vui lòng nhập > 5 ký tự.")
        elif len(user_input.strip()) > 50:
            st.error("⚠️ Câu quá dài! Vui lòng nhập <= 50 ký tự.")
        else:
            with st.spinner("Đang phân tích..."):
                # Gọi hàm xử lý từ file classifier.py
                label, score, clean_text = classifier.predict_sentiment(user_input)
                
                # Lưu vào DB qua file database.py
                database.save_result(user_input, label)
                
                # Hiển thị
                st.success("Hoàn tất!")
                st.json({
                    "text": user_input,
                    "processed_text": clean_text,
                    "sentiment": label
                })
                
                # Tô màu kết quả
                color = "green" if label == "POSITIVE" else "red" if label == "NEGATIVE" else "blue"
                st.markdown(f"Kết quả: **:{color}[{label}]** (Độ tin cậy: {score}%)")

# --- CỘT PHẢI: LỊCH SỬ ---
with col2:
    st.subheader("🕒 Lịch sử phân loại")
    
    # Khởi tạo biến session state để lưu giới hạn hiển thị
    if 'history_limit' not in st.session_state:
        st.session_state.history_limit = 50

    if st.button("🔄 Làm mới"):
        st.rerun()
        
    data = database.get_recent_history(limit=st.session_state.history_limit)
    if data:
        df = pd.DataFrame(data, columns=["Thời gian", "Câu gốc", "Cảm xúc"])
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Nút tải toàn bộ / Thu gọn
        if st.session_state.history_limit == 50:
            if st.button("⬇️ Tải toàn bộ lịch sử"):
                st.session_state.history_limit = 10000 # Số đủ lớn để lấy hết
                st.rerun()
        else:
            if st.button("⬆️ Thu gọn (50 dòng)"):
                st.session_state.history_limit = 50
                st.rerun()
    else:
        st.info("Chưa có dữ liệu.")