import streamlit as st
import random

# List of songs with YouTube URLs
canco_list = {
    "L'Estaca": "https://www.youtube.com/watch?v=kd81T2p3qCQ",
    "Camins": "https://www.youtube.com/watch?v=example2",
    "Boig per tu": "https://www.youtube.com/watch?v=example3",
    "Bon dia": "https://www.youtube.com/watch?v=example4",
    "Amagada primavera": "https://www.youtube.com/watch?v=example5",
  
}

# Streamlit app
def main():
    st.title("Joc de Hister - Cançons Catalanes")

    # Button to trigger random song playback
    if st.button("Play Random Song"):
        # Select a random song from the list
        selected_song = random.choice(list(canco_list.items()))
        song_name, song_url = selected_song

        # Display the selected song (without showing details, just "Playing...")
        st.write(f"Playing song...")

        # Embed YouTube player for the selected song
        st.video(song_url)

if __name__ == "__main__":
    main()
