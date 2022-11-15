from flask_restful import Resource, reqparse, request
from flask import Response
from models.file import FileModel
import os
import time
import sys

DIR = "./arquivos/"


class Files(Resource):
    def get(self):
        # SELECT * FROM files
        return {'all_files': [file.json() for file in FileModel.query.all()]}
        # return archive_name, 200


class File(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('file_name', type=str, required=True,
                           help="The field 'file' cannot be left blank.")

    def get(self, file_name):
        file = File.find_file(file_name)
        if file:
            return file.json()
        return None

    def post(self, file_name):
        archive = request.files.get("meuArquivo")
        id = str(time.time()) + str(archive.filename)
        archive.save(DIR + id)

        file = FileModel(str(id), str(archive.filename))

        try:
            file.save_file()
        except:
            # Internal Server Error
            return str(sys.exc_info()[0]), 500

        return Response('<script>alert("Arquivo enviado com sucesso!");'
                        'window.onload = () => { window.location.replace("/");}'
                        '</script>', content_type='text/html')

    def put(self, file_name):
        file = FileModel.find_file(file_name)
        if file:
            os.remove(DIR + file_name)
            archive = request.files.get("meuArquivo")
            archive.save(DIR + str(archive.filename))
            return 200

        return 500

    def delete(self, file_name):
        file = FileModel.find_file(file_name)
        if file:
            file.delete_file()
            os.remove(DIR + file_name)
            return {'message': 'File deleted.'}
        return {'message': 'File not found.'}, 404

        # dados = Hotel.atributos.parse_args()
        # hotel = HotelModel(hotel_id, **dados)
        # try:
        #     hotel.save_hotel()
        # except:
        #     return {"message": "An error ocurred trying to create hotel."}, 500 #Internal Server Error
        # return hotel.json(), 201

    # @jwt_required
    # def put(self, hotel_id):
    #     dados = Hotel.atributos.parse_args()
    #     hotel = HotelModel(hotel_id, **dados)
    #
    #     hotel_encontrado = HotelModel.find_hotel(hotel_id)
    #     if hotel_encontrado:
    #         hotel_encontrado.update_hotel(**dados)
    #         hotel_encontrado.save_hotel()
    #         return hotel_encontrado.json(), 200
    #     hotel.save_hotel()
    #     return hotel.json(), 201
    #
    # @jwt_required
    # def delete(self, hotel_id):
    #     hotel = HotelModel.find_hotel(hotel_id)
    #     if hotel:
    #         hotel.delete_hotel()
    #         return {'message': 'Hotel deleted.'}
    #     return {'message': 'Hotel not found.'}, 404
