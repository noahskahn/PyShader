# Basic shader template for integrating GLSL & Pygame

# Designed by Noah Kahn
# December 15, 2023

# Additional Info:
# MacOS 12.5 (21G72), PyOpenGL 3.1.7, pygame 2.5.2
# PyCharm 2023.3.1 CE #PC-233.11799.298


# Import libraries:
# Pygame for window & event management
# OpenGL for rendering
# ctypes for handling C data types in Python.
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from ctypes import c_float


# Vertex Shader code in GLSL (OpenGL Shading Language).
# Transforms vertex positions to clip coordinates.
# 'vertices' is the input vector for vertex positions.
# gl_Position is the output clip coordinates for each vertex.
VERTEX_SHADER = """

// comment

#version 330
in vec3 vertices;
void main() {
    gl_Position = vec4(vertices, 1.0);
}

"""


# Fragment Shader code in GLSL.
# Sets the color of each pixel fragment.
# Outputs 'fragColor', color of pixels, set to red.
FRAGMENT_SHADER = """

// comment

#version 330
out vec4 fragColor;
void main() {
    fragColor = vec4(1.0, 0.0, 0.0, 1.0); // Red color
}

"""

def main():
    pygame.init()
    display = (800, 600)
    # Initialize Pygame and set up window dimensions.

    # Some OpenGL specifications cause versions are silly
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # Make it have double buffering
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Create Vertex Array Object (VAO)
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # Triangle vertices
    vertices_list = [
        -0.5, -0.5, 0.0,
         0.5, -0.5, 0.0,
         0.0,  0.5, 0.0
    ]

    # Translate to OpenGL-speak
    vertices = (c_float * len(vertices_list))(*vertices_list)

    # Create Vertex Buffer Object (VBO)
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW)

    # Set up vertex array attributes.
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    # Compile!
    shader = compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )

    # Activate!
    glUseProgram(shader)

    # Loop for whenever the window is running
    running = True
    while running:

        # Quit function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Render (Clear, draw, update)
        glClear(GL_COLOR_BUFFER_BIT)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        pygame.display.flip()

    # Delete leftover bits
    glDeleteVertexArrays(1, [VAO])
    glDeleteBuffers(1, [VBO])
    glDeleteProgram(shader)

    # Exit
    pygame.quit()

if __name__ == "__main__":
    main()
    # Actually run it!