"""
espiral
"""


def setup():
    size(1000, 1000, P2D)
    background(255)
    noLoop()

def draw():
    stroke(0)
    smooth(8)
    x0 = width / 2
    y0 = height / 2
    l = 50
    for n in xrange(2):
        a = asin(sqrt(n)/ 2)
        x1 = x0 + l * cos(a)
        y1 = y0 - l * sin(a)
        line(x0, y0, x1, y1)
         
        
        
        
    
