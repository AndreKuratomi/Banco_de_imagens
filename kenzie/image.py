from flask import jsonify, send_file
from flask.helpers import safe_join
from werkzeug.datastructures import FileStorage
from os import getenv
from dotenv import load_dotenv
import os.path

load_dotenv()

max = getenv("MAX_CONTENT_LENGTH")
directory = getenv("FILES_DIRECTORY")
download = getenv("DOWNLOAD_DIRECTORY")
allowed = getenv("ALLOWED_EXTENSIONS")


def create_directories():
    allowed_split = allowed.split(', ')
    if not os.path.exists(f"{directory}"):
        os.mkdir(f"{directory}")
    os.chdir(f"{directory}")
    for elem in allowed_split:
        if not os.path.exists(f"{elem}"):
            os.mkdir(f"{elem}")
    os.chdir("..")


def upload(file):
    os.chdir(f"{directory}")

    if file.filename.endswith(".jpg"):
        os.chdir("jpg")
        jpg_dir = os.listdir("./")
        for files in jpg_dir:
            if file.filename == files:
                os.chdir("../..")
                return {"message": "Arquivo já existe no diretório!"}, 409
        file.save(f"./{file.filename}")
        os.chdir("../..")
        return {"message": f"{file.filename} adicionado com sucesso!"}, 201

    if file.filename.endswith(".png"):
        os.chdir("png")
        png_dir = os.listdir("./")
        for files in png_dir:
            if file.filename == files:
                os.chdir("../..")
                return {"message": "Arquivo já existe no diretório!"}, 409
        file.save(f"./{file.filename}")
        os.chdir("../..")
        return {"message": f"{file.filename} adicionado com sucesso!"}, 201

    if file.filename.endswith(".gif"):
        os.chdir("gif")
        gif_dir = os.listdir("./")
        print(gif_dir)
        for files in gif_dir:
            if file.filename == files:
                os.chdir("../..")
                return {"message": "Arquivo já existe no diretório!"}, 409
        file.save(f"./{file.filename}")
        os.chdir("../..")
        return {"message": f"{file.filename} adicionado com sucesso!"}, 201

    os.chdir("..")
    return {"message": "Outro formato além do permitido!"}, 415


def get_files():
    arquives_list = []

    for elem in os.listdir(f"{directory}"):
        for sub_elem in os.listdir(f"{directory}/{elem}"):
            arquives_list.append(sub_elem)

    return jsonify(arquives_list), 200


def get_files_by_extension(extension):
    extension_list = []

    for elem in os.listdir(f"{directory}"):
        for sub_elem in os.listdir(f"{directory}/{elem}"):
            if sub_elem.endswith(f"{extension}"):
                extension_list.append(sub_elem)

    return jsonify(extension_list), 200


def download_files(file_name: FileStorage):
    ext = file_name.split('.')[1]
    if file_name in os.listdir(f"{directory}/{ext}"):
        path = safe_join(f"../{directory}/{ext}", f"{file_name}")
        return send_file(path, as_attachment=True)
    return {"message": f"{file_name} não encontrado!"}, 404


# def download_zip_file():
    
