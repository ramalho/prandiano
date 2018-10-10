"""
espiral
"""


def setup():
    size(1000, 1000)
    background(255)


def draw():
    stroke(0)
    x0 = width / 2
    y0 = width / 2
    l = 10
    a = 0
    for _ in xrange(15):
        line(x0, y0, l * cos(a), l * sin(a)
    
