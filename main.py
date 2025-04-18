import streamlit as st
import pandas as pd
import numpy as np
import time

# Define the pages
page_0 = st.Page("page-00.py", title="Page 00", icon="🎈")
page_1 = st.Page("page-01.py", title="Page 01", icon="🚲")
page_2 = st.Page("page-02.py", title="Page 02", icon="❄️")
page_3 = st.Page("page-03.py", title="Page 03", icon="🎉")
page_4 = st.Page("page-04.py", title="Page 04", icon="🍴")

# Set up navigation
pg = st.navigation([page_0, page_1, page_2, page_3, page_4])

# Run the selected page
pg.run()