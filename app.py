import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode
import requests
from io import BytesIO
import youtube_dl
import vlc

# Llista de cançons amb els codis QR corresponents
canco_list = {
    "https://example.com/qr1": "https://www.youtube.com/watch?v=example1",
    "https://example.com/qr2": "https://www.youtube.com/watch?v=example2",
    "https://example.com/qr3": "https://www.youtube.com/watch?v=example3",
    "https://example.com/qr4": "https://www.youtube.com/watch?v=example4",
    "https://example.com/qr5": "https://www.youtube.com/watch?v=example5",
    "https://example.com/qr6": "https://m.youtube.com/watch?v=WakP10DXiD0"
}

# Funció per obtenir l'enllaç d'àudio des de YouTube
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

# Funció per reproduir la cançó
def reproduir_canco(url):
    audio_url = obtenir_audio(url)
    player = vlc.MediaPlayer(audio_url)
    player.play()
    return player

# Funció per escanejar el codi QR
def escanejar_qr(imatge):
    decoded_objects = decode(imatge)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    return None

# Interfície de l'aplicació Streamlit
def main():
    st.title("Joc de Temazus - Cançons Catalanes")

    # Pujar imatge
    uploaded_file = st.file_uploader("Carrega una imatge amb codi QR", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        qr_code = escanejar_qr(image)

        if qr_code:
            st.write(f"QR Code: {qr_code}")
            if qr_code in canco_list:
                canco_url = canco_list[qr_code]
                st.write("Cançó trobada! Fes clic per escoltar:")
                player = reproduir_canco(canco_url)
                if st.button("Atura"):
                    player.stop()
            else:
                st.write("No s'ha trobat cap codi QR vàlid.")
        else:
            st.write("No s'ha pogut escanejar el codi QR.")

if __name__ == "__main__":
    main()
