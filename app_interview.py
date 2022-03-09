import streamlit as st
import datetime
from long_text_Java import java
from long_text_JVM import jvm
from long_text_Jmt import jmt
from long_text_CNet import cnet
from long_text_OS import os
from long_text_DM import dm
from long_text_Ds_Al import ds_al
from long_text_Mysql import mysql


# 程序入口
def main():
    # 应用页面设置（显示在网站标签）
    st.set_page_config(page_title="路明非的面试题库", page_icon=":rainbow:", layout="wide", initial_sidebar_state="auto")
    # 加载成功动画
    st.balloons()

    a11, a12 = st.columns([3, 7])
    with a11:
        a11.success('## ' + datetime.datetime.now().strftime("%Y-%m-%d"))
    with a12:
        a12.info("## 欢迎来到路明非的面试题库")

    st.markdown('''---''')  # 分割线

    b11, _, b12, _, b13, _ = st.columns([2.5, 0.5, 2.5, 0.5, 2.5, 0.5])
    with b11:
        gs_selectbox = st.selectbox(label="", options=["全部", "阿里巴巴", "字节跳动"])
    with b12:
        gw_selectbox = st.selectbox(label="", options=["后端"])
    with b13:
        tm_selectbox = st.selectbox(label="",
                                    options=[
                                        "计算机网络", "操作系统",
                                        "Java基础", "Java多线程", "Java虚拟机", "设计模式",
                                        "数据结构与算法", "数据库", "Redis"])

    st.markdown('''---''')  # 分割线
    c11, c12, _ = st.columns([0.5, 8.5, 1])
    c11.markdown("##### 编号")
    c12.markdown("##### 题目")
    st.markdown('''---''')  # 分割线

    data = ()
    if tm_selectbox:
        if tm_selectbox == "计算机网络":
            data = cnet
        elif tm_selectbox == "操作系统":
            data = os
        elif tm_selectbox == "Java基础":
            data = java
        elif tm_selectbox == "Java虚拟机":
            data = jvm
        elif tm_selectbox == "Java多线程":
            data = jmt
        elif tm_selectbox == "设计模式":
            data = dm
        elif tm_selectbox == "数据结构与算法":
            data = ds_al
        elif tm_selectbox == "数据库":
            data = mysql
        n = len(data)
        st.write(f"该目录下有{n}道题：")
        for cnt in range(n):
            d11, d12, _ = st.columns([0.5, 8.5, 1])
            d11.markdown("#### " + str(cnt + 1))
            with d12:
                with st.expander(data[cnt][0]):
                    st.markdown(data[cnt][1])


# 运行：streamlit run app_interview.py
if __name__ == '__main__':
    main()
