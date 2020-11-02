import plot_matrix
import numpy as np


def test_generate_matrix():
    matrix = plot_matrix.generate_random_matrix(10, 10)
    assert matrix.shape == (10, 10), "矩阵形状不一致！"
    assert set([0, 1]) == set(matrix.ravel()), "矩阵元素不是二值！"
    matrix2 = plot_matrix.generate_random_matrix(10, 10)
    assert not np.array_equal(matrix, matrix2), "生成矩阵不满足随机性"


def test_save_matrix(tmp_path):
    path = tmp_path / "example.jpg"
    matrix = plot_matrix.generate_random_matrix(10, 10)
    plot_matrix.save_matrix(matrix, path)
    assert path.exists()
