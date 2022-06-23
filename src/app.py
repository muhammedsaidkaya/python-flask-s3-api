from flask import Flask
from .controllers.s3_controller import s3_api as s3


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(s3, url_prefix="/")

    @app.route('/', methods=['GET'])
    def index():
        """
        Root endpoint for populating root route

        Returns:
            Greeting message
        """
        return """
        Welcome to the S3 API
        """

    return app
