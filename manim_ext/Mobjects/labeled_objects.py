"""
Labeled Polygon classes
"""
from manim import *
class LabeledPoly(Mobject):
  """
  points :
  vertices of polygon
  format:
    LabeledPoly(points={
      "A":(2,4),
      "B":(3,2),
      ...
    })
  """
  def __init__(self, **kwargs):
    super().__init__(self, **kwargs)
    coords_labels = kwargs.points
    verts = []
    labels = []
    for key, value in coords_labels:
      labels += key
      verts += value

    self.submobjects += Polygon(*verts)