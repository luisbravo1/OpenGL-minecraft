# Instituto Tecnológico de Monterrey
# Challenge 2 (Transformations)
# Minecraft Scene done in pyOpenGL and pyGame
# Prof. Maria Raquel Landa
# Luis Gerardo Bravo  A01282014
# Hector de Luna      A01282272
# Jorge Arturo Torres A01176590


import pygame
from pygame.locals import *
from math import *

from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

from constants import *
import numpy as np


class Object3D:
    def __init__(self, parts, filename=""):
        self.img = None
        if filename is not "":
            self.img = Image.open(filename)
            self.img = self.img.convert("RGB")
            self.img_data = np.array(list(self.img.getdata()), np.int8)
        self.parts = parts
        self.vertsTmp = {}
        self.facesTmp = {}
        self.__text_flags = {}
        for value, part in self.parts.items():
            self.vertsTmp[value] = self.set_vertices(
                part["position"], part["size"], part["rotation"][0])
            size = len(self.vertsTmp[value]) - 8
            self.facesTmp[value] = []
            for face in surfaces:
                newface = []
                for ang in face:
                    newface.append(ang + size)
                self.facesTmp[value].append(tuple(newface))

    def set_vertices(self, position, size, r):
        new_vertices = []

        for vert in vertices:
            new_vert = []

            vert_x = vert[0]
            vert_y = vert[1]
            vert_z = vert[2]

            new_x = vert_x * size[0]
            new_y = vert_y * size[1]
            new_z = vert_z * size[2]

            new_vert.append(new_x)
            new_vert.append(new_y)
            new_vert.append(new_z)
            new_vertices.append(tuple(new_vert))

        return new_vertices

    def run(self, position, rotation, scale):
        glPushMatrix()
        if rotation > 1:
            glRotate(rotation, 0, 1, 0)
        if scale > 1:
            print(scale)
            glScaled(scale, scale, scale)
        glTranslate(position[0], position[1], position[2])
        for value, part in self.parts.items():
            if 'texture' in part.keys():
                print(value)
                self.__text_flags[value] = True
                self.read_texture()
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, self.texture_id[0])
                qobj = gluNewQuadric()
                gluQuadricTexture(qobj, GL_TRUE)
                glEnable(GL_TEXTURE_GEN_S)
                glEnable(GL_TEXTURE_GEN_T)

            glPushMatrix()
            glColor(part["color"])
            glTranslate(part["position"][0], part["position"]
                        [1], part["position"][2])
            if part["rotation"][0] != 0:
                glRotate(part["rotation"][0], part["rotation"][1],
                         part["rotation"][2], part["rotation"][3])
            glBegin(GL_QUADS)
            for face in self.facesTmp[value]:
                for ver in face:
                    glVertex3fv(self.vertsTmp[value][ver])
            glEnd()
            glPopMatrix()
        glPopMatrix()

    def read_texture(self):
        self.texture_id = [0] * 1
        glGenTextures(1, self.texture_id)
        print(self.texture_id)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                     self.img.size[0], self.img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, self.img_data)
        glDisable(GL_TEXTURE_2D)
