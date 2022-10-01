import turtle as t
import random as r

t.shape('turtle')

for i in range(30):
    lenghth = r.randrange(1, 101, 1)
    t.forward(lenghth)
    angle = r.randrange(-180, 181)
    t.right(angle)
t.done()