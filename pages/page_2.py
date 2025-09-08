import streamlit as st

with st.form(key='profile_form'):
        # テキストボックス
        name = st.text_input("名前")
        address = st.text_input("住所")
        
        # セレクトボックス
        age_category = st.radio(
            '年齢層を選んでください',
            ('10代', '20代', '30代', '40代', '50代以上'))
        
        # 複数選択
        interests = st.multiselect(
            '興味のある分野を選んでください',
            ['AI', 'Web開発', 'データサイエンス', 'ゲーム', 'その他'])
        
        # ボタン
        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")
if submit_btn:
        st.text(f"こんにちは、{name}さん！{address}にお住まいなんですね。")
        st.text(f"年齢層は{age_category}ですね。")
        st.text(f"興味のある分野は{', '.join(interests)}ですね。")