import os

def get_files_info(working_directory, directory=None):
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The permitted working directory
        directory (str, optional): The directory to list. Defaults to None.

    Returns:
        str: Formatted directory contents or error message
    """
    try:
        # Handle default directory case
        if directory is None:
            directory = working_directory
        
        # Get absolute paths for safety checks
        working_dir_abs = os.path.abspath(working_directory)
        requested_dir_abs = os.path.abspath(os.path.join(working_directory, directory))
        
        # Check if requested directory is outside working directory
        if not requested_dir_abs.startswith(working_dir_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if it's actually a directory
        if not os.path.isdir(requested_dir_abs):
            return f'Error: "{directory}" is not a directory'
        
        # List directory contents
        entries = os.listdir(requested_dir_abs)
        result = []
        
        for entry in entries:
            entry_path = os.path.join(requested_dir_abs, entry)
            size = os.path.getsize(entry_path)
            if os.path.isfile(entry_path):
                result.append(f"- {entry}: file_size={size} bytes, is_dir=False")
            else:
                # For directories, we don't include size in the requirements
                result.append(f"- {entry}: file_size={size} bytes, is_dir=True")
        
        return "\n".join(result)
    
    except Exception as e:
        return f"Error: {str(e)}"