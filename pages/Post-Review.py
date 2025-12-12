import streamlit as st

st.set_page_config(page_title="Machine Learning")

st.title("Logistic Regression Evaluation")

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
     border-left: 5px solid #4a90e2;
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
    height: 5px;
    background: linear-gradient(to right, #4a90e2, transparent);
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


st.write("""
The Logistic Regression model actually did a pretty good job, reaching about 96% accuracy. It was able to correctly classify most of the AQI categories, especially the major ones like Moderate, Poor, and Satisfactory. These categories had very strong precision and recall scores.

The only area where the model struggled a bit was with the Good category, where it mixed things up more often. This is not surprising because Logistic Regression is a simpler model and sometimes has trouble with complex boundaries between classes.

Overall, the model still performs well and gives a solid baseline, but it’s clear that more advanced models like Random Forest and XGBoost do a better job at capturing the full patterns in the data.
""")
col1, col2, col3 = st.columns(3)

# ============================
# COLUMN 1
# ============================
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Project Background & Significance</h4>", unsafe_allow_html=True)
    st.write("""
This project delivers a comprehensive exploration of air quality conditions across major Indian cities between **2015 and 2020**, a period marked by rapid industrial growth, increased vehicular emissions, and evolving environmental policies. The dataset captures essential pollutants such as **PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3**, and volatile organic compounds like **Benzene, Toluene, and Xylene**. These indicators collectively reveal the extent of urban pollution, highlight high-risk regions, and uncover seasonal fluctuations driven by climatic conditions and human activity.

By combining pollutant data with the **Air Quality Index (AQI)** and **AQI_Bucket**, the project provides a nuanced understanding of public exposure risks. This insight is vital for environmental monitoring, healthcare planning, and government interventions. The findings support evidence-based policies aimed at reducing pollution, improving respiratory health, and fostering sustainable city development.
""")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)



# ============================
# COLUMN 2
# ============================
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Project Purpose & Analytical Approach</h4>", unsafe_allow_html=True)
    st.write("""
The goal of this project is to transform raw environmental data into meaningful insights through a structured analytical pipeline. The first stage focuses on **data cleaning**, addressing missing values, removing inconsistencies, and standardizing formats to ensure accuracy. This is followed by **exploratory data analysis (EDA)**, where pollutant distributions, temporal trends, and inter-variable correlations are examined to uncover hidden behaviors.

Advanced visualization tools—including correlation heatmaps, time-series graphs, and pollutant distribution charts—enable clearer interpretation of pollutant dynamics. Through **feature engineering**, new meaningful attributes are created to strengthen predictive modeling. This systematic approach ensures that every stage of analysis contributes to a richer and more interpretable dataset, paving the way for reliable machine learning outcomes.
""")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)



# ============================
# COLUMN 3
# ============================
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='subsection-title'>Machine Learning, Implementation & Tools</h4>", unsafe_allow_html=True)
    st.write("""
Building on the analytical insights, the project employs **machine learning techniques** to predict AQI categories using pollutant concentrations as inputs. Several classification models— including Logistic Regression, Random Forest, and XGBoost—are trained and compared to identify the most accurate performer. Performance metrics such as accuracy, precision, recall, and confusion matrices help evaluate model reliability.

To enhance usability, the system is integrated into an interactive **Streamlit-based GUI**, allowing users to visualize trends, explore pollutant behaviors, and generate AQI predictions in real time. Version control and collaboration are maintained through **GitHub**, ensuring transparent development, traceable updates, and professional project structure. Together, these components deliver a complete end-to-end data science solution that transitions seamlessly from raw data analysis to intelligent, actionable predictions.
""")
    st.markdown("</div>", unsafe_allow_html=True)


st.title("Comparison Between Random Forest and Logistic Regression")



st.write("""
Both models did a solid job, but Random Forest clearly stood out. It achieved almost perfect accuracy, correctly predicting nearly every AQI category. Even the tricky categories like Very Poor and Severe were handled really well. This makes sense because Random Forest is great at picking up complex patterns in the data.

Logistic Regression also performed nicely with about 96% accuracy, but it struggled a bit more—especially with the Good category. This happens because Logistic Regression is a simpler model and doesn’t capture complicated relationships as well as Random Forest does.

**In simple terms:**
Random Forest understands the data better and gives much more accurate predictions.
Logistic Regression is good, but not as strong for this type of problem.
""")



