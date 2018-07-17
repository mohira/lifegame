import itertools

import cv2
import numpy as np


def main():
    # TODO: pathlib使おう
    # img_path = '../../image/block_with_border.png'
    img_path = '../../image/beehive.png'

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.dtype)
    width_cell = 14
    width_gray = 2

    # 正方形でない場合にも対応してる
    cell左上座標_横 = np.arange(width_gray + 1, gray.shape[0], width_cell + width_gray)
    cell左上座標_縦 = np.arange(width_gray + 1, gray.shape[1], width_cell + width_gray)

    hoge = [gray[idx] for idx in itertools.product(cell左上座標_横, cell左上座標_縦)]

    fuga = np.array(hoge).reshape(len(cell左上座標_横), len(cell左上座標_縦))
    array = np.where(fuga == 255, 1, fuga)
    np.savetxt('out.csv', array, fmt='%i', delimiter=',')


if __name__ == '__main__':
    main()
