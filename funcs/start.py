from funcs.load_names import load_names
from funcs.process import process_names
from funcs.sb.config import delay

def go(file_name):
    names = load_names(file_name)
    process_names(names, delay=delay)