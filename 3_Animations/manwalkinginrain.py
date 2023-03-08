from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random
wsize=1000
x_ref=0
y_ref=0
mazha = []
def rain(x_ref):
    global mazha   
    if x_ref % 15 ==0:
        mazha.append([wsize*random.random(),wsize])
    for m in mazha:
        circle(m[0],m[1],10,(0.,0,1))
        circle(-m[0],m[1],10,(0,1,1))
    for i in range(len(mazha)):
        mazha[i][1]-=10
def circle(x,y,r,color=(1,1,1)):
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for theta in range(360):
        glVertex2f(r*math.cos(math.radians(theta))+x,r*math.sin(math.radians(theta))+y)
    glEnd()
def semiCircle(x,y,r):
    glBegin(GL_LINES)
    for theta in range(180):
        glVertex2f(x,y)
        glVertex2f(r*math.cos(math.radians(theta))+x,r*math.sin(math.radians(theta))+y)
    glEnd()
def Clear_screen():
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
def display():
    global x_ref,y_ref
    x_ref+=.5
    glClearColor(0,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    rain(x_ref)
    glLineWidth(7)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(x_ref,0)
    glVertex2f(x_ref,-500)
    glVertex2f(x_ref,0)
    glVertex2f(150+x_ref,-150)
    glVertex2f(x_ref,0)
    glVertex2f(-150+x_ref,-150)
    glVertex2f(x_ref,-500)
    glVertex2f(x_ref+150*math.sin(math.radians(x_ref)),-650)
    glVertex2f(x_ref,-500)
    glVertex2f(x_ref-150*math.sin(math.radians(x_ref)),-650)
    glEnd()
    circle(x_ref,50,50)
    glColor3f(1,0,1)
    glBegin(GL_LINES)
    glVertex2f(x_ref+150,-150)
    glVertex2f(x_ref+150,300)
    glEnd()
    semiCircle(x_ref+150,300,300)
    glFlush()
def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutCreateWindow("man")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    Clear_screen()
    glutMainLoop()
main()