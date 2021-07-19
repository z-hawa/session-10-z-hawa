from ast import Index
import pytest
import re
from session10_special import *
from session10 import *
import inspect
import session10
import os
import test_session10

README_CONTENT_CHECK_FOR = ['session10', 'Sequence', 'vertices', 'edges', 'properties', 'max', 'ratio']


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


def test_normal_polygon_properties():
    polygon = RegPolygon(4, 5)
    assert polygon.area == 0.5 * 4 * 5 * math.cos(math.pi / 4) * 2 * 5 * math.sin(math.pi / 4)
    assert polygon.edges == 4
    assert polygon.perimeter == 4 * 2 * 5 * math.sin(math.pi / 4)
    assert polygon.interiorangle == (4 - 2) * 180 / 4
    assert polygon.edgelength == 2 * 5 * math.sin(math.pi / 4)
    assert polygon.apothem == 5 * math.cos(math.pi / 4)
    assert polygon.perimeter == 4 * 2 * 5 * math.sin(math.pi / 4)


def test_polygon_with_illegal_sides():
    with pytest.raises(ValueError):
        RegPolygon(2, 3)


def test_polygon_with_illegal_data_type():
    with pytest.raises(TypeError):
        RegPolygon("hmm", "ee")


def test_polygon_greater_than():
    assert RegPolygon(4, 2) > RegPolygon(3, 1)


def test_polygon_equals_to():
    assert RegPolygon(4, 2) == RegPolygon(4, 2)


def test_polygon_repr():
    temp = RegPolygon(4, 4)
    assert len(temp.__repr__()) > 25


# Special Polygon tests

def test_special_polygon_properties():
    SpPolygon = SpecialPolygon(3, 1)
    assert SpPolygon.Circum == 1
    assert SpPolygon.MaxVertice == 3


def test_special_polygon_with_illegal_sides():
    with pytest.raises(ValueError):
        SpecialPolygon(2, 3)


def test_special_polygon_with_illegal_data_type():
    with pytest.raises(TypeError):
        SpecialPolygon("hmm", "ee")


def test_special_polygon_length():
    temp=SpecialPolygon(3,5)
    assert temp.__len__()==1


def test_special_polygon_max_ratio():
    main=SpecialPolygon(5,1)
    temp1=RegPolygon(3,1)
    temp2=RegPolygon(4,1)
    temp3=RegPolygon(5,1)
    ls=[temp1.area/temp1.perimeter,temp2.area/temp2.perimeter,temp3.area/temp3.perimeter]
    assert max(ls)==main.highest_ratios()

def test_special_polygon_repr():
    temp = SpecialPolygon(4, 4)
    assert len(temp.__repr__()) > 25

def test_special_polygon_getitem_():
    temp=SpecialPolygon(8,2)
    assert len(temp[2:4])==2

def test_special_polygon_getitem_illegal():
    temp=SpecialPolygon(3,4)
    with pytest.raises(IndexError):
        temp[1]
  
