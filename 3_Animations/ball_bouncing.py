from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
wsize=1000
x_ref=-wsize
y_ref=0
angle=0
def clear_screen():
    gluOrtho2D(-wsize,wsize,-wsize,wsize)   
def circle(x,y,r):
    global angle
    glBegin(GL_LINES)
    for theta in range(0,360,1):
         glVertex2f(x,y)
         glVertex2f(r*math.cos(math.radians(theta))+x,r*math.sin(math.radians(theta))+y)
    glEnd()
    glLineWidth(5)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(r*math.cos(math.radians(angle))+x,r*math.sin(math.radians(angle))+y)
    glVertex2f(r*math.cos(math.radians(angle+180))+x,r*math.sin(math.radians(angle+180))+y)

    glVertex2f(r*math.cos(math.radians(angle+90))+x,r*math.sin(math.radians(angle+90))+y)
    glVertex2f(r*math.cos(math.radians(angle+270))+x,r*math.sin(math.radians(angle+270))+y)
    glEnd()
def display():
        global x_ref,y_ref,angle
        angle-=0.07
        glClear(GL_COLOR_BUFFER_BIT)  
        glColor3f(1.0,0.0,0.0)
        x_ref+=0.1
        y=abs(math.sin(math.radians(x_ref)))*abs((wsize- x_ref))/4
        circle(x_ref,y,80)    
        glFlush()
def main():
    glutInit(sys.argv)
    glutInitWindowSize(wsize,wsize)
    glutCreateWindow("ball bounce")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    clear_screen()
    glutMainLoop()
main()