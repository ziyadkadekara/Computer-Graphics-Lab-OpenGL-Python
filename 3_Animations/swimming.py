from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

wsize=1000
x_ref=0

def init():
    gluOrtho2D(-wsize,wsize,-wsize,wsize)

def circle(x,y,r):
    glBegin(GL_POLYGON)
    for theta in range(360):
        glVertex2f(r*math.cos(math.radians(theta))+x,r*math.sin(math.radians(theta))+y)
    glEnd()

def display():
    global x_ref
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,1)
    x_ref-=.05
    glBegin(GL_POLYGON)
    glVertex2f(-wsize,0)
    glVertex2f(wsize,0)
    glVertex2f(wsize,-wsize)
    glVertex2f(-wsize,-wsize)
    glEnd()

    glLineWidth(7)
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    
    glVertex2f(x_ref,0)
    glVertex2f(x_ref+500,0)

    glVertex2f(x_ref,0)
    glVertex2f(x_ref+150*math.cos(math.radians(x_ref)),-150*math.sin(math.radians(x_ref)))

    glVertex2f(x_ref,0)
    glVertex2f(x_ref-150*math.cos(math.radians(x_ref)),150*math.sin(math.radians(x_ref)))

    glVertex2f(x_ref+500,0)
    glVertex2f(x_ref+650,150*math.sin(math.radians(x_ref)))

    glVertex2f(x_ref+500,0)
    glVertex2f(x_ref+650,-150*math.sin(math.radians(x_ref)))


    glEnd()

    circle(x_ref-50,0,50)

    glFlush()


def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutCreateWindow("Swimming")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()

main()