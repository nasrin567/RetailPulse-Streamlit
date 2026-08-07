import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================

def show():

    # -------------------------------------------------
    # CUSTOM CSS
    # -------------------------------------------------

    st.markdown("""
    <style>

    .stApp{
        background:#F5F7FB;
    }

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    #MainMenu{
        visibility:hidden;
    }

    /* Sidebar */

    [data-testid="stSidebar"]{
        background:linear-gradient(180deg,#312E81,#4338CA);
    }

    [data-testid="stSidebar"] *{
        color:white;
    }

    /* Dashboard Title */

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

    /* KPI */

    div[data-testid="metric-container"]{

        background:white;

        border-radius:18px;

        padding:20px;

        border-left:6px solid #6366F1;

        box-shadow:0px 8px 20px rgba(0,0,0,0.08);

    }

    </style>

    """,unsafe_allow_html=True)

    # -------------------------------------------------
    # LOAD DATA
    # -------------------------------------------------

    DATA = Path("data/dashboard")

    sales = pd.read_csv(DATA/"sales_analytics.csv")

    sales["ds"] = pd.to_datetime(sales["ds"])

    country = pd.read_csv(DATA/"country_analytics.csv")

    products = pd.read_csv(DATA/"product_analytics.csv")

    customers = pd.read_csv(DATA/"customer_segmentation.csv")

    business = pd.read_csv(DATA/"business_insights.csv")

        # =====================================================
    # DASHBOARD HEADER
    # =====================================================

    st.markdown("""
    <div class="dashboard-title">
        📊 RetailPulse Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dashboard-subtitle">
        AI-Powered Customer Analytics & Demand Forecasting
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================================================
    # KPI VALUES
    # =====================================================

    total_revenue = float(
        business.loc[
            business["Metric"]=="Total Revenue",
            "Value"
        ].values[0]
    )

    total_orders = int(
        business.loc[
            business["Metric"]=="Total Orders",
            "Value"
        ].values[0]
    )

    total_customers = int(
        business.loc[
            business["Metric"]=="Total Customers",
            "Value"
        ].values[0]
    )

    total_products = int(
        business.loc[
            business["Metric"]=="Products",
            "Value"
        ].values[0]
    )

    # =====================================================
    # KPI CARDS
    # =====================================================

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.metric(
            "💰 Total Revenue",
            f"${total_revenue:,.0f}"
        )

    with c2:

        st.metric(
            "📦 Total Orders",
            f"{total_orders:,}"
        )

    with c3:

        st.metric(
            "👥 Customers",
            f"{total_customers:,}"
        )

    with c4:

        st.metric(
            "🛍 Products",
            f"{total_products:,}"
        )

    st.divider()

        # =====================================================
    # REVENUE TREND
    # =====================================================

    st.subheader("📈 Revenue Trend")

    revenue_trend = (
        sales
        .set_index("ds")
        .resample("ME")
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue_trend,
        x="ds",
        y="y",
        markers=True,
        color_discrete_sequence=["#4F46E5"]
    )

    fig.update_traces(
        line=dict(width=4)
    )

    fig.update_layout(
        height=450,
        xaxis_title="Month",
        yaxis_title="Revenue ($)",
        paper_bgcolor="white",
        plot_bgcolor="white",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # MONTHLY REVENUE & DISTRIBUTION
    # =====================================================

    monthly = revenue_trend.copy()

    monthly["Month"] = monthly["ds"].dt.strftime("%b %Y")

    left,right = st.columns(2)

    # -----------------------------------------------------

    with left:

        st.subheader("📅 Monthly Revenue")

        fig = px.bar(

            monthly,

            x="Month",

            y="y",

            text_auto=".2s",

            color="y",

            color_continuous_scale="Blues"

        )

        fig.update_layout(

            height=420,

            xaxis_title="",

            yaxis_title="Revenue",

            coloraxis_showscale=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # -----------------------------------------------------

    with right:

        st.subheader("📊 Revenue Distribution")

        fig = px.histogram(

            sales,

            x="y",

            nbins=30,

            color_discrete_sequence=["#4338CA"]

        )

        fig.update_layout(

            height=420,

            xaxis_title="Revenue",

            yaxis_title="Frequency",

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

        # =====================================================
    # TOP COUNTRIES & TOP PRODUCTS
    # =====================================================

    left, right = st.columns(2)

    # =====================================================
    # TOP COUNTRIES
    # =====================================================

    with left:

        st.subheader("🌍 Top 10 Countries by Revenue")

        top_country = (
            country
            .sort_values("TotalRevenue", ascending=False)
            .head(10)
        )

        fig = px.bar(

            top_country,

            x="TotalRevenue",

            y="Country",

            orientation="h",

            text_auto=".2s",

            color="Country",

            color_discrete_sequence=px.colors.qualitative.Bold

        )

        fig.update_layout(

            height=500,

            yaxis=dict(categoryorder="total ascending"),

            xaxis_title="Revenue ($)",

            yaxis_title="",

            showlegend=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # TOP PRODUCTS
    # =====================================================

    with right:

        st.subheader("🛍 Top 10 Products by Revenue")

        top_products = (
            products
            .sort_values("TotalRevenue", ascending=False)
            .head(10)
        )

        fig = px.bar(

            top_products,

            x="TotalRevenue",

            y="Description",

            orientation="h",

            text_auto=".2s",

            color="Description",

            color_discrete_sequence=px.colors.qualitative.Set3

        )

        fig.update_layout(

            height=500,

            yaxis=dict(categoryorder="total ascending"),

            xaxis_title="Revenue ($)",

            yaxis_title="",

            showlegend=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

        # =====================================================
    # CUSTOMER SEGMENTATION
    # =====================================================

    st.subheader("👥 Customer Segmentation")

    segment_summary = (
        customers["CustomerSegment"]
        .value_counts()
        .reset_index()
    )

    segment_summary.columns = [
        "CustomerSegment",
        "Count"
    ]

    segment_summary["Percentage"] = (
        segment_summary["Count"]
        / segment_summary["Count"].sum()
        *100
    ).round(2)

    left,right = st.columns([1.2,1])

    # -----------------------------------------------------

    with left:

        fig = px.pie(

            segment_summary,

            names="CustomerSegment",

            values="Count",

            hole=0.60,

            color="CustomerSegment",

            color_discrete_sequence=[
                "#4F46E5",
                "#10B981",
                "#F59E0B",
                "#EF4444",
                "#8B5CF6",
                "#06B6D4"
            ]

        )

        fig.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        fig.update_layout(

            height=480,

            paper_bgcolor="white",

            showlegend=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # -----------------------------------------------------

    with right:

        st.subheader("📋 Segment Summary")

        st.dataframe(

            segment_summary,

            use_container_width=True,

            hide_index=True

        )

    st.divider()

    # =====================================================
    # BUSINESS INSIGHTS
    # =====================================================

    st.subheader("💡 Business Insights")

    col1,col2 = st.columns(2)

    with col1:

        for _,row in business.iloc[:len(business)//2].iterrows():

            st.success(
                f"**{row['Metric']}**\n\n{row['Value']}"
            )

    with col2:

        for _,row in business.iloc[len(business)//2:].iterrows():

            st.info(
                f"**{row['Metric']}**\n\n{row['Value']}"
            )

    st.divider()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    st.subheader("📌 Executive Summary")

    st.success("""

✅ Revenue is primarily driven by high-performing markets.

✅ Customer segmentation identifies valuable customer groups.

✅ Product analysis highlights the highest revenue-generating products.

✅ Country-wise analysis reveals geographic sales distribution.

✅ This dashboard provides a quick executive snapshot for strategic business decisions.

""")

    st.download_button(

        "📥 Download Executive Overview",

        data=sales.to_csv(index=False),

        file_name="executive_overview.csv",

        mime="text/csv"

    )

    st.divider()

    st.caption(
        "RetailPulse • AI-Powered Customer Analytics & Demand Forecasting"
    )