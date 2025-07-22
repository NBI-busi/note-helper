# app_main.py
import streamlit as st

# 曜日別ルーティンの読み込み
from routines import thursday_energy, tuesday_agri

st.set_page_config(page_title="Weekly Market Routine", layout="wide")
st.title("📅 ファンダメンタルズの確認の各曜日ルーティン")

# セレクトボックスで曜日を選択
weekday = st.selectbox("曜日を選んでください:", ["火曜（農業商品）","木曜（エネルギー）", "金曜（日本市場）"])

# 曜日に応じて処理を切り替え
if weekday.startswith("火曜"):
    tuesday_agri.run()
elif weekday.startswith("木曜"):
    thursday_energy.run()
elif weekday.startswith("金曜"):
    friday_jpmarket.run()
