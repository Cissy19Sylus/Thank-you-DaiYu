import streamlit as st
from PIL import Image
import base64

# 设置页面配置
st.set_page_config(page_title="感谢我的委托老师", layout="wide")

# 自定义 CSS 样式
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f9f2f4; /* 浅粉色背景 */
        color: #333;
    }
    .container {
        text-align: center;
        padding: 20px;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #ffcccc; /* 浅粉色 */
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #ffcc66; /* 浅黄色 */
        margin-bottom: 40px;
    }
    .message {
        font-size: 18px;
        line-height: 1.6;
        margin-bottom: 40px;
        color: #666;
    }
    .button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        background-color: #ffcccc;
        color: #333;
        border: none;
        border-radius: 5px;
    }
    .button:hover {
        background-color: #ffcc66;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 页面内容
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<div class='title'>Thank You</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>MAKE A WISH</div>", unsafe_allow_html=True)

# 添加照片
photo = Image.open("path_to_your_photo.jpg")  # 替换为你的照片路径
st.image(photo, caption="A Special Day", use_column_width=True)

# 添加视频
with open("path_to_your_video.mp4", "rb") as video_file:
    video_bytes = video_file.read()
st.video(video_bytes)

# 添加音乐
with open("path_to_your_music.mp3", "rb") as audio_file:
    audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

# 祝福文字
st.markdown("<div class='message'>May this love and happiness always be with you! ;)</div>", unsafe_allow_html=True)
st.markdown("<div class='message'>Thank you for being my special someone!</div>", unsafe_allow_html=True)

# 显示按钮
st.markdown("<button class='button' onclick='location.reload()'>Watch Again</button>", unsafe_allow_html=True)

# 创意元素：添加一个随机祝福语
import random
blessings = [
    "Wishing you all the joy you bring to others!",
    "Here's to another year of wonderful memories!",
    "May your day be as special as you are!"
]
st.write(random.choice(blessings))

# 创意元素：添加一个互动环节
st.write("Please leave a message for your special someone:")
user_message = st.text_input("Your message", "")
if st.button("Send"):
    st.write("Message sent with love!")

# 结束标记
st.markdown("</div>", unsafe_allow_html=True)
