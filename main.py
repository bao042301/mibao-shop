
import streamlit as st
import os

# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 (終極防深色模式)
# ==========================================
st.set_page_config(page_title="米寶漢方｜植感日常選物", layout="centered")

st.markdown("""
    <style>
    /* 1. 品牌字體與全局高對比度設定 */
    /* 在 OS 開啟深色模式時，這段設定會強制文字保持高Legibility */
    p, label, h1, h2, h3, h4, h5, h6, li, div[data-testid="stMarkdownContainer"], span[data-testid="stMarkdownContainer"] p { 
        font-family: 'Noto Sans TC', sans-serif !important; 
        color: #FFFFFF !important; /* 全局設為白色，與深色背景形成強烈對比 */
        -webkit-text-fill-color: #FFFFFF !important; /* 強制文字填充顏色 */
        text-shadow: none !important;
    }
    
    /* 2. 標題與區塊設計 */
    /* 讓區塊標題（淡綠底）在黑化背景中脫穎而出 */
    .section-title { 
        background-color: #E9EDC9 !important; /* 淡綠色背景保持 */
        padding: 10px; 
        border-radius: 8px; 
        text-align: center; 
        font-weight: bold; 
        margin: 20px 0 10px; 
        font-size: 1.05rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    /* 區塊標題內的文字必須設為深綠色，與淡綠底對比 */
    .section-title p, .section-title h3 {
        color: #4A4E31 !important;
        -webkit-text-fill-color: #4A4E31 !important;
    }

    /* 3. Logo 尺寸 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    
    /* 4. 🚀 🚀 🚀 重點：徹底修復 NumberInput 黑底隱形按鈕與字體 */
    /* 將數量輸入框的背景設為深綠色，邊框淡綠色，文字白色 */
    [data-testid="stNumberInput"] div[data-baseweb="input"] {
        background-color: #7A8450 !important; /* 中等橄欖綠 */
        border: 1.5px solid #E9EDC9 !important; /* 淡綠色邊框 */
        border-radius: 8px !important;
    }
    [data-testid="stNumberInput"] input {
        color: #FFFFFF !important; /* 強制白色文字 */
        -webkit-text-fill-color: #FFFFFF !important;
    }
    /* 將加減按鈕漆上淡綠色圖示，消滅黑底 */
    [data-testid="stNumberInput"] button {
        background-color: transparent !important; /* 按鈕背景透明 */
        color: #E9EDC9 !important; /* 按鈕圖示 (+, -) 設為淡綠色，最高 LEGIBILITY */
        -webkit-text-fill-color: #E9EDC9 !important;
        border: 1px solid rgba(233, 237, 201, 0.3) !important;
    }
    
    /* 其他輸入框 (TextInput: 姓名、電話、地址) 背景與文字 */
    [data-testid="stTextInput"] div[data-baseweb="input"] {
        background-color: #7A8450 !important;
        border: 1.5px solid #E9EDC9 !important;
        border-radius: 8px !important;
    }
    [data-testid="stTextInput"] input {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }
    [data-testid="stTextInput"] input::placeholder {
        color: rgba(233, 237, 201, 0.6) !important; /* 淡綠色佔位符 */
    }

    /* Checkbox 文字與勾選框 */
    [data-testid="stCheckbox"] label div div[role="checkbox"] {
        border-color: #E9EDC9 !important;
        background-color: #7A8450 !important;
    }

    /* 5. LINE 原生跳轉按鈕樣式鎖定 */
    [data-testid="stLinkButton"] a {
        width: 100% !important; background-color: #06C755 !important; border-radius: 15px !important; height: 3.2em !important; 
        display: flex !important; justify-content: center !important; align-items: center !important; text-decoration: none !important;
    }
    [data-testid="stLinkButton"] a * { color: #FFFFFF !important; font-size: 1.05rem !important; font-weight: 900 !important; }

    /* 6. 🚀 🚀 🚀 終極修復「黑色複製框」與「隱形文字」 */
    /* 當 OS 變黑時，我們讓這個複製框也變成高對比度的深橄欖綠底，文字強制為白色 */
    [data-testid="stCodeBlock"] { 
        background-color: #7A8450 !important; /* 深橄欖綠底 */
        border: 1px solid #E9EDC9 !important; /* 淡綠色邊框 */
        border-radius: 12px !important; 
    }
    /* 強制複製框內所有代碼文字為白色，絕對 Legible */
    [data-testid="stCodeBlock"] code, [data-testid="stCodeBlock"] code *, [data-testid="stCodeBlock"] pre * {
        color: #FFFFFF !important; 
        -webkit-text-fill-color: #FFFFFF !important;
        text-shadow: none !important;
        font-family: 'Noto Sans TC', sans-serif !important;
    }
    [data-testid="stCodeBlock"] button { opacity: 1 !important; background-color: rgba(233, 237, 201, 1) !important; scale: 0.8; }

    /* 7. 頁尾固定 */
    .custom-footer { position: fixed; left: 0; bottom: 0; width: 100vw; text-align: center; background-color: rgba(74, 78, 49, 0.9); padding: 8px 0; z-index: 9999; box-shadow: 0 -2px 10px rgba(0,0,0,0.1); }
    .footer-text { font-size: 0.65rem !important; color: #E9EDC9 !important; margin: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 第二步：版面配置與商品陳列 (全面折疊版)
# ==========================================
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-style:italic; font-size:0.85rem; color:#8B8B7A; margin-bottom: 20px;">「將這份溫潤，訂製成您的日常習慣。」</p>', unsafe_allow_html=True)

order_summary = []
total_price = 0

# --- 1. 六種漢方茶飲 ---
st.markdown('<div class="section-title">🍵 漢方植感茶飲系列</div>', unsafe_allow_html=True)
with st.expander("點擊展開茶飲品項"):
    teas = ["黃耆元氣茶", "金菊牛蒡茶", "當歸紅棗茶", "黑豆漢方茶", "洛神山楂茶", "玫瑰決明茶"]
    for t in teas:
        qty = st.number_input(f"{t} (10入) $680", min_value=0, step=1, key=t)
        if qty > 0:
            order_summary.append(f"• {t}(10入) x {qty}")
            total_price += 680 * qty

# --- 2. 藥膳燉湯區 ---
st.markdown('<div class="section-title">🥣 藥膳燉湯包 (需自燉)</div>', unsafe_allow_html=True)
with st.expander("點擊展開湯包品項"):
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
st.markdown('<div class="section-title">🛍️ 日常真空調理包</div>', unsafe_allow_html=True)
with st.expander("點擊展開調理包品項"):
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
st.markdown('<div class="section-title">🌾 漢方代餐包</div>', unsafe_allow_html=True)
with st.expander("點擊展開代餐包品項"):
    m_qty = st.number_input("32味五穀養生餐 $300", min_value=0, step=1)
    if m_qty > 0:
        order_summary.append(f"• 32味五穀養生餐 x {m_qty}")
        total_price += 300 * m_qty

# ==========================================
# 第三步：顧客資訊、溫暖提示與結帳總計
# ==========================================
st.markdown("<br><hr style='border: 0.5px solid #E9EDC9; rgba(233, 237, 201, 0.3);'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#E9EDC9;'>📝 配送資訊與結帳</h4>", unsafe_allow_html=True)

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
        <div style='background-color:transparent; border-left: 5px solid #E8A87C; padding:12px; border-radius:5px; margin-bottom:15px; border: 1px solid rgba(232, 168, 124, 0.3);'>
            <p style='color:#E8A87C; font-weight:bold; margin:0; font-size:0.95rem; -webkit-text-fill-color: #E8A87C !important;'>🐢 溫馨小提醒：</p>
            <p style='color:#FDFBF7; margin:5px 0 0; font-size:0.9rem; -webkit-text-fill-color: #FDFBF7 !important;'>您尚未填寫完整的「<b>{'、'.join(missing_fields)}</b>」，記得補上資訊，米寶才能將溫暖順利送達給您喔！</p>
        </div>
        """, unsafe_allow_html=True)

    # 顯眼大字體總金額
    st.markdown(f'<p style="font-size: 1.5rem; font-weight: 900; color: #FFFFFF; text-align: center; margin: 20px 0; background-color: rgba(122, 132, 80, 0.5); padding: 10px; border-radius: 10px; -webkit-text-fill-color: #FFFFFF !important;">🛒 本次預約總計：${total_price}</p>', unsafe_allow_html=True)
    
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

# 更新頁尾在深色模式下的 LEGIBILITY
st.markdown("""<div class="custom-footer"><p class="footer-text" style="-webkit-text-fill-color: #E9EDC9 !important;">米寶漢方｜植感日常選物｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
