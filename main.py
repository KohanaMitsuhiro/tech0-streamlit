
import streamlit as st
import time


st.title('Streamlit 超入門')
st.write("プログレスバーの表示")

"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!!!!"


left_column, right_columu = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_columu.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ内容")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ内容")
