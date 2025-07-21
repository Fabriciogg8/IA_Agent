# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

def run():
    """
    Run the get_files_info function with various test cases.
    """
    # Test cases
    print(get_files_info("calculator", "."))  # Current directory
    print(get_files_info("calculator", "pkg"))  # Subdirectory within the working directory
    print(get_files_info("calculator", "/bin"))  # Absolute path outside the working directory
    print(get_files_info("calculator", "../"))  # Parent directory outside the working directory

if __name__ == "__main__":
    run()