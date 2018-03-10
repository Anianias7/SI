import itertools


def __create_connections_list(individual):
    return list(itertools.permutations(individual, 2))


def __get_index_of_gene(gene, individual):
    return list(individual).index(gene)


def __indexes_of_single_connection(single_connection, individual):
    return __get_index_of_gene(single_connection[0], individual), \
           __get_index_of_gene(single_connection[1], individual)


def __calculate_single_flow(single_connection, flow_matrix):
    return int(flow_matrix[single_connection[0]][single_connection[1]])


def __calculate_single_distance(single_connection, individual, distance_matrix):
    return distance_matrix[__indexes_of_single_connection(single_connection, individual)[0],
                           __indexes_of_single_connection(single_connection, individual)[1]]

