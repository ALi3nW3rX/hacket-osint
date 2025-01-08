import threading
from utils.color_logger import log_info, log_success, log_error

def run_in_threads(functions_with_args):
    """
    Runs a list of functions with their arguments in parallel using threading.
    
    :param functions_with_args: List of tuples where each tuple contains a function and its arguments.
    Example: [(func1, (arg1, arg2)), (func2, (arg1,))]
    """
    threads = []

    for func, args in functions_with_args:
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
        

    for thread in threads:
        thread.join()
        
