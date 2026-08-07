"""Shared UI helpers — CSS loading, headers, and footers."""

from __future__ import annotations

from pathlib import Path

import streamlit as st


def load_css() -> None:
    """Inject the global stylesheet for the current Streamlit rerun.

    ``app.py`` is its only caller. Navigation causes a fresh render, so the
    style block must be emitted on each rerun instead of being skipped through
    a session-state flag.
    """
    css_path = Path(__file__).resolve().parent.parent / "assets" / "style.css"
    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )


def render_page_template(title: str, subtitle: str, page_name: str, render_body) -> None:
    """Render the common RetailPulse shell around a dashboard body."""
    render_page_header(title, subtitle)
    st.session_state["_shared_page_template_active"] = True
    try:
        render_body()
    finally:
        st.session_state["_shared_page_template_active"] = False
    render_footer(page_name)


def render_page_header(title: str, subtitle: str) -> None:
    """Render a consistent page header with title and subtitle."""
    if st.session_state.get("_shared_page_template_active"):
        return
    st.markdown(
        f'<div class="dashboard-title">{title}</div>'
        f'<div class="dashboard-subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )
    st.divider()


def render_section_header(title: str) -> None:
    """Render a consistent section header (same size as st.subheader).

    Use this instead of mixing st.subheader() and st.markdown("### ...") so
    every page renders section titles identically.  The CSS class
    ``.section-header`` is normalised alongside h2/h3 in style.css.
    """
    st.markdown(
        f'<h3 class="section-header">{title}</h3>',
        unsafe_allow_html=True,
    )


def render_footer(page_name: str = "") -> None:
    """Render the standard page footer."""
    if st.session_state.get("_shared_page_template_active"):
        return
    suffix = f" • {page_name}" if page_name else ""
    st.caption(f"RetailPulse{suffix} • AI-Powered Customer Analytics & Demand Forecasting")
