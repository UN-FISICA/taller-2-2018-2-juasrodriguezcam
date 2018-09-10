# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:03:00 2018

@author: Juan
"""

import turtle as t
from math import cos, sin,  radians as rad

nnll=int(input('Por favor de el número de lados del polígono: '))

aacc=180/(nnll)
aaii=180*(nnll-2)/nnll
ll=100/nnll
rr=abs((ll/2)/sin(rad(aacc)))
aapp=abs(rr*cos(rad(aacc)))
jj=1
vvx=50
vvy=50
cc=0

t.setup(500, 500, 0, 0)
t.screensize(500, 500)

t.hideturtle()

while cc < 4:
    t.penup()
    t.goto(vvx,vvy)
    t.seth(270)
    t.forward(aapp)
    t.pendown()
    while jj <= nnll+1:
        if jj==1:
            t.left(90)
            t.fd(ll/2)
        else:
            t.left(180-aaii)
            t.fd(ll)
        jj += 1
    if cc==0:
        vvx=(-1)*vvx
    if cc==1:
        vvy=(-1)*vvy
    if cc==2:
        vvx=(-1)*vvx
    jj=1
    cc +=1
    
t.done()
t.bye()