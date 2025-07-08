import streamlit as st
import time

# 设置页面配置
st.set_page_config(page_title="感谢黛玉", layout="wide")

# 自定义 CSS 样式
st.markdown(
    """
    <style>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        font-family: 'Arial', sans-serif;
    }
    .container {
        text-align: center;
    }
    .title {
        font-size: 48px;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        margin-bottom: 40px;
    }
    .message {
        font-size: 18px;
        line-height: 1.6;
        margin-bottom: 40px;
    }
    .button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 页面内容
def type_writer(text, speed=0.05):
    empty = st.empty()
    for i in range(len(text)):
        empty.text_area(text[:i+1], height=200)
        time.sleep(speed)

# 显示标题
st.markdown("<div class='title'>🎉 感谢黛玉 🎉</div>", unsafe_allow_html=True)

# 显示副标题
st.markdown("<div class='subtitle'>黛玉，你是我生命中的光！</div>", unsafe_allow_html=True)

# 显示消息
message = "感谢你一直以来的支持和陪伴！黛玉，你的善良和温柔让我感到无比温暖。感谢你在我最需要的时候陪伴在我身边。你是我生命中最重要的人，我会永远珍惜你。愿你的每一天都充满阳光和快乐！"
type_writer(message)

# 显示按钮
st.markdown("<button class='button' onclick='location.reload()'>再次观看</button>", unsafe_allow_html=True)
