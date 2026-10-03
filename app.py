import streamlit as st

st.set_page_config(page_title="YASSINE + SALMA=💖", page_icon="💖", layout="centered")

# CSS pour le style du dessin et du texte
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    .pendu-dessin {
        font-family: monospace;
        font-size: 18px;
        white-space: pre;
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        line-height: 1.2;
    }
    .mot-secret {
        font-size: 32px;
        font-weight: bold;
        letter-spacing: 8px;
        color: #ff4b4b;
        text-align: center;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ETAPES DU DESSIN DU PENDU TRADITIONNEL
# ---------------------------------------------------------
DESSINS_PENDU = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

MOT_SECRET = "JE T AIME".upper()  # mot ou  phrase à deviner
MAX_ERREURS = 6

# ---------------------------------------------------------
# INITIALISATION
# ---------------------------------------------------------
if 'lettres_trouvees' not in st.session_state:
    st.session_state.lettres_trouvees = set()
if 'erreurs' not in st.session_state:
    st.session_state.erreurs = 0

# ---------------------------------------------------------
# INTERFACE
# ---------------------------------------------------------
st.title("💖 Le Jeu du Pendu 💖")

# Affichage du pendu
dessin_actuel = DESSINS_PENDU[st.session_state.erreurs]
st.markdown(f'<div class="pendu-dessin">{dessin_actuel}</div>', unsafe_allow_html=True)

# Affichage du mot masqué
affichage_mot = ""
gagne = True
for lettre in MOT_SECRET:
    if lettre in [" ", "'", "-", "!", "?"]:
        affichage_mot += lettre + " "
    elif lettre in st.session_state.lettres_trouvees:
        affichage_mot += lettre + " "
    else:
        affichage_mot += "_ "
        gagne = False

st.markdown(f'<div class="mot-secret">{affichage_mot}</div>', unsafe_allow_html=True)

# Clavier de boutons A-Z
if not gagne and st.session_state.erreurs < MAX_ERREURS:
    st.write("### Choisis une lettre :")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = st.columns(7)
    
    for i, lettre in enumerate(alphabet):
        col = cols[i % 7]
        deja_joue = lettre in st.session_state.lettres_trouvees
        if col.button(lettre, key=f"btn_{lettre}", disabled=deja_joue):
            st.session_state.lettres_trouvees.add(lettre)
            if lettre not in MOT_SECRET:
                st.session_state.erreurs += 1
            st.rerun()

# ---------------------------------------------------------
# FIN DE PARTIE
# ---------------------------------------------------------
if gagne:
    st.balloons()
    st.success("🎉 BRAVO HABIBI ! hak tala3tha ! 🎉")
    st.markdown("""
        ### 🎁 Message secret :
        > *Joyeux Anniversaire Yassine , 3a9ba le 100 sne ! Je t'aime fort ! ❤️*
    """)
    if st.button("Recommencer 🔄"):
        st.session_state.lettres_trouvees = set()
        st.session_state.erreurs = 0
        st.rerun()

elif st.session_state.erreurs >= MAX_ERREURS:
    st.error("💔 3ejbek haka ! chna9tou rajel... 'AMA MISELECH JOYEUX ANNIVERSAIRE , KOL 3AM W ENTI HAY B 5IR , Nhebek❤️ ")
    if st.button("Réessayer 🔄"):
        st.session_state.lettres_trouvees = set()
        st.session_state.erreurs = 0
        st.rerun() 
