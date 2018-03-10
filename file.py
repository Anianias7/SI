import numpy as np


def get_number_of_cols(file_name):
    with open(file_name) as my_file:
        num = my_file.readlines()[0]
    return int(num)


def get_distance_matrix(file_name):
    matrix = np.loadtxt(file_name, skiprows=1)
    matrix_d = matrix[:get_number_of_cols(file_name), :]
    return matrix_d


def get_flow_matrix(file_name):
    matrix = np.loadtxt(file_name, skiprows=1)
    matrix_f = matrix[get_number_of_cols(file_name):, :]
    return matrix_f


def mm(file_name):
    return np.loadtxt(file_name)

