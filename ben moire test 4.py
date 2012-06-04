import math
import rhinoscriptsyntax as rs

#function describing initial line

pstart = -2.0
pstop = 2.0
pstep = 1
for x in rs.frange(pstart, pstop, pstep):
    y = math.sinh(x)
    rs.AddPoint([x, y, 0])

mpoints= rs.ObjectsByType(1)
#copy points to creat "piecewise function"

cpystart = 0
cpystop = 24.0
cpystep = 4
for x in rs.frange(cpystart, cpystop, cpystep):
	y = 0
        rs.CopyObject(mpoints, (x, y, 0))

#create line through function points

#mpoints= rs.ObjectsByType(1)
#if mpoints: rs.AddCurve(mpoints)

#delete the original points

#rs.DeleteObjects(mpoints)

#duplicate the curves

#mcurve= rs.ObjectsByType(4)

#cstart = 1
#cstop = 50.0
#cstep = 1
#for x in rs.frange(cstart, cstop, cstep):
    #rs.CopyObject(mcurve, (x, 0, 0))



