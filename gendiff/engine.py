from collections import OrderedDict
import json
import os

formats = {
    'json': json.load}

PREFIX_ADD = '  + '
PREFIX_DEL = '  - '
PREFIX_NCh = '    '


def read_data(path):
    """
    Open file
    """
    return open(path)


def get_format(pathfile: str) -> str:
    """
    Read filename and return extension of a file
    """
    extension = os.path.splitext(pathfile)[1].lstrip('.')
    return extension


def convertator(data, extension):
    """
    Сonverts files of different formats into a python dictionary
    """
    if extension not in formats:
        raise TypeError('Unsupported format. Next formats are supported: {}'
                        .format(formats.keys()))
    return formats[extension](data)


def get_diff(old, new):
    """
    Сompares two dictionaries and outputs the differences between them
    old (dict): first dict
    new (dict): second dict
    return (OrderDict): OrderDict with differences
    """
    Ord = {}
    for key, value in new.items():
        Ord[key] = value
    for key, value in old.items():
        Ord[key] = value
        
    Ord = OrderedDict(sorted(Ord.items()))
    
    result = '{\n'
    old_keys = set(old.keys()) - set(new.keys())
    new_keys = set(new.keys()) - set(old.keys())
    for key in Ord:
        if key in old_keys:
            result += f'{PREFIX_DEL}{key}: {old[key]},\n'
        elif key in old.keys() and key in new.keys() and old[key] != new[key]:
            result += f'{PREFIX_DEL}{key}: {old[key]},\n'
            result += f'{PREFIX_ADD}{key}: {new[key]},\n'
        elif key in old.keys() and key in new.keys() and old[key] == new[key]:
            result += f'{PREFIX_NCh}{key}: {old[key]},\n'
        else:
            result += f'{PREFIX_ADD}{key}: {new[key]},\n'
    result += '}'
    return result
        
        
def generate_diff(file_path1, file_path2):
    """
    Finds differences between two files
    """
    data1 = convertator(read_data(file_path1), get_format(file_path1))
    data2 = convertator(read_data(file_path2), get_format(file_path2))
    diff = get_diff(data1, data2)
    return diff
    