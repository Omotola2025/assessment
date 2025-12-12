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
    padding: 15px 10px;
    border-radius: 8px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
    margin-top: -40px;
}


.topnav a {
    color:#f518ed;
    text-decoration: none;
    font-size: 18px;
    padding: 10px 18px;
    border-radius: 5px;
    background: #f518ed;
    white-space: nowrap;
}


.topnav a:hover {
    background-color: #f518ed;
    color: white;
}

/* Active page */
.topnav a.active {
    background-color: #2563eb;
    color: white;
}


.card {
    background: #e962f5;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid #e0e0e0;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    border-left: 5px solid #4a90e2;
}

/* Section Title */
.section-title {
    font-size: 28px;
    color: #2c7be5;
    font-weight: 700;
    margin-bottom: 15px;
}

.subsection-title {
    font-size: 20px;
    color: #ff9900;
    font-weight: 600;
    margin-top: 5px;
}

/* Divider */
.custom-divider {
    margin-top: 5px;
    margin-bottom: 20px;
    height: 5px;
    background: linear-gradient(to right, #4a90e2, transparent);
}

/* Center Text */
.center-text { text-align: center; }


/* ---------- MOBILE RESPONSIVENESS ---------- */
@media (max-width: 600px) {

    .topnav {
        padding: 10px;
        gap: 6px;
        justify-content: center;
        margin-left: 0;
        margin-top: -20px;
    }

    .topnav a {
        font-size: 14px !important;
        padding: 8px 12px;
    }

    .section-title {
        font-size: 22px;
    }

    .subsection-title {
        font-size: 18px;
    }

    .card {
        padding: 15px;
    }
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

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Project Background & Significance</h4>", unsafe_allow_html=True)
    st.write("""
This project conducts a comprehensive analysis of daily air quality data collected from major Indian cities between 2015 and 2020, capturing a crucial period of rapid urbanization and environmental change. The dataset contains measurements of critical atmospheric pollutants such as PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, and O3, alongside volatile organic compounds including Benzene, Toluene, and Xylene. Together with the Air Quality Index (AQI) and its associated AQI_Bucket classifications, these variables provide an in-depth picture of pollution levels, seasonal variations, and regional disparities across India. Understanding these trends is essential for developing informed environmental policies,
improving public health outcomes, and supporting sustainable urban planning.
""")
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)


with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Project Purpose & Analytical Approach</h4>", unsafe_allow_html=True)
    st.write("""
    The primary objective of this project is to clean, preprocess, and transform the raw dataset into a reliable and structured form suitable for detailed analysis. Through comprehensive exploratory data analysis (EDA), the project identifies pollutant behaviors, uncovers hidden patterns, and examines correlations that influence overall air quality. Feature engineering techniques are applied to enrich the dataset, enabling deeper insights into pollutant interactions and AQI trends. Visualizations—including time-series plots, heatmaps, and distribution charts—enhance interpretability and support evidence-based conclusions.
    This rigorous analytical approach ensures that the findings are both meaningful and actionable.
""")
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)


with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Machine Learning, Implementation & Tools</h4>", unsafe_allow_html=True)
    st.write("""
    Building on the analytical foundation, the project develops a machine learning classification model capable of predicting AQI_Bucket categories based on pollutant concentrations. This model is trained, evaluated, and optimized using modern machine learning techniques to ensure robust predictive performance. To enhance accessibility and real-world applicability, a lightweight GUI application is implemented, allowing users to explore the data interactively and generate AQI predictions in real time. Throughout the project lifecycle, GitHub is utilized for version control, collaboration, documentation, and workflow management, ensuring transparency and reproducibility. Together,
    these components create a complete end-to-end data science solution—from raw data to actionable insights and intelligent prediction.
""")
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

st.subheader("Static Analysis Plots")


st.write("""
The heatmap shows which columns contain missing values and how they are distributed. Most pollutants had scattered missing points, which is common in environmental datasets due to sensor downtime or incomplete reporting. This visualization helped confirm the need for imputation during data cleaning.
""")

image_path_1 = os.path.join("images", "opk.png")


if os.path.exists(image_path_1):
    st.image(image_path_1, caption="Correlation heatmap", use_column_width=True)
else:
    st.warning(f"Image not found at path: {image_path_1}")


