from fastapi import FastAPI
import requests
from fastapi.responses import HTMLResponse
from fastapi.responses import Response


def decode(chaine):
    lien = ""
    for i in range(len(chaine)//3):
        print(int(chaine[i*3:i*3+3]))
        lien += chr(int(chaine[i*3:i*3+3]))
    return lien

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome to U_Search !"}

@app.get("/get/{lien_encode}", response_class=HTMLResponse)
def get(lien_encode):
    lien = decode(lien_encode)
    reponse = requests.get(lien)
    if reponse.status_code == 200:

        # bytes -> str
        html = reponse.content.decode("utf-8")

        # Modification
        html = html.replace(
            'href="./',
            f'href="{lien}/'
        )

        # str -> bytes
        contenu = html.encode("utf-8")

        return Response(
            content=contenu,
            media_type=reponse.headers.get("content-type")
        )
    return "Something went wrong..."
