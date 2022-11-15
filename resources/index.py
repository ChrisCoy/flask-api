from flask_restful import Resource, reqparse, request
from flask import Response
# from models.file import FileModel

import time

# DIR = "./arquivos/"
API_LINK = 'http://127.0.0.1:5000'


class Index(Resource):
    def get(self):
        html = f'<form action="{API_LINK}/send-archives"' \
               'method="POST"' \
               'enctype="multipart/form-data"' \
               '>' \
               '<label for="meuArquivo">Selecione o arquivo</label><br>' \
               '<input type="file" id="meuArquivo" name="meuArquivo" /><br><br>' \
               '<input type="submit" value="Submit" />' \
               '</form>'
        return Response(html, content_type='text/html')
