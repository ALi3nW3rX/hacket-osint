import threading
from utils.color_logger import log_info, log_success, log_error

def run_in_threads(functions_with_args):

    threads = []

    for func, args in functions_with_args:
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
        

    for thread in threads:
        thread.join()
        
