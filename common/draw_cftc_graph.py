import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import pathlib

# 商品名マッピング（必要なら外部定義化も可）
target_commodities = {
    "GOLD - COMMODITY EXCHANGE INC.": "Gold",
    "SILVER - COMMODITY EXCHANGE INC.": "Silver",
    "COPPER- #1 - COMMODITY EXCHANGE INC.": "Copper",
    "PLATINUM - NEW YORK MERCANTILE EXCHANGE": "Platina",
    "PALLADIUM - NEW YORK MERCANTILE EXCHANGE": "Palladium",
    "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE": "Crude Oil",
    "GASOLINE RBOB - NEW YORK MERCANTILE EXCHANGE": "Gasoline",
    "NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE": "Natural Gas",
    "WHEAT-SRW - CHICAGO BOARD OF TRADE": "WHEAT",
    "CORN - CHICAGO BOARD OF TRADE": "CORN",
    "SOYBEANS - CHICAGO BOARD OF TRADE": "SOYBEANS",
    "COTTON NO. 2 - ICE FUTURES U.S.": "COTTON"
}

linestyles = {
    'Managed Money': '-',
    'Swap Dealers': '-',
}

def draw_cftc_graph(file_names, label):
    """複数CSVファイルから対象商品のCFTCグラフを描画し、保存も行う"""
    folder_path = os.path.join(os.path.dirname(__file__), '..', 'assets')

    try:
        dfs = [pd.read_csv(os.path.join(folder_path, fname)) for fname in file_names]
    except FileNotFoundError:
        st.error("必要なCFTCデータCSVファイルが見つかりません。assets/ に配置されているか確認してください。")
        return

    df = pd.concat(dfs, ignore_index=True)
    df['Date'] = pd.to_datetime(df['Report_Date_as_YYYY-MM-DD'])

    current_file = pathlib.Path(__file__)
    parent_path = current_file.parent.parent.resolve()

    try:
        latest_raw_date = df['As_of_Date_In_Form_YYMMDD'].astype(str).max()
        latest_date_str = '20' + latest_raw_date if len(latest_raw_date) == 6 else 'unknown_date'
    except Exception:
        latest_date_str = 'unknown_date'

    for keyword, short_name in target_commodities.items():
        prod_df = df[df['Market_and_Exchange_Names'].str.contains(keyword, case=False)].copy()
        if prod_df.empty:
            continue

        prod_df = prod_df.sort_values('Date')
        prod_df['MM_Net'] = prod_df['M_Money_Positions_Long_All'] - prod_df['M_Money_Positions_Short_All']
        prod_df['SD_Net'] = prod_df['Swap_Positions_Long_All'] - prod_df['Swap__Positions_Short_All']

        plt.figure(figsize=(14, 6))
        plt.plot(prod_df['Date'], prod_df['MM_Net'], label='Managed Money', linestyle=linestyles['Managed Money'], color='black')
        plt.plot(prod_df['Date'], prod_df['SD_Net'], label='Swap Dealers', linestyle=linestyles['Swap Dealers'], color='blue')
        plt.axhline(0, color='gray', linestyle='--')
        plt.title(f"Net Positions of {short_name}")
        plt.xlabel("Date")
        plt.ylabel("Net Position")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        image_filename = f"{latest_date_str}_{short_name}_{label}.png"
        image_path = os.path.join(parent_path, image_filename)
        plt.savefig(image_path)

    st.success("グラフの作成が完了しました。")
    st.pyplot(plt)
