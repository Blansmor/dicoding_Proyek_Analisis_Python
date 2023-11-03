import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Dataset
data_df = pd.read_csv('main_data.csv')

st.header("Project Dicoding")

#Pertanyaan 1
st.subheader("Grafik PM2.5")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(40, 20))

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="PM2.5", y="station", data=data_df.sort_values(by='PM2.5', ascending=False).head(10), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Daerah dengan PM2.5 tertinggi", loc="center", fontsize=50)
ax[0].tick_params(axis ='y', labelsize=40)
ax[0].tick_params(axis ='x', labelsize=40)

sns.barplot(x="PM2.5", y="station", data=data_df.sort_values(by="PM2.5", ascending=True).head(10), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Daerah dengan PM2.5 terendah", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=40)
ax[1].tick_params(axis ='x', labelsize=40)

st.pyplot(fig)

#Pertanyaan 2
st.subheader("Grafik Wind Direction")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"])

with tab1:
    Aotizhongxin_df = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    Aotizhongxin_wd = Aotizhongxin_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Aotizhongxin_wd.index,
            y=Aotizhongxin_wd.values,
            order=Aotizhongxin_wd.index,
            palette=["#068DA9" if score == Aotizhongxin_wd.idxmax() or score == Aotizhongxin_wd.idxmin() else "#D3D3D3" for score in Aotizhongxin_wd.index]
            )
    
    plt.title("Jumlah Terjadinya Wind Direction di Aotizhongxi", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)

    st.pyplot(fig)

   
with tab2:
    Changping_df = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
    Changping_wd = Changping_df['wd'].value_counts().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Changping_wd.index,
            y=Changping_wd.values,
            order=Changping_wd.index,
            palette=["#068DA9" if score == Changping_wd.idxmax() or score == Changping_wd.idxmin() else "#D3D3D3" for score in Changping_wd.index]
            )
    
    plt.title("Jumlah Terjadinya Wind Direction di Changping", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)

    st.pyplot(fig)
    
with tab3:
    Dingling_df = pd.read_csv("PRSA_Data_Dingling_20130301-20170228.csv")
    Dingling_wd = Dingling_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Dingling_wd.index,
                y=Dingling_wd.values,
                order=Dingling_wd.index,
                palette=["#068DA9" if score == Dingling_wd.idxmax() or score == Dingling_wd.idxmin() else "#D3D3D3" for score in Dingling_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Dingling", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab4:
    Dongsi_df = pd.read_csv("PRSA_Data_Dongsi_20130301-20170228.csv")
    Dongsi_wd = Dongsi_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Dongsi_wd.index,
                y=Dongsi_wd.values,
                order=Dongsi_wd.index,
                palette=["#068DA9" if score == Dongsi_wd.idxmax() or score == Dongsi_wd.idxmin() else "#D3D3D3" for score in Dongsi_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Dongsi", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab5:
    Guanyuan_df = pd.read_csv("PRSA_Data_Guanyuan_20130301-20170228.csv")
    Guanyuan_wd = Guanyuan_df['wd'].value_counts().sort_values(ascending=False)
 
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Guanyuan_wd.index,
                y=Guanyuan_wd.values,
                order=Guanyuan_wd.index,
                palette=["#068DA9" if score == Guanyuan_wd.idxmax() or score == Guanyuan_wd.idxmin() else "#D3D3D3" for score in Guanyuan_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Guanyuan", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab6:
    Gucheng_df = pd.read_csv("PRSA_Data_Gucheng_20130301-20170228.csv")
    Gucheng_wd = Gucheng_df['wd'].value_counts().sort_values(ascending=False)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=Gucheng_wd.index,
                y=Gucheng_wd.values,
                order=Gucheng_wd.index,
                palette=["#068DA9" if score == Gucheng_wd.idxmax() or score == Gucheng_wd.idxmin() else "#D3D3D3" for score in Gucheng_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Gucheng", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab7:
    Huairou_df = pd.read_csv("PRSA_Data_Huairou_20130301-20170228.csv")
    Huairou_wd = Huairou_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Huairou_wd.index,
                y=Huairou_wd.values,
                order=Huairou_wd.index,
                palette=["#068DA9" if score == Huairou_wd.idxmax() or score == Huairou_wd.idxmin() else "#D3D3D3" for score in Huairou_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Huairou", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab8:
    Nongzhanguan_df = pd.read_csv("PRSA_Data_Nongzhanguan_20130301-20170228.csv")
    Nongzhanguan_wd = Nongzhanguan_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Nongzhanguan_wd.index,
            y=Nongzhanguan_wd.values,
            order=Nongzhanguan_wd.index,
            palette=["#068DA9" if score == Nongzhanguan_wd.idxmax() or score == Nongzhanguan_wd.idxmin() else "#D3D3D3" for score in Nongzhanguan_wd.index]
            )

    plt.title("Jumlah Terjadinya Wind Direction di Nongzhanguan", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab9:
    Shunyi_df = pd.read_csv("PRSA_Data_Shunyi_20130301-20170228.csv")
    Shunyi_wd = Shunyi_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Shunyi_wd.index,
                y=Shunyi_wd.values,
                order=Shunyi_wd.index,
                palette=["#068DA9" if score == Shunyi_wd.idxmax() or score == Shunyi_wd.idxmin() else "#D3D3D3" for score in Shunyi_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Shunyi", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab10:
    Tiantan_df = pd.read_csv("PRSA_Data_Tiantan_20130301-20170228.csv")
    Tiantan_wd = Tiantan_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Tiantan_wd.index,
                y=Tiantan_wd.values,
                order=Tiantan_wd.index,
                palette=["#068DA9" if score == Tiantan_wd.idxmax() or score == Tiantan_wd.idxmin() else "#D3D3D3" for score in Tiantan_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Tiantan", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab11:
    Wanliu_df = pd.read_csv("PRSA_Data_Wanliu_20130301-20170228.csv")
    Wanliu_wd = Wanliu_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Wanliu_wd.index,
                y=Wanliu_wd.values,
                order=Wanliu_wd.index,
                palette=["#068DA9" if score == Wanliu_wd.idxmax() or score == Wanliu_wd.idxmin() else "#D3D3D3" for score in Wanliu_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Wanliu", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab12:
    Wanshouxigong_df = pd.read_csv("PRSA_Data_Wanshouxigong_20130301-20170228.csv")
    Wanshouxigong_wd = Wanshouxigong_df['wd'].value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=Wanshouxigong_wd.index,
                y=Wanshouxigong_wd.values,
                order=Wanshouxigong_wd.index,
                palette=["#068DA9" if score == Wanshouxigong_wd.idxmax() or score == Wanshouxigong_wd.idxmin() else "#D3D3D3" for score in Wanshouxigong_wd.index]
                )

    plt.title("Jumlah Terjadinya Wind Direction di Wanshouxigong", fontsize=15)
    plt.xlabel("Wind Direction")
    plt.ylabel("Jumlah Terjadi")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

#Pertanyaan 3
st.subheader("Intensitas Hujan")

data_df_q3 = data_df.groupby(by=['station']).agg({'RAIN': 'mean'})
data_df_q3 = data_df_q3.rename(columns={'RAIN': "mean_rain"})
data_df_q3 = data_df_q3.sort_values(by='mean_rain', ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=data_df_q3.station, 
            y=data_df_q3.mean_rain, 
            order=data_df_q3.station,
            palette=["#068DA9" if score == data_df_q3['mean_rain'].max() else "#D3D3D3" for score in data_df_q3.mean_rain]
            )

plt.title("Rata-rata Intensitas Hujan di Daerah", fontsize=15)
plt.xlabel("Daerah")
plt.ylabel("Intensitas")
plt.xticks(fontsize=7.3)

st.pyplot(fig)

