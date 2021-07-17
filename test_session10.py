import pytest
import re
from session10 import *
import inspect
import session10
import os
import test_session10

README_CONTENT_CHECK_FOR=['session10','Sequence','vertices','edges','properties','max','ratio']
def test_readme_exists():
    assert os.path.isfile(
        "README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md",
                  "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_repeatations():
    functions = inspect.getmembers(test_session10, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    """
    Test case to check whether the functions have docstrings or not.
    """
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
            assert function[1].__doc__

