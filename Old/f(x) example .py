import math
import rhinoscriptsyntax as rs

xstart = -10.0
xstop = 10.0
xstep = 1
for x in rs.frange(xstart, xstop, xstep):
    y = x**2
    rs.AddPoint([x, y, 0])
