import math
import rhinoscriptsyntax as rs

dblA = -8.0
dblB = 8.0
dblStep = 1
for x in rs.frange(dblA, dblB, dblStep):
    y = math.sinh(x)
    rs.AddPoint([x, y, 0])