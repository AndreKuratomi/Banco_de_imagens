from flask import Flask, request
import os
from os import getenv
from dotenv import load_dotenv
from kenzie.image import upload, get_files
# , get_files_by_extension, download_files, download_zip_file

load_dotenv()


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(getenv("MAX_CONTENT_LENGTH"))

# 'Error: While importing 'app', an ImportError was raised.' em geral aparece importando coisas que não existem


# app.kenzie.image ou .kenzie.image
@app.post("/upload")
def decorated_upload():
    variable = request.files["file"]
    return upload(variable)


@app.errorhandler(413)
def name_size_error(_):
    return {"message": "Tamanho maior que 1MB!"}, 413


# @app.errorhandler(415)
# def name_extension_error(_):
#     return {"message": "Outro formato além do permitido!"}, 415


@app.post('/')
def func():
    # file = request.files["file"]
    # print(file.filename[-3:])
    return "Hello"


@app.get("/files")
def decorated_get_files():
    return get_files()


# @app.get("/files/<extension>")
# def decorated_get_files_by_extension():
#     return get_files_by_extension()


# @app.get("/download/<filename>")
# def decorated_download_files():
#     return download_files()


# @app.get("/download-zip/query_params")
# def decorated_download_zip_file():
#     return download_zip_file()


