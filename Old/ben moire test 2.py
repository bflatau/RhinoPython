import math
import rhinoscriptsyntax as rs


mpoints = rs.GetObjects("Select Points", 1)

mcurves = rs.AddCurve(mpoints)

rs.DeleteObjects(mpoints)

dblA = -8.0
dblB = 8.0
dblStep = 0.25
for x in rs.frange(dblA, dblB, dblStep):
    y = 2*math.sin(x)

rs.CopyObject( mcurves, [x,y,0] )