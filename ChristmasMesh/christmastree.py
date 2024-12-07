from ngsolve import *
from netgen.occ import *

def ChristmasTreeGeometry():
    trunk = Rectangle(0.4,0.2).Face().Move((-0.2,0,0))
    seg1 = Segment(Pnt(0,0.2,0),(0.6,0.2,0))
    seg2 = Segment(Pnt(0.6,0.2,0),Pnt(0.3,0.4,0))
    seg3 = Segment(Pnt(0.3,0.4,0),Pnt(0.5,0.4,0))
    seg4 = Segment(Pnt(0.5,0.4,0),Pnt(0.2,0.6,0))
    seg5 = Segment(Pnt(0.2,0.6,0),Pnt(0.4,0.6,0))
    seg6 = Segment(Pnt(0.4,0.6,0),Pnt(0.1,0.8,0))
    seg7 = Segment(Pnt(0.1,0.8,0),Pnt(0.3,0.8,0))
    seg8 = Segment(Pnt(0.3,0.8,0),Pnt(0,1,0))
    wire = Wire([seg1,seg2,seg3,seg4,seg5,seg6,seg7,seg8])
    mirrored_wire = wire.Mirror(Axis((0,0,0), Y))
    Green = Face(Wire([wire, mirrored_wire]))
    trunk.faces.name="trunk_inner"
    trunk.col = (0.55, 0.27, 0.07)
    Green.faces.name="tree_inner"
    trunk.edges.Min(Y).name = "trunk"
    trunk.edges.Min(X).name = "trunk"
    trunk.edges.Max(X).name = "trunk"
    tree = Glue([trunk,Green])
    tree.edges.Nearest((0.6,0.2,0)).name = "tree"
    tree.edges.Nearest((-0.6,0.2,0)).name = "tree"
    tree.edges.Nearest((0.3,0.4,0)).name = "tree"
    tree.edges.Nearest((-0.3,0.4,0)).name = "tree"
    tree.edges.Nearest((0.5,0.4,0)).name = "tree"
    tree.edges.Nearest((-0.5,0.4,0)).name = "tree"
    tree.edges.Nearest((0.2,0.6,0)).name = "tree"
    tree.edges.Nearest((-0.2,0.6,0)).name = "tree"
    tree.edges.Nearest((0.4,0.6,0)).name = "tree"
    tree.edges.Nearest((-0.4,0.6,0)).name = "tree"
    tree.edges.Nearest((0.1,0.8,0)).name = "tree"
    tree.edges.Nearest((-0.1,0.8,0)).name = "tree"
    tree.edges.Nearest((0.3,0.8,0)).name = "tree"
    tree.edges.Nearest((-0.3,0.8,0)).name = "tree"
    tree.edges.Nearest((0.001,1,0)).name = "tree"
    tree.edges.Nearest((-0.001,1,0)).name = "tree"
    geometry = OCCGeometry (tree, dim=2)
    return geometry

geo = ChristmasTreeGeometry()
mesh = Mesh ( geo . GenerateMesh ( maxh =0.12))