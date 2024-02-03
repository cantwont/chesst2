def load_names(file_name):
    names = []
    with open(file_name, 'r') as file:
        for line in file:
            names.append(line.strip())
    return names