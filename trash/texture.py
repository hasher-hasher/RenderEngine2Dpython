import pygame

from OpenGL.GL import *  # noqa


class Texture:
    def __init__(self, file_name=None, properties={}):
        # pygame surface object to store the image data
        self.surface = None

        # texture reference
        self.texture_reference = glGenTextures(1)

        self.properties = {
            "magFilter": GL_LINEAR,
            "minFilter": GL_LINEAR_MIPMAP_LINEAR,
            "wrap": GL_REPEAT
        }

        # overwrite default property values
        self.set_properties(properties)

        self.load_image(file_name)
        self.upload_image_to_gpu()

    # load an image fdata from a file
    def load_image(self, file_name):
        self.surface = pygame.image.load(file_name)

    def set_properties(self, props):
        for name, data in props.items():
            if name in self.properties.keys():
                self.properties[name] = data
            else:
                raise Exception("No property named: " + name)

    # upload pixel data into the GPU
    def upload_image_to_gpu(self):
        # store image dimension
        width = self.surface.get_width()
        height = self.surface.get_height()

        # convert image to string buffer
        pixel_data = pygame.image.tostring(self.surface, "RGBA", 1)

        # bind texture
        glBindTexture(GL_TEXTURE_2D, self.texture_reference)

        # send data to the texture object
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                     GL_UNSIGNED_BYTE, pixel_data)

        # mipmaps
        glGenerateMipmap(GL_TEXTURE_2D)

        # set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                        self.properties["magFilter"])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                        self.properties["minFilter"])
        # uv properties
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,
                        self.properties["wrap"])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                        self.properties["wrap"])
