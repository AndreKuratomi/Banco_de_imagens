from flask import jsonify, request
import os
from os import getenv
from dotenv import load_dotenv
# from uuid import uuid4
import os.path

load_dotenv()

max = getenv("MAX_CONTENT_LENGTH")
directory = getenv("FILES_DIRECTORY")
allowed = getenv("ALLOWED_EXTENSIONS")

def upload(file):
    # print(os.stat(f"{file.filename}").st_size)
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

    return {"message": "Outro formato além do permitido!"}, 415
# CRTL + D!


def get_files():
    arquives = request.files
    print(request.files)
    return jsonify(arquives)


# def get_files_by_extension():
    # fazer aqui um for in selecionando pela extensão



# def download_files():
    #



# def download_zip_file():
#     extension = request.args.get("file_extension")
#     #  qual o tipo da extensão? string?
#     ratio = request.args.get("compression-ratio")
#     # e da taxa de compressão? int?
