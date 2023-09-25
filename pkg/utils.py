import importlib.resources as pkg_resources

def get_data_path(dir):
    if __package__:
        return str(pkg_resources.files(__package__).joinpath(dir))
    else:
        return dir
    
def load_vocabulary_from_file(filepath, name):
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip().replace("{name}", name).split("|") for line in file.readlines()]