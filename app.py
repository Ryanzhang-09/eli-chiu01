# %%
import streamlit as st
import pandas as pd

# 1. 页面配置
st.set_page_config(page_title="For Elizabeth, with Love ☁️", page_icon="💙")

# --- 2. 视觉风格：Ryan 的专属蓝色氛围 ---
st.markdown("""
<style>
    .stApp {
        background-color: #F0F8FF; /* 像云朵一样的淡蓝色 */
    }
    .main-title {
        color: #4A90E2;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
        font-size: 50px;
        margin-bottom: 0px;
    }
    .heart-box {
        text-align: center;
        font-size: 180px;
        color: #66CCFF;
        margin: -20px 0px;
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
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 网站内容 ---

# 蓝色大爱心 (带跳动效果)
st.markdown('<div class="heart-box">💙</div>', unsafe_allow_html=True)

# 专属标题
st.markdown('<h1 class="main-title">Elizabeth Chiu</h1>', unsafe_allow_html=True)
st.markdown('<p class="secret-note">"To the girl who carries the clouds in her heart..."</p>', unsafe_allow_html=True)

# --- 4. 互动组件 1：关于你的碎碎念 ---
st.write("---")
with st.expander("✨ A Little Secret from Ryan... (Click me)"):
    st.write(f"""
    Elizabeth, someone once said Anthropology is the study of what makes us human. 
    But looking at you, I think it's the study of how someone can be as sweet as a Cinnamon Roll. 
    I built this little corner of the internet just for you.
    """)

# --- 5. 互动组件 2：关于她的世界 (表格) ---
st.header("🌙 Her World")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Profile")
    about_df = pd.DataFrame({
        "Detail": ["Hometown", "Studying at", "Specialty"],
        "Value": ["Hong Kong 🇭🇰", "Davidson College 🏫", "Anthropology 🏺"]
    })
    st.table(about_df)

with col2:
    # 交互组件 2：选择她今天的心情
    mood = st.select_slider(
        "Elizabeth's Mood Today:",
        options=["Sleepy Cloud", "Fluffy Cinnamoroll", "Curious Scholar", "Energetic Hong Konger"]
    )
    st.write(f"Today, she is feeling like a **{mood}**. (Ryan thinks you're cute regardless!)")

# --- 6. 交互组件 3：为什么她是满分 (图表) ---
st.header("📊 Why She's Amazing")

# 交互组件 3：通过 Checkbox 解锁“隐藏分”
show_truth = st.checkbox("Unlock Ryan's True Observations")

if show_truth:
    stats = pd.DataFrame({
        "Attribute": ["Anthropology Wisdom", "Cinnamoroll Vibes", "Kindness", "Attractiveness to Ryan"],
        "Score": [95, 100, 98, 999] # 爆表的分数
    })
else:
    stats = pd.DataFrame({
        "Attribute": ["Anthropology Wisdom", "Cinnamoroll Vibes", "Kindness", "Attractiveness to Ryan"],
        "Score": [95, 100, 98, 100]
    })

st.bar_chart(stats.set_index("Attribute"), color="#66CCFF")

# --- 7. 页脚：私密留言 ---
st.sidebar.title("☁️ Message for Eli")
st.sidebar.write("If you're reading this at Davidson...")
if st.sidebar.button("Click for a hug"):
    st.sidebar.balloons()
    st.sidebar.success("A virtual hug from Ryan is on its way to North Carolina! 🧸")

st.sidebar.markdown("---")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Cinnamoroll_Sanrio_characters.png/220px-Cinnamoroll_Sanrio_characters.png")
