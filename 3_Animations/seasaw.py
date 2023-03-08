from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math
wsize=500
def elipse(xc,yc,a,b):
    for theta in range(360):
        glBegin(GL_LINES)
        glVertex2f(xc/wsize,yc/wsize)
        glVertex2f((a*math.cos(math.radians(theta))+xc)/wsize ,(b*math.sin(math.radians(theta))+yc)/wsize)
        glEnd()
coordinates=[[0,0],[400,400]]
coordinates1=[[0,0],[-400,400]]
steps=0
def display():
    global coordinates,coordinates1,steps
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(coordinates[0][0]/wsize,coordinates[0][1]/wsize)
    glVertex2f(coordinates[1][0]/wsize,coordinates[1][1]/wsize)
    glVertex2f(coordinates1[0][0]/wsize,coordinates1[0][1]/wsize)
    glVertex2f(coordinates1[1][0]/wsize,coordinates1[1][1]/wsize)
    time.sleep(.01)
    coordinates[1][1]=100*math.sin(math.radians(steps))
    coordinates1[1][1]=-100*math.sin(math.radians(steps))
    glEnd()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(-200/wsize,-200/wsize)
    glVertex2f(200/wsize,-200/wsize)
    glEnd()
    elipse(400,coordinates[1][1],50,20)
    elipse(-400,coordinates1[1][1],50,20)
    glFlush()
    steps+=1
def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutCreateWindow("Line animation")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()
main()