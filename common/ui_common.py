import streamlit as st

def render_ui(title, steps, buttons, futures_files, options_files, draw_func):
    st.header(title)

    for i, step in enumerate(steps):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write(f"{i+1}. {step}")
        with col2:
            if "ポジション" in step:
                col21, col22 = st.columns(2)
                with col21:
                    if st.button("先物のみ", key=f"fonly_{i}"):
                        draw_func(futures_files, "futuresonly")
                        st.success("先物のみ のネットポジションのグラフを描画しました ✅")
                with col22:
                    if st.button("オプション含む", key=f"fopt_{i}"):
                        draw_func(options_files, "optionscombined")
                        st.success("オプション含む のネットポジションのグラフを描画しました ✅")
            elif buttons[i]:  # 空でなければ表示
                if st.button(buttons[i], key=f"btn_{i}"):
                    st.success(f"「{step}」を実行しました ✅")
