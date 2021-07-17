# Session10 assignment
### Sequence types

## Regular Polygon class
```py
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
``` 
This class takes in two values while initialising . One is the vertex and the other is the circumradius. The vertex cannot be less than 3 due to polygon's with less than 3 sides not existing or possible. After this is done , the init calculates all the properties of the polygon which are required . A greater than function is available which checks the vertex and returns True if the provided object has a smaller vertex than the self object . An \_\_eq__ function is also present which checks the equality of the vertex and the circumradius of the provided object and the current object . a \_\_repr__ function is also present .

## Special Polygon instance
```py
from session10 import RegPolygon
from typing import Union

class SpecialPolygon:
    def __init__(self,MaxVertice:int,Circum:Union[float,int]) -> None:
        '''Initialises all the properties'''
        if isinstance(MaxVertice,int):
            if MaxVertice<3:
                raise ValueError("Vertex for a polygon cannot be less than 3!")
        else:
            raise TypeError
        self.MaxVertice=MaxVertice
        self.Circum=Circum
    
    def __getitem__(self,vertex:int)->float:
        '''This function returns the area at the specific index'''
        if isinstance(vertex,int):
            # To emulate reverse indexing
            if vertex<0:
                vertex=vertex+self.MaxVertice+1
            if vertex<3:
                raise IndexError("A Polygon with less than 3 sides does not exist!")
            if vertex>self.MaxVertice:
                raise IndexError("A Polygon with that vertice is out of bounds!")
            else:
                temp=RegPolygon(vertex,self.Circum)
                return temp.area/temp.perimeter
        else:
            raise TypeError("Index does not accept strings")
    
    def __len__(self) -> int:
        '''Returns the length of this Polygon instance'''
        return self.MaxVertice-2  #Since Polygons with less than 3 sides do not exist

    def __repr__(self) -> str:
        '''Representation of the instance'''
        return "Custom Polygon sequence with a max efficiency function"
    
    def highest_ratios(self) -> int:
        '''Calculates all ratios and finds the highest one'''
        ratiodict={}
        for i in range(3,self.MaxVertice):
            temp=RegPolygon(i,self.Circum)
            ratiodict[i]=temp.area/temp.perimeter
        return max(ratiodict.values())
```
This class takes in two values at initialisation. The purpose of the class is to return the highest area:perimeter ratio and this is done by the highest_ratios function. It stores the ratios in a dict which is a sequence type. It returns the dictionary key of the highest area:perimeter ratio. The getitem function takes in an integer and returns the area:perimeter ratio for the vertex if it is less than the MaxVertex and greater than 3.
<br>
Note- Vertex has to be greater than or equal to three since a Polygon with less than 3 sides is a 1D shape since it never gets closed.