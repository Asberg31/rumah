import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk membaca data dari file Excel
def read_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Fungsi untuk menampilkan histogram
def show_histogram(data, column_name):
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto')
    ax.set_xlabel(column_name)
    ax.set_ylabel('Frekuensi')
    ax.set_title(f"Histogram {column_name}")
    st.pyplot(fig)

# Fungsi untuk menampilkan data kolom
def show_column_data(df):
    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox('Pilih kolom', columns)
    st.subheader(f'Kolom {selected_column}')
    st.write(df[selected_column])
    show_histogram(df[selected_column], selected_column)

# Main program
def main():
    st.title('Analisis Data')
    file_path = st.file_uploader("Pilih file Excel", type=["xlsx"])
    if file_path is not None:
        df = read_data(file_path)
        show_column_data(df)

if __name__ == '__main__':
    main()
