import sys

from OpenGL import GL


class OpenGLUtils:
    @staticmethod
    def initialize_shader(shader_code: str, shader_type) -> None:
        # pprint(GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION).decode("utf-8").split())
        # specify opengl version and requirements

        # if mac, ignore the extension
        if sys.platform == 'darwin':
            shader_code = "#version 120\n" + shader_code
        else:
            extension = "#extension GL_ARB_shading_language_420pack: require\n"
            shader_code = "#version 130 \n" + extension + shader_code

        # create empty shader object and return reference value
        shader_ref = GL.glCreateShader(shader_type)
        # store source code in the shader
        GL.glShaderSource(shader_ref, shader_code)
        # compile shader code stored in shader
        GL.glCompileShader(shader_ref)

        # query weather the compilation was successful
        compile_sucessful = GL.glGetShaderiv(shader_ref, GL.GL_COMPILE_STATUS)
        if not compile_sucessful:
            # retrieve error message
            error_message = GL.glGetShaderInfoLog(
                shader_ref
            )
            # free memory
            GL.glDeleteShader(shader_ref)
            # convert byte string to char string
            error_message = "\n" + error_message.decode("utf-8")
            # raise error
            raise Exception(error_message)

        # compilation was successful
        return shader_ref

    @staticmethod
    def initialize_program(vertex_shader_code, fragment_shader_code):
        # compile shaders and store references
        vertex_shader_ref = OpenGLUtils.initialize_shader(
            vertex_shader_code,
            GL.GL_VERTEX_SHADER
        )
        fragment_shader_ref = OpenGLUtils.initialize_shader(
            fragment_shader_code,
            GL.GL_FRAGMENT_SHADER
        )
        # create empty program object
        program_ref = GL.glCreateProgram()

        # attach previously compiled shaders
        GL.glAttachShader(program_ref, vertex_shader_ref)
        GL.glAttachShader(program_ref, fragment_shader_ref)

        # link the shaders together
        GL.glLinkProgram(program_ref)

        # query if linking was successful
        link_sucess = GL.glGetProgramiv(
            program_ref,
            GL.GL_LINK_STATUS
        )
        if not link_sucess:
            # retrieve error message
            error_message = GL.glGetProgramInfoLog(program_ref)
            # free memory
            GL.glDeleteProgram(program_ref)
            # convert byte string to char string
            error_message = "\n" + error_message.decode("utf-8")
            # raise error
            raise Exception(error_message)

        return program_ref
