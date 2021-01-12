from core.base import Base
from core.open_gl_utils import OpenGLUtils
from OpenGL import GL


# render a single point
class Test(Base):
    def initialize(self):
        print("Initializing program ...")

        # create GPU program #

        # write vertex shader code
        vertex_shader_code = """
        void main()
        {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """

        fragment_shader_code = """
        void main()
        {
            gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
        }
        """

        self.program_ref = OpenGLUtils.initialize_program(
            vertex_shader_code,
            fragment_shader_code
        )

        # render settings (optional)
        GL.glPointSize(16)

    def update(self):
        # select program to use
        GL.glUseProgram(self.program_ref)

        # renders geometric objects using program
        GL.glDrawArrays(GL.GL_POINTS, 0, 1)


Test().run()
