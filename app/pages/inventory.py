import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# =====================================================
# INVENTORY DASHBOARD
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

    inventory = pd.read_csv(DATA / "inventory_dashboard.csv")

    # =====================================================
    # SIDEBAR FILTERS
    # =====================================================

    st.sidebar.markdown("## 🔍 Filters")

    selected_abc = st.sidebar.selectbox(

        "ABC Class",

        ["All"] + sorted(inventory["ABC_Class"].dropna().unique().tolist())

    )

    selected_movement = st.sidebar.selectbox(

        "Movement Category",

        ["All"] + sorted(inventory["MovementCategory"].dropna().unique().tolist())

    )

    # =====================================================
    # FILTER DATA
    # =====================================================

    filtered = inventory.copy()

    if selected_abc != "All":

        filtered = filtered[
            filtered["ABC_Class"] == selected_abc
        ]

    if selected_movement != "All":

        filtered = filtered[
            filtered["MovementCategory"] == selected_movement
        ]

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="dashboard-title">
    📦 Inventory Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dashboard-subtitle">
    Monitor inventory performance, product movement and stock value.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================================================
    # KPI VALUES
    # =====================================================

    total_products = filtered["StockCode"].nunique()

    total_quantity = filtered["TotalQuantity"].sum()

    total_revenue = filtered["TotalRevenue"].sum()

    avg_price = filtered["AveragePrice"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "Products",

            f"{total_products:,}"

        )

    with c2:

        st.metric(

            "Total Quantity",

            f"{int(total_quantity):,}"

        )

    with c3:

        st.metric(

            "Revenue",

            f"${total_revenue:,.2f}"

        )

    with c4:

        st.metric(

            "Average Price",

            f"${avg_price:.2f}"

        )

    st.divider()

        # =====================================================
    # ABC CLASSIFICATION
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("📦 ABC Classification")

        abc = (

            filtered

            .groupby("ABC_Class")["TotalRevenue"]

            .sum()

            .reset_index()

            .sort_values("TotalRevenue", ascending=False)

        )

        fig = px.pie(

            abc,

            names="ABC_Class",

            values="TotalRevenue",

            hole=0.60,

            color="ABC_Class",

            color_discrete_sequence=px.colors.qualitative.Set2

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
    # MOVEMENT CATEGORY
    # =====================================================

    with right:

        st.subheader("🚚 Inventory Movement")

        movement = (

            filtered

            .groupby("MovementCategory")["StockCode"]

            .count()

            .reset_index(name="Products")

            .sort_values("Products", ascending=False)

        )

        fig = px.bar(

            movement,

            x="MovementCategory",

            y="Products",

            text_auto=True,

            color="MovementCategory",

            color_discrete_sequence=px.colors.qualitative.Bold

        )

        fig.update_layout(

            height=450,

            xaxis_title="Movement Category",

            yaxis_title="Products",

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
    # TOP 10 PRODUCTS BY REVENUE
    # =====================================================

    st.subheader("💰 Top 10 Products by Revenue")

    revenue = (

        filtered

        .sort_values(

            "TotalRevenue",

            ascending=False

        )

        .head(10)

    )

    fig = px.bar(

        revenue,

        x="TotalRevenue",

        y="Description",

        orientation="h",

        text_auto=".2s",

        color="TotalRevenue",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        height=550,

        xaxis_title="Revenue",

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
    # TOP 10 PRODUCTS BY QUANTITY
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("📦 Top 10 Products by Quantity")

        quantity = (

            filtered

            .sort_values(

                "TotalQuantity",

                ascending=False

            )

            .head(10)

        )

        fig = px.bar(

            quantity,

            x="TotalQuantity",

            y="Description",

            orientation="h",

            text_auto=True,

            color="TotalQuantity",

            color_continuous_scale="Greens"

        )

        fig.update_layout(

            height=500,

            xaxis_title="Total Quantity",

            yaxis_title="",

            coloraxis_showscale=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # AVERAGE PRICE ANALYSIS
    # =====================================================

    with right:

        st.subheader("💲 Average Price Distribution")

        fig = px.box(

            filtered,

            y="AveragePrice",

            points="outliers",

            color_discrete_sequence=["#F59E0B"]

        )

        fig.update_layout(

            height=500,

            yaxis_title="Average Price",

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
    # REVENUE VS QUANTITY
    # =====================================================

    st.subheader("📊 Revenue vs Quantity Analysis")

    fig = px.scatter(

        filtered,

        x="TotalQuantity",

        y="TotalRevenue",

        size="AveragePrice",

        color="ABC_Class",

        hover_name="Description",

        hover_data=[

            "StockCode",

            "MovementCategory"

        ],

        color_discrete_sequence=px.colors.qualitative.Set2

    )

    fig.update_layout(

        height=600,

        xaxis_title="Total Quantity",

        yaxis_title="Total Revenue",

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

        # =====================================================
    # INVENTORY DETAILS TABLE
    # =====================================================

    st.subheader("📋 Inventory Details")

    inventory_table = filtered.copy()

    inventory_table = inventory_table.sort_values(
        "TotalRevenue",
        ascending=False
    )

    st.dataframe(

        inventory_table[
            [
                "StockCode",
                "Description",
                "TotalQuantity",
                "TotalRevenue",
                "TotalOrders",
                "AveragePrice",
                "ABC_Class",
                "MovementCategory"
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

    highest_quantity = filtered.loc[
        filtered["TotalQuantity"].idxmax()
    ]

    left, right = st.columns(2)

    with left:

        st.success(f"""

### 💰 Highest Revenue Product

**Product**

{highest_revenue['Description']}

**Revenue**

${highest_revenue['TotalRevenue']:,.2f}

**ABC Class**

{highest_revenue['ABC_Class']}

""")

    with right:

        st.info(f"""

### 📦 Highest Quantity Product

**Product**

{highest_quantity['Description']}

**Quantity Sold**

{int(highest_quantity['TotalQuantity']):,}

**Movement**

{highest_quantity['MovementCategory']}

""")

    st.divider()

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    st.download_button(

        "📥 Download Inventory Report",

        data=filtered.to_csv(index=False),

        file_name="inventory_report.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    st.subheader("📌 Executive Summary")

    total_products = filtered["StockCode"].nunique()

    total_quantity = filtered["TotalQuantity"].sum()

    total_revenue = filtered["TotalRevenue"].sum()

    avg_price = filtered["AveragePrice"].mean()

    st.success(f"""

### Inventory Performance Summary

• Total Products : **{total_products:,}**

• Total Quantity Sold : **{int(total_quantity):,}**

• Total Revenue : **${total_revenue:,.2f}**

• Average Product Price : **${avg_price:.2f}**

• ABC Classification highlights high-value inventory.

• Movement Categories help identify fast and slow moving products.

• Dashboard supports inventory optimization and stock planning.

""")

    st.divider()

    st.caption(
        "RetailPulse • Inventory Dashboard • Powered by Streamlit & Plotly"
    )