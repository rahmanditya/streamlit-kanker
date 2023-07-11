import pickle
import streamlit as st

# membaca model
kankerp_model = pickle.load(open('kankerp_model.sav', 'rb'))

#judul web
st.title('Prediksi Kanker Payudara')

#membagi kolom
mean_radius = st.number_input ('Input Mean Radius')

mean_texture = st.number_input ('Input Mean Tesktur')

mean_perimeter = st.number_input ('Input Mean Perimeter')

mean_area = st.number_input ('Input Mean Area')

mean_smoothness = st.number_input ('Input Mean Smoothness')

# code untuk prediksi
kankerp_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    kankerp_pred = kankerp_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])

    if (kankerp_pred[0] == 0):
        kankerp_diagnosis = 'Pasien tidak terkena kanker'
    else :
        kankerp_diagnosis = 'Pasien terkena kanker'
st.success(kankerp_diagnosis)
