import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# =====================================================
# COUNTRY ANALYSIS DASHBOARD
# =====================================================

def show():

    # =====================================================
    # CSS
    # =====================================================

    st.markdown("""
    <style>

    .dashboard-title{
        font-size:40px;
        font-weight:700;
        color:#312E81;
    }

    .dashboard-subtitle{
        font-size:18px;
        color:#64748B;
        margin-top:-10px;
    }

    div[data-testid="metric-container"]{

        background:white;
        border-radius:18px;
        padding:18px;
        border-left:6px solid #6366F1;
        box-shadow:0px 8px 20px rgba(0,0,0,0.08);

    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # LOAD DATA
    # =====================================================

    DATA = Path("data/dashboard")

    country = pd.read_csv(DATA / "country_analytics.csv")

    # =====================================================
    # SIDEBAR FILTERS
    # =====================================================

    st.sidebar.markdown("## 🔍 Filters")

    selected_country = st.sidebar.selectbox(

        "Country",

        ["All"] + sorted(country["Country"].dropna().unique().tolist())

    )

    # =====================================================
    # FILTER DATA
    # =====================================================

    filtered = country.copy()

    if selected_country != "All":

        filtered = filtered[
            filtered["Country"] == selected_country
        ]

    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.markdown("""
    <div class="dashboard-title">
    🌍 Country Analysis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dashboard-subtitle">
    Analyze country-wise sales performance, customers and revenue contribution.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================================================
    # KPI CALCULATIONS
    # =====================================================

    total_countries = filtered["Country"].nunique()

    total_revenue = filtered["TotalRevenue"].sum()

    total_orders = filtered["TotalOrders"].sum()

    total_customers = filtered["TotalCustomers"].sum()

    avg_revenue_customer = filtered["AverageRevenuePerCustomer"].mean()

    # =====================================================
    # KPI CARDS
    # =====================================================

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.metric(

            "Countries",

            f"{total_countries:,}"

        )

    with c2:

        st.metric(

            "Revenue",

            f"${total_revenue:,.2f}"

        )

    with c3:

        st.metric(

            "Orders",

            f"{int(total_orders):,}"

        )

    with c4:

        st.metric(

            "Customers",

            f"{int(total_customers):,}"

        )

    with c5:

        st.metric(

            "Avg Revenue / Customer",

            f"${avg_revenue_customer:,.2f}"

        )

    st.divider()

        # =====================================================
    # REVENUE BY COUNTRY
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("💰 Revenue by Country")

        revenue = (

            filtered

            .sort_values("TotalRevenue", ascending=False)

        )

        fig = px.bar(

            revenue,

            x="Country",

            y="TotalRevenue",

            text_auto=".2s",

            color="TotalRevenue",

            color_continuous_scale="Blues"

        )

        fig.update_layout(

            height=450,

            xaxis_title="Country",

            yaxis_title="Revenue ($)",

            coloraxis_showscale=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # CUSTOMERS BY COUNTRY
    # =====================================================

    with right:

        st.subheader("👥 Customers by Country")

        customers = (

            filtered

            .sort_values("TotalCustomers", ascending=False)

        )

        fig = px.bar(

            customers,

            x="Country",

            y="TotalCustomers",

            text_auto=True,

            color="TotalCustomers",

            color_continuous_scale="Greens"

        )

        fig.update_layout(

            height=450,

            xaxis_title="Country",

            yaxis_title="Customers",

            coloraxis_showscale=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # TOTAL ORDERS BY COUNTRY
    # =====================================================

    st.subheader("📦 Orders by Country")

    orders = (

        filtered

        .sort_values("TotalOrders", ascending=False)

    )

    fig = px.bar(

        orders,

        x="Country",

        y="TotalOrders",

        text_auto=True,

        color="TotalOrders",

        color_continuous_scale="Oranges"

    )

    fig.update_layout(

        height=500,

        xaxis_title="Country",

        yaxis_title="Total Orders",

        coloraxis_showscale=False,

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

        # =====================================================
    # QUANTITY SOLD BY COUNTRY
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("📦 Quantity Sold by Country")

        quantity = (

            filtered

            .sort_values("TotalQuantity", ascending=False)

        )

        fig = px.bar(

            quantity,

            x="Country",

            y="TotalQuantity",

            text_auto=True,

            color="TotalQuantity",

            color_continuous_scale="Purples"

        )

        fig.update_layout(

            height=450,

            xaxis_title="Country",

            yaxis_title="Quantity Sold",

            coloraxis_showscale=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # AVERAGE REVENUE PER CUSTOMER
    # =====================================================

    with right:

        st.subheader("💵 Average Revenue per Customer")

        avg_rev = (

            filtered

            .sort_values(

                "AverageRevenuePerCustomer",

                ascending=False

            )

        )

        fig = px.bar(

            avg_rev,

            x="Country",

            y="AverageRevenuePerCustomer",

            text_auto=".2f",

            color="AverageRevenuePerCustomer",

            color_continuous_scale="Teal"

        )

        fig.update_layout(

            height=450,

            xaxis_title="Country",

            yaxis_title="Average Revenue ($)",

            coloraxis_showscale=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # REVENUE VS CUSTOMERS
    # =====================================================

    st.subheader("🌍 Revenue vs Customers")

    fig = px.scatter(

        filtered,

        x="TotalCustomers",

        y="TotalRevenue",

        size="TotalOrders",

        color="TotalQuantity",

        hover_name="Country",

        hover_data=[

            "AverageRevenuePerCustomer"

        ],

        color_continuous_scale="Viridis"

    )

    fig.update_layout(

        height=600,

        xaxis_title="Total Customers",

        yaxis_title="Total Revenue ($)",

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

        # =====================================================
    # COUNTRY SUMMARY TABLE
    # =====================================================

    st.subheader("📋 Country Performance Summary")

    summary = filtered.copy()

    summary = summary.sort_values(
        "TotalRevenue",
        ascending=False
    )

    st.dataframe(

        summary[
            [
                "Country",
                "TotalRevenue",
                "TotalOrders",
                "TotalCustomers",
                "TotalQuantity",
                "AverageRevenuePerCustomer"
            ]
        ],

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # BUSINESS INSIGHTS
    # =====================================================

    highest_revenue = filtered.loc[
        filtered["TotalRevenue"].idxmax()
    ]

    highest_customers = filtered.loc[
        filtered["TotalCustomers"].idxmax()
    ]

    left, right = st.columns(2)

    with left:

        st.success(f"""

### 💰 Highest Revenue Country

**Country**

{highest_revenue['Country']}

**Revenue**

${highest_revenue['TotalRevenue']:,.2f}

**Orders**

{int(highest_revenue['TotalOrders']):,}

""")

    with right:

        st.info(f"""

### 👥 Largest Customer Base

**Country**

{highest_customers['Country']}

**Customers**

{int(highest_customers['TotalCustomers']):,}

**Average Revenue / Customer**

${highest_customers['AverageRevenuePerCustomer']:,.2f}

""")

    st.divider()

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    st.download_button(

        "📥 Download Country Analysis Report",

        data=filtered.to_csv(index=False),

        file_name="country_analysis_report.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    st.subheader("📌 Executive Summary")

    total_countries = filtered["Country"].nunique()

    total_revenue = filtered["TotalRevenue"].sum()

    total_orders = filtered["TotalOrders"].sum()

    total_customers = filtered["TotalCustomers"].sum()

    avg_customer_revenue = filtered["AverageRevenuePerCustomer"].mean()

    st.success(f"""

### Country Performance Summary

• Total Countries Analysed : **{total_countries:,}**

• Total Revenue : **${total_revenue:,.2f}**

• Total Orders : **{int(total_orders):,}**

• Total Customers : **{int(total_customers):,}**

• Average Revenue per Customer : **${avg_customer_revenue:,.2f}**

• Identify countries contributing the highest revenue.

• Compare customer base and order volume across markets.

• Support business expansion and regional marketing decisions.

""")

    st.divider()

    st.caption(
        "RetailPulse • Country Analysis Dashboard • Powered by Streamlit & Plotly"
    )