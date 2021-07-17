import math
from typing import Union


class RegPolygon:
    def __init__(self,vertices:int,circumradius:Union[float,int]):
        '''Initialise all properties here'''
        if isinstance(vertices,int):
            if vertices<3:
                raise ValueError("Vertex for a polygon cannot be less than 3!")
        else:
            raise TypeError
        self.edges=vertices
        self.circumradius=circumradius
        self.interiorangle=(vertices-2)*180/vertices
        self.edgelength=2*circumradius*math.sin(math.pi/vertices)
        self.apothem=circumradius*math.cos(math.pi/vertices)
        self.area=0.5*vertices*self.apothem*self.edgelength
        self.perimeter=vertices*self.edgelength
    

    def __eq__(self, o: object) -> bool:
        '''Checks if object provided is equal to the current object'''
        if isinstance(o,RegPolygon):
            return self.circumradius==o.circumradius and self.edges==o.edges
        else:
            return False
    def __repr__(self) -> str:
        '''Representation of the instance'''
        return "RegPolygon class instance for storing properties of a regular polygon"
    
    def __gt__(self,o:object) -> bool:
        '''Checks if object provided is larger than the current object'''
        if isinstance(o,RegPolygon):
            return self.edges>o.edges
        else:
            return False


Polygon1=RegPolygon(3,4)
print(Polygon1.perimeter,Polygon1.circumradius,Polygon1.edgelength,Polygon1.interiorangle,Polygon1.edges,Polygon1.apothem,RegPolygon(2,3)>Polygon1,sep="\n")

        

