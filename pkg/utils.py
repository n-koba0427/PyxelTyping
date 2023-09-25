import importlib.resources as pkg_resources

def get_data_path(dir):
    if __package__:
        return str(pkg_resources.files(__package__).joinpath(dir))
    else:
        return dir
    
def load_vocabulary_from_file(filepath, replace_token):
    result = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line_text = line.strip()
            for token, value in replace_token.items():
                line_text = line_text.replace(token, value)
            result.append(line_text.split("|"))
        return result