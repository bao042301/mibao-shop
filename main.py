import streamlit as st
import os

# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 (絕對明亮抗干擾)
# ==========================================
st.set_page_config(page_title="米寶漢方｜植感日常選物", layout="centered")

st.markdown("""
    <style>
    /* 1. 安全字體設定 (精準避開系統圖示，終結 _arrow_right 亂碼) */
    .stApp, header { background-color: #FDFBF7 !important; }
    p, h1, h2, h3, h4, h5, h6, label, li { 
        font-family: 'Noto Sans TC', sans-serif !important; 
        color: #4A4E31 !important; 
    }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 90px !important; }

    /* 2. 標題與 Logo 設計 */
    h3 { font-size: 1.15rem !important; font-weight: 700 !important; margin: 20px 0 10px !important; text-align: center !important; color: #7A8450 !important; letter-spacing: 1px; }
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    
    /* 3. 🚀 整合式折疊標題 (把原本的綠底直接給展開選單) */
    [data-testid="stExpander"] details { 
        border: none !important; 
        background-color: transparent !important; 
        margin-bottom: 10px !important;
    }
    [data-testid="stExpander"] summary { 
        background-color: #E9EDC9 !important; 
        border-radius: 8px !important; 
        padding: 12px 15px !important; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    /* 展開選單的標題文字放大加粗，取代原本的 Section Title */
    [data-testid="stExpander"] summary p { 
        font-size: 1.1rem !important; 
        font-weight: 900 !important; 
        color: #4A4E31 !important; 
        -webkit-text-fill-color: #4A4E31 !important; 
    }
    /* 箭頭顏色 */
    [data-testid="stExpander"] summary svg {
        fill: #4A4E31 !important;
        color: #4A4E31 !important;
    }

    /* 4. 抗深色模式：輸入框與按鈕 */
    div[data-baseweb="input"], div[data-baseweb="base-input"] { 
        background-color: #FFFFFF !important; 
        border: 1.5px solid #E9EDC9 !important; 
        border-radius: 8px !important; 
    }
    input { 
        background-color: #FFFFFF !important; 
        color: #4A4E31 !important; 
        -webkit-text-fill-color: #4A4E31 !important; 
        font-weight: bold !important;
    }
    input::placeholder { color: rgba(74, 78, 49, 0.5) !important; -webkit-text-fill-color: rgba(74, 78, 49, 0.5) !important; font-weight: normal !important;}
    
    [data-testid="stNumberInput"] button {
        background-color: #F1F4E8 !important;
        color: #4A4E31 !important;
        border: none !important;
    }
    [data-testid="stNumberInput"] button * { color: #4A4E31 !important; fill: #4A4E31 !important; }

    /* Checkbox 防黑底 */
    [data-testid="stCheckbox"] label > div:first-child { background-color: #FFFFFF !important; border: 2px solid #7A8450 !important; }
    [data-testid="stCheckbox"] p { color: #4A4E31 !important; -webkit-text-fill-color: #4A4E31 !important; }

    /* 5. LINE 原生跳轉按鈕 */
    [data-testid="stLinkButton"] a {
        width: 100% !important; background-color: #06C755 !important; border-radius: 15px !important; height: 3.2em !important; 
        display: flex !important; justify-content: center !important; align-items: center !important; text-decoration: none !important;
    }
    [data-testid="stLinkButton"] a p { color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; font-size: 1.05rem !important; font-weight: 900 !important; margin:0 !important; }

    /* 6. 複製訂單框強制淺色底綠字 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre { 
        background-color: #F8F9F1 !important; 
        border: 1px solid #E9EDC9 !important; 
        border-radius: 12px !important; 
    }
    [data-testid="stCodeBlock"] code, [data-testid="stCodeBlock"] span, [data-testid="stCodeBlock"] * {
        color: #4A4E31 !important; 
        -webkit-text-fill-color: #4A4E31 !important;
        background-color: transparent !important;
        text-shadow: none !important;
    }
    [data-testid="stCodeBlock"] button { opacity: 1 !important; background-color: #E9EDC9 !important; scale: 0.8; }

    /* 7. 頁尾 */
    .custom-footer { position: fixed; left: 0; bottom: 0; width: 100vw; text-align: center; background-color: #FDFBF7; padding: 8px 0; z-index: 9999; box-shadow: 0 -2px 10px rgba(0,0,0,0.03); border-top: 1px solid #E9EDC9; }
    .footer-text { font-size: 0.65rem !important; color: #8B8B7A !important; -webkit-text-fill-color: #8B8B7A !important; margin: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 第二步：版面配置與商品陳列 (整合大標題折疊版)
# ==========================================
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-style:italic; font-size:0.85rem; color:#8B8B7A; margin-bottom: 25px;">「將這份溫潤，訂製成您的日常習慣。」</p>', unsafe_allow_html=True)

order_summary = []
total_price = 0

# --- 1. 六種漢方茶飲 ---
with st.expander("🍵 漢方植感茶飲系列 (10入)"):
    teas = ["黃耆元氣茶", "金菊牛蒡茶", "當歸紅棗茶", "黑豆漢方茶", "洛神山楂茶", "玫瑰決明茶"]
    for t in teas:
        qty = st.number_input(f"{t} $680", min_value=0, step=1, key=t)
        if qty > 0:
            order_summary.append(f"• {t}(10入) x {qty}")
            total_price += 680 * qty

# --- 2. 藥膳燉湯區 ---
with st.expander("🥣 藥膳燉湯包 (需自燉)"):
    st.markdown("**【 $150/包 系列 】**")
    for s in ["獨家 四神藥膳", "獨家 四物藥膳", "秘 羊肉爐藥膳", "秘 胡椒雞藥膳"]:
        qty = st.number_input(f"{s} ($150)", min_value=0, step=1, key=s)
        if qty > 0:
            order_summary.append(f"• {s}燉湯包 x {qty}")
            total_price += 150 * qty
            
    st.markdown("**【 $250/包 系列 】**")
    for s in ["獨家 十全藥膳", "秘 人蔘雞藥膳", "秘 薑母鴨藥膳", "秘 何首烏藥膳"]:
        qty = st.number_input(f"{s} ($250)", min_value=0, step=1, key=s)
        if qty > 0:
            order_summary.append(f"• {s}燉湯包 x {qty}")
            total_price += 250 * qty

# --- 3. 日常真空調理區 ---
with st.expander("🛍️ 日常真空調理包"):
    d_qty1 = st.number_input("杜仲茶 (真空包) $90", min_value=0, step=1, key="杜仲")
    if d_qty1 > 0:
        order_summary.append(f"• 杜仲茶(真空包) x {d_qty1}")
        total_price += 90 * d_qty1

    d_qty2 = st.number_input("四物茶 (真空包) $80", min_value=0, step=1, key="四物")
    if d_qty2 > 0:
        order_summary.append(f"• 四物茶(真空包) x {d_qty2}")
        total_price += 80 * d_qty2

    bz_qty = st.number_input("八珍茶 (真空包) $95", min_value=0, step=1, key="八珍")
    if bz_qty > 0:
        order_summary.append(f"• 八珍茶(真空包) x {bz_qty}")
        total_price += 95 * bz_qty

# --- 4. 漢方代餐 ---
with st.expander("🌾 漢方代餐包"):
    m_qty = st.number_input("32味五穀養生餐 $300", min_value=0, step=1)
    if m_qty > 0:
        order_summary.append(f"• 32味五穀養生餐 x {m_qty}")
        total_price += 300 * m_qty

# ==========================================
# 第三步：顧客資訊、溫暖提示與結帳總計
# ==========================================
st.markdown("<br><h4 style='text-align:center; color:#7A8450; font-weight:900;'>📝 配送資訊與結帳</h4>", unsafe_allow_html=True)

# 完整顧客資訊欄位
name = st.text_input("👤 收件人姓名", placeholder="請填寫您的姓名...")
phone = st.text_input("📱 聯絡電話", placeholder="請填寫您的手機號碼...")
address = st.text_input("📍 收件地址", placeholder="請填寫您的完整收件地址...")

sub_choice = st.checkbox("✅ 我想加入「米寶健康訂閱制」，每月固定配送以上品項")

if total_price > 0:
    # 溫馨小提醒邏輯：檢查是否有漏填
    missing_fields = []
    if not name: missing_fields.append("姓名")
    if not phone: missing_fields.append("電話")
    if not address: missing_fields.append("收件地址")
    
    if missing_fields:
        st.markdown(f"""
        <div style='background-color:#FDF5E6; border-left: 5px solid #E8A87C; padding:12px; border-radius:5px; margin-bottom:15px;'>
            <p style='color:#C38D5E !important; -webkit-text-fill-color: #C38D5E !important; font-weight:bold; margin:0; font-size:0.95rem;'>🐢 溫馨小提醒：</p>
            <p style='color:#8B8B7A !important; -webkit-text-fill-color: #8B8B7A !important; margin:5px 0 0; font-size:0.9rem;'>您尚未填寫完整的「<b>{'、'.join(missing_fields)}</b>」，記得補上資訊，米寶才能將溫暖順利送達給您喔！</p>
        </div>
        """, unsafe_allow_html=True)

    # 顯眼大字體總金額
    st.markdown(f'<p style="font-size: 1.5rem; font-weight: 900; color: #7A8450 !important; -webkit-text-fill-color: #7A8450 !important; text-align: center; margin: 20px 0; background-color: #F1F4E8; padding: 10px; border-radius: 10px;">🛒 本次預約總計：${total_price}</p>', unsafe_allow_html=True)
    
    sub_text = "【✅ 已開啟每月訂閱制固定配送】" if sub_choice else "【單次預約方案】"
    summary_str = "\n".join(order_summary)
    
    # 組合顧客資訊
    info_str = f"👤 姓名：{name if name else '(未填寫)'}\n📱 電話：{phone if phone else '(未填寫)'}\n📍 地址：{address if address else '(未填寫)'}"
    
    msg = f"Hi 米寶！🐢✨\n我已完成線上選購囉！\n{sub_text}\n---\n{summary_str}\n---\n{info_str}\n💰 總計預約金額：${total_price}\n期待這份草本溫暖。🌿"
    
    # 複製代碼框
    st.code(msg, language=None)
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-top:10px; margin-bottom:5px;">點擊☆上框右上角☆複製訂單明細：</p>', unsafe_allow_html=True)
    
    line_url = "https://line.me/R/ti/p/@716osfvq"
    st.link_button("🌿 前往 LINE@ 貼上訂單並預約配送 ➔", line_url, use_container_width=True)

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜植感日常選物｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
