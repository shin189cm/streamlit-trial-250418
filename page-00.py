import streamlit as st
import pandas as pd
import numpy as np
import time

# page content
st.markdown("# page 00 🎈")
st.sidebar.markdown("# page 00 🎈")
st.write("Hello world")

# セッションステートに値が無ければ初期化
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

name_input = st.text_input("名前を入力", value=st.session_state.user_name)

if st.button("OK"):
    st.session_state.user_name = name_input

st.write(f"セッションに格納されている名前: {st.session_state.user_name}")
