import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# CUSTOMER SEGMENTATION
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

    customers = pd.read_csv(DATA / "customer_segmentation.csv")

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="dashboard-title">
    🎯 Customer Segmentation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dashboard-subtitle">
    RFM-Based Customer Segmentation Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================================================
    # KPI VALUES
    # =====================================================

    total_customers = customers["CustomerID"].nunique()

    avg_recency = customers["Recency"].mean()

    avg_frequency = customers["Frequency"].mean()

    avg_monetary = customers["Monetary"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "👥 Customers",
            f"{total_customers:,}"
        )

    with c2:

        st.metric(
            "📅 Avg Recency",
            f"{avg_recency:.1f} Days"
        )

    with c3:

        st.metric(
            "🛒 Avg Frequency",
            f"{avg_frequency:.2f}"
        )

    with c4:

        st.metric(
            "💰 Avg Monetary",
            f"${avg_monetary:,.2f}"
        )

    st.divider()

        # =====================================================
    # CUSTOMER SEGMENT DISTRIBUTION
    # =====================================================

    left, right = st.columns(2)

    # -----------------------------------------------------

    with left:

        st.subheader("👥 Customer Segment Distribution")

        segment = (
            customers["CustomerSegment"]
            .value_counts()
            .reset_index()
        )

        segment.columns = [
            "Customer Segment",
            "Customers"
        ]

        fig = px.pie(

            segment,

            names="Customer Segment",

            values="Customers",

            hole=0.60,

            color="Customer Segment",

            color_discrete_sequence=[
                "#4F46E5",
                "#10B981",
                "#F59E0B",
                "#EF4444",
                "#06B6D4",
                "#8B5CF6"
            ]

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
    # CLUSTER DISTRIBUTION
    # =====================================================

    with right:

        st.subheader("🎯 Cluster Distribution")

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
    # RFM METRICS DISTRIBUTION
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("📅 Recency Distribution")

        fig = px.histogram(

            customers,

            x="Recency",

            nbins=30,

            color_discrete_sequence=["#F59E0B"]

        )

        fig.update_layout(

            height=420,

            xaxis_title="Recency (Days)",

            yaxis_title="Customers",

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        st.subheader("🛒 Frequency Distribution")

        fig = px.histogram(

            customers,

            x="Frequency",

            nbins=30,

            color_discrete_sequence=["#10B981"]

        )

        fig.update_layout(

            height=420,

            xaxis_title="Frequency",

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
    # MONETARY DISTRIBUTION
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("💰 Monetary Distribution")

        fig = px.box(

            customers,

            y="Monetary",

            points="outliers",

            color_discrete_sequence=["#4F46E5"]

        )

        fig.update_layout(

            height=430,

            yaxis_title="Monetary Value ($)",

            paper_bgcolor="white",

            plot_bgcolor="white",

            showlegend=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # RFM SCATTER PLOT
    # =====================================================

    with right:

        st.subheader("📊 Frequency vs Monetary")

        fig = px.scatter(

            customers,

            x="Frequency",

            y="Monetary",

            size="Monetary",

            color="Cluster",

            hover_data=[

                "CustomerID",

                "CustomerSegment"

            ],

            color_continuous_scale="Viridis"

        )

        fig.update_layout(

            height=430,

            xaxis_title="Frequency",

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
    # TOP CUSTOMER SEGMENTS
    # =====================================================

    st.subheader("🏆 Top Customer Segments")

    segment_summary = (

        customers

        .groupby("CustomerSegment")

        .agg(

            Customers=("CustomerID", "count"),

            AvgMonetary=("Monetary", "mean"),

            AvgFrequency=("Frequency", "mean"),

            AvgRecency=("Recency", "mean")

        )

        .reset_index()

        .sort_values(

            "AvgMonetary",

            ascending=False

        )

    )

    fig = px.bar(

        segment_summary,

        x="CustomerSegment",

        y="AvgMonetary",

        color="CustomerSegment",

        text_auto=".2s",

        color_discrete_sequence=px.colors.qualitative.Bold

    )

    fig.update_layout(

        height=450,

        xaxis_title="Customer Segment",

        yaxis_title="Average Monetary Value",

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
    # SEGMENT SUMMARY TABLE
    # =====================================================

    st.subheader("📋 Customer Segment Summary")

    summary = customers.groupby("CustomerSegment").agg(

        Customers=("CustomerID", "count"),
        AvgRecency=("Recency", "mean"),
        AvgFrequency=("Frequency", "mean"),
        AvgMonetary=("Monetary", "mean")

    ).reset_index()

    summary["AvgRecency"] = summary["AvgRecency"].round(1)
    summary["AvgFrequency"] = summary["AvgFrequency"].round(2)
    summary["AvgMonetary"] = summary["AvgMonetary"].round(2)

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # KEY BUSINESS INSIGHTS
    # =====================================================

    highest_segment = summary.loc[
        summary["AvgMonetary"].idxmax(),
        "CustomerSegment"
    ]

    largest_segment = summary.loc[
        summary["Customers"].idxmax(),
        "CustomerSegment"
    ]

    lowest_recency = summary.loc[
        summary["AvgRecency"].idxmin(),
        "CustomerSegment"
    ]

    c1, c2 = st.columns(2)

    with c1:

        st.success(f"""

### 🏆 Segment Highlights

💰 Highest Average Monetary

**{highest_segment}**

👥 Largest Customer Segment

**{largest_segment}**

""")

    with c2:

        st.info(f"""

### 📈 Customer Engagement

🔥 Most Recent Active Segment

**{lowest_recency}**

🎯 Total Segments

**{customers['CustomerSegment'].nunique()}**

""")

    st.divider()

    # =====================================================
    # DOWNLOAD BUTTON
    # =====================================================

    st.download_button(

        label="📥 Download Customer Segmentation Report",

        data=customers.to_csv(index=False),

        file_name="customer_segmentation.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    st.subheader("📌 Executive Summary")

    st.success("""

✅ RFM-based customer segmentation completed.

✅ Customer clusters have been visualized.

✅ Spending (Monetary), purchase frequency, and recency patterns have been analyzed.

✅ High-value customer segments have been identified.

✅ This dashboard supports targeted marketing campaigns and customer retention strategies.

""")

    st.divider()

    st.caption(
        "RetailPulse • Customer Segmentation Dashboard • Powered by Streamlit & Plotly"
    )