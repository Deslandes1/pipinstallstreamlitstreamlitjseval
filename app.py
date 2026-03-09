import streamlit as st
import pandas as pd
from streamlit_js_eval import get_geolocation
# Configuration de la page
st.set_page_config(page_title="Infinity Engine", page_icon="🚀")
st.title("🚀 GESNER DESLANDES INFINITY")
st.subheader("Global Resource Detection & Mapping Engine")
# Bouton pour rafraîchir la position
if st.button("📍 Refresh GPS Location"):
    st.rerun()

location = get_geolocation()
if location and 'coords' in location:
    lat = location['coords']['latitude']
    lon = location['coords']['longitude']
    st.success(f"Coordinates Locked!")
    st.metric("Latitude", f"{lat:.4f}")
    st.metric("Longitude", f"{lon:.4f}")
    # Affichage de la carte
    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(map_data)
else:
    st.info("📡 Waiting for device GPS signal... Please allow location access in your browser.")
st.write("---")
st.caption("Developed by GESNER DESLANDES | 2026")
