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
st.markdown("<div class='message'>好事来，好运来，全都缠上黛玉来！</div>", unsafe_allow_html=True)
st.markdown("<div class='message'>感谢小黛成为我特别的人！</div>", unsafe_allow_html=True)



# 特别惊喜
st.markdown('<h3>🎉 特别惊喜 🎉</h3>', unsafe_allow_html=True)
st.markdown("点击下方按钮，给小黛一个特别的惊喜！")

if st.button("🎉 求你了小黛点一下吧 🎉"):
    st.balloons()

    st.markdown(
        """
        <div class="surprise">
            <h3>🎈 亲密度+10000！🎈</h3>
            <p>小黛你超棒的</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 页脚
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p>🎉 希望小黛平安健康！且喜且乐！ 🎉</p>
        <p> 以上内容全部为小果冻一人制作啦，学术不精，只能做成这样啦，小黛见谅 </p>
        <p> 不见谅也得见谅╭(╯^╰)╮ </p>
    </div>
    """,
    unsafe_allow_html=True
)
