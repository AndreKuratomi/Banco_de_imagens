from flask import Flask, request
import os
from os import getenv
from dotenv import load_dotenv
from kenzie.image import create_directories, upload, get_files, get_files_by_extension, download_files
# , download_zip_file

load_dotenv()


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(getenv("MAX_CONTENT_LENGTH"))


create_directories()


@app.get("/")
def home():
    return {"msg": "Olá"}


@app.post("/upload")
def decorated_upload():
    variable = request.files["file"]
    return upload(variable)


@app.errorhandler(413)
def name_size_error(_):
    return {"message": "Tamanho maior que 1MB!"}, 413


@app.get("/files")
def decorated_get_files():
    return get_files()


@app.get("/files/<extension>")
def decorated_get_files_by_extension(extension):
    return get_files_by_extension(extension)


@app.get("/download/<file_name>")
def decorated_download_files(file_name):
    return download_files(file_name)


# @app.get("/download-zip/query_params")
# def decorated_download_zip_file():
#     return download_zip_file()

