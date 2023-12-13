import math
import os
import ast
import shutil

from PIL import Image

path = "home/optcode"
path2 = "/home/destinationImg"
newLines = []

os.chdir(path)
dictionary = {}


def str_to_colorscale(string):
    bit = "0"
    pixel_list = []

    tmp = tuple(map(int, string.split(',')))
    pixel_list.append(tmp)
    pixel = tmp

    return pixel


def logs_files():
    for file in os.listdir(path):
        yield file


def img_generator(lines):
    '''conteggio le righe per la dimensione dell'immagine'''
    k = 0
    for line in lines:
        string = line
        if line == '\n':
            continue
        k += 1


    '''genero pixelmap e immagine'''
    dim = int(math.sqrt(k)) + 1
    img = Image.new('RGB', (dim, dim), 'white')
    pixMap = img.load()
    return img, pixMap, dim


def fil_image(pixmap, pixel, x, y, dim):
    if x < dim:
        pixmap[x, y] = pixel
        x += 1
    else:
        x = 0
        y += 1
        pixmap[x, y] = pixel
        x += 1

    return x, y, pixmap


def lines_reader(lines, pixMap, dim):
    x, y = 0, 0  # coordinate pixelmap
    '''loop per le righe'''
    for line in lines:
        string = line
        if line == '\n':
            continue

        '''genero pixel e inserisco nella pixelmap'''
        single_pixel = str_to_colorscale(string)
        print(single_pixel)
        if y < dim:
            x, y, pixMap = fil_image(pixMap, single_pixel, x, y, dim)
        else:
            print("image size error")
            break

    return pixMap


def file_reader(files):
    '''loop per i file'''
    for file in files:
        file_p = path + '/' + file
        print(file_p)

        with open(file_p, 'r', encoding='utf8') as file_reader:
            lines = file_reader.readlines()

        img, pixMap, dim = img_generator(lines)
        pixMap = lines_reader(lines, pixMap, dim)

        file_name = file.split(".")
        img.save(path2 + '/' + file_name[0] + '.png')


def file_move():

    for filename in os.listdir():
        if filename.endswith(".png"):
            shutil.move(path + filename, path2 + filename)
            print("moved")


if __name__ == "__main__":
    files = list(logs_files())
    file_reader(files)
