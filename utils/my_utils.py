
def read_file(path:str):
    f = open(path)
    return f.read()

def get_current_directory(file: str) -> str: 
    return "/".join(file.split('/')[:-1])