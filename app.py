import streamlit as st
import random

st.set_page_config(page_title="Ergonomi & Sağlık Paneli", page_icon="🛡️", layout="wide")

st.title("🛡️ Akıllı Ergonomi ve Sağlık Takip İstasyonu")
st.markdown("Optisyenlik, Odyometri ve Çevresel Otomasyon Modülleri Canlı İzleme Paneli")
st.divider()

# Sidebar
max_eye_dist = st.sidebar.slider("Maks. Göz Yakınlık Eşiği (px)", 40, 100, 60)
max_noise_db = st.sidebar.slider("Maks. Gürültü Eşiği (dB)", 50, 100, 75)

# Metrikler
col1, col2, col3 = st.columns(3)

eye_distance_px = random.randint(35, 75)
noise_level_db = random.randint(45, 88)
ambient_light_ldr = random.randint(800, 3200)
temperature_c = random.randint(20, 30)

with col1:
    st.subheader("👁️ Optisyenlik (Göz)")
    if eye_distance_px > max_eye_dist:
        st.metric(label="Göz Mesafesi", value=f"{eye_distance_px} px", delta="Ekrana Çok Yakın!", delta_color="inverse")
        st.error("⚠️ UYARI: Duruş pozisyonunuzu düzeltin.")
    else:
        st.metric(label="Göz Mesafesi", value=f"{eye_distance_px} px", delta="İdeal Mesafe")
        st.success("✅ Göz mesafeniz uygun.")

with col2:
    st.subheader("🎧 Odyometri (Ses)")
    if noise_level_db > max_noise_db:
        st.metric(label="Ortam Gürültüsü", value=f"{noise_level_db} dB", delta="Yüksek Gürültü!", delta_color="inverse")
        st.warning("⚠️ UYARI: Yüksek ses seviyesi.")
    else:
        st.metric(label="Ortam Gürültüsü", value=f"{noise_level_db} dB", delta="Güvenli Seviye")
        st.info("✅ Ortam ses düzeyi ideal.")

with col3:
    st.subheader("💡 Otomasyon (ESP32)")
    st.metric(label="Ortam Işığı (LDR)", value=f"{ambient_light_ldr} lux")
    st.metric(label="Sıcaklık", value=f"{temperature_c} °C")

st.divider()
st.subheader("📊 Zaman İçindeki Ergonomi Değişim Grafiği")
chart_data = {
    "Göz Mesafesi (px)": [random.randint(40, 70) for _ in range(20)],
    "Gürültü Seviyesi (dB)": [random.randint(50, 85) for _ in range(20)]
}
st.line_chart(chart_data)
