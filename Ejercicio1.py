# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 09:34:03 2018

@author: Juan
"""

import turtle as t
t.setup(500, 500, 0, 0)
t.screensize(500, 500)

t.hideturtle()

t.penup()
t.goto(-55,55)

t.pendown()
t.setx(-45)
t.sety(45)
t.setx(-55)
t.sety(55)

t.penup()
t.goto(55,55)

t.pendown()
t.setx(45)
t.sety(45)
t.setx(55)
t.sety(55)

t.penup()
t.goto(-55,-55)

t.pendown()
t.setx(-45)
t.sety(-45)
t.setx(-55)
t.sety(-55)

t.penup()
t.goto(55,-55)

t.pendown()
t.setx(45)
t.sety(-45)
t.setx(55)
t.sety(-55)

t.done()
t.bye()