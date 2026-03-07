# %%
import streamlit as st
import pandas as pd

# 1. 页面配置
st.set_page_config(page_title="For Elizabeth, with Love ☁️", page_icon="💙")

# --- 2. 视觉风格：Ryan 的专属蓝色氛围 (包含心跳动画) ---
st.markdown("""
<style>
    .stApp {
        background-color: #F0F8FF; 
    }
    .main-title {
        color: #4A90E2;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
        font-size: 45px;
        margin-top: -20px;
    }
    .heart-box {
        text-align: center;
        font-size: 150px;
        color: #66CCFF;
        margin: -30px 0px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .secret-note {
        font-style: italic;
        color: #888;
        text-align: center;
        margin-bottom: 20px;
    }
    /* 让侧边栏图片变圆一点 */
    [data-testid="stSidebarNav"] {margin-top: -50px;}
</style>
""", unsafe_allow_html=True)

# --- 3. 侧边栏：放第二张玉桂狗头像 ---
st.sidebar.image("https://static.wikia.nocookie.net/sanrio/images/2/23/Cinnamoroll.png/revision/latest/scale-to-width-down/340?cb=20170220231727", width=150)
st.sidebar.title("☁️ Message for Eli")
st.sidebar.write("Hey Elizabeth, if you're reading this at Davidson...")

if st.sidebar.button("Click for a hug"):
    st.sidebar.balloons()
    st.sidebar.success("A virtual hug from Ryan is flying to NC! 🧸")

# --- 4. 主页面：顶部放你上传的那张吃蛋糕的玉桂狗 ---
# 注意：在本地运行时，请确保图片 image_450440.png 和 app.py 在同一个文件夹
# 如果已经部署，建议将这张图也上传到 GitHub 仓库
try:
    st.image("image_450440.png", use_container_width=True)
except:
    # 如果图片还没上传成功，先用占位符防止报错
    st.write("*(Cinnamoroll is eating cake here... 🍰)*")

# 蓝色大爱心
st.markdown('<div class="heart-box">💙</div>', unsafe_allow_html=True)

# 专属标题
st.markdown('<h1 class="main-title">Elizabeth Chiu</h1>', unsafe_allow_html=True)
st.markdown('<p class="secret-note">"To the girl who makes my world feel like a soft blue cloud."</p>', unsafe_allow_html=True)

# --- 5. 互动部分：关于她的世界 ---
st.write("---")
with st.expander("✨ A Little Secret from Ryan..."):
    st.write(f"""
    Elizabeth, Anthropology says culture is shared, but I think the best part of my culture 
    is just spending time with you. I hope Davidson is treating its favorite Hong Konger well today.
    """)

# 表格展示
st.header("🌙 Her Profile")
col1, col2 = st.columns(2)

with col1:
    about_df = pd.DataFrame({
        "Detail": ["Hometown", "University", "Major", "Cinnamoroll Level"],
        "Value": ["Hong Kong 🇭🇰", "Davidson College 🏫", "Anthropology 🏺", "100% Fluffy"]
    })
    st.table(about_df)

with col2:
    mood = st.select_slider(
        "How is Elizabeth feeling right now?",
        options=["Sleepy", "Fluffy", "Studying Hard", "Misses HK"]
    )
    st.write(f"Ryan says: Even as a **{mood}** Cinnamoroll, you're the best.")

# --- 6. 为什么她是满分 (图表) ---
st.header("📊 Why You're Amazing")
show_truth = st.checkbox("Unlock Ryan's Hidden Observations")

if show_truth:
    stats = pd.DataFrame({
        "Attribute": ["Anthropology Wisdom", "Cinnamoroll Vibes", "Kindness", "Ryan's Adoration"],
        "Score": [95, 100, 98, 999] 
    })
else:
    stats = pd.DataFrame({
        "Attribute": ["Anthropology Wisdom", "Cinnamoroll Vibes", "Kindness", "Ryan's Adoration"],
        "Score": [95, 100, 98, 100]
    })

st.bar_chart(stats.set_index("Attribute"), color="#66CCFF")

st.markdown("---")
st.caption("Made with 💙 by Ryan | For Elizabeth's eyes only")
