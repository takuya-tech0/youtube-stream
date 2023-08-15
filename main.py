import streamlit as st
import time

st.title('超入門')

st.write('プログレスバーの表示')
'Start!'

latest_literation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_literation.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'

left_column , right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ3の回答')

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション：',condition

# if st.checkbox('show image'):
#     img = Image.open("zoo.jpeg")
#     st.image(img,caption="zoo!!",use_column_width=True)