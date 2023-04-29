'''
This piece of code first creates a graph with randomly chosen variables
based on the input graph size.
Later, it finds the shortest path between the nodes in the graph
by applying iterative method.
Lastly, it prints out the input graph and the solution graph,
which includes the shortest distances.
'''

import sys
import itertools
import random


NO_PATH = sys.maxsize
MAX_LENGTH = 4

def get_user_input():
    '''
    Input: is a range of a graph to be registered by the user.
    Process: This function gets input from the user and checks whether
    it is validated or not.
    Output: is a range of a graph.
    '''
    while True:
        # Input graph_range will be used to produce a graph.
        graph_range = input('''
                Please, input an integer as the size of the graph 
                    to generate it with random values: ''')

        # We try to convert graph_range into an integer.
        # If we get an error which means graph_range is not an integer.
        # Then, it raises a ValueError and exits the system.
        # If the conversion into integer works,
        # the 'if' clause checks whether GRAPH_RANGE is a minus.
        # If yes, it exits the system. If no, it returns graph_range.
        try:
            graph_range = int(graph_range)
        except ValueError:
            print('''
            -----------------------------------------------   
                Graph range must be an integer value.
            ''')
            sys.exit()
        if graph_range < 0:
            print('''
            -----------------------------------------------   
                Graph range can not be negative integer.
            ''')
            sys.exit()

        return graph_range


def graph_creator(graph_size):
    '''
    This function creates a graph with random values.
    Input: Range of a graph.
    Process: A graph is to be created with random variables and
    a size arranged based on the input "size" value.
    For instance, size=4 creates a 4x4 graph.
    Output: A graph.
    '''

    graph = []
    values = [NO_PATH]+list(range(1, 10))
    # We will chose our values for the graph from the values list.

    for i in range(graph_size):  # Loop for the rows
        columns = []
        for j in range(graph_size):  # Loop for the columns
            if i == j:  # Distance should be 0 between same nodes.
                random_value = 0
            else:
                random_value = random.choice(values)
            columns.append(random_value)  # Appending randomly chosen values
        graph.append(columns)  # Appending the row into the graph

    return graph


def floyd_it(distance):
    """
    A simple implementation of Floyd's algorithm
    """

    for intermediate, start_node,end_node\
    in itertools.product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):

        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                        distance[start_node][intermediate] + distance[intermediate][end_node] )
        #Any value that have sys.maxsize has no path
    print_graph(distance)


# A utility function to print the solution and the input graphes
def print_graph(distance):
    '''
    This function is to print the input graph or the solution graph produced in floyd
    function.
    Also, it will be used to print the input graph.
    Input: is a graph.
    Process: is printing the distances between each nodes.
    Output: is a print of the graph.
    '''

    graph_size = len(distance[0])
    no_path = 999999

    for i in range(graph_size):  # Loops for rows.
        for j in range(graph_size):  # Loops for columns.

            # If the distance from i to j is above to no_path
            # which is int(999999), then print "NO_PATH".
            # Else, print the distance itself.
            if distance[i][j] > no_path:
                print(f'{"NO_PATH":>8}', end=' ')
            else:
                print(f'{distance[i][j]:>8}', end=' ')

            # If j reaches (graph_size-1), the function prints
            # to break the line. So, it will continue printing
            # from the next row.
            if j == graph_size-1:
                print('')


if __name__ == '__main__':

    GRAPH_RANGE = get_user_input()
    graph_param = graph_creator(GRAPH_RANGE)
    MAX_LENGTH = GRAPH_RANGE

    print('------------------------------------------------------')

    print('''
        Following graph is created by random values
       to be used as the input of the floyd function
            ''')
    print_graph(graph_param)

    print('------------------------------------------------------')

    print('''
        Following graph shows the shortest distances
            between every pair of vertices
        ''')
    # Function call
    floyd_it(graph_param)
