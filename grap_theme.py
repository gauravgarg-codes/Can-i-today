"""
CAN I TODAY? — theme layer for Streamlit.
"""
import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --paper: #F4F4F2;
  --panel: #FFFFFF;
  --ink: #000000;
  --rule: #CFCFCA;
  --muted: #66665F;
  --accent: #FF4F00;
  --sans: 'Space Grotesk', system-ui, sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, monospace;
}

/* ---------- Base ---------- */
html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"],
[data-testid="stMain"] {
  background: var(--paper) !important;
  color: var(--ink) !important;
  font-family: var(--sans) !important;
}

/* Keep header visible for layout but transparent */
[data-testid="stHeader"] {
  background: transparent !important;
}
#MainMenu, footer {
  display: none !important;
}

/* Restored original padding so the title isn't covered by the floating button */
.block-container {
  max-width: 1360px !important;
  padding: 3.5rem 4vw 6rem 6vw !important;
}
p, li, label, span, div { font-family: var(--sans); }
hr {
  border: 0 !important;
  border-top: 1px solid var(--ink) !important;
  margin: 2.5rem 0 !important;
  opacity: 1 !important;
}

/* ---------- Type ---------- */
h1, h2, h3, h4 {
  font-family: var(--sans) !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  background: none !important;
  font-weight: 700 !important;
  letter-spacing: -0.035em !important;
  line-height: 0.98 !important;
}
h1 { font-size: clamp(2.6rem, 6vw, 5.5rem) !important; padding: 0 0 1.5rem !important; }
h2 { font-size: clamp(1.8rem, 3vw, 2.75rem) !important; }
h3 { font-size: 1.5rem !important; padding-top: 0.5rem !important; }
h4 { font-size: 1.05rem !important; letter-spacing: -0.01em !important; }

[data-testid="stCaptionContainer"], .stCaption {
  color: var(--muted) !important;
  font-family: var(--mono) !important;
  font-size: 0.75rem !important;
}

/* ---------- Hero ---------- */
.hero { padding: 1rem 0 2rem; border-top: 8px solid var(--ink); }
.hero-title {
  font-family: var(--sans);
  font-weight: 700;
  font-size: clamp(4.5rem, 12vw, 11rem);
  line-height: 0.84;
  letter-spacing: -0.06em;
  margin: 1.5rem 0 2rem;
  color: var(--ink);
}
.hero-title i { font-style: normal; color: var(--accent); }
.hero-sub {
  font-size: 1.25rem; max-width: 28ch; line-height: 1.25;
  margin: 0; color: var(--ink); font-weight: 500;
}
.hero-tag {
  font-family: var(--mono); font-size: 0.78rem; color: var(--muted);
  margin-top: 2.5rem; max-width: 46ch; line-height: 1.5;
}

/* ---------- Tabs ---------- */
[role="tablist"] {
  gap: 0 !important;
  border-bottom: 1px solid var(--ink) !important;
  background: transparent !important;
}
[role="tab"], [data-testid="stTab"] {
  background: transparent !important;
  color: var(--muted) !important;
  padding: 0.9rem 1.5rem 0.9rem 0 !important;
  margin-right: 1.5rem !important;
  height: auto !important;
  border-radius: 0 !important;
}
[role="tab"] *, [data-testid="stTab"] * {
  color: inherit !important;
  -webkit-text-fill-color: currentColor !important;
  font-family: var(--sans) !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
}
[role="tab"]:hover, [data-testid="stTab"]:hover {
  color: var(--ink) !important;
  background: transparent !important;
}
[role="tab"][aria-selected="true"], [data-testid="stTab"][aria-selected="true"] {
  color: var(--ink) !important;
  box-shadow: inset 0 -4px 0 var(--accent) !important;
}
[data-testid="stTabs"] [data-baseweb="tab-panel"] {
  padding-top: 1.5rem !important;
}

/* ---------- Inputs ---------- */
[data-testid="stWidgetLabel"] p, label p {
  font-family: var(--sans) !important;
  font-weight: 700 !important;
  font-size: 0.85rem !important;
  color: var(--ink) !important;
  letter-spacing: 0 !important;
}
[data-testid="stTextInputRootElement"],
[data-testid="stTextAreaRootElement"],
[data-testid="stNumberInputContainer"],
[data-testid="stDateInputField"],
[data-testid="stSelectbox"] div:has(> input) {
  background: var(--ink) !important;
  border: 1px solid var(--ink) !important;
  border-radius: 2px !important;
  box-shadow: none !important;
}
[data-testid="stTextInputRootElement"]:focus-within,
[data-testid="stTextAreaRootElement"]:focus-within,
[data-testid="stNumberInputContainer"]:focus-within,
[data-testid="stDateInputField"]:focus-within,
[data-testid="stSelectbox"] div:has(> input):focus-within {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 1px var(--accent) !important;
}
input, textarea {
  background: transparent !important;
  color: var(--paper) !important;
  -webkit-text-fill-color: var(--paper) !important;
  caret-color: var(--accent) !important;
  font-family: var(--mono) !important;
  font-size: 0.9rem !important;
}
[data-testid="stDateInputField"], [data-testid="stDateInputField"] * {
  color: var(--paper) !important;
  -webkit-text-fill-color: var(--paper) !important;
  font-family: var(--mono) !important;
}
::placeholder {
  color: #A8A8A2 !important;
  opacity: 1 !important;
  -webkit-text-fill-color: #A8A8A2 !important;
}
[data-testid="stTextInputRootElement"] svg,
[data-testid="stTextAreaRootElement"] svg,
[data-testid="stSelectbox"] svg,
[data-testid="stDateInput"] svg {
  fill: var(--paper) !important;
  color: var(--paper) !important;
}

/* ---------- Buttons ---------- */
:is([data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondaryFormSubmit"],
    [data-testid="stBaseButton-primaryFormSubmit"],
    [data-testid="stDownloadButton"] button) {
  font-family: var(--sans) !important;
  font-weight: 700 !important;
  font-size: 0.95rem !important;
  border-radius: 2px !important;
  border: 1px solid var(--ink) !important;
  background: var(--panel) !important;
  color: var(--ink) !important;
  padding: 0.7rem 1.4rem !important;
  box-shadow: 3px 3px 0 var(--ink) !important;
  transition: none !important;
  min-height: 0 !important;
}
:is([data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondaryFormSubmit"],
    [data-testid="stBaseButton-primaryFormSubmit"],
    [data-testid="stDownloadButton"] button) * {
  color: inherit !important;
  -webkit-text-fill-color: currentColor !important;
  font-weight: 700 !important;
  font-family: var(--sans) !important;
}
:is([data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondaryFormSubmit"],
    [data-testid="stBaseButton-primaryFormSubmit"],
    [data-testid="stDownloadButton"] button):hover {
  background: var(--ink) !important;
  color: var(--paper) !important;
  box-shadow: 3px 3px 0 var(--accent) !important;
}
:is([data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondaryFormSubmit"],
    [data-testid="stBaseButton-primaryFormSubmit"],
    [data-testid="stDownloadButton"] button):active {
  transform: translate(3px, 3px) !important;
  box-shadow: 0 0 0 var(--ink) !important;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
  background: var(--ink) !important;
  border: 0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
}
[data-testid="stSidebar"] :is(p, span, label, li, h1, h2, h3, h4, a) {
  color: var(--paper) !important;
  -webkit-text-fill-color: var(--paper) !important;
}
[data-testid="stSidebar"] h3 {
  font-size: 1.15rem !important;
  letter-spacing: -0.02em !important;
}
[data-testid="stSidebar"] hr {
  border-top: 1px solid #3A3A38 !important;
  margin: 1.5rem 0 !important;
}
[data-testid="stSidebar"] :is(
  [data-testid="stTextInputRootElement"],
  [data-testid="stDateInputField"],
  [data-testid="stSelectbox"] div:has(> input)
) {
  border-color: var(--paper) !important;
}

/* Sidebar buttons */
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
  background: transparent !important;
  color: var(--paper) !important;
  border: 1px solid var(--paper) !important;
  box-shadow: none !important;
}
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {
  background: var(--accent) !important;
  color: var(--ink) !important;
  border-color: var(--accent) !important;
}
[data-testid="stSidebar"] [data-testid="stBaseButton-primary"] {
  background: var(--accent) !important;
  color: var(--ink) !important;
  border: 1px solid var(--accent) !important;
  box-shadow: none !important;
}
[data-testid="stSidebar"] [data-testid="stBaseButton-primary"]:hover {
  background: var(--ink) !important;
  color: var(--accent) !important;
  border-color: var(--accent) !important;
}

/* ---------- Sidebar toggle buttons ---------- */
[data-testid="stSidebarCollapseButton"] button {
  color: var(--paper) !important;
  opacity: 0.85 !important;
  background: transparent !important;
  border: 0 !important;
}

[data-testid="stExpandSidebarButton"] {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
  color: var(--ink) !important;
  background: var(--panel) !important;
  border: 2px solid var(--ink) !important;
  border-radius: 2px !important;
  padding: 0.4rem !important;
  margin: 1rem !important;
  position: fixed !important;
  top: 10px !important;
  left: 10px !important;
  z-index: 99999 !important;
  box-shadow: 2px 2px 0 var(--accent) !important;
}
[data-testid="stExpandSidebarButton"]:hover {
  background: var(--accent) !important;
  color: var(--ink) !important;
  cursor: pointer !important;
}

/* 🔥 FORCE THE ICON TO BE BLACK */
[data-testid="stExpandSidebarButton"] svg {
  fill: var(--ink) !important;
  color: var(--ink) !important;
  stroke: var(--ink) !important;
}

/* Data + map */
[data-testid="stDataFrame"] {
  border: 1px solid var(--ink) !important;
  border-radius: 0 !important;
}
iframe[title="streamlit_folium.st_folium"] {
  border: 1px solid var(--ink) !important;
  border-radius: 0 !important;
}
</style>
"""

HERO_HTML = """
<div class="hero">
  <div class="hero-title">Can I<br>today<i>?</i></div>
  <p class="hero-sub">Official rules. Your situation. A clearer decision.</p>
  <p class="hero-tag">Reads the current CAQM GRAP orders and checks them against your vehicle for entry into Delhi.</p>
</div>
"""

def apply_theme():
    st.markdown(CSS, unsafe_allow_html=True)

def hero():
    st.markdown(HERO_HTML, unsafe_allow_html=True)