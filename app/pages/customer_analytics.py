import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# CUSTOMER ANALYTICS
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

    customers = pd.read_csv(DATA / "customer_analytics.csv")

    customers["FirstPurchaseDate"] = pd.to_datetime(
        customers["FirstPurchaseDate"]
    )

    customers["LastPurchaseDate"] = pd.to_datetime(
        customers["LastPurchaseDate"]
    )

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="dashboard-title">
    ðŸ‘¥ Customer Analytics
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dashboard-subtitle">
    Analyze customer purchasing behaviour, revenue and engagement.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================================================
    # KPI VALUES
    # =====================================================

    total_customers = customers["CustomerID"].nunique()

    total_revenue = customers["TotalRevenue"].sum()

    total_invoices = customers["TotalInvoices"].sum()

    avg_order_value = customers["AvgOrderValue"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "ðŸ‘¥ Customers",
            f"{total_customers:,}"
        )

    with c2:

        st.metric(
            "ðŸ’° Revenue",
            f"${total_revenue:,.0f}"
        )

    with c3:

        st.metric(
            "ðŸ§¾ Total Invoices",
            f"{int(total_invoices):,}"
        )

    with c4:

        st.metric(
            "ðŸ›’ Avg Order Value",
            f"${avg_order_value:,.2f}"
        )

    st.divider()

    # =====================================================
    # CUSTOMER REVENUE ANALYSIS
    # =====================================================

    left, right = st.columns(2)

    # -----------------------------------------------------

    with left:

        st.subheader("Top 10 Customers by Revenue")

        top_customers = (

            customers

            .sort_values("TotalRevenue", ascending=False)

            .head(10)

        )

        fig = px.bar(

            top_customers,

            x="TotalRevenue",

            y=top_customers["CustomerID"].astype(str),

            orientation="h",

            text_auto=".2s",

            color="TotalRevenue",

            color_continuous_scale="Blues"

        )

        fig.update_layout(

            height=450,

            yaxis=dict(categoryorder="total ascending"),

            xaxis_title="Revenue ($)",

            yaxis_title="Customer ID",

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

        st.subheader("Invoice Distribution")

        fig = px.histogram(

            customers,

            x="TotalInvoices",

            nbins=25,

            color_discrete_sequence=["#4F46E5"]

        )

        fig.update_layout(

            height=450,

            xaxis_title="Invoices",

            yaxis_title="Customers",

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # ORDER VALUE ANALYSIS
    # =====================================================

    left, right = st.columns(2)

    # -----------------------------------------------------

    with left:

        st.subheader("Average Order Value")

        fig = px.box(

            customers,

            y="AvgOrderValue",

            points="outliers",

            color_discrete_sequence=["#10B981"]

        )

        fig.update_layout(

            height=420,

            yaxis_title="Average Order Value ($)",

            paper_bgcolor="white",

            plot_bgcolor="white",

            showlegend=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # -----------------------------------------------------

    with right:

        st.subheader("Basket Size")

        fig = px.box(

            customers,

            y="AvgBasketSize",

            color_discrete_sequence=["#F59E0B"]

        )

        fig.update_layout(

            height=420,

            yaxis_title="Average Basket Size",

            paper_bgcolor="white",

            plot_bgcolor="white",

            showlegend=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # CUSTOMER SEGMENTS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("Customer Segments")

        segment = (
            customers["CustomerSegment"]
            .value_counts()
            .reset_index()
        )

        segment.columns = [
            "CustomerSegment",
            "Count"
        ]

        fig = px.pie(

            segment,

            names="CustomerSegment",

            values="Count",

            hole=0.60,

            color="CustomerSegment",

            color_discrete_sequence=px.colors.qualitative.Bold

        )

        fig.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        fig.update_layout(

            height=450,

            showlegend=False,

            paper_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # CUSTOMER CLUSTERS
    # =====================================================

    with right:

        st.subheader("Cluster Distribution")

        cluster = (
            customers["Cluster"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        cluster.columns = [
            "Cluster",
            "Customers"
        ]

        fig = px.bar(

            cluster,

            x="Cluster",

            y="Customers",

            text_auto=True,

            color="Customers",

            color_continuous_scale="Purples"

        )

        fig.update_layout(

            height=450,

            xaxis_title="Cluster",

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
    # COUNTRY ANALYSIS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("Top Countries")

        country = (
            customers
            .groupby("Country")["TotalRevenue"]
            .sum()
            .reset_index()
            .sort_values("TotalRevenue", ascending=False)
            .head(10)
        )

        fig = px.bar(

            country,

            x="TotalRevenue",

            y="Country",

            orientation="h",

            text_auto=".2s",

            color="Country",

            color_discrete_sequence=px.colors.qualitative.Set2

        )

        fig.update_layout(

            height=450,

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

    with right:

        st.subheader("Preferred Purchase Hour")

        hour = (
            customers["PreferredPurchaseHour"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        hour.columns = [
            "Hour",
            "Customers"
        ]

        fig = px.line(

            hour,

            x="Hour",

            y="Customers",

            markers=True,

            color_discrete_sequence=["#4F46E5"]

        )

        fig.update_traces(

            line=dict(width=4)

        )

        fig.update_layout(

            height=450,

            xaxis_title="Hour of Day",

            yaxis_title="Customers",

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # PREFERRED SEASON ANALYSIS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("Preferred Shopping Season")

        season = (
            customers["PreferredSeason"]
            .value_counts()
            .reset_index()
        )

        season.columns = [
            "Season",
            "Customers"
        ]

        fig = px.pie(

            season,

            names="Season",

            values="Customers",

            hole=0.55,

            color="Season",

            color_discrete_sequence=px.colors.qualitative.Pastel

        )

        fig.update_traces(
            textinfo="percent+label"
        )

        fig.update_layout(
            height=430,
            showlegend=False,
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =====================================================
    # CUSTOMER BEHAVIOUR
    # =====================================================

    with right:

        st.subheader("Customer Behaviour")

        fig = px.scatter(

            customers,

            x="Recency",

            y="Monetary",

            size="Frequency",

            color="Cluster",

            hover_data=[
                "CustomerID",
                "CustomerSegment"
            ],

            color_continuous_scale="Viridis"

        )

        fig.update_layout(

            height=430,

            xaxis_title="Recency",

            yaxis_title="Monetary",

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # =====================================================
    # KEY INSIGHTS
    # =====================================================

    highest_revenue = customers.loc[
        customers["TotalRevenue"].idxmax()
    ]

    highest_invoice = customers.loc[
        customers["TotalInvoices"].idxmax()
    ]

    c1, c2 = st.columns(2)

    with c1:

        st.success(f"""

### ðŸ† Highest Revenue Customer

ðŸ‘¤ Customer ID

**{highest_revenue['CustomerID']}**

ðŸ’° Revenue

**${highest_revenue['TotalRevenue']:,.2f}**

ðŸ§¾ Invoices

**{highest_revenue['TotalInvoices']}**

""")

    with c2:

        st.info(f"""

### ðŸ“¦ Most Active Customer

ðŸ‘¤ Customer ID

**{highest_invoice['CustomerID']}**

ðŸ§¾ Total Invoices

**{highest_invoice['TotalInvoices']}**

ðŸ’µ Avg Order Value

**${highest_invoice['AvgOrderValue']:,.2f}**

""")

    st.divider()

    # =====================================================
    # CUSTOMER SUMMARY
    # =====================================================

    st.subheader("ðŸ“‹ Customer Summary")

    summary = customers[
        [
            "CustomerID",
            "Country",
            "TotalRevenue",
            "TotalInvoices",
            "AvgOrderValue",
            "CustomerSegment"
        ]
    ].sort_values(
        "TotalRevenue",
        ascending=False
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.download_button(

        "ðŸ“¥ Download Customer Analytics Report",

        data=customers.to_csv(index=False),

        file_name="customer_analytics.csv",

        mime="text/csv"

    )

    st.divider()

    st.success("""

### ðŸ“Œ Executive Summary

âœ… Customer revenue distribution analyzed.

âœ… High-value customers identified.

âœ… Purchase behaviour visualized using RFM metrics.

âœ… Country and seasonal preferences analyzed.

âœ… Dashboard supports customer retention and marketing strategies.

""")

    st.divider()

    st.caption(
        "RetailPulse â€¢ Customer Analytics Dashboard â€¢ Powered by Streamlit & Plotly"
    )
