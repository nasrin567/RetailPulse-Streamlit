import streamlit as st

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# IMPORT PAGES
# ======================================================

from dashboard_pages import executive_overview
from dashboard_pages import sales_analytics
from dashboard_pages import customer_analytics
from dashboard_pages import customer_segmentation
from dashboard_pages import customer_churn
from dashboard_pages import inventory
from dashboard_pages import country_analysis

# ======================================================
# GLOBAL CSS
# ======================================================

st.markdown("""
<style>

/* Hide Streamlit */

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

/* Sidebar */

[data-testid="stSidebar"]{
background:linear-gradient(180deg,#312E81,#4338CA);
}

[data-testid="stSidebar"] *{
color:white;
}

/* Navigation */

div[role="radiogroup"] label{
font-size:18px;
padding:8px;
}

/* Filter Labels */

[data-testid="stSidebar"] label{
color:white !important;
font-weight:600;
}

/* Selectbox */

[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"]{
background:white;
color:black !important;
border-radius:8px;
}

/* Input */

[data-testid="stSidebar"] input{
color:black !important;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("🛒 RetailPulse")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Executive Dashboard",

        "📈 Sales Analytics",

        "👥 Customer Analytics",

        "🎯 Customer Segmentation",

        "⚠ Customer Churn",

        "📦 Inventory",

        "🌍 Country Analysis",

        "🛍 Product Analytics",

        "📅 Demand Forecast",

        "💡 Business Insights"

    ]

)

# ======================================================
# NAVIGATION
# ======================================================

if page=="🏠 Executive Dashboard":

    executive_overview.show()

elif page=="📈 Sales Analytics":

    sales_analytics.show()

elif page=="👥 Customer Analytics":

    customer_analytics.show()

elif page=="🎯 Customer Segmentation":

    customer_segmentation.show()

elif page=="⚠ Customer Churn":

    customer_churn.show()

elif page=="📦 Inventory":

    inventory.show()  

elif page == "🌍 Country Analysis":

    country_analysis.show()      

else:

    st.title(page)

    st.info("🚧 This dashboard will be built next.")