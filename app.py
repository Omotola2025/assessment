import streamlit as st
import os


hide_sidebar = """
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
</style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

navbar = """
<style>
.topnav {
    background-color: #f518ed;
    padding: 20px 30px;
    border-radius: 8px;
    width: 1000px;
    display: flex;
    justify-content: space-between;  
    align-items: center;
    margin-top:-60px;
    margin-left: 80px;
}

.topnav a {
    color: #f2f2f2;
    text-decoration: none;
    font-size: 17px;
    padding: 12px 25px;  
    border-radius: 5px;
    display: inline-block;
}

.topnav a:hover {
    background-color: #4b5563;
    color: white;
}

.topnav a.active {
    background-color: #2563eb;
    color: white;
}

.main {
    background-color: #2f7aeb;
}


.card {
    background: #e962f5;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #e0e0e0;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}


.section-title {
    font-size: 30px;
    color: #2c7be5;
    font-weight: 700;
    margin-bottom: 15px;
}


.subsection-title {
    font-size: 22px;
    color: #ff9900;
    font-weight: 600;
    margin-top: 5px;
}

.custom-divider {
    margin-top: 5px;
    margin-bottom: 20px;
    height: 2px;
    background: #e962f5;
}


.center-text {
    text-align: center;
}


ul li {
    margin-bottom: 5px;
}
h4 {
    text-align = center
    }
</style>

<div class="topnav">
  <a href="/app" class="active">Home</a>
  <a href="/Data_Cleaning">Data Cleaning</a>
  <a href="/Data_Visualization">Data Visualization</a>
  <a href="/Model_Training">Model_Training</a>
  <a href="/Post-Review">Project Review</a>
</div>
"""
st.markdown(navbar, unsafe_allow_html=True)



st.set_page_config(page_title="Overview", layout="wide")

st.title('Project Objective')



st.write("""
This project analyzes daily air quality data collected from major Indian cities between 2015 and 2020. The dataset includes key pollutants such as PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, and VOCs (Benzene, Toluene, Xylene), as well as the Air Quality Index (AQI) and categorized AQI_Bucket. These measurements help describe pollution levels, seasonal patterns, and overall environmental conditions across different regions in India.

The aim of this project is to clean and preprocess the dataset, perform exploratory data analysis (EDA), engineer new features, and build a machine learning model to predict AQI_Bucket. The workflow includes visualizing pollutant behavior, analyzing correlations, training a classification model, and developing a simple GUI application for data exploration and prediction. GitHub is used for version control and project documentation.
""")

st.subheader("Static Analysis Plots")


st.write("""
The heatmap shows which columns contain missing values and how they are distributed. Most pollutants had scattered missing points, which is common in environmental datasets due to sensor downtime or incomplete reporting. This visualization helped confirm the need for imputation during data cleaning.
""")

col1, col2, = st.columns(2)

with col1:
    st.markdown("<h4 class='subsection-title'>Univariate Analysis</h4>", unsafe_allow_html=True)
    st.write("""
Univariate analysis examines **one variable at a time**, helping understand:
- PM2.5 histograms  
- Summary statistics  
- AQI category frequency  

Useful for spotting outliers and skewness.
""")

with col2:
    st.markdown("<h4 class='subsection-title'>Bivariate Analysis</h4>", unsafe_allow_html=True)
    st.write("""
Bivariate analysis explores relationships between **two variables**, such as:
- PM2.5 vs AQI scatter  
- NO2 vs NOx correlation  
- AQI buckets across cities  

Reveals pollutant–AQI influence.
""")

image_path_1 = os.path.join("images", "opk.png")


if os.path.exists(image_path_1):
    st.image(image_path_1, caption="Correlation heatmap", use_column_width=True)
else:
    st.warning(f"Image not found at path: {image_path_1}")


