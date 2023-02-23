from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
def hut():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(50,50)
    glVertex2f(-50,50)
    glVertex2f(-50,-50)
    glVertex2f(50,-50)
    glEnd()
    glutSwapBuffers()
def animate(temp):
    glRotate(-1,1,0,0)
    glutTimerFunc(10, animate, 0)
    glutPostRedisplay()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Shapes")
    glutDisplayFunc(hut)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()
main()