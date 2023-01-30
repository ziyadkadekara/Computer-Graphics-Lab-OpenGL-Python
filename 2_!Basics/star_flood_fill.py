from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import numpy as np

WINDOW_SIZE =500
pointsize=5
sys.setrecursionlimit(1000000)



def set_pixel(x,y,fill_color=(0,0,0)):
    glColor3f(*fill_color)
    glPointSize(pointsize)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def get_pixel(x,y):
     pixel = glReadPixels(x,WINDOW_SIZE-y,1,1,GL_RGB,GL_FLOAT)
     return np.array([round(x,1) for x in pixel[0][0]])

def flood_fill(x,y,new_color,old_color):
     color=get_pixel(x,y)
     if all(color==old_color):
        set_pixel(x,y,new_color)
        flood_fill(x+pointsize,y,new_color,old_color)
        flood_fill(x,y+pointsize,new_color,old_color)
        flood_fill(x-pointsize,y,new_color,old_color)
        flood_fill(x,y-pointsize,new_color,old_color)

def mouse_click(button,state,x,y):
      if button==GLUT_LEFT_BUTTON and state == GLUT_DOWN:
          print(x,y)
          flood_fill(x,y,[1,1,0],get_pixel(x,y))
          
      
def star():
     #glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(0.0,1,0.0)
     gluOrtho2D(0, WINDOW_SIZE , WINDOW_SIZE , 0)
     glPointSize(10)
     glLineWidth(5)
     glBegin(GL_LINES)
     glVertex2f(50,250)
     glVertex2f(200,200)
     glVertex2f(200,200)
     glVertex2f(250,50)
     glVertex2f(250,50)
     glVertex2f(300,200)
     glVertex2f(300,200)
     glVertex2f(450,250)
     glVertex2f(450,250)
     glVertex2f(300,300)
     glVertex2f(300,300)
     glVertex2f(250,450)
     glVertex2f(250,450)
     glVertex2f(200,300)
     glVertex2f(200,300)
     glVertex2f(50,250)
    
     glEnd()
     glFlush()
     

      
def main():
     glutInit()
     glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
     glutCreateWindow("Star")
     glutDisplayFunc(star)
     glutMouseFunc(mouse_click)
     glutMainLoop()
     
main()