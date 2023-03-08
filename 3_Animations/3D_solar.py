from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def init():
    global MatShn
    LightPos = [1,0,0,1]
    LightAmb = [0.2,0.2,0.2,1]
    LightDiff = [1,1,1,1]
    LightSpec = [1,1,1,1 ]
    MatShn = [128]
    glLightfv(GL_LIGHT0,GL_POSITION,LightPos)
    glLightfv(GL_LIGHT0,GL_DIFFUSE,LightDiff)
    glLightfv(GL_LIGHT0,GL_AMBIENT,LightAmb)
    glLightfv(GL_LIGHT0,GL_SPECULAR,LightSpec)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  
    glClearColor(0.0,0.0,0.0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1,0.1,50)
    gluLookAt(15,15,15,0,0,0,0,1,0)
    glEnable(GL_DEPTH_TEST)
def planet(dist_from_sun,radius,angle,r,g,b):
    global MatShn
    glLoadIdentity()
    MatAmb = [r,g,b,1]
    MatDif = [r,g,b,1]
    MatSpec = [r,g,b,1]
    glMaterialfv(GL_FRONT,GL_AMBIENT,MatAmb)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,MatDif)
    glMaterialfv(GL_FRONT,GL_SPECULAR,MatSpec)
    glMaterialfv(GL_FRONT,GL_SHININESS,MatShn)
    glColor(1,1,1)
    glutSolidTorus(0.01,dist_from_sun,30,30)
    glColor(r,g,b)
    glRotate(angle,0,0,1)
    glTranslate(dist_from_sun,0,0)
    glutSolidSphere(radius,30,30)
angle = [0, 0,0,0,0,0,0,0]
def display1():
    global angle
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #sun
    MatAmb = [10,10,0,1]
    MatDif = [1,1,0,1]
    MatSpec = [1,1,0,1]
    glMaterialfv(GL_FRONT,GL_AMBIENT,MatAmb)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,MatDif)
    glMaterialfv(GL_FRONT,GL_SPECULAR,MatSpec)
    glMaterialfv(GL_FRONT,GL_SHININESS,MatShn)
    glColor(1.0,1.0,0.0)
    glutSolidSphere(1,30,30)
    #mercury
    planet(3,0.2,angle[0],1,0,0)
    angle[0] = (angle[0] % 360)+ 0.3
    glutSwapBuffers()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE|GLUT_DEPTH)
    glutInitWindowSize(800,800)
    glutCreateWindow(b'Wire Cube')
    glutDisplayFunc(display1)
    glutIdleFunc(display1)
    init()
    glutMainLoop()
main()