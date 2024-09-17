import streamlit as st
import random

# List of songs with title, year, artist, and YouTube URL
canco_list = [
    {
        "titol": "L'Estaca",
        "any": 1968,
        "artista": "Lluís Llach",
        "url": "https://www.youtube.com/watch?v=aX4eZ1fpYwA"
    },
    {
        "titol": "Camins",
        "any": 2001,
        "artista": "Sopa de Cabra",
        "url": "https://www.youtube.com/watch?v=79foFSDoOxY"
    },
    {
        "titol": "Boig per tu",
        "any": 1990,
        "artista": "Sau",
        "url": "https://www.youtube.com/watch?v=XtbAhey3c88"
    },
    {
        "titol": "Bon dia",
        "any": 1997,
        "artista": "Els Pets",
        "url": "https://www.youtube.com/watch?v=XgwnYXOfIkk"
    },
    {
        "titol": "Esta Morena",
        "any": 2021,
        "artista": "La Marina",
        "url": "https://m.youtube.com/watch?v=WakP10DXiD0"
    }
]

def get_embed_url(video_url):
    video_id = video_url.split('watch?v=')[1]
    return f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1"

def check_password():
    if 'password_entered' not in st.session_state:
        st.session_state.password_entered = False

    if not st.session_state.password_entered:
        def set_password():
            if st.session_state["password"] == "Gemma":  # Replace with your actual password
                st.session_state.password_entered = True
            else:
                st.session_state.password_entered = False
                st.error("Password incorrecta")

        st.text_input("Introdueix la contrasenya:", type="password", key="password", on_change=set_password)
        return False
    else:
        return True

if check_password():
    st.title("Joc de Hister - Cançons Catalanes")

    if 'current_song' not in st.session_state:
        st.session_state.current_song = None
    if 'show_info' not in st.session_state:
        st.session_state.show_info = False

    # Display the current song info if available
    if st.session_state.current_song:
        song = st.session_state.current_song
        if not st.session_state.show_info:
            st.markdown("""
            <div style="text-align: center; font-size: 50px;">
                🎶 🎵 🎶 <br>
                <span style="font-size: 20px;">Reproduint música...</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="display:flex; justify-content:center; align-items:center; height:300px;">
                <div style="
                    background-color: #f0f0f0;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                    max-width: 400px;
                    text-align: center;
                ">
                    <h3 style="color: #333;">{song['titol']}</h3>
                    <p style="font-size: 18px; color: #555;">Artista: {song['artista']}</p>
                    <p style="font-size: 16px; color: #777;">Any de publicació: {song['any']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("▶️ Play"):
            if st.session_state.current_song is None:
                st.session_state.current_song = random.choice(canco_list)
                st.session_state.show_info = False

    with col2:
        if st.button("⏹️ Stop"):
            if st.session_state.current_song:
                st.session_state.current_song = None
                st.session_state.show_info = False

    with col3:
        if st.button("ℹ️ Show Info"):
            if st.session_state.current_song:
                st.session_state.show_info = True

    if st.session_state.current_song:
        st.markdown(f"""
        <style>
            .hidden-iframe {{
                display: none;
            }}
        </style>
        <iframe class="hidden-iframe" src="{get_embed_url(st.session_state.current_song['url'])}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
