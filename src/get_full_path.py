
import os


def get_full_path(*path_parts):
    """
    Construct a full path from the current working directory
    and given path parts."""

    return os.path.join(os.getcwd(), *path_parts)
