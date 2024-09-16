import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import youtube_dl
import vlc
import tempfile
import os
import numpy as np
import tempfile

# Llista de cançons amb els codis QR corresponents
canco_list = {
    "qr1": "https://www.youtube.com/watch?v=example1",  # Exemple: L'Estaca
    "qr2": "https://www.youtube.com/watch?v=example2",  # Exemple: Camins
    "qr3": "https://www.youtube.com/watch?v=example3",  # Exemple: Boig per tu
    "qr4": "https://www.youtube.com/watch?v=example4",  # Exemple: Bon dia
    "qr5": "https://www.youtube.com/watch?v=example5",   # Exemple: Amagada primavera
    "qr6": "https://m.youtube.com/watch?v=WakP10DXiD0"  # Exemple: La Marina - Esta Morena


}

# Funció per utilitzar la càmera i escanejar QR
def escanejar_qr_camera():
    cap = cv2.VideoCapture(0)
    canco_url = None

    while canco_url is None:
        _, frame = cap.read()
        for barcode in decode(frame):
            qr_code = barcode.data.decode('utf-8')
            if qr_code in canco_list:
                canco_url = canco_list[qr_code]
                break

        cv2.imshow("Escaneja el codi QR", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return canco_url

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

# Interfície de l'aplicació Streamlit
def main():
    st.title("Joc Temazus - Cançons Catalanes")

    # Botó Play per escanejar i reproduir la cançó
    if st.button("Play"):
        st.write("Escanejant codi QR...")

        # Escanejar QR utilitzant la càmera
        canco_url = escanejar_qr_camera()

        if canco_url:
            st.write("Cançó trobada! Reproduint...")
            player = reproduir_canco(canco_url)
            if st.button("Atura"):
                player.stop()

if __name__ == "__main__":
    main()
