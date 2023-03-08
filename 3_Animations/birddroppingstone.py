from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math

wsize=1000
x_ref=0

kallu=[]
deposited =[]

def draw_water():
    water_level=100
    global deposited
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(400,-750)
    glVertex2f(100,-750)
    glVertex2f(100,-750+len(deposited)*2)
    glVertex2f(400,-750+len(deposited)*2)
    glEnd()
    glColor3f(0,1,1)
    glBegin(GL_POLYGON)
    
    glVertex2f(100,-750+len(deposited)*2)
    glVertex2f(400,-750+len(deposited)*2)
    glVertex2f(400,-750+len(deposited)*2+water_level)
    glVertex2f(100,-750+len(deposited)*2+water_level)
    glEnd()
    
def drop():
    new_kallu=[]
    global kallu,x_ref

    if x_ref%70==0:

        kallu.append([280,0])

    for k in range(len(kallu)):
        glColor3f(0,0,0)
        ellipse(kallu[k][0],kallu[k][1],10,10)
        if kallu[k][1]<-750:
            deposited.append(kallu[k])
        else:
            kallu[k][1]-=1
            new_kallu.append(kallu[k])
            
    kallu = new_kallu

    

def clearscreen():
    gluOrtho2D(-wsize,wsize,-wsize,wsize)

def ellipse(xc,yc,a,b):
    glBegin(GL_POLYGON)
    for theta in range(360):
        glVertex2f(a*math.cos(math.radians(theta))+xc,b*math.sin(math.radians(theta))+yc)
    glEnd()
def triangle(x1,y1,x2,y2,x3,y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

def display():
    global x_ref
    x_ref+=1
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(100,-450)
    glVertex2f(400,-450)
    glVertex2f(400,-750)
    glVertex2f(100,-750)
    glEnd()
    glColor3f(0,1,0)
    ellipse(0,0,200,120)
    glColor3f(1,0,0)
    triangle(280,0,200,25,200,-25)
    glColor3f(1,1,1)
    ellipse(140,50,15,15)
    glColor3f(0,0,0)
    ellipse(140,50,7,7)
    glColor3f(0,0,1)
    triangle(-200,0,-300,50,-300,-50)
    drop()
    draw_water()
    glFlush()

def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutCreateWindow("kili")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    clearscreen()
    glutMainLoop()
main()