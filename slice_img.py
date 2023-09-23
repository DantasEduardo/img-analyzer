import matplotlib.pyplot as plt


def main(path_img:str, path_save:str) -> None:
    img = plt.imread(path_img)[120:-360, 350:-130]
    plt.imsave(path_save, img)


if __name__ == "__main__":
    img = "data_raw\img_infra.jpg"
    file = "data\img_infra_slice.png"
    main(img, file)