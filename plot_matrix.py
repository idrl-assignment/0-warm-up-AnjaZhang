# TODO: import ...
import numpy as np
from PIL import Image


def generate_random_matrix(m, n):
    random_matrix = np.random.rand(m, n)
    for i in range(m):
        for j in range(n):
            if random_matrix[i, j] >= 0.5:
                random_matrix[i, j] = 1
            else:
                random_matrix[i, j] = 0
    return random_matrix


def save_matrix(matrix, file_name):
    im = Image.fromarray(matrix.astype('uint8'))
    im.save(file_name)
    return None


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
