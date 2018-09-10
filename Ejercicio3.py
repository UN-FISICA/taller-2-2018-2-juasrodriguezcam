# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:06:01 2018

@author: Juan
"""

import turtle as t
from math import sin, cos, radians as rad

nnll=int(input('Por favor de el número de lados del polígono: '))
nnlb=int(input('Por favor de el número de lados del polígono de base: '))

#Para la base
aacb=180/(nnlb)
aaib=180*(nnlb-2)/nnlb
llb=1000/nnlb
rr=abs((llb/2)/sin(rad(aacb)))
aapb=abs(rr*cos(rad(aacb)))

#Definición contadores
kk=1
ii=0

t.setup(600, 600, 0, 0)
t.screensize(600, 600)

t.hideturtle()

def fver(nnll):
    aacc=180/(nnll)
    aaii=180*(nnll-2)/nnll
    ll=100/nnll
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

t.penup()
t.seth(270)
t.fd(aapb)
t.pendown()
while ii<=nnlb:
    if ii == 0:
        t.penup()
        t.left(90)
        t.fd(llb/2)
        fver(nnll)
    elif ii == nnlb:
        while kk<=ii:
            t.left(180-aaib)
            kk +=1
        t.penup()
        t.fd(llb/2)
    else:
        while kk<=ii:
            t.left(180-aaib)
            kk+=1
        kk=1
        t.penup()
        t.fd(llb)
        fver(nnll)
    ii +=1
    
t.done()
t.bye()