import streamlit as st
import pandas as pd
import numpy as np
import time

# page content
st.markdown("# page 02 ❄️")
st.sidebar.markdown("# page 02 ❄️")
st.write("Hello world")

# 折れ線グラフ描画テスト
#@st.cache_data
def show_line_chart():
    tab_03 = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return st.title("Line chart"), st.line_chart(tab_03)
show_line_chart()

# 地図描画のテスト
#@st.cache_data
def show_map():
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / [100, 100] + [35.68, 139.75],
        columns=['lat', 'lon'])
    return st.title("Map"), st.map(map_data)
show_map()
