import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# from steve import *
from wolf import *
from objects import *


def main():
    xPos = 3
    zPos = 5
    yRot = 2
    scale = 1

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(40, (display[0]/display[1]), 0.1, 150.0)

    glTranslatef(0, -10, -80)

    steveObject = Object3D(steveAtt, {
                           "right_leg": "./textures/blue_pants.jpeg", "left_leg": "./textures/blue_pants.jpeg"})
    pigObject = Object3D(pigAtt, {"body": './textures/pink_text.jpeg'})
    wolfObject = Object3D(wolfAtt, {"body": "./textures/fur_texture.png"})
    skeletonObject = Object3D(skeletonAtt)
    treeObject1 = Object3D(treeAtt, {"leaves_lower": "./textures/tree.jpeg", "leaves_middle": "./textures/tree.jpeg",
                                     "leaves_upper1": "./textures/tree.jpeg", "leaves_upper2": "./textures/tree.jpeg"})
    treeObject2 = Object3D(treeAtt, {"leaves_lower": "./textures/tree.jpeg", "leaves_middle": "./textures/tree.jpeg",
                                     "leaves_upper1": "./textures/tree.jpeg", "leaves_upper2": "./textures/tree.jpeg"})
    treeObject3 = Object3D(treeAtt, {"leaves_lower": "./textures/tree.jpeg", "leaves_middle": "./textures/tree.jpeg",
                                     "leaves_upper1": "./textures/tree.jpeg", "leaves_upper2": "./textures/tree.jpeg"})
    treeObject4 = Object3D(treeAtt, {"leaves_lower": "./textures/tree.jpeg", "leaves_middle": "./textures/tree.jpeg",
                                     "leaves_upper1": "./textures/tree.jpeg", "leaves_upper2": "./textures/tree.jpeg"})
    treeObject5 = Object3D(treeAtt, {"leaves_lower": "./textures/tree.jpeg", "leaves_middle": "./textures/tree.jpeg",
                                     "leaves_upper1": "./textures/tree.jpeg", "leaves_upper2": "./textures/tree.jpeg"})
    treeObject6 = Object3D(treeAtt, {"leaves_lower": "./textures/tree.jpeg", "leaves_middle": "./textures/tree.jpeg",
                                     "leaves_upper1": "./textures/tree.jpeg", "leaves_upper2": "./textures/tree.jpeg"})
    mountainObject = Object3D(
        mountainAtt, {"floor_lower1": "./textures/dirt.jpg", "floor_lower2": "./textures/dirt.jpg", "floor_middle1": "./textures/dirt.jpg",
                      "floor_middle2": "./textures/dirt.jpg", "floor_middle3": "./textures/dirt.jpg", "floor_middle4": "./textures/dirt.jpg",
                      "floor_upper1": "./textures/dirt.jpg", "floor_upper2": "./textures/dirt.jpg", "floor_upper3": "./textures/dirt.jpg",
                      "floor_upper4": "./textures/dirt.jpg"})
    glRotatef(20, 2, 3, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xPos -= 1
                if event.key == pygame.K_RIGHT:
                    xPos += 1

                if event.key == pygame.K_UP:
                    zPos += 1
                if event.key == pygame.K_DOWN:
                    zPos -= 1

                if event.key == pygame.K_q:
                    yRot += 10
                if event.key == pygame.K_e:
                    yRot -= 10

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scale += 1

                if event.button == 5:
                    scale -= 1

            x = glGetDoublev(GL_MODELVIEW_MATRIX)
        # print(x)

            camera_x = x[3][0]
            camera_y = x[3][1]
            camera_z = x[3][2]

            glDepthFunc(GL_LESS)     # this is default
            glEnable(GL_DEPTH_TEST)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            steveObject.run([xPos, 0, zPos], yRot, scale)
            wolfObject.run([-1, -1, 0], 0, 0)
            pigObject.run([-10, -2, 0], 0, 0)
            skeletonObject.run([12, 0, -8], 0, 0)
            treeObject1.run([-20, 4, -6], 0, 0)
            treeObject2.run([-18, 5, -25], 0, 0)
            treeObject3.run([10, 6, -35], 0, 0)
            treeObject4.run([-22, 8, -45], 0, 0)
            treeObject5.run([-2, 4, -30], 0, 0)
            treeObject6.run([-9, 4, -43], 0, 0)
            mountainObject.run([0, 0, 0], 0, 0)

        pygame.display.flip()
        pygame.time.wait(10)


main()
