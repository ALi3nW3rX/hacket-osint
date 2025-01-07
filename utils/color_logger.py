def log_info(message):
    print(f"\033[94m[INFO]\033[0m {message}")  # Light Blue

def log_success(message):
    print(f"\033[92m[SUCCESS]\033[0m {message}")  # Green

def log_warning(message):
    print(f"\033[93m[WARNING]\033[0m {message}")  # Orange

def log_error(message):
    print(f"\033[91m[ERROR]\033[0m {message}")  # Red
