import streamlit as st
import pandas as pd
import os

# 页面配置
st.set_page_config(page_title="Ryan's Love 💙", page_icon="☁️", layout="wide")

cinnamoroll_img = "https://www.pngkit.com/png/detail/325-3258825_cinnamoroll-transparent.png"

# ========= 本地持久化计数器 =========
COUNTER_FILE = "hug_counter.txt"

def load_count():
    if os.path.exists(COUNTER_FILE):
        try:
            with open(COUNTER_FILE, "r", encoding="utf-8") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def save_count(count):
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        f.write(str(count))

# 读取当前计数
count = load_count()

# CSS 样式
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg,#EAF6FF,#F7FBFF);
}

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:800;
    color:#2A6EDB;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#555;
}

.heart{
    text-align:center;
    font-size:120px;
    color:#6EC6FF;
    animation:pulse 1.6s infinite;
}

@keyframes pulse{
0%{transform:scale(1)}
50%{transform:scale(1.08)}
100%{transform:scale(1)}
}

.section-title{
    font-size:26px;
    font-weight:700;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# --- 侧边栏 ---
st.sidebar.image(cinnamoroll_img, width=160)
st.sidebar.title("☁️ Hug Station")

if st.sidebar.button("Click to send a hug 💙💙💙"):
    count += 1
    save_count(count)
    st.sidebar.balloons()
    st.sidebar.success(f"You sent a hug! Elizabeth now has {count} total.")

st.sidebar.metric(label="Total Hugs from Ryan", value=count)

# Header 图片
colA, colB, colC = st.columns([1,2,1])
with colB:
    st.image(cinnamoroll_img, width=300)

# 爱心
st.markdown('<div class="heart">💙</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">RYAN\'S PROFESSIONAL LOVE</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Featuring Elizabeth\'s Cinnamoroll Faves</div>', unsafe_allow_html=True)

st.divider()

# 表格
st.markdown('<div class="section-title">The Elizabeth & Cinnamoroll Effect</div>', unsafe_allow_html=True)

df = pd.DataFrame({
    "Attribute": ["Elizabeth Chiu"],
    "Davidson Major": ["Anthropology"],
    "Favorite Hong Kong Spot": ["TBA"],
    "Cinnamoroll Level": ["Maximum Fluff"]
})
st.table(df)

# 图表
st.markdown('<div class="section-title">Fluffy Faves & Skills Timeline</div>', unsafe_allow_html=True)

chart = pd.DataFrame({
    "Month": ["July","Aug","Sep","Oct","Nov","Dec"],
    "Cinnamoroll Passion": [25,40,55,70,85,100]
})
st.bar_chart(chart.set_index("Month"))

# 互动
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌙 Her Profile")
    profile = pd.DataFrame({
        "Detail": ["Hometown","University","Major","Fluff Level"],
        "Value": ["Hong Kong 🇭🇰","Davidson College","Anthropology","100%"]
    })
    st.table(profile)

with col2:
    mood = st.select_slider(
        "How is Elizabeth feeling?",
        options=["Sleepy","Fluffy","Studying","Misses HK"]
    )
    st.write(f"Ryan says: Even as **{mood}**, you're still amazing.")

# hidden stats
st.subheader("📊 Why You're Amazing")
unlock = st.checkbox("Unlock Ryan's secret observations")

if unlock:
    stats = pd.DataFrame({
        "Attribute": ["Anthropology Wisdom","Cinnamoroll Energy","Kindness","Ryan's Adoration"],
        "Score": [100,100,100,999]
    })
else:
    stats = pd.DataFrame({
        "Attribute": ["Anthropology Wisdom","Cinnamoroll Energy","Kindness","Ryan's Adoration"],
        "Score": [100,100,100,100]
    })

st.bar_chart(stats.set_index("Attribute"))

st.divider()
st.caption("Made with 💙 by Ryan | For Elizabeth")
