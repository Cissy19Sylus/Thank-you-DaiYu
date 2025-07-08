import streamlit as st
from datetime import datetime
import time
import os
from PIL import Image
import base64
import random
import altair as alt
import pandas as pd

# 设置页面配置
st.set_page_config(
    page_title="加油黛玉！",
    page_icon="💪",
    layout="wide"
)

# 创建标题
st.title("加油黛玉！")
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
    .photo-card {
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

# 显示当前时间
st.markdown('<div class="time-display"></div>', unsafe_allow_html=True)
st.markdown(f"<p>记录日期：{datetime.now().strftime('%Y年%m月%d日')}</p>", unsafe_allow_html=True)

# 添加留言板
st.markdown('<div class="message-box"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<h3>给黛玉的留言</h3>', unsafe_allow_html=True)
    user_message = st.text_area("写下你此刻的心情...", height=100)
    if st.button("发送给黛玉"):
        st.success(f"已发送：{user_message}")
        st.balloons()

# 照片展示区域
st.markdown('<div class="photo-container"></div>', unsafe_allow_html=True)
st.markdown('<h3>黛玉的加油瞬间</h3>', unsafe_allow_html=True)

# 创建照片画廊
st.markdown('<div class="photo-gallery"></div>', unsafe_allow_html=True)

# 照片上传功能
st.markdown('<h4>添加更多加油瞬间</h4>', unsafe_allow_html=True)
uploaded_files = st.file_uploader("上传照片", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# 照片展示
if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"来自 {uploaded_file.name}", use_column_width=True)

# 视频展示区域
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>加油视频</h3>', unsafe_allow_html=True)

# 视频上传功能
st.markdown('<h4>添加加油视频</h4>', unsafe_allow_html=True)
video_file = st.file_uploader("上传视频", type=["mp4", "mov"])

if video_file:
    st.video(video_file)

# 音乐播放器
st.markdown('<div class="music-player"></div>', unsafe_allow_html=True)
st.markdown('<h3>加油的音乐</h3>', unsafe_allow_html=True)

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
st.markdown('<h3>今日加油进度</h3>', unsafe_allow_html=True)

# 创建一个浪漫的进度条
with st.container():
    st.markdown('<div style="background-color: #e6d7ff; border-radius: 10px; padding: 10px; margin: 20px 0;"></div>', unsafe_allow_html=True)
    progress = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        progress.progress(percent_complete + 1)
    st.success("今日加油状态：完美!")

# 添加一个浪漫的聊天记录模拟
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>加油的对话</h3>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background-color: white; border-radius: 15px; padding: 20px; margin: 20px 0;"></div>', unsafe_allow_html=True)
    st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 20px;"></div>', unsafe_allow_html=True)
    
    # 模拟聊天对话
    chat_messages = [
        {"sender": "我", "message": "黛玉，你今天真的很棒！", "time": "18:30"},
        {"sender": "黛玉", "message": "谢谢，我今天也很开心！", "time": "18:32"},
        {"sender": "我", "message": "你以后还会更棒的！", "time": "18:33"},
        {"sender": "黛玉", "message": "我会努力的，谢谢你陪伴我！", "time": "18:35"},
        {"sender": "我", "message": "❤️", "time": "18:36"}
    ]
    
    for msg in chat_messages:
        if msg["sender"] == "我":
            st.markdown(f'<div style="text-align: right; margin-bottom: 10px;"><span style="background-color: #e6d7ff; padding: 8px 15px; border-radius: 10px 10px 0 10px; display: inline-block;">{msg["message"]}</span><span style="color: #7b52c4; font-size: 0.8em; margin-left: 5px;">{msg["time"]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: left; margin-bottom: 10px;"><span style="background-color: #f0f0f0; padding: 8px 15px; border-radius: 10px 10px 10px 0; display: inline-block;">{msg["message"]}</span><span style="color: #7b52c4; font-size: 08.em; margin-left: 5px;">{msg["time"]}</span></div>', unsafe_allow_html=True)

# 添加一个浪漫的"加油时间轴"
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3>今日加油时间轴</h3>', unsafe_allow_html=True)

# 创建时间轴数据
timeline_data = pd.DataFrame({
    "时间": ["早上9:00", "中午12:30", "下午2:00", "傍晚5:30", "晚上8:00"],
    "事件": ["开始加油", "
