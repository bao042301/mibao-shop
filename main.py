import streamlit as st
import os

# ==========================================
# 第一步：環境設定與精緻化 CSS 視覺靈魂
# ==========================================
st.set_page_config(page_title="米寶漢方｜植感日常選物", layout="centered")

st.markdown("""
    <style>
    /* 修正字體覆蓋問題，保護系統圖示不變亂碼 */
    html, body, p, span, h1, h2, h3, h4, h5, h6, label, input, button { 
        font-family: 'Noto Sans TC', sans-serif !important; 
        color: #4A4E31 !important; 
    }
    .stApp { background-color: #FDFBF7 !important; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 90px !important; }

    /* 標題與區塊設計 */
    h3 { font-size: 1.15rem !important; font-weight: 700 !important; margin: 20px 0 10px !important; text-align: center !important; color: #7A8450 !important; letter-spacing: 1px; }
    .section-title { background-color: #E9EDC9; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin: 25px 0 15px; font-size: 1.05rem;}
    
    /* Logo 尺寸 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    
    /* 🚀 徹底解決深色模式黑底，包含 + 與 - 按鈕 */
    div[data-baseweb="input"], div[data-baseweb="base-input"] { 
        background-color: #FFFFFF !important; 
        border: 1.5px solid #E9EDC9 !important; 
        border-radius: 8px !important; 
    }
    input { 
        background-color: #FFFFFF !important; 
        color: #4A4E31 !important; 
        -webkit-text-fill-color: #4A4E31 !important; 
    }
    /* 針對數量選擇器的 + 和 - 按鈕上色，消滅黑底 */
    [data-testid="stNumberInput"] button {
        background-color: #F1F4E8 !important;
        color: #4A4E31 !important;
        border: none !important;
    }

    /* 壓縮元件間距，讓畫面不要太冗長 */
    [data-testid="stVerticalBlock"] > div {
        padding-bottom: 0.2rem !important;
    }

    /* LINE 原生跳轉按鈕樣式鎖定 */
    [data-testid="stLinkButton"] a {
        width: 100% !important; background-color: #06C755 !important; border-radius: 15px !important; height: 3.2em !important; 
        display: flex !important; justify-content: center !important; align-items: center !important; text-decoration: none !important;
    }
    [data-testid="stLinkButton"] a * { color: #FFFFFF !important; font-size: 1.05rem !important; font-weight: 900 !important; }

    /* 程式碼複製框防黑底 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre, code { background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important; }
    [data-testid="stCodeBlock"] button { opacity: 1 !important; background-color: rgba(233, 237, 201, 1) !important; scale: 0.8; }

    /* 頁尾固定 */
    .custom-footer { position: fixed; left: 0; bottom: 0; width: 100vw; text-align: center; background-color: #FDFBF7; padding: 8px 0; z-index: 9999; box-shadow: 0 -2px 10px rgba(0,0,0,0.03); }
    .footer-text { font-size: 0.65rem !important; color: #8B8B7A !important; margin: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 第二步：版面配置與商品陳列 (雙欄位壓縮版)
# ==========================================
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-style:italic; font-size:0.85rem; color:#8B8B7A; margin-bottom: 10px;">「將這份溫潤，訂製成您的日常習慣。」</p>', unsafe_allow_html=True)

order_summary = []
total_price = 0

# --- 1. 六種漢方茶飲 (雙欄位排版) ---
st.markdown('<div class="section-title">🍵 漢方植感茶飲系列 (10入)</div>', unsafe_allow_html=True)
teas = ["黃耆元氣茶", "金菊牛蒡茶", "當歸紅棗茶", "黑豆漢方茶", "洛神山楂茶", "玫瑰決明茶"]
t_cols = st.columns(2)
for i, t in enumerate(teas):
    with t_cols[i % 2]:
        qty = st.number_input(f"{t} $680", min_value=0, step=1, key=t)
        if qty > 0:
            order_summary.append(f"• {t}(10入) x {qty}")
            total_price += 680 * qty

# --- 2. 藥膳燉湯區 (拿掉折疊，直接雙欄顯示) ---
st.markdown('<div class="section-title">🥣 藥膳燉湯包 (需自燉)</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold; color:#7A8450; font-size:0.9rem; margin-top:-5px;'>【$150/包 系列】</p>", unsafe_allow_html=True)
soups_150 = ["四神藥膳", "四物藥膳", "羊肉爐藥膳", "胡椒雞藥膳"]
s1_cols = st.columns(2)
for i, s in enumerate(soups_150):
    with s1_cols[i % 2]:
        qty = st.number_input(f"{s}", min_value=0, step=1, key=s)
        if qty > 0:
            order_summary.append(f"• {s}燉湯包 x {qty}")
            total_price += 150 * qty

st.markdown("<p style='text-align:center; font-weight:bold; color:#7A8450; font-size:0.9rem; margin-top:10px;'>【$250/包 系列】</p>", unsafe_allow_html=True)
soups_250 = ["十全藥膳", "人蔘雞藥膳", "薑母鴨藥膳", "何首烏藥膳"]
s2_cols = st.columns(2)
for i, s in enumerate(soups_250):
    with s2_cols[i % 2]:
        qty = st.number_input(f"{s}", min_value=0, step=1, key=s)
        if qty > 0:
            order_summary.append(f"• {s}燉湯包 x {qty}")
            total_price += 250 * qty

# --- 3. 日常真空與代餐 (雙欄位排版) ---
st.markdown('<div class="section-title">🛍️ 日常真空調理包 ($90) & 代餐</div>', unsafe_allow_html=True)
d_cols = st.columns(2)
with d_cols[0]:
    d_qty1 = st.number_input("杜仲茶 (真空包)", min_value=0, step=1)
    if d_qty1 > 0:
        order_summary.append(f"• 杜仲茶(真空包) x {d_qty1}")
        total_price += 90 * d_qty1
    
    m_qty = st.number_input("五穀養生餐 $300", min_value=0, step=1)
    if m_qty > 0:
        order_summary.append(f"• 五穀養生餐 x {m_qty}")
        total_price += 300 * m_qty

with d_cols[1]:
    d_qty2 = st.number_input("四物茶 (真空包)", min_value=0, step=1)
    if d_qty2 > 0:
        order_summary.append(f"• 四物茶(真空包) x {d_qty2}")
        total_price += 90 * d_qty2

# ==========================================
# 第三步：收件地址與結帳總計
# ==========================================
st.markdown("<br><hr style='border: 0.5px solid #E9EDC9;'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#7A8450;'>📝 配送資訊與結帳</h4>", unsafe_allow_html=True)

address = st.text_input("📍 收件地址", placeholder="請填寫您的收件地址...")
sub_choice = st.checkbox("✅ 我想加入「米寶健康訂閱制」，每月固定配送以上品項")

if total_price > 0:
    st.markdown(f'<p style="font-size: 1.5rem; font-weight: 900; color: #7A8450; text-align: center; margin: 20px 0; background-color: #F1F4E8; padding: 10px; border-radius: 10px;">🛒 本次預約總計：${total_price}</p>', unsafe_allow_html=True)
    
    sub_text = "【✅ 已開啟每月訂閱制固定配送】" if sub_choice else "【單次預約方案】"
    summary_str = "\n".join(order_summary)
    addr_str = f"📍 收件地址：{address}" if address else "📍 收件地址：(未填寫)"
    
    msg = f"Hi 米寶！🐢✨\n我已完成線上選購囉！\n{sub_text}\n---\n{summary_str}\n---\n{addr_str}\n💰 總計預約金額：${total_price}\n期待這份草本溫暖。🌿"
    
    st.code(msg, language=None)
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-top:10px; margin-bottom:5px;">點擊☆上框右上角☆複製訂單明細：</p>', unsafe_allow_html=True)
    
    line_url = "https://line.me/R/ti/p/@716osfvq"
    st.link_button("🌿 前往 LINE@ 貼上訂單並預約配送 ➔", line_url, use_container_width=True)

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜植感日常選物｜©
