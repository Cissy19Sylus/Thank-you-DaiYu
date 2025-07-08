import streamlit as st

# 设置页面配置
st.set_page_config(page_title="感谢黛玉", page_icon="❤️", layout="wide")

# 自定义 CSS 样式
st.markdown(
    """
    <style>
    .container {
        height: 100vh;
        width: 100vw;
        margin: 0 auto;
        text-align: center;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .one {
        font-size: 4.5rem;
        animation: fadeIn 1s ease-in-out;
    }
    .two {
        font-size: 1.2rem;
        font-weight: lighter;
        animation: fadeIn 1s ease-in-out 1s;
    }
    .three {
        font-size: 3rem;
        animation: fadeIn 1s ease-in-out 2s;
    }
    .four {
        width: 600px;
        margin: 20px auto;
        border: 3px solid #aaa;
        border-radius: 5px;
        padding: 10px;
        position: relative;
        animation: fadeIn 1s ease-in-out 3s;
    }
    .text-box p {
        margin: 0;
        text-align: left;
    }
    .fake-btn {
        position: absolute;
        right: 5px;
        bottom: 5px;
        color: #fff;
        background-color: rgb(21, 161, 237);
        padding: 5px 8px;
        border-radius: 3px;
    }
    .five p {
        font-size: 2rem;
        position: absolute;
        left: 0;
        right: 0;
        animation: fadeIn 1s ease-in-out 4s;
    }
    .idea-3 strong {
        padding: 3px 5px;
        border-radius: 3px;
        display: inline-block;
    }
    .idea-5 {
        font-size: 4rem;
        animation: fadeIn 1s ease-in-out 5s;
    }
    .idea-6 {
        font-size: 15rem;
        animation: fadeIn 1s ease-in-out 6s;
    }
    .six img {
        display: inline-block;
        max-width: 100%;
        height: auto;
        animation: fadeIn 1s ease-in-out 7s;
    }
    .six .hat {
        position: absolute;
        width: 80px;
        top: -35px;
        left: 41.5%;
        animation: fadeIn 1s ease-in-out 7s;
    }
    .baloons img {
        display: inline-block;
        position: absolute;
        animation: floatUp 3s ease-in-out infinite;
    }
    .baloons img:nth-child(even) {
        left: -10%;
    }
    .baloons img:nth-child(odd) {
        right: -10%;
    }
    .baloons img:nth-child(3n + 0) {
        left: 30%;
    }
    .eight svg {
        width: 25px;
        position: absolute;
        top: 0;
        left: 0;
        visibility: hidden;
        z-index: -1;
    }
    .eight svg:nth-child(1) {
        top: 7vh;
        left: 5vw;
        fill: #bd6ecf;
    }
    .eight svg:nth-child(2) {
        top: 23vh;
        left: 35vw;
        fill: #7dd175;
    }
    .eight svg:nth-child(3) {
        top: 33vh;
        left: 23vw;
        fill: #349d8b;
    }
    .eight svg:nth-child(4) {
        top: 43vh;
        left: 57vw;
        fill: #347a9d;
    }
    .eight svg:nth-child(5) {
        top: 68vh;
        left: 7vw;
        fill: #c66053;
    }
    .eight svg:nth-child(6) {
        top: 42vh;
        left: 77vw;
        fill: #bfaa40;
    }
    .eight svg:nth-child(7) {
        top: 68vh;
        left: 83vw;
        fill: #e3bae8;
    }
    .eight svg:nth-child(8) {
        top: 86vh;
        left: 37vw;
        fill: #8762cb;
    }
    .eight svg:nth-child(9) {
        top: 94vh;
        left: 87vw;
        fill: #9a90da;
    }
    .wish-hbd {
        font-size: 3em;
        margin: 0;
        text-transform: uppercase;
        animation: fadeIn 1s ease-in-out 8s;
    }
    .wish h5 {
        font-weight: lighter;
        font-size: 2rem;
        margin: 10px 0 0;
        animation: fadeIn 1s ease-in-out 8s;
    }
    .nine p {
        font-size: 2rem;
        font-weight: lighter;
        animation: fadeIn 1s ease-in-out 9s;
    }
    #replay {
        z-index: 3;
        cursor: pointer;
        animation: fadeIn 1s ease-in-out 10s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes floatUp {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-50px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 页面内容
st.markdown(
    """
    <div class="container">
        <div class="one">🎉 感谢黛玉 🎉</div>
        <div class="two">黛玉，你是我生命中的光！</div>
        <div class="three">感谢你一直以来的支持和陪伴！</div>
        <div class="four">
            <div class="text-box">
                <p>黛玉，你的善良和温柔让我感到无比温暖。感谢你在我最需要的时候陪伴在我身边。</p>
                <div class="fake-btn">感谢</div>
            </div>
        </div>
        <div class="five">
            <p class="idea-1">你的每一个微笑都让我感到幸福。</p>
            <p class="idea-2">你的每一个鼓励都让我充满力量。</p>
            <p class="idea-3">你是我生命中最重要的人，我会永远珍惜你。</p>
            <p class="idea-4">因为有你，我的生活充满了阳光。</p>
            <p class="idea-5">你是我心中的宝藏，我永远爱你！</p>
            <p class="idea-6">THANK YOU!</p>
        </div>
        <div class="six">
            <img src="https://example.com/daiyu.jpg" alt="黛玉" class="lydia-dp">
            <img src="https://example.com/hat.svg" alt="帽子" class="hat">
        </div>
        <div class="seven">
            <div class="baloons">
                <img src="https://example.com/balloon1.svg" alt="气球">
                <img src="https://example.com/balloon2.svg" alt="气球">
            </div>
        </div>
        <div class="eight">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
        </div>
        <div class="nine">
            <p>愿你的每一天都充满阳光和快乐！</p>
        </div>
        <button id="replay">再次观看</button>
    </div>
    """,
    unsafe_allow_html=True
)
