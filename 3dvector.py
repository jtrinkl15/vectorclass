# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:35:12 2019

@author: james
"""


class Vector:
  vec = []
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
    # Getters and setters
  def getX(self):
    return self.x
  def setX(self, x):
    self.x = x
  def getY(self):
    return self.y
  def setY(self, y):
    self.y = y
  def getZ(self):
    return self.z
  def setZ(self, z):
    self.z = z
    
    # define string for vector
  def __str__(self):
    return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"
    
    # Define vector addition
  def __add__(self, other):
    """ assume other is Vector """
    assert isinstance(other, Vector)
    x1 = self.getX()+other.getX()
    y1 = self.getY()+other.getY()
    z1 = self.getZ()+other.getZ()
    newvec = Vector(x1,y1,z1)
    return newvec
  
  def __mul__(self, other):
    """ ASsume other is int or float """
    x2 = self.getX()*other
    y2 = self.getY()*other
    z2 = self.getZ()*other
    newvec1 = Vector(x2, y2, z2)
    return newvec1
  
  def dot(self, other):
    """ generates dot product.
        Takes 2 vectors. """
    x3 = ( (self.getX()*other.getX())
          +(self.getY()*other.getY())
          +(self.getZ()*other.getZ()))
    return x3
  
  def cross(self, other):
    """generates cross product as a vector.
       takes 2 vectors"""
    assert isinstance(other, Vector)
    x4 = (self.getY()*other.getZ()) - (self.getZ()*other.getY())
    y4 = (self.getX()*other.getZ()) - (self.getZ()*other.getX())
    z4 = (self.getX()*other.getY()) - (self.getY()*other.getX())
    newvec2 = Vector(x4,y4,z4)
    return newvec2
  
  def unit(self):
    """generates the unit vector."""
    t = self.getX()**2 + self.getY()**2 + self.getZ()**2
    scalar = (1/(t**.5))
    ## Round it to 4 places after zero because that's usually as many sig figs
    ## as I need.
    x5 = round(self.getX()*scalar, 4)
    y5 = round(self.getY()*scalar, 4)
    z5 = round(self.getZ()*scalar, 4)
    newvec3 = Vector(x5, y5, z5)
    return newvec3
