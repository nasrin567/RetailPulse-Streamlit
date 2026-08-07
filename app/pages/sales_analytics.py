import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# SALES ANALYTICS
# =====================================================

def show():

    # -------------------------------------------------
    # CSS
    # -------------------------------------------------

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

    """,unsafe_allow_html=True)

    # -------------------------------------------------
    # LOAD DATA
    # -------------------------------------------------

    DATA = Path("data/dashboard")

    sales = pd.read_csv(DATA/"sales_analytics.csv")

    sales["ds"] = pd.to_datetime(sales["ds"])

    # -------------------------------------------------
    # HEADER
    # -------------------------------------------------

    st.markdown("""
    <div class="dashboard-title">
        📈 Sales Analytics
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class="dashboard-subtitle">
        Analyze revenue trends and overall sales performance.
    </div>
    """,unsafe_allow_html=True)

    st.divider()

    # -------------------------------------------------
    # KPI VALUES
    # -------------------------------------------------

    total_revenue = sales["y"].sum()

    avg_daily = sales["y"].mean()

    max_sales = sales["y"].max()

    total_days = sales["ds"].nunique()

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.metric(
            "💰 Total Revenue",
            f"${total_revenue:,.0f}"
        )

    with c2:

        st.metric(
            "📊 Average Daily Sales",
            f"${avg_daily:,.0f}"
        )

    with c3:

        st.metric(
            "🔥 Highest Sales",
            f"${max_sales:,.0f}"
        )

    with c4:

        st.metric(
            "📅 Sales Days",
            total_days
        )

    st.divider()

        # =====================================================
    # DAILY SALES TREND
    # =====================================================

    st.subheader("📈 Daily Sales Trend")

    fig = px.line(

        sales,

        x="ds",

        y="y",

        markers=True,

        color_discrete_sequence=["#4F46E5"]

    )

    fig.update_traces(

        line=dict(width=3)

    )

    fig.update_layout(

        height=450,

        xaxis_title="Date",

        yaxis_title="Revenue ($)",

        hovermode="x unified",

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # MONTHLY REVENUE
    # =====================================================

    monthly = (

        sales

        .set_index("ds")

        .resample("ME")

        .sum()

        .reset_index()

    )

    monthly["Month"] = monthly["ds"].dt.strftime("%b %Y")

    left, right = st.columns(2)

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

            height=430,

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

            height=430,

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
    # 7-DAY MOVING AVERAGE
    # =====================================================

    st.subheader("📉 7-Day Moving Average")

    moving = sales.copy()

    moving["Moving Average"] = (
        moving["y"]
        .rolling(window=7)
        .mean()
    )

    fig = px.line(

        moving,

        x="ds",

        y=["y", "Moving Average"],

        template="plotly_white"

    )

    fig.data[0].name = "Daily Revenue"
    fig.data[1].name = "7-Day Average"

    fig.data[0].line.color = "#4338CA"
    fig.data[1].line.color = "#F59E0B"

    fig.update_layout(

        height=450,

        hovermode="x unified",

        xaxis_title="Date",

        yaxis_title="Revenue ($)",

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # TOP 10 SALES DAYS
    # =====================================================

    st.subheader("🏆 Top 10 Highest Revenue Days")

    top_days = (
        sales
        .sort_values("y", ascending=False)
        .head(10)
        .copy()
    )

    top_days["Date"] = top_days["ds"].dt.strftime("%d %b %Y")

    fig = px.bar(

        top_days,

        x="y",

        y="Date",

        orientation="h",

        text_auto=".2s",

        color="y",

        color_continuous_scale="Purples"

    )

    fig.update_layout(

        height=450,

        yaxis=dict(categoryorder="total ascending"),

        xaxis_title="Revenue ($)",

        yaxis_title="",

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
    # REVENUE GROWTH ANALYSIS
    # =====================================================

    st.subheader("📊 Revenue Growth Analysis")

    monthly_growth = monthly.copy()

    monthly_growth["Growth %"] = (
        monthly_growth["y"]
        .pct_change()
        *100
    )

    fig = px.bar(

        monthly_growth,

        x="Month",

        y="Growth %",

        text_auto=".1f",

        color="Growth %",

        color_continuous_scale="RdYlGn"

    )

    fig.update_layout(

        height=430,

        xaxis_title="",

        yaxis_title="Growth (%)",

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

        # =====================================================
    # SALES INSIGHTS
    # =====================================================

    st.subheader("💡 Sales Insights")

    best_day = sales.loc[sales["y"].idxmax()]
    worst_day = sales.loc[sales["y"].idxmin()]

    best_month = monthly.loc[monthly["y"].idxmax()]
    worst_month = monthly.loc[monthly["y"].idxmin()]

    total_months = monthly.shape[0]

    c1, c2 = st.columns(2)

    # -----------------------------------------------------

    with c1:

        st.success(f"""

### 📈 Performance Highlights

💰 **Total Revenue**

${total_revenue:,.2f}

📅 **Best Revenue Month**

{best_month['Month']}

Revenue:

${best_month['y']:,.2f}

🔥 **Highest Revenue Day**

{best_day['ds'].strftime('%d %b %Y')}

Revenue:

${best_day['y']:,.2f}

""")

    # -----------------------------------------------------

    with c2:

        st.info(f"""

### 📊 Business Statistics

📉 **Lowest Revenue Month**

{worst_month['Month']}

Revenue:

${worst_month['y']:,.2f}

📅 **Lowest Revenue Day**

{worst_day['ds'].strftime('%d %b %Y')}

Revenue:

${worst_day['y']:,.2f}

🗓 **Months Available**

{total_months}

""")

    st.divider()

    # =====================================================
    # MONTHLY SUMMARY TABLE
    # =====================================================

    st.subheader("📋 Monthly Revenue Summary")

    summary = monthly.copy()

    summary.columns = [
        "Date",
        "Revenue",
        "Month"
    ]

    summary = summary[
        [
            "Month",
            "Revenue"
        ]
    ]

    summary["Revenue"] = summary["Revenue"].round(2)

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    st.download_button(

        "📥 Download Sales Analytics CSV",

        data=sales.to_csv(index=False),

        file_name="sales_analytics.csv",

        mime="text/csv"

    )

    st.divider()

    st.success("""

### 📌 Executive Summary

✅ Daily revenue trend has been analyzed.

✅ Monthly revenue highlights seasonality.

✅ Moving average smooths sales fluctuations.

✅ Highest revenue days help identify peak demand.

✅ Revenue growth analysis supports business planning.

""")

    st.divider()

    st.caption(
        "RetailPulse • Sales Analytics Dashboard • AI-Powered Business Intelligence"
    )