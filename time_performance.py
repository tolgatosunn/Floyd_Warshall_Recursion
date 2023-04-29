'''
This module compares the running time of the iterative
and recursive versions of the Floyd-Warshall algorithm.
'''

import time
import sys
from io import StringIO
from floyd_recursion import floyd, graph_creator
from floyd_iteration import floyd_it


class Capturing(list):
    '''
    This class catches the printed result.
    It will be needed to test whether printed results are valid or not.
    '''
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def recursion_performance():
    '''
    This function is designed to measure the runtime required to execute 
    the floyd function (recursive version of Floyd-Warshall Algorithm) 
    10,000 times on 10,000 randomly generated 4x4 graphs.
    '''

    start_time_recur = time.perf_counter()

    for i in range(0,10000):
        graph_size = 5
        graph_param = graph_creator(graph_size)
        with Capturing() as output:
            floyd(graph_param, graph_size)

    end_time_recur = time.perf_counter()

    execution_time_recur = end_time_recur - start_time_recur
    return execution_time_recur


def iterative_performance():
    '''
    This function is designed to measure the runtime required to execute 
    the floydWarshall function (iterative version of Floyd-Warshall Algorithm) 
    10,000 times on 10,000 randomly generated 4x4 graphs.
    '''
    start_time_iter = time.perf_counter()

    for i in range(0,10000):
        graph_size = 5
        graph_param = graph_creator(graph_size)
        with Capturing() as output:
            floyd_it(graph_param)
    end_time_iter = time.perf_counter()

    execution_time_iter = end_time_iter - start_time_iter
    return execution_time_iter


def comparison():
    '''
    This function is designed to compare the required execution time 
    of recursive and iterative versions of the Floyd-Warshall algorithm. 
    The output is a print of the difference in ratio.
    '''

    execution_time_recursion = recursion_performance()
    execution_time_itersion = iterative_performance()

    print('After running 10,000 times, the execution time of recursion is: '
          , round(execution_time_recursion, 2), ' seconds')
    print('After running 10,000 times, the execution time of iteration is: '
          , round(execution_time_itersion, 2), ' seconds')

    if execution_time_itersion > execution_time_recursion:
        ratio = ( execution_time_recursion / execution_time_itersion - 1 ) * ( -1 )
        ratio = '{0:.0f}%'.format(ratio * 100)
        print('Recursive version is about ', ratio, ' faster than iterative version.')

    else :
        ratio = ( execution_time_itersion / execution_time_recursion - 1 ) * ( -1 )
        ratio = '{0:.0f}%'.format(ratio * 100)
        print('Iterative version is about ', ratio, ' faster than recursive version.')


if __name__ == '__main__':
    comparison()
