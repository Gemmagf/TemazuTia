import streamlit as st
import random
import youtube_dl
import vlc

# List of songs with URLs
canco_list = {
    "L'Estaca": "https://www.youtube.com/watch?v=example1",
    "Camins": "https://www.youtube.com/watch?v=example2",
    "Boig per tu": "https://www.youtube.com/watch?v=example3",
    "Bon dia": "https://www.youtube.com/watch?v=example4",
    "Amagada primavera": "https://www.youtube.com/watch?v=example5",
    "Esta Morena": "https://m.youtube.com/watch?v=WakP10DXiD0"
}

# Function to get the audio URL from YouTube
def obtenir_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict['url']
        return audio_url

# Function to play the song
def reproduir_canco(url):
    audio_url = obtenir_audio(url)
    player = vlc.MediaPlayer(audio_url)
    player.play()
    return player

# Streamlit app interface
def main():
    st.title("Joc de Hister - Cançons Catalanes")

    # Button to play a random song
    if st.button("Reprodueix una cançó aleatòria"):
        song_name = random.choice(list(canco_list.keys()))
        canco_url = canco_list[song_name]
        st.write(f"Reproduint: {song_name}")
        player = reproduir_canco(canco_url)
        if st.button("Atura"):
            player.stop()

if __name__ == "__main__":
    main()
