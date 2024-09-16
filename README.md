# TemazuTia
Aquesta és una aplicació web desenvolupada amb **Streamlit** per jugar al Joc de les cançons utilitzant codis QR per identificar i reproduir cançons catalanes.

## Com funciona

1. Escanejar un codi QR.
2. Si el codi QR coincideix amb alguna de les cançons de la nostra llista, es reproduirà l'àudio directament.

## Tecnologies utilitzades

- Python
- Streamlit
- OpenCV
- Pyzbar
- youtube_dl

## Explicació del codi
1. Escanejar QR amb la càmera:
Utilitzem OpenCV per accedir a la càmera i detectar codis QR amb pyzbar.
La funció escanejar_qr_camera() obre la càmera, captura imatges i les analitza en temps real fins que es detecta un codi QR vàlid que es correspon amb un enllaç a la llista de cançons.
Un cop es detecta un QR, es tanca la càmera i es retorna l'URL de la cançó.

2. Obtenir l'àudio de YouTube:
La funció obtenir_audio() utilitza youtube_dl per obtenir l'enllaç directe de l'àudio d'una cançó a partir de l'URL de YouTube.

3. Reproducció de la cançó:
Utilitzem VLC per reproduir l'enllaç d'àudio directament des de YouTube sense necessitat de descarregar la cançó.
El botó "Play" fa que l'aplicació comenci a escanejar el codi QR. Quan es detecta un codi vàlid, es reprodueix la cançó corresponent.
També s'inclou un botó "Atura" que atura la reproducció si es prem després de començar la cançó.

4. Interfície gràfica amb Streamlit:
La interfície és molt minimalista, només mostra el botó "Play". Quan es prem, s'inicia l'escaneig del QR i es reprodueix la cançó automàticament sense mostrar informació addicional.
També es mostra un botó d'"Atura" per aturar la reproducció.



## Desplegament

Aquesta aplicació està desplegada utilitzant **Streamlit Cloud**. Pots accedir a la versió web [aquí](enllaç_de_la_teva_aplicació).

## Instal·lació local

Si vols executar l'aplicació localment:

1. Clona aquest repositori.
2. Instal·la les dependències:
    ```
    pip install -r requirements.txt
    ```
3. Executa l'aplicació:
    ```
    streamlit run app.py
    ```



