from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from db import db
from resources.user import user_blueprint

def create_app():
    app = Flask(__name__)
    
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "JWT Example API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    # Строка подключения к удалённой БД Neon.tech
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://DB_Tests_owner:e4xZpR7jazwW@ep-still-water-a5deoor3.us-east-2.aws.neon.tech/DB_Tests?sslmode=require"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "Key"

    db.init_app(app)
    api = Api(app)
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()  # Создание таблиц на удалённой БД

    app.register_blueprint(user_blueprint, url_prefix="/user")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
