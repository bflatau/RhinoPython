import math
import rhinoscriptsyntax as rs


dblA = -8.0
dblB = 8.0
dblStep = 0.25
for x in rs.frange(dblA, dblB, dblStep):
    y = 2*math.sin(x)
    rs.AddPoint([x, y, 0])

mpoints = rs.ObjectsByType(1, True)


mcurves = rs.AddCurve(mpoints)

rs.DeleteObjects(mpoints)

rs.CopyObject( mcurves, [0,1,0] )