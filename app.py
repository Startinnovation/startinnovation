import streamlit as st
import random
import base64

# --- Seiten-Layout & Design ---
st.set_page_config(
    page_title="Startwise",
    page_icon="🌱",
    layout="centered"
)

# --- Hintergrundbild setzen ---
def set_background(png_file: str):
    with open(png_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* Zentrierung der gesamten Seite */
        .main {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        /* Titel */
        h1 {{
            text-align: center;
            color: white;
            font-size: clamp(28px, 5vw, 56px);
            line-height: 1.15;
            margin-bottom: 2rem;
        }}

        /* Button Styling */
        div.stButton > button {{
            background: #ffffff;
            color: #4a4a4a;
            border: 0;
            border-radius: 999px;
            padding: 0.9rem 2.2rem;
            font-weight: 700;
            font-size: 1.05rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
            cursor: pointer;
        }}
        div.stButton > button:hover {{
            background: #f4f4f4;
            color: #2f2f2f;
        }}

        /* Ergebnis-Box */
        .task-box {{
            max-width: 900px;
            margin-top: 2rem;
            background: rgba(0,0,0,0.25);
            backdrop-filter: blur(2px);
            color: #ffffff;
            padding: 1.6rem 2rem;
            border-radius: 16px;
            text-align: center;
            font-size: clamp(18px, 2.8vw, 28px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("Hintergrund.png")

# --- Logo oben zentriert ---
st.image("Logo.png", width=280)

# --- Titel ---
st.markdown("<h1>Starte deinen Tag mit 1 %</h1>", unsafe_allow_html=True)

# --- Aufgabenliste ---
tasks = [
    "Trinke ein Glas Wasser.",
    "Gehe für 5 Minuten an die frische Luft.",
    "Schreibe drei Dinge auf, für die du dankbar bist.",
    "Mache deinem Spiegelbild ein Kompliment.",
    "Atme 10 Mal bewusst tief ein und aus.",
    "Bewege dich für 1 Minute – tanze, dehne dich, hüpfe.",
    "Höre deinem Lieblingslied bewusst zu.",
    "Lächle jemanden bewusst an – auch wenn’s digital ist.",
    "Räume einen kleinen Bereich auf.",
    "Schalte für 10 Minuten alle Geräte aus."
]

# --- Button mittig anzeigen ---
if st.button("START"):
    task = random.choice(tasks)
    st.markdown(f"<div class='task-box'>{task}</div>", unsafe_allow_html=True)
