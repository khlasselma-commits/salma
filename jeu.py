import streamlit as st

# Config page
st.set_page_config(page_title="HAPPY BIRTHDAY YASSINE 💖", page_icon="💖", layout="centered")


st.markdown("""
    <style>
    /* Fond romantique rose doux */
    .stApp {
        background: linear-gradient(135deg, #ffe6ea 0%, #ffc2d1 100%);
    }
    
    /* Titre principal grand et gras */
    h1 {
        color: #d63384 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800 !important;
        font-size: 2.3rem !important;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* Consigne et textes secondaires */
    .stMarkdown p {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        color: #4a1525 !important;
    }

    /* Zone du dessin du pendu */
    .pendu-dessin {
        font-family: 'Courier New', monospace;
        font-size: 20px;
        font-weight: bold;
        white-space: pre;
        background-color: #ffffffd0;
        color: #b5179e;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        line-height: 1.2;
        border: 2px solid #ff85a1;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }

    /* Mot masqué : Très grand et en gras */
    .mot-secret {
        font-size: 40px !important;
        font-weight: 900 !important;
        letter-spacing: 10px;
        color: #ff0d57;
        text-align: center;
        margin: 25px 0;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.8);
    }

    /* Boîte de gage romantique */
    .gage-box {
        background-color: #ffffffee;
        padding: 18px;
        border-radius: 15px;
        border-left: 6px solid #ff4d6d;
        margin-top: 20px;
        box-shadow: 0px 4px 12px rgba(255, 77, 109, 0.15);
    }
    .gage-titre {
        color: #c9184a;
        font-size: 1.2rem;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .gage-texte {
        color: #590d22;
        font-size: 1.15rem;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ETAPES DU PENDU (6 Erreurs max)
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

# ---------------------------------------------------------
# PARAMÈTRES DU JEU 
# ---------------------------------------------------------
MOT_SECRET = "JE T AIME".upper()  # Ton mot ou ta phrase à deviner
MAX_ERREURS = 6

GAGES = [
    "😘 **Gage 1 :** otlobni !",
    "💌 **Gage 2 :** 9oli mahlek ;) !",
    "🤫 **Gage 3 :** a7la souvenir binetna benesba lik .",
    "🎶 **Gage 4 :** 7aja t7eb na3mlouha ma3a b3adhna 3ala 9rib !",
    "👑 **Gage 5 :** ur wish for this year !",
    "🙈 **Gage 6 :** haka tawa !"
]

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
st.title("💖 HAPPY BIRTHDAY YASSINE 💖")
st.write("**tala3 lkelma ! rod belek tochno9 rajel... 😉**")

# Affichage du dessin du pendu
dessin_actuel = DESSINS_PENDU[st.session_state.erreurs]
st.markdown(f'<div class="pendu-dessin">{dessin_actuel}</div>', unsafe_allow_html=True)

# Affichage du mot masqué
affichage_mot = ""
gagne = True
for lettre in MOT_SECRET:
    if lettre in [" ", "'", "-", "!", "?", "📱"]:
        affichage_mot += lettre + " "
    elif lettre in st.session_state.lettres_trouvees:
        affichage_mot += lettre + " "
    else:
        affichage_mot += "_ "
        gagne = False

st.markdown(f'<div class="mot-secret">{affichage_mot}</div>', unsafe_allow_html=True)

# Clavier de boutons A-Z
if not gagne and st.session_state.erreurs < MAX_ERREURS:
    st.write("**Choisis une lettre :**")
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

# Affichage du gage à chaque erreur
if st.session_state.erreurs > 0 and not gagne and st.session_state.erreurs <= MAX_ERREURS:
    index_gage = min(st.session_state.erreurs - 1, len(GAGES) - 1)
    st.markdown(f"""
        <div class="gage-box">
            <div class="gage-titre">⚠️ lee ! faux...</div>
            <div class="gage-texte">{GAGES[index_gage]}</div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# FIN DE PARTIE
# ---------------------------------------------------------
if gagne:
    st.balloons()
    st.success("🎉 BRAVO HABIBI ! nhebek barcha yassounti ! 🎉")
    st.markdown("""
        ### 🎁 :
        > **Joyeux anniversaire habibi ! Merci d'être la personne incroyable que tu es '... ❤️**
    """)
    if st.button("Recommencer 🔄"):
        st.session_state.lettres_trouvees = set()
        st.session_state.erreurs = 0
        st.rerun()

elif st.session_state.erreurs >= MAX_ERREURS:
    st.error("💔 Oups ! chna9et rajel :l... Mais comme je t'aime trop, tu as le droit de rejouer !")
    if st.button("Réessayer 🔄"):
        st.session_state.lettres_trouvees = set()
        st.session_state.erreurs = 0
