# %%
import streamlit as st

# --- 1. 页面配置 (必须是第一行 Streamlit 命令) ---
st.set_page_config(
    page_title="Elizabeth's Kawaii Resume ☁️",
    page_icon="🐶",
    layout="centered"
)

# --- 2. 自定义 CSS (关键 coding 部分，用于实现卡哇伊风格和蓝色爱心) ---
st.markdown("""
<style>
    /* 1. 设置整体网页背景为淡蓝色/白色，像天空和云朵 */
    .stApp {
        background-color: #E6F7FF; /* 淡天空蓝 */
    }

    /* 2. 自定义标题字体颜色 (玉桂狗的蓝色) */
    h1, h2, h3, p {
        color: #4A90E2; 
        font-family: 'Comic Sans MS', cursive, sans-serif; /* 卡哇伊字体 */
    }

    /* 3. 设计蓝色大爱心 */
    .blue-heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 150px;
        margin-top: -30px;
    }

    .blue-heart {
        font-size: 150px; /* 大大的爱心 */
        color: #66CCFF; /* 玉桂狗的主体蓝色 */
        text-shadow: 0 0 15px rgba(102, 204, 255, 0.7);
    }
</style>
""", unsafe_allow_html=True)


# --- 3. 网站内容 ---

# --- 大大的蓝色爱心 (用 HTML 代码实现) ---
st.markdown('<div class="blue-heart-container"><span class="blue-heart">💙</span></div>', unsafe_allow_html=True)

# --- 主标题 ---
st.title("Elizabeth Chiu ☁️")
st.subheader("Anthropology Student | Cinnamoroll Fan")

# --- 个人简介 (玉桂狗风格) ---
col1, col2 = st.columns([1, 2])
with col1:
    # 交互组件 1: 显示/隐藏头像
    show_avatar = st.checkbox("Show My Cinnamoroll Avatar")
    if show_avatar:
        st.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Cinnamoroll_Sanrio_characters.png/220px-Cinnamoroll_Sanrio_characters.png", width=150, caption="Cloud-like Friend!")

with col2:
    st.markdown("""
    Hey there! I'm Elizabeth, a cloud-soft spirit with a deep love for **Cinnamoroll**! Just like my fluffy friend, I'm always curious and ready for an adventure.
    
    My favorite things are **cinnamon rolls**, fluffy clouds, and understanding the cozy stories behind people and cultures.
    """)

# --- 基础信息 (表格展示) ---
st.header("🐾 About Me")
st.markdown("""
- 🇭🇰 **Hometown**: Hong Kong (From the busy streets to the fluffy clouds!)
- 🏫 **University**: **Davidson College** (Currently exploring the human cozy-verse!)
- 📚 **Major**: **Anthropology** (Studying how humans make their own 'warm cinnamon rolls' of culture!)
""")


# --- 技能/爱好图表 (图表展示 + 交互组件 2) ---
st.header("🛠 'Floppy Ear' Skills & Hobbies")

# 交互组件 2: 选择框切换视图
skill_view = st.selectbox("Show me how Elizabeth does...", ["Magic Skills", "Cinnamoroll Cozy Tasks"])

# 准备数据结构
if skill_view == "Magic Skills":
    skills_data = {
        "Skill": ["Anthropology Theory", "Ethnographic Research", "Cross-Cultural Communication", "Cinnamon Roll Making"],
        "Level": [85, 90, 80, 100]
    }
else:
    skills_data = {
        "Skill": ["Flying with Big Ears", "Dreaming of Clouds", "Making Friends", "Being Fluffy"],
        "Level": [100, 95, 100, 100]
    }

# 绘制图表 (使用 st.bar_chart)
st.bar_chart(skills_data, x="Skill", y="Level", color="#66CCFF")

# --- 联系方式 (侧边栏) ---
st.sidebar.title("Connect with Elizabeth!")
st.sidebar.markdown("If you want to share some cinnamon rolls or talk about Anthropology...")
st.sidebar.write("📧 [Elizabeth@email.com](mailto:elizabeth@email.com)")

# 交互组件 3: 侧边栏开关，改变页面布局
wide_layout = st.sidebar.toggle("Enable Super Wide Layout")
if wide_layout:
    st.set_page_config(layout="wide")