import os


def get_file_names_from_directory(directory=r"E:\Python Course\Replay_Data\Replays"):
    file_list = []
    for filename in os.listdir(directory):
        file_list.append(filename)
    return file_list
