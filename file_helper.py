import os


def clear_dir(d):
    for filename in os.listdir(d):
        file_path = os.path.join(d, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path} due to {e}")


def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def check_clear_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        clear_dir(path)
