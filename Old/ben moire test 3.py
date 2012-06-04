import math
import rhinoscriptsyntax as rs

#x values
xstart = -20.0
xend = 20.0
xstep = 1

#y values
ystart = -10.0
yend = 10.0
ystep = 2

#note using rs.frange will let you use floats 
#using "range" requires all integers
for x in rs.frange(xstart, xend, xstep):
    for y in rs.frange(ystart, yend, ystep):
        rs.AddPoint([x, (y**2), 0])

#mpoints = rs.ObjectsByType(1, True)

#rs.CopyObject( mpoints, [0,20,0] )