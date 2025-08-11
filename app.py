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
    "Schalte für 10 Minuten alle Geräte aus.",
    "Trinke ein Glas Wasser langsam und bewusst.",
    "Schreibe drei Dinge auf, für die du dankbar bist.",
    "Gehe fünf Minuten an die frische Luft.",
    "Atme zehnmal tief ein und aus.",
    "Lächle dich im Spiegel an.",
    "Räume einen kleinen Bereich auf.",
    "Höre dein Lieblingslied bewusst.",
    "Dehne dich für zwei Minuten.",
    "Schließe für eine Minute die Augen und entspanne dich.",
    "Schreibe einer Person eine nette Nachricht.",
    "Trinke eine Tasse Tee ohne Ablenkung.",
    "Lies eine inspirierende Kurzgeschichte.",
    "Mache zehn Kniebeugen.",
    "Zünde eine Kerze an und beobachte die Flamme.",
    "Schreibe dein Tagesziel auf.",
    "Sortiere eine Schublade.",
    "Schreibe drei positive Eigenschaften von dir auf.",
    "Stehe für fünf Minuten auf.",
    "Höre die Geräusche um dich herum bewusst.",
    "Putze deine Brille oder den Bildschirm.",
    "Mache zehn tiefe Atemzüge am offenen Fenster.",
    "Trinke ein Glas Wasser mit Zitrone.",
    "Sage dir selbst: Ich schaffe das.",
    "Falte ein Kleidungsstück ordentlich.",
    "Öffne kurz das Fenster und atme frische Luft ein.",
    "Lächle einer fremden Person zu.",
    "Schreibe eine kleine To-do-Liste.",
    "Mach eine Minute lang Schulterkreisen.",
    "Lies ein inspirierendes Zitat.",
    "Lege für zehn Minuten dein Handy weg.",
    "Nimm bewusst wahr, wie du sitzt oder stehst.",
    "Schreibe drei schöne Erinnerungen auf.",
    "Lobe dich für etwas, das du gut gemacht hast.",
    "Schreibe auf, wofür du dich heute bedanken willst.",
    "Trinke einen Schluck Wasser zwischen Aufgaben.",
    "Mache eine Minute lang bewusst nichts.",
    "Höre ein Lied aus deiner Kindheit.",
    "Schreibe auf, was dich heute motiviert.",
    "Dehne sanft deinen Nacken.",
    "Male eine kleine Skizze.",
    "Lese drei Seiten eines Buchs.",
    "Atme tief durch und lächle.",
    "Trinke langsam einen warmen Schluck Tee oder Kaffee.",
    "Strecke dich nach oben.",
    "Schreibe eine kurze Dankes-E-Mail.",
    "Stehe auf und bewege dich kurz.",
    "Denke an eine Person, die dich inspiriert.",
    "Schreibe auf, was dich heute glücklich macht.",
    "Schalte für fünf Minuten Musik an, die dich beruhigt.",
    "Zähle zehn Dinge in deiner Umgebung.",
    "Nimm dir vor, heute etwas Neues zu lernen.",
    "Mache für zehn Sekunden die Augen zu.",
    "Atme tief durch und denke: Danke.",
    "Schließe kurz die Augen und lächle.",
    "Trinke bewusst einen Schluck Wasser.",
    "Schreibe auf, was du heute erreichen willst.",
    "Putze einen kleinen Bereich in deinem Zimmer.",
    "Denke an einen positiven Moment der letzten Woche.",
    "Schreibe drei Dinge auf, die du liebst.",
    "Höre einen Vogel singen.",
    "Lächle bewusst für 20 Sekunden.",
    "Trinke ein Glas stilles Wasser.",
    "Dehne deine Handgelenke.",
    "Schreibe eine Mini-Motivation auf.",
    "Mache für eine Minute tiefe Atemübungen.",
    "Denke an einen Ort, an dem du dich wohlfühlst.",
    "Schreibe einen Satz aus deinem Lieblingsbuch auf.",
    "Mache eine kleine Pause im Stehen.",
    "Lächle, während du atmest.",
    "Schreibe eine Sache auf, die du morgen tun willst.",
    "Höre kurz den Straßenlärm und konzentriere dich darauf.",
    "Schalte dein Handy für fünf Minuten aus.",
    "Mache 15 Sekunden lang einen Sonnengruß.",
    "Schreibe auf, wen du heute anrufen willst.",
    "Finde ein Foto, das dich glücklich macht.",
    "Sage dir selbst: Heute wird gut.",
    "Lege dich für zwei Minuten hin.",
    "Schreibe drei Gründe auf, warum du dankbar bist.",
    "Gehe kurz ans Fenster und schaue hinaus.",
    "Nimm fünf tiefe Atemzüge durch die Nase.",
    "Lächle einem Kollegen zu.",
    "Schreibe eine kleine Wunschliste.",
    "Höre eine Minute lang bewusst auf deine Atmung.",
    "Trinke einen Schluck Wasser zwischen Gesprächen.",
    "Denke an dein Lieblingsessen.",
    "Schreibe einen Satz mit einem positiven Wort.",
    "Mache kurz eine Atem-Meditation.",
    "Öffne das Fenster für frische Luft.",
    "Denke an etwas, worauf du dich freust.",
    "Schreibe ein neues Ziel auf.",
    "Singe leise ein Lied mit.",
    "Halte für zehn Sekunden inne.",
    "Schreibe drei Dinge auf, die du heute lernen willst.",
    "Atme tief durch und entspanne deine Schultern.",
    "Schalte für eine Minute den Bildschirm aus.",
    "Schreibe eine kurze Nachricht an einen Freund.",
    "Nimm dir vor, heute freundlich zu anderen zu sein.",
    "Zähle langsam von eins bis zehn.",
    "Lächle und strecke dich.",
    "Gehe 100 Schritte langsam und bewusst.",
    "Male ein Herz auf ein Blatt Papier.",
    "Schalte alle Benachrichtigungen für 30 Minuten aus.",
    "Schreibe deinen Lieblingsspruch auf.",
    "Mache fünf tiefe Atemzüge mit geschlossenen Augen.",
    "Ordne deinen Schreibtisch kurz.",
    "Schreibe auf, welche drei Dinge dich glücklich machen.",
    "Dehne deine Waden.",
    "Zünde eine Duftkerze an.",
    "Lies ein Gedicht.",
    "Schreibe eine Postkarte.",
    "Stelle dir vor, wie du am Meer sitzt.",
    "Schreibe auf, worauf du heute stolz bist.",
    "Schalte für zehn Minuten Musik an, die dich motiviert.",
    "Male drei Sterne auf ein Papier.",
    "Trinke ein Glas Wasser mit Minze.",
    "Schreibe einen Witz auf.",
    "Lächle in den Spiegel und sage: Danke.",
    "Atme fünf Sekunden ein und sieben Sekunden aus.",
    "Schreibe eine kleine Bucket List.",
    "Strecke deine Arme weit nach oben.",
    "Schreibe auf, welche Orte du besuchen willst.",
    "Lege für fünf Minuten die Hände auf den Bauch und atme.",
    "Schalte für zehn Minuten den Fernseher aus.",
    "Schreibe eine kurze Affirmation.",
    "Gehe eine Runde um den Block.",
    "Trinke langsam einen Schluck Wasser.",
    "Male eine Sonne.",
    "Schreibe drei Dinge auf, die du loslassen willst.",
    "Denke an einen schönen Urlaub.",
    "Mache kurz die Augen zu und höre zu.",
    "Schreibe eine positive Erinnerung auf.",
    "Trinke einen Schluck warmes Wasser.",
    "Lächle jemandem zu, den du nicht kennst.",
    "Male eine Blume.",
    "Schreibe auf, was dich heute entspannt.",
    "Strecke deine Beine aus.",
    "Schreibe eine kleine Mut-Botschaft.",
    "Gehe zwei Minuten barfuß.",
    "Schreibe eine Sache auf, die du besser machen willst.",
    "Schalte kurz dein Licht aus und genieße die Stille.",
    "Male ein Smiley.",
    "Schreibe drei Komplimente an dich selbst.",
    "Trinke ein Glas Wasser mit Eiswürfeln.",
    "Schalte für fünf Minuten alles aus.",
    "Male einen Regenbogen.",
    "Schreibe drei Dinge auf, die dich inspirieren.",
    "Gehe an die frische Luft und atme tief ein.",
    "Schreibe eine schöne Erinnerung aus der Kindheit auf.",
    "Schalte dein Handy stumm.",
    "Trinke langsam einen Schluck Wasser.",
    "Male einen Baum.",
    "Schreibe drei Dinge auf, die du heute geschafft hast.",
    "Dehne deinen Rücken.",
    "Schreibe auf, was du morgen erreichen willst.",
    "Schalte für zehn Minuten das WLAN aus.",
    "Male einen Kreis.",
    "Schreibe eine Dankesnachricht.",
    "Trinke ein Glas Wasser in kleinen Schlucken.",
    "Lege dich für zwei Minuten hin und entspanne.",
    "Schalte alle Geräte für fünf Minuten aus.",
    "Male eine Wolke.",
    "Schreibe auf, was dich gerade glücklich macht.",
    "Trinke bewusst einen Schluck Wasser.",
    "Gehe kurz ans Fenster.",
    "Schalte für eine Minute alle Geräusche aus.",
    "Male einen Stern.",
    "Schreibe drei Dinge auf, die du liebst.",
    "Schalte dein Handy für eine Minute aus.",
    "Trinke ein Glas Wasser mit einer Scheibe Gurke.",
    "Male eine Blume.",
    "Schreibe eine Sache auf, die dich heute zum Lächeln gebracht hat.",
    "Gehe an einen ruhigen Ort.",
    "Schalte alle Lichter aus und atme tief ein.",
    "Male einen Vogel.",
    "Schreibe drei Wünsche auf.",
    "Schalte dein Handy in den Flugmodus.",
    "Trinke einen Schluck Wasser.",
    "Male ein Herz.",
    "Schreibe eine positive Botschaft.",
    "Schalte für zehn Sekunden alles aus.",
    "Gehe für eine Minute barfuß.",
    "Schreibe auf, was dir heute gut gelungen ist.", 
    "Schreibe deinen Traumberuf auf und frag die KI für den ersten Schritt!"
]

# --- Button mittig anzeigen ---
if st.button("START"):
    task = random.choice(tasks)
    st.markdown(f"<div class='task-box'>{task}</div>", unsafe_allow_html=True)
