import streamlit as st

# 设置页面配置
st.set_page_config(page_title="感谢黛玉", page_icon="❤️", layout="wide")

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
        font-family: Arial, sans-serif;
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
st.markdown(
    """
    <div class="container">
        <div class="title">🎉 感谢黛玉 🎉</div>
        <div class="subtitle">黛玉，你是我生命中的光！</div>
        <div class="message">
            感谢你一直以来的支持和陪伴！<br>
            黛玉，你的善良和温柔让我感到无比温暖。感谢你在我最需要的时候陪伴在我身边。<br>
            你是我生命中最重要的人，我会永远珍惜你。<br>
            愿你的每一天都充满阳光和快乐！
        </div>
        <button class="button" onclick="location.reload()">再次观看</button>
    </div>
    """,
    unsafe_allow_html=True
)
