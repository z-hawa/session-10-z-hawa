from session10 import RegPolygon
from typing import Union


class SpecialPolygon:
    def __init__(self, MaxVertice: int, Circum: Union[float, int]) -> None:
        '''Initialises all the properties'''
        if isinstance(MaxVertice, int):
            if MaxVertice < 3:
                raise ValueError("Vertex for a polygon cannot be less than 3!")
        else:
            raise TypeError
        if not isinstance(Circum,(float,int)):
            raise TypeError
        self.MaxVertice = MaxVertice
        self.Circum = Circum

    def __getitem__(self, vertex):
        """This function returns the area at the specific index"""
        if isinstance(vertex, int):
            # To emulate reverse indexing
            if vertex == 0:
                vertex=self.MaxVertice
            if vertex < 1:
                vertex = vertex + self.MaxVertice + 1
            if vertex < 3:
                raise IndexError("A Polygon with less than 3 sides does not exist!")
            if vertex > self.MaxVertice:
                raise IndexError("A Polygon with that vertice is out of bounds!")
            else:
                temp = RegPolygon(vertex, self.Circum)
                return temp.area / temp.perimeter
        else:
            idx = list(vertex.indices(self.MaxVertice))
            RangeOfNumbersToGet = range(idx[0]+3, idx[1] + 3, idx[2])
            return [self[n] for n in RangeOfNumbersToGet]

    def __len__(self) -> int:
        '''Returns the length of this Polygon instance'''
        return self.MaxVertice - 2  # Since Polygons with less than 3 sides do not exist

    def __repr__(self) -> str:
        '''Representation of the instance'''
        return "Custom Polygon sequence with a max efficiency function"

    def highest_ratios(self) -> int:
        '''Calculates all ratios and finds the highest one'''
        ratiodict = {}
        for i in range(3, self.MaxVertice+1):
            temp = RegPolygon(i, self.Circum)
            ratiodict[i] = temp.area / temp.perimeter
        return max(ratiodict.values())
