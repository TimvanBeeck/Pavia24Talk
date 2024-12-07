# ------------------------------ LOAD LIBRARIES -------------------------------
#from netgen.geom2d import SplineGeometry
from ngsolve import *
from netgen.occ import * 
import os
from christmastree import ChristmasTreeGeometry

import matplotlib.cm as cm
ngsglobals.msg_level = 2

#For a Structured Grid
#from ngsolve.meshes import *

#Run:
# python3 drawmesh.py
# latexmk -pdf drawmesh.tex
# Delete mesh.tex before changing the mesh

# ----------------------------- DATA & PARAMETERS -----------------------------
lowerleft, upperright = (-1.1, -1.1), (1.1, 1.1)
h_max = 0.19
filename = "mesh.tex"

# ----------------------------------- MESH ------------------------------------
#geo = SplineGeometry()
#geo.AddRectangle(lowerleft, upperright, bc=1)
#mesh = Mesh(geo.GenerateMesh(maxh=h_max, quad_dominated=False) )

#r = 3-1

#Structured Grid
#mesh = MakeStructured2DMesh(quads=False, nx=2**r, ny=2**r,mapping = lambda x,y: (2*x-1,2*y-1))


#Structured Grid flipped triangles
#mesh = MakeStructured2DMesh(quads=False, nx=2**r, ny=2**r,mapping = lambda x,y: (2*x-1,2*y-1),flip_triangles=True)


#Unstructured Grid
#square = SplineGeometry()
#square.AddRectangle((-1.0, -1.0), (1.0, 1.0))
#ngmesh = square.GenerateMesh(maxh=1)
#mesh = Mesh(ngmesh)

#for i in range(r):
    #ngmesh.Refine()

#mesh = Mesh(ngmesh)

#Circle geometry
#output is not curved... maybe because we draw lines?
#maxh = 0.5**(r)
#geo = SplineGeometry()
#geo.AddCircle(c=(0,0),r=1,bc="circle")
#ngmesh = geo.GenerateMesh(maxh=maxh)
#Note that the mesh is not structured anymore, can we do this?
#mesh = Mesh(ngmesh)
#Curving the boundary, use degree high enough
#mesh.Curve(7)

#for maxh in [0.25,0.15,0.05]:
#mesh = Mesh(unit_square.GenerateMesh(maxh=maxh))
#wp = WorkPlane()
#wp.MoveTo(0,0).LineTo(1,0).LineTo(1,1).LineTo(2,1).LineTo(2,2).LineTo(0,2).LineTo(0,0).Close()
#geo=OCCGeometry(wp.Face(),dim=2)
#mesh = Mesh(geo.GenerateMesh(maxh=maxh))

geo = ChristmasTreeGeometry()
mesh = Mesh ( geo . GenerateMesh ( maxh =0.12))

# ------------------------- DRAW AND COLOUR ELEMENTS --------------------------

os.system('rm mesh.tex')

fid = open(filename, "a")
# skiped_els = []
for el in mesh.Elements():

    verts = [mesh.ngmesh.Points()[v.nr + 1] for v in el.vertices]
    #fid.write("\\draw[fill={:}]".format("els_bnd"))
    fid.write("\\draw[fill=none, draw=black!75]")
    for p in verts:
        fid.write("({:.5f},{:.5f}) --".format(p[0], p[1]))
    fid.write(" cycle;\n")

#For unit square
#fid.write("\\draw[black,line width=0.15pt] (0,0) -- (1,0) -- (1,1) -- (0,1) -- cycle;\n")
fid.write("\\draw[black,line width=0.2pt] (-0.2,0.2) -- (-0.2,0) -- (0.2,0) -- (0.2,0.2);\n")
fid.write("\\draw[black,line width=0.2pt] (0.2,0.2) -- (0.6,0.2) -- (0.3,0.4) -- (0.5,0.4) -- (0.2,0.6) -- (0.4,0.6) -- (0.1,0.8) -- (0.3,0.8) -- (0,1);\n")
fid.write("\\draw[black,line width=0.2pt] (-0.2,0.2) -- (-0.6,0.2) -- (-0.3,0.4) -- (-0.5,0.4) -- (-0.2,0.6) -- (-0.4,0.6) -- (-0.1,0.8) -- (-0.3,0.8) -- (0,1);\n")


fid.close()

os.system('pdflatex drawmesh.tex')
#os.system('cp drawmesh.pdf Lshapemesh_h{}.pdf'.format(maxh))