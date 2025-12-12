import streamlit as st

st.set_page_config(page_title="Machine Learning", layout="wide")

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

.card {
    background: #e962f5;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #e0e0e0;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    border-left: 6px solid #4a90e2;
}

.subsection-title {
    font-size: 22px;
    color: #ff9900;
    font-weight: 600;
}

.custom-divider {
    height: 5px;
    background: linear-gradient(to right, #4a90e2, transparent);
    margin: 20px 0;
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

st.title("Logistic Regression Evaluation")

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.write("""
The Logistic Regression model performed strongly with an accuracy of **about 96%**, especially for major AQI categories like **Moderate**, **Poor**, and **Satisfactory**, where both precision and recall were high.

However, it struggled slightly with the **Good** category, often confusing it with nearby AQI classes. This is expected because Logistic Regression is a simpler linear model that cannot perfectly capture complex, non-linear relationships between pollutants and AQI categories.

**In summary:**  
- Logistic Regression gives a strong, reliable baseline  
- But it lacks the deeper pattern recognition capability of tree-based models  
""")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

# -------- COLUMN 1 --------
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Project Background & Significance</h4>", unsafe_allow_html=True)
    st.write("""
This project explores major Indian cities' air quality from **2015 to 2020**, capturing a period of intense industrial and urban expansion. The dataset includes pollutants such as **PM2.5, PM10, NO₂, NOx, NH₃, CO, SO₂, O₃**, and VOCs (Benzene, Toluene, Xylene), offering a complete profile of environmental health.

Combined with AQI and AQI_Bucket values, the data reveals regional disparities, seasonal pollution cycles, and population exposure risks. These insights are critical for public health strategies, urban planning, and environmental policy development.
""")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

# -------- COLUMN 2 --------
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Project Purpose & Analytical Approach</h4>", unsafe_allow_html=True)
    st.write("""
The project transforms raw environmental data into structured insights through **data cleaning, preprocessing**, and **exploratory data analysis (EDA)**. Missing values are treated, irregularities removed, and pollutant patterns are explored using distributions, heatmaps, and time trends.

Through **feature engineering**, new variables are created to strengthen model performance. The analytical workflow ensures clarity, accuracy, and deeper understanding of pollution behavior across cities and time periods.
""")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

# -------- COLUMN 3 --------
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Machine Learning, Implementation & Tools</h4>", unsafe_allow_html=True)
    st.write("""
Using the cleaned dataset, multiple machine learning models—including **Logistic Regression**, **Random Forest**, and **XGBoost**—were trained to predict AQI categories. Their performance was evaluated using accuracy, precision, recall, and confusion matrices.

The final project includes an interactive **Streamlit app** for real-time pollutant visualization and AQI prediction. Version control through **GitHub** ensures transparency, collaboration, and reproducibility, forming a complete end-to-end machine learning pipeline.
""")
    st.markdown("</div>", unsafe_allow_html=True)


st.title("Comparison Between Random Forest and Logistic Regression")

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.write("""
**Random Forest performed exceptionally**, achieving near-perfect accuracy across all AQI categories—even the difficult ones like **Very Poor** and **Severe**. Its strength comes from handling complex, non-linear patterns that Logistic Regression cannot capture.

**Logistic Regression**, with its 96% accuracy, still performs well but struggles with subtle class boundaries such as the **Good** category.

###  Summary:
- **Random Forest:** superior accuracy, deeper pattern recognition  
- **Logistic Regression:** strong baseline model but limited by linear assumptions  
""")
st.markdown("</div>", unsafe_allow_html=True)
