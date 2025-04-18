import streamlit as st
import pandas as pd
import numpy as np
import time

# page content
st.markdown("# page 03 🎉")
st.sidebar.markdown("# page 03 🎉")
st.write("Hello world")

# パラメータのテスト
#@st.cache_data
def show_param():
    x = st.slider('x')  # 👈 this is a widget
    return x,st.write(x, 'squared is', x * x)
show_param()

# チェックボックスのテスト
#@st.cache_data
def show_checkbox():
    st.markdown("### チェックボックスのテスト")
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        chart_data
show_checkbox()

# リストからの選択のテスト
#@st.cache_data
def show_checklist():
    st.markdown("### リストからの選択")
    tab_04 = pd.DataFrame({
        'first column': ["option_1", "op_02", "op0_3", "op_04"],
        'second column': [10, 20, 30, 40]
        })

    option = st.selectbox(
        'Which number do you like best?',
        tab_04['first column'])

    'You selected: ', option
show_checklist()

# パラメータを画面の左に固定
# Add a selectbox to the sidebar:
#@st.cache_data
def show_params_left():
    st.markdown("### 左側にパラメータを表示\n ※メインボディの表示なし")
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )
    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )
show_params_left()

#@st.cache_data
def show_2cols():
    st.markdown("### 画面を縦に2列で表示")
    # 画面を縦2列に分割する
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")
show_2cols()

@st.cache_data
def show_progressbar(value_end):
    st.markdown("### 進捗バー")
    # 進捗バーの表示
    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    value_end = value_end

    for i in range(value_end):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1} / {value_end}')
        bar.progress((i + 1)/value_end)
        time.sleep(0.2)

    '...and now we\'re done!'
show_progressbar(20)