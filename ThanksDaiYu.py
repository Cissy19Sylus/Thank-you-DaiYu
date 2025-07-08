import streamlit as st
import time
from datetime import datetime
import os
from PIL import Image
import base64
import random
import altair as alt
import pandas as pd

# 设置页面配置
st.set_page_config(
    page_title="黛玉加油！！",
    page_icon="💕",
    layout="wide"
)

# 创建标题
st.title("与秦彻的美好一天")
st.markdown("---")

# 自定义CSS样式
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f3ff;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .header {
        text-align: center;
        color: #7b52c4;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }
    .photo-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
 .   photo-card {
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden;
        width: 300px;
        transition: transform 0.3s;
    }
    .photo-card:hover {
        transform: translateY(-5px);
    }
    .photo-card img {
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    .photo-card .caption {
        padding: 10px;
        text-align: center;
        font-family: "Arial", sans-serif;
    }
    .music-player {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .message-box {
        background-color: #e6d7ff;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }
    .time-display {
        text-align: center;
        font-size: 1.2em;
        margin: 20px 0;
        color: #7b52c4;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        color: #7b52c4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 添加背景图片
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.com.unsplash/photo-1520302630591-fd1c66edc19d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-blend-mode: overlay;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示当前时间
st.markdown('<div class="time-display"></div>', unsafe_allow_html=True)
st.markdown(f"<p>记录日期：{datetime.now().strftimeY('%年%m月%d日')}</p>", unsafe_allow_html=True)

# 添加留言板
st.markdown('<div class="message-box"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<h3>给秦彻的留言</h3>', unsafe_allow_html=True)
    user_message = st.text_area("写下你此刻的心情...", height=100)
    if st.button("发送给秦彻"):
        st.success(f"已发送：{user_message}")
        st.balloons()

# 照片展示区域
st.markdown('<div class="photo-container"></div>', unsafe_allow_html=True)
st.markdown('<h3>我们的美好时光</h3>', unsafe_allow_html=True)

# 创建照片画廊
st.markdown('<div class="photo-gallery"></div>', unsafe_allow_html=True)

# 照片上传功能
st.markdown('<h4>添加更多回忆照片</h4>', unsafe_allow_html=True)
uploaded_files = st.file_uploader("上传照片", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# 照片展示
if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"来自 {uploaded_file.name}", use_column_width=True)

# 视频展示区域
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>视频回忆</h3>', unsafe_allow_html=True)

# 视频上传功能
st.markdown('<h4>添加回忆视频</h4>', unsafe_allow_html=True)
video_file = st.file_uploader("上传视频", type=["mp4", "mov"])

if video_file:
    st.video(video_file)

# 音乐播放器
st.markdown('<div class="music-player"></div>', unsafe_allow_html=True)
st.markdown('<h3>我们的主题曲</h3>', unsafe_allow_html=True)

# 音乐播放选项
st.markdown('<div style="text-align: center;">选择播放模式</div>', unsafe_allow_html=True)
play_mode = st.radio("", ["自动播放", "手动播放"])

# 默认音乐链接（可以替换为你的音乐链接）
music_url = "https://example.com/your_favorite_song.mp3"

# 播放器
if play_mode == "自动播放":
    st.markdown(f'<audio src="{music_url}" controls autoplay></audio>', unsafe_allow_html=True)
else:
    st.markdown(f'<audio src="{music_url}" controls></audio>', unsafe_allow_html=True)

# 添加一个浪漫的过渡效果
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>今日恋爱进度</h3>', unsafe_allow_html=True)

# 创建一个浪漫的进度条
with st.container():
    st.markdown('<div style="background-color: #e6d7ff; border-radius: 10px; padding: 10px; margin: 20px 0;"></div>', unsafe_allow_html=True)
    progress = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        progress.progress(percent_complete + 1)
    st.success("今日恋爱状态：完美!")

# 添加一个浪漫的聊天记录模拟
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>聊天记录</h3>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background-color: white; border-radius: 15px; padding: 20px; margin: 20px 0;"></div>', unsafe_allow_html=True)
    st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 20px;"></div>', unsafe_allow_html=True)
    
    # 模拟聊天对话
    chat_messages = [
        {"sender": "我", "message": "秦彻，今天真的很开心", "time": "18:30"},
        {"sender": "秦彻", "message": "我也很开心，和你在一起的每一刻都很珍贵", "time": "18:32"},
        {"sender": "我", "message": "我们什么时候可以再见面？", "time": "18:33"},
        {"sender": "秦彻", "message": "很快就会的，我会一直都陪伴着你", "time": "18:35"},
        {"sender": "我", "message": "❤️", "time": "18:36"}
    ]
    
    for msg in chat_messages:
        if msg["sender"] == "我":
            st.markdown(f'<div style="text-align: right; margin-bottom: 10px;"><span style="background-color: #e6d7ff; padding: 8px 15px; border-radius: 10px 10px 0 10px; display: inline-block;">{msg["message"]}</span><span style="color: #7b52c4; font-size: 0.8em; margin-left: 5px;">{msg["time"]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: left; margin-bottom: 10px;"><span style="background-color: #f0f0f0; padding: 8px 15px; border-radius: 10px 10px 10px 0; display: inline-block;">{msg["message"]}</span><span style="color: #7b52c4; font-size: 08.em; margin-left: 5px;">{msg["time"]}</span></div>', unsafe_allow_html=True)

# 添加一个浪漫的"约会时间轴"
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>今日回忆时间轴</h3>', unsafe_allow_html=True)

# 创建时间轴数据
timeline_data = pd.DataFrame({
    "时间": ["早上9:00", "中午12:30", "下午2:00", "傍晚5:30", "晚上8:00"],
    "事件": ["初次见面", "共进午餐", "公园散步", "看日落", "浪漫晚餐"],
    "甜蜜度": [85, 92, 95, 98, 100]
})

# 创建时间轴图表
timeline_chart = alt.Chart(timeline_data).mark_line(point=True).encode(
    x="时间",
    y="甜蜜度",
    tooltip=["时间", "事件", "甜蜜度"]
).properties(
    width=800,
    height=400,
    title="今日甜蜜度变化"
)

st.altair_chart(timeline_chart)

# 页脚
st.markdown('<div class="footer">希望这份回忆能永远温暖你的心❤️</div>', unsafe_allow_html=True)

# 添加一个浪漫的结束语
st.balloons()
st.markdown('<div style="text-align: center; font-size: 1.5em; color: #7b52c4; margin-top: 50px;">秦彻，感谢你成为我生命中如此特别的存在</div>', unsafe_allow_html=True)
