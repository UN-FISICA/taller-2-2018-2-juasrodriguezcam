# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:32:07 2018

@author: Juan
"""

import turtle as t
from math import sin, cos, radians as rad

nnpp=int(input('Por favor de el número de pisos de la pirámide: '))

t.setup(600, 600, 0, 0)
t.screensize(600, 600)

t.hideturtle()

aacc=180/(nnpp+2)
aaii=180*(nnpp)/(nnpp+2)
ll=10
rr=abs((ll/2)/sin(rad(aacc)))

def fver(nnll):
    aacc=180/(nnll)
    aaii=180*(nnll-2)/nnll
    ll=10
    rr=abs((ll/2)/sin(rad(aacc)))
    aapp=abs(rr*cos(rad(aacc)))
    jj=1
    
    t.penup()
    t.seth(270)
    t.forward(aapp)
    t.pendown()
    while jj <= nnll+1:
        if jj==1:
            t.left(90)
            t.fd(ll/2)
        elif jj==nnll+1:
            t.left(180-aaii)
            t.fd(ll)
            t.penup()
            t.bk(ll/2)
            t.left(90)
            t.fd(aapp)
            t.seth(0)
            t.pendown()
        else:
            t.left(180-aaii)
            t.fd(ll)
        jj += 1
    return()

def piso(nnpp,nnll):
    ccp=1
    while ccp<=nnpp:
        if ccp==nnpp:
            fver(nnll)
        else:
            fver(nnll)
            xxp=t.xcor()
            t.penup()
            t.setx(xxp-3*rr)
            t.pendown()
        ccp+=1
    return()

ccpir=1
t.penup()
t.sety(280)
t.pendown()
while ccpir <=nnpp:
    aall=t.ycor()
    t.penup()
    t.sety(aall-4*rr)
    t.setx(2*rr*(ccpir-1))
    t.pendown()
    piso(ccpir, ccpir+2)
    ccpir+=1

t.done()
t.bye()