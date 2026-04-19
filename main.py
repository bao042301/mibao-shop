import streamlit as st
import os

# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 
# ==========================================
st.set_page_config(page_title="米寶漢方｜植感日常選物", layout="centered")

st.markdown("""
    <style>
    /* 全域品牌與背景 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 90px !important; }

    /* 標題與區塊設計 */
    h3 { font-size: 1.15rem !important; font-weight: 700 !important; margin: 20px 0 10px !important; text-align: center !important; color: #7A8450 !important; letter-spacing: 1px; }
    .section-title { background-color: #E9EDC9; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin: 20px 0 10px; font-size: 1.05rem;}
    
    /* Logo 尺寸 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    
    /* 防黑底：數量輸入框與下拉選單 */
    [data-testid="stNumberInput"] div[data-baseweb="input"], [data-testid="stTextInput"] div[data-baseweb="input"], [data-testid="stSelectbox"] div[data-baseweb="select"] { 
        background-color: #FFFFFF !important; border: 1.5px solid #E9EDC9 !important; border-radius: 8px !important; 
    }
    [data-testid="stNumberInput"] input, [data-testid="stTextInput"] input, [data-testid="stSelectbox"] div[data-baseweb="select"] * { color: #4A4E31 !important; }

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
# 第二步：版面配置與商品陳列
# ==========================================
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-style:italic; font-size:0.85rem; color:#8B8B7A; margin-bottom: 20px;">「將這份溫潤，訂製成您的日常習慣。」</p>', unsafe_allow_html=True)

order_summary = []
total_price = 0

# --- 1. 客製化漢方茶區 ---
st.markdown('<div class="section-title">🍵 漢方植感茶飲系列</div>', unsafe_allow_html=True)
tea_type = st.selectbox("選擇茶飲氣質", ["請選擇...", "暖陽系 (晨:黃耆金菊/午:當歸黑豆)", "微風系 (晨:洛神金菊/午:玫瑰黑豆)", "清泉系 (晨:金菊黃耆/午:玫瑰當歸)"])

if tea_type != "請選擇...":
    col1, col2 = st.columns(2)
    with col1:
        q_new = st.number_input("首購組(40入) $1980", min_value=0, step=1)
        if q_new > 0:
            order_summary.append(f"• {tea_type}\n  首購組合 x {q_new}")
            total_price += 1980 * q_new
    with col2:
        q_old = st.number_input("老友組(40入) $1880", min_value=0, step=1)
        if q_old > 0:
            order_summary.append(f"• {tea_type}\n  老友組合 x {q_old}")
            total_price += 1880 * q_old
            
    q_exp = st.number_input("輕體驗組(10入) $680", min_value=0, step=1)
    if q_exp > 0:
        order_summary.append(f"• {tea_type}\n  輕體驗組 x {q_exp}")
        total_price += 680 * q_exp

# --- 2. 藥膳燉湯區 ---
st.markdown('<div class="section-title">🥣 藥膳燉湯包 (需自燉)</div>', unsafe_allow_html=True)
with st.expander("點擊展開湯包品項 ($150 / $250)"):
    st.markdown("**$150/包 系列**")
    for s in ["獨家 四神藥膳", "獨家 四物藥膳", "秘 羊肉爐藥膳", "秘 胡椒雞藥膳"]:
        qty = st.number_input(f"{s} ($150)", min_value=0, step=1, key=s)
        if qty > 0:
            order_summary.append(f"• {s}燉湯包 x {qty}")
            total_price += 150 * qty
            
    st.markdown("**$250/包 系列**")
    for s in ["獨家 十全藥膳", "秘 人蔘雞藥膳", "秘 薑母鴨藥膳", "秘 何首烏藥膳"]:
        qty = st.number_input(f"{s} ($250)", min_value=0, step=1, key=s)
        if qty > 0:
            order_summary.append(f"• {s}燉湯包 x {qty}")
            total_price += 250 * qty

# --- 3. 日常真空調理區 ($90) ---
st.markdown('<div class="section-title">🛍️ 日常真空調理包 ($90/包)</div>', unsafe_allow_html=True)
for d in ["杜仲茶 (真空包)", "四物茶 (真空包)"]:
    d_qty = st.number_input(f"{d}", min_value=0, step=1, key=d)
    if d_qty > 0:
        order_summary.append(f"• {d} x {d_qty}")
        total_price += 90 * d_qty

# --- 4. 漢方代餐 ---
st.markdown('<div class="section-title">🌾 漢方代餐包 ($300/包)</div>', unsafe_allow_html=True)
m_qty = st.number_input("32味五穀養生餐", min_value=0, step=1)
if m_qty > 0:
    order_summary.append(f"• 32味五穀養生餐 x {m_qty}")
    total_price += 300 * m_qty

# ==========================================
# 第三步：訂閱制與自動結帳總計
# ==========================================
st.markdown("<br><hr style='border: 0.5px solid #E9EDC9;'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#7A8450;'>💎 每月訂閱・定額配送</h4>", unsafe_allow_html=True)
sub_choice = st.checkbox("✅ 我想加入「米寶健康訂閱制」，每月固定配送以上品項")

if total_price > 0:
    st.markdown(f'<p style="font-size: 1.45rem; font-weight: bold; color: #7A8450; text-align: center; margin-top: 15px;">🛒 本次預約總計：${total_price}</p>', unsafe_allow_html=True)
    
    sub_text = "【✅ 已開啟每月訂閱制固定配送】" if sub_choice else "【單次預約方案】"
    summary_str = "\n".join(order_summary)
    msg = f"Hi 米寶！🐢✨\n我已完成線上選購囉！\n{sub_text}\n---\n{summary_str}\n---\n💰 總計預約金額：${total_price}\n期待這份草本溫暖。🌿"
    
    st.code(msg, language=None)
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-top:10px; margin-bottom:5px;">點擊☆上框右上角☆複製訂單明細：</p>', unsafe_allow_html=True)
    
    line_url = "https://line.me/R/ti/p/@716osfvq"
    st.link_button("🌿 前往 LINE@ 貼上訂單並預約配送 ➔", line_url, use_container_width=True)

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜植感日常選物｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)

