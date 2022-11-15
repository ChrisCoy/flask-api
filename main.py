from flask import Flask
from flask_restful import Api
# from resources.usuario import User, UserRegister, UserLogin
# from flask_jwt_extended import JWTManager
from resources.file import File, Files
from resources.index import Index


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    banco.create_all()


# api.add_resource(Hoteis, '/hoteis')
# api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
# api.add_resource(User, '/usuarios/<int:user_id>')
# api.add_resource(UserRegister, '/cadastro')
# api.add_resource(UserLogin, '/login')
api.add_resource(File, "/file/<string:file_name>")
api.add_resource(Files, "/file")
api.add_resource(Index, "/")


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
