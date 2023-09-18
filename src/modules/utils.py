import os


def is_valid_c_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension == '.c'


def get_line_by_char_index(text, char_index):
    lines = text.split('\n')
    current_index = 0

    for line in lines:
        line_length = len(line) + 1
        if current_index + line_length > char_index:
            return line
        current_index += line_length

    return ''
