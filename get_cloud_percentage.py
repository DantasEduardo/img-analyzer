import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def get_percentage(img_path:str) -> float:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

    sure_bg = cv2.dilate(opening,kernel,iterations=1)
    percentage = (np.count_nonzero(sure_bg == 0) * 100)/(sure_bg.shape[0] * sure_bg.shape[1])
    return round(percentage, 2)


def slice(path_img:str, path_save:str) -> None:
    img = plt.imread(path_img)[279:-155, 383:-190]
    plt.imsave(path_save, img)

def save_csv(percenteage, data):
    with open('percentage_cloud.csv', 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Verifica se o cabeçalho já foi escrito
        if arquivo_csv.tell() == 0:
            escritor_csv.writerow(['percentage', 'data'])

        # Adiciona uma nova linha com a data e porcentagem
        escritor_csv.writerow([percenteage, data])


if __name__ =='__main__':

    data_inicio = datetime.strptime("2021-07-01", "%Y-%m-%d")
    data_fim = datetime.strptime("2021-07-13", "%Y-%m-%d")

    data_atual = data_inicio
    while data_atual <= data_fim:
        print(data_atual.strftime("%Y%m%d"))
        data_atual += timedelta(days=1)

        img = f"data_raw\MERGE_CPTEC_{data_atual.strftime('%Y%m%d')}.jpeg"
        file = f"data\MERGE_CPTEC_{data_atual.strftime('%Y%m%d')}.png"

        slice(img, file)
        percenteage = get_percentage(img)

        save_csv(percenteage, data_atual)