import streamlit as st

st.set_page_config(page_title="Smart Farmer Advisory", page_icon="??", layout="centered")

st.title("?? Smart Farmer Soil & Crop Advisory")
st.write("Input your soil data below to find the best crops and management tips for your land.")

st.markdown("---")
st.subheader("?? Enter Soil Parameters")

col1, col2 = st.columns(2)

with col1:
    soil_moisture = st.selectbox(
        "Soil Moisture Level",
        options=["Low (Dry)", "Medium (Well-drained)", "High (Wet/Clayey)"]
    )
    soil_ph = st.slider("Soil pH Level", min_value=4.0, max_value=9.0, value=6.5, step=0.1)

with col2:
    soil_eca = st.selectbox(
        "Soil Texture / ECa (Electrical Conductivity)",
        options=["Sandy (Low ECa)", "Loamy (Medium ECa)", "Clayey (High ECa)"]
    )

st.markdown("---")
st.subheader("?? AI Agricultural Recommendations")

recommended_crop = "Mixed Pulses / Legumes"
management_tip = "Maintain organic compost addition to balance soil health."
crop_suitability_reason = "Pulses are hardy and fix nitrogen naturally, making them excellent for varied or recovering soils."

if soil_moisture == "High (Wet/Clayey)" and soil_eca == "Clayey (High ECa)":
    if 5.5 <= soil_ph <= 7.0:
        recommended_crop = "Rice / Paddy"
        crop_suitability_reason = "Rice thrives in heavy, clayey soils that retain a layer of water on the surface."
        management_tip = "Monitor water levels closely. Ensure proper field levelling to avoid uneven water distribution."
    else:
        recommended_crop = "Sugarcane"
        crop_suitability_reason = "Sugarcane likes plenty of water and can handle slightly more alkaline or acidic clay soils."
        management_tip = "Apply gypsum if your soil pH tilts too far alkaline to improve structural permeability."

elif soil_moisture == "Medium (Well-drained)" and soil_eca == "Loamy (Medium ECa)":
    if 6.0 <= soil_ph <= 7.5:
        recommended_crop = "Maize (Corn) or Cotton"
        crop_suitability_reason = "Loamy soils with moderate moisture provide the perfect nutrient-air balance for deep-rooted crops."
        management_tip = "Practice crop rotation with legumes next season to maintain soil nitrogen levels."
    else:
        recommended_crop = "Potatoes"
        crop_suitability_reason = "Potatoes favor well-drained, slightly loose soils and prefer a mildly acidic pH (5.2 - 6.0)."
        management_tip = "Avoid excess nitrogen fertilizers, which favor leaf growth over potato tuber development."

elif soil_moisture == "Low (Dry)" or soil_eca == "Sandy (Low ECa)":
    recommended_crop = "Millets (Sorghum/Pearl Millet) or Groundnuts"
    crop_suitability_reason = "These crops have deep roots or specialized biology that allows them to tolerate dry, sandy conditions."
    management_tip = "Incorporate drip irrigation or mulching to trap moisture in sandy soils."

st.metric(label="?? Recommended Crop to Cultivate", value=recommended_crop)
st.info(f"**Why this crop fits:** {crop_suitability_reason}")
st.success(f"**??? Soil Management Action Item:** {management_tip}")

if soil_ph < 5.5:
    st.warning("?? **Soil Health Alert:** Your soil is highly acidic. Consider applying agricultural lime to neutralise it.")
elif soil_ph > 7.8:
    st.warning("?? **Soil Health Alert:** Your soil is highly alkaline. Consider applying organic sulfur to lower the pH.")
