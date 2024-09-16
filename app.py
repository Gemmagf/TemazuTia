import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner
import youtube_dl
import vlc

# Llista de cançons amb els codis QR corresponents
canco_list = {
    "qr1": "https://www.youtube.com/watch?v=example1",  # Exemple: L'Estaca
    "qr2": "https://www.youtube.com/watch?v=example2",  # Exemple: Camins
    "qr3": "https://www.youtube.com/watch?v=example3",  # Exemple: Boig per tu
    "qr4": "https://www.youtube.com/watch?v=example4",  # Exemple: Bon dia
    "qr5": "https://www.youtube.com/watch?v=example5",   # Exemple: Amagada primavera
    "qr6": "https://m.youtube.com/watch?v=WakP10DXiD0"  # Exemple: La Marina - Esta Morena


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

# Interfície de l'aplicació Streamlit
def main():
    st.title("Joc Temazus - Cançons Catalanes")

    # Escaneig de QR
    qr_code = qrcode_scanner(key='qrcode_scanner')

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

if __name__ == "__main__":
    main()
