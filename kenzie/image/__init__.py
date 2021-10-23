from flask import jsonify, request
import os
from os import getenv
from dotenv import load_dotenv
import os.path

load_dotenv()

max = getenv("MAX_CONTENT_LENGTH")
directory = getenv("FILES_DIRECTORY")
download = getenv("DOWNLOAD_DIRECTORY")
allowed = getenv("ALLOWED_EXTENSIONS")


def upload(file):

    if file.filename.endswith(".jpg"):
        os.chdir(f"{directory}")

        if not os.path.exists("jpg"):
            os.system("mkdir jpg")
            file.save(f"{directory}/jpg/{file.filename}")
            return {"message": f"{file.filename} adicionado com sucesso!"}, 201

        jpg_dir = os.listdir("jpg")
        for files in jpg_dir:
            if file.filename == files:
                return {"message": "Arquivo já existe no diretório!"}, 409
        file.save(f"{directory}/jpg/{file.filename}")
        return {"message": f"{file.filename} adicionado com sucesso!"}, 201

    if file.filename.endswith(".png"):
        os.chdir(f"{directory}")

        if not os.path.exists("png"):
            os.system("mkdir png")
            file.save(f"{directory}/png/{file.filename}")
            return {"message": f"{file.filename} adicionado com sucesso!"}, 201

        png_dir = os.listdir("png")
        for files in png_dir:
            if file.filename == files:
                return {"message": "Arquivo já existe no diretório!"}, 409
        file.save(f"{directory}/png/{file.filename}")

        return {"message": f"{file.filename} adicionado com sucesso!"}, 201

    if file.filename.endswith(".gif"):
        os.chdir(f"{directory}")

        if not os.path.exists("gif"):
            os.system("mkdir gif")
            file.save(f"{directory}/gif/{file.filename}")
            return {"message": f"{file.filename} adicionado com sucesso!"}, 201

        gif_dir = os.listdir("gif")
        for files in gif_dir:
            if file.filename == files:
                return {"message": "Arquivo já existe no diretório!"}, 409
        file.save(f"{directory}/gif/{file.filename}")

        return {"message": f"{file.filename} adicionado com sucesso!"}, 201

    arquive = request.files
    print(arquive)

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


def download_files(file_name):
    arquive = request.files
    print(arquive)
    for elem in arquive:
        print(elem)
    #     if elem.filename == file_name:
    #         elem.save(f"{download}/{file_name}")
    #         return {"message": f"Download de {file_name} feito com sucesso!"}, 200
    # return {"message": f"{file_name} não encontrado!"}, 404
    # file_name


# def download_zip_file():
#     extension = request.args.get("file_extension")
#     #  qual o tipo da extensão? string?
#     ratio = request.args.get("compression-ratio")
#     # e da taxa de compressão? int?
