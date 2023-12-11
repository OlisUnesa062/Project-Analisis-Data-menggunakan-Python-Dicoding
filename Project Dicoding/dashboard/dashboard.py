# Import library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    # Ganti 'nama_file.csv' dengan nama file dataset Anda
    df = pd.read_csv('bike_sharing_df.csv')
    return df

df = load_data()

# Judul Dashboard
st.title('Dashboard Analisis Data Penyewaan Sepeda 💥')

# Sidebar untuk memilih visualisasi
sidebar_options = ['Distribusi Penyewaan Sepeda pada Setiap Musim', 
                    'Dampak Hari Kerja vs. Hari Libur', 
                    'Pola Penyewaan Sepeda per Jam']

# Menambahkan satu gambar di atas sidebar_options
sidebar_image = 'https://images.unsplash.com/photo-1475666675596-cca2035b3d79?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

# Menampilkan gambar di sidebar
st.sidebar.image(sidebar_image, caption='Dataset Bike Sharing', use_column_width=True)

selected_option = st.sidebar.selectbox('Pilih macam-macam EDA', sidebar_options)

# Inisialisasi conclusion_text
conclusion_text = ""

# Visualisasi berdasarkan pilihan
if selected_option == 'Distribusi Penyewaan Sepeda pada Setiap Musim':
    # Menggunakan violin plot
    st.subheader('Distribusi Penyewaan Sepeda pada Setiap Musim🈁')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='musim', y='total_penyewaan_sepeda', data=df, palette='pastel')
    st.pyplot(fig)
    
    # Teks conclusion 1
    conclusion_text = """
    **Conclution Pertanyaan 1 :** *Bagaimana distribusi penyewaan sepeda pada setiap musim? Apakah ada musim yang memiliki tingkat penyewaan lebih tinggi dibandingkan dengan musim lainnya?*
            
    Berdasarkan analisis distribusi penyewaan sepeda pada setiap musim, dapat disimpulkan bahwa terdapat perbedaan yang signifikan dalam tingkat penyewaan sepeda antar musim. Musim gugur menunjukkan tingkat penyewaan sepeda yang paling tinggi, sedangkan musim semi memiliki tingkat penyewaan yang lebih rendah dibandingkan dengan musim lainnya. Meskipun terdapat perbedaan, perlu dicatat bahwa perbedaan tersebut mungkin tidak terlalu signifikan secara praktis. Oleh karena itu, sementara musim gugur dapat dianggap sebagai puncak periode aktivitas penyewaan sepeda, dan musim semi cenderung memiliki tingkat penyewaan yang lebih rendah
    """
    # Tampilkan conclusion sebagai text box
    st.info(conclusion_text)

elif selected_option == 'Dampak Hari Kerja vs. Hari Libur':
    # Histogram untuk distribusi penyewaan pada hari kerja dan hari libur
    st.subheader('Dampak Hari Kerja vs. Hari Libur🈵')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x='total_penyewaan_sepeda', hue='hari_libur/kerja', bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    # Teks conclusion
    conclusion_text = """
    **Conclution Pertanyaan 2:** *Apakah hari-hari libur atau hari kerja memiliki dampak yang signifikan pada jumlah penyewaan sepeda? Bagaimana distribusi penyewaan pada hari-hari libur dan hari kerja?*

    Berdasarkan analisis terhadap dampak hari-hari libur dan hari kerja terhadap jumlah penyewaan sepeda, dapat disimpulkan bahwa terdapat perbedaan yang signifikan dalam distribusi penyewaan sepeda antara hari kerja dan hari libur. Frekuensi penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan hari libur. Hal ini menunjukkan bahwa aktivitas penyewaan sepeda lebih diminati dan lebih tinggi pada hari-hari kerja.
    """
    # Tampilkan conclusion sebagai text box
    st.info(conclusion_text)

elif selected_option == 'Pola Penyewaan Sepeda per Jam':
    # Line chart untuk pola penyewaan sepeda per jam
    st.subheader('Pola Penyewaan Sepeda per Jam🈺')
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.lineplot(x='jam', y='total_penyewaan_sepeda', data=df, ci=None, ax=ax)
    st.pyplot(fig)

    # Teks conclusion
    conclusion_text ="""
    **Conclution Pertanyaan 3:** *Pada jam berapa sepeda paling sering disewa, dan apakah ada tren atau pola menarik dalam pola penyewaan tersebut?*

    Berdasarkan analisis pola penyewaan sepeda pada setiap jam, dapat disimpulkan bahwa rata-rata jumlah penyewaan sepeda relatif stabil sepanjang hari. Namun, terdapat tren menarik yang dapat diamati pada jam-jam dini hari, khususnya pada jam 2, 3, dan 4 pagi. Pada jam-jam tersebut, terjadi peningkatan yang cukup signifikan dalam jumlah penyewaan sepeda. Hal ini menunjukkan adanya pola unik di mana sepeda paling sering disewa pada jam-jam tertentu di dini hari.
    """
    # Tampilkan conclusion sebagai text box
    st.info(conclusion_text)

# Menampilkan dataframe (opsional)
if st.checkbox('Tampilkan Dataframe'):
    st.write(df)

st.caption('by Nur Cholis Majid')