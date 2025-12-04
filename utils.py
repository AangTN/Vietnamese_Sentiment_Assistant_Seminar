def preprocess_text(text):
    """
    Chuẩn hóa văn bản: chuyển chữ thường, xử lý teencode/viết tắt
    Dựa trên các test case: 'rat vui', 'hom nay', 'ok', ...
    """
    if not text:
        return ""
        
    text = text.lower().strip()
    
    # Từ điển ánh xạ lỗi chính tả/viết tắt
    replace_dict = {
        # 1. NHÓM PHỦ ĐỊNH (Cực kỳ quan trọng: "không thích" khác hẳn "thích")
        "ko": "không",
        "k": "không",
        "kh": "không",
        "khong": "không",
        "hok": "không",
        "hong": "không",
        "hem": "không",
        "n0": "không",
        "no": "không", # Cẩn thận ngữ cảnh, nhưng trong chat thường là "no" (không)

        # 2. NHÓM ĐỒNG Ý / KHẲNG ĐỊNH
        "ok": "tốt",
        "oke": "tốt",
        "okay": "tốt",
        "oki": "tốt",
        "uk": "ừ",
        "uhm": "ừ",
        "dc": "được",
        "duoc": "được",
        "dk": "được",
        "đc": "được",
        "đk": "được",
        "yeap": "đúng",
        "yep": "đúng",

        # 3. NHÓM MỨC ĐỘ (Ảnh hưởng đến Score của AI)
        "rat": "rất",
        "rt": "rất",
        "wa": "quá",
        "qua": "quá",
        "wá": "quá",
        "hơi": "hơi",
        "hoi": "hơi",
        "sieu": "siêu",
        "max": "tuyệt đối",
        "vl": "vô cùng", # (Từ lóng, chuyển thành mức độ cao)
        "vcl": "vô cùng",
        "vai": "vãi",

        # 4. NHÓM CẢM XÚC TÍCH CỰC (POSITIVE)
        "thich": "thích",
        "iu": "yêu",
        "yeu": "yêu",
        "love": "yêu",
        "fê": "phê",
        "phe": "phê",
        "ngon": "ngon",
        "gud": "tốt",
        "good": "tốt",
        "tuyet": "tuyệt",
        "dep": "đẹp",
        "xinh": "xinh",
        "vui": "vui",
        "happy": "vui",
        "hepy": "vui",
        "suong": "sướng",
        "phan khich": "phấn khích",
        "ung": "ưng",

        # 5. NHÓM CẢM XÚC TIÊU CỰC (NEGATIVE)
        "chan": "chán",
        "buon": "buồn",
        "sau": "sầu",
        "do": "dở", # Từ này quan trọng
        "te": "tệ",
        "bad": "tệ",
        "kem": "kém",
        "xau": "xấu",
        "ghe": "ghê",
        "ghet": "ghét",
        "uc": "ức",
        "tuc": "tức",
        "buc": "bực",
        "dien": "điên",
        "met": "mệt",
        "tiêc": "tiếc",
        "tiec": "tiếc",
        "hut hang": "hụt hẫng",
        "that vong": "thất vọng",

        # 6. NHÓM TRUNG TÍNH / TỪ NỐI / ĐẠI TỪ
        "bt": "bình thường",
        "bth": "bình thường",
        "tam": "tạm",
        "cung": "cũng",
        "cx": "cũng",
        "ms": "mới",
        "vs": "với",
        "ntn": "như thế này",
        "nv": "như vậy",
        "z": "vậy",
        "j": "gì",
        "gi": "gì",
        "bn": "bạn",
        "mik": "mình",
        "mk": "mình",
        "t": "tôi",
        "tao": "tôi",
        "may": "mày",
        "hom nay": "hôm nay",
        "h": "giờ",
        "tr": "trời",
        "trùi": "trời",
        "hic": "huhu", 
        "hu hu": "huhu",
        "cam on": "cảm ơn",
        "tk": "cảm ơn", # thanks
        "tks": "cảm ơn",
        "shop": "cửa hàng",
        "sp": "sản phẩm"
    }
    
    words = text.split()
    corrected_words = [replace_dict.get(word, word) for word in words]
    return " ".join(corrected_words)

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