import pandas as pd
import streamlit as st
import psycopg2 
import seaborn as sns
import json
import plotly.express as px
import matplotlib.pyplot as plt
import base64
import joblib


st.set_page_config(layout="wide")


def set_bg(image_file):
    with open(image_file,"rb") as f:
        encoded_string=base64.b64encode(f.read())
    st.markdown(
        f"""
        <style>
        .stApp{{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

        }}

        </style>
        """,
    unsafe_allow_html=True
    )

set_bg('Content_monetization_modeler/v960-ning-30.jpg')
st.markdown(
    "<h1 style='text-align: center; color: black;'>Content Monetization Modeler</h1>" \
    "<h4 style='text-align: center; color: black;'>Predict YouTube Ad Revenue Based on Video Performance</h4>", 
    unsafe_allow_html=True
)



left_col,right_col= st.columns([1,2])

# --- Left: Input Panel ---
with left_col:
        st.markdown("<h2 style='text-align: left; color: black; '>Input Video Metrics</h2>", unsafe_allow_html=True)
        st.markdown("""
    <style>
    .custom-line {
        height: 4px;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        border: none;
        margin-bottom: 20px;
    }
    </style>
    <div class="custom-line"></div>
    """, unsafe_allow_html=True)
        views = st.number_input("Views:", placeholder="Enter number")
        likes = st.number_input("Likes:", placeholder="Enter number")
        comments = st.number_input("Comments:", placeholder="Enter number")
        watch_time_minutes = st.number_input("Watch Time (Minutes):", placeholder="Enter number")
        video_length_minutes = st.number_input("Video Length (Minutes):", placeholder="Enter number")
        subscribers = st.number_input("Subscribers:", placeholder="Enter number")
        
        category = st.selectbox("Category:", ["Entertainment", "Education", "Gaming", "Music", "Tech","Lifestyle"])
        device = st.selectbox("Device:", ["Mobile", "Desktop", "TV","Tablet"])
        country = st.selectbox("Country:", ["US", "IN", "UK", "CA","DE","AU"])
        
        predict_btn = st.button("Predict Revenue",width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)



watch_time_rate = watch_time_minutes/(views*video_length_minutes) if views > 0 else 0
engagement_rate = (likes + comments) / views if views > 0 else 0

input_df = pd.DataFrame({
    "watch_time_rate":[watch_time_rate],
    "watch_time_minutes": [watch_time_minutes],
    "engagement_rate": [engagement_rate],
    "category":[category]
})


@st.cache_resource
def load_model():
    return joblib.load("Content_monetization_modeler/final_revenue_model.pkl")

model = load_model()

# -----------------------------------
# Prediction
# -----------------------------------
predicted_revenue = 532.45

if predict_btn:
    try:
        predicted_revenue = float(model.predict(input_df)[0])
    except Exception as e:
        st.error(f"Prediction error: {e}")
with right_col:
        st.markdown("<h2 style='text-align: left; color: black; '>Predicted Ad Revenue</h2>", unsafe_allow_html=True)
        st.markdown("""
    <style>
    .custom-line {
        height: 4px;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        border: none;
        margin-bottom: 20px;
    }
    </style>
    <div class="custom-line"></div>
    """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style="
            background:#f5f8ff;
            padding:20px;
            border-radius:15px;
            border-left:8px solid red;
            color:black;
            font-size:28px;
            font-weight:700;">
            Estimated Revenue: ${predicted_revenue:,.2f}
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
    <style>
    .custom-line {
        height: 4px;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        border: none;
        margin-top: 20px;
        margin-bottom: 20px;
        
    }
    </style>
    <div class="custom-line"></div>
    """, unsafe_allow_html=True)
        st.markdown("<h2 style='color:black;'>Key Insights</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div style="
            background:#f5f8ff;
            padding:18px;
            border-radius:15px;
            color:black;
            font-size:25px;">
            ✅ Higher engagement rate tends to improve revenue<br>
            ✅ Longer watch time supports better monetization<br>
            ✅ Watch time rate correlate with ad revenue
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
    <style>
    .custom-line {
        height: 4px;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        border: none;
        margin-top: 20px;
        margin-bottom: 20px;
        
    }
    </style>
    <div class="custom-line"></div>
    """, unsafe_allow_html=True)
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-heading">No correlation between categories</div>', unsafe_allow_html=True)
        
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            category =  ["Entertainment", "Education", "Gaming", "Music", "Tech","Lifestyle"]
            value = [50,49,52,53,51,50]
            sns.barplot(x=category,y=value)
            ax1.set_ylabel("Revenue")
            ax1.set_xlabel("")
            plt.xticks(rotation=30)
            st.pyplot(fig1, use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)

        with chart_col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-heading">Feature Importance</div>', unsafe_allow_html=True)
            categories =  ['watch_time_minutes','watch_time_rate','engagement_rate']
            values = [80,33,14]
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.barplot(x=values,y=categories,palette="flare")
            ax2.invert_yaxis()
            ax2.set_xlabel("Importance Score")
            st.pyplot(fig2, use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)



st.markdown("""
<style>
    div[data-testid="stHorizontalBlock"] > div {
    background-color: white !important;
    border-radius: 20px !important;
    padding: 20px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
    border: none !important;
}


div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] label,
label p {
    color: black !important;
    font-size: 20px !important;
    font-weight: 600 !important;
}
            .stButton > button {
        width: 100%;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        color: white;
        font-size: 30px !important;
        font-weight: 1200;
        color:black;
        border: none;
        border-radius: 12px;
        padding: 12px 0;
        box-shadow: 0 8px 20px rgba(255, 59, 59, 0.35);
    }

    .stButton > button:hover {
        color: white;
        background: linear-gradient(to right, #4facfe 0%, #00f2fa 40%);
    }

    .section-heading{
            font-size:20px;
            text-align:center;
            color:black;
            font-weight:700;
            }
</style>
""", unsafe_allow_html=True)

        
