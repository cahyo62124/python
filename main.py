import streamlit as st

st.write("""
         # Aplikasi Luas Segitiga
         Ini adalah aplikasi penghitung luas segitiga """)
alas = st.number_input("Masukkan alas", 0)
tinggi = st.number_input("Masukkan tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas segitiga adalah {luas}")