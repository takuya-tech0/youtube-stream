import streamlit as st

st.title('のるっぽアプリ')
st.caption('これは東急線スタンプラリーの最短ルート検索テストアプリです')
st.subheader('自己紹介')
import streamlit.components.v1 as components
components.html('''
<a href="https://64d2a9d0e37b850a5c8a1ac2--dynamic-torte-f0c2c5.netlify.app/">Link</a>
''')