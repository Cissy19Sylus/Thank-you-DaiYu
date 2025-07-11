import streamlit as st
from PIL import Image
import base64

# 设置页面配置
st.set_page_config(page_title="黛玉加油！！", layout="wide")

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
st.markdown("<div class='title'>我真的很感谢你，黛玉</div>", unsafe_allow_html=True)


# 读取视频文件
with open('7月9日(1).mp4', 'rb') as video_file:
    video_bytes = video_file.read()

# 使用st.video并设置autoplay和muted
st.video(video_bytes, autoplay=True, muted=False)

st.markdown('清晰度致歉，Github只能上传25MB的文件')


# 祝福文字
st.markdown("<div class='message'>愿这份爱和快乐永远伴随着你！;)</div>", unsafe_allow_html=True)
st.markdown("<div class='message'>感谢你成为我特别的人！</div>", unsafe_allow_html=True)



# 创意元素：添加一个随机祝福语
import random
blessings = [
    "愿你的每一天都充满阳光和快乐！",
    "祝你年年有今日，岁岁有今朝！",
    "愿你的生活比蜜甜，幸福无边！"
]
st.write(random.choice(blessings))

# 创意元素：添加一个互动环节
st.write("请留下你想对她说的悄悄话：")
user_message = st.text_input("你的悄悄话", "")
if st.button("发送"):
    st.write("你的心意已发送！")

# 结束标记
st.markdown("</div>", unsafe_allow_html=True)
