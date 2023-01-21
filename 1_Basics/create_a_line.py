
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def init2D(r,g,b):

    glClearColor(r, g, b, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)

def display():

  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.0, 1.0, 0.0) #color of the line
  glBegin(GL_LINES) #for line
  glVertex2i(10, 10) #inital point vertex
  glVertex2i(490, 490) #final point vertex
  glEnd()
  glFlush()

def view():
    viewport = (GLint * 4)()
    glGetIntegerv(GL_VIEWPORT, viewport)
    print("Viewport dimensions: x=", viewport[0], ", y=", viewport[1], ", width=", viewport[2], ", height=", viewport[3])


def main():

  glutInit(sys.argv) #initialize GLUT
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(500, 500)
  glutInitWindowPosition(0,0)
  glutCreateWindow("line")
  init2D(0.0, 0.0, 0.0)
  glutDisplayFunc(display)
  view()
  glutMainLoop()

main()