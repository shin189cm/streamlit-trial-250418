import streamlit as st
import pandas as pd
import numpy as np
import time

# page content
st.markdown("# page 01 🚲")
st.sidebar.markdown("# page 01 🚲")
st.write("Hello world")

#@st.cache_data
def show_tab():
    tab_01 = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=["col_00", "col_01", "col_02", "col_03"],
    index=["row_00", "row_01", "row_02"]
    )
    # 表を複数の方法で表示するテスト
    # st.table(tab_01)
    # print(tab_01)
    # tab_01
    return st.title("table"), st.dataframe(tab_01.style.highlight_max(color="#999933", axis=0))
show_tab()

# ちょっと小ぎれいに表を描く
#@st.cache_data
def show_tab02():
    tab_02 = pd.DataFrame(
        np.random.randn(5, 10),
        columns=('col %d' % i for i in range(10)))
    return st.title("table_version 2"), st.dataframe(tab_02)
show_tab02()
