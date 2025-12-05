import streamlit as st
from transformers import pipeline
from utils import preprocess_text

# Cache resource để không phải load model lại mỗi lần F5
@st.cache_resource
def load_model():
    print("⏳ Đang tải model PhoBERT...")
    return pipeline("sentiment-analysis", model="wonrax/phobert-base-vietnamese-sentiment")

def map_label(model_label):
    """
    Chuyển đổi nhãn từ Model (POS/NEG/NEU) sang yêu cầu đề bài (POSITIVE/...)
    """
    mapping = {
        "POS": "POSITIVE",
        "NEG": "NEGATIVE",
        "NEU": "NEUTRAL"
    }
    return mapping.get(model_label, "NEUTRAL")

def predict_sentiment(text):
    # 1. Load model (lấy từ cache)
    classifier = load_model()
    
    # 2. Tiền xử lý (Gọi hàm từ utils.py)
    clean_text = preprocess_text(text)
    
    # 3. Dự đoán
    # Trả về list dict, lấy phần tử đầu tiên
    result = classifier(clean_text)[0]
    
    # 4. Map nhãn (Gọi hàm từ utils.py)
    # Yêu cầu kỹ thuật: Nếu xác suất < 0.5, trả về NEUTRAL mặc định
    if result['score'] < 0.5:
        final_label = "NEUTRAL"
    else:
        final_label = map_label(result['label'])
        
    score = round(result['score'] * 100, 2)
    
    # Trả về Dictionary theo yêu cầu đề bài
    return {
        "text": clean_text,
        "sentiment": final_label,
        "score": score,
        "original_text": text
    }