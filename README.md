# PyShader: Python + OpenGL Template

## Overview
PyShader is a basic shader template designed to integrate GLSL (OpenGL Shading Language) with Pygame. This template provides a simple yet comprehensive example of how to render basic shapes using vertex and fragment shaders in OpenGL within a Pygame window. It's ideal for those who are beginning to learn about computer graphics or for anyone interested in simple OpenGL integrations with Python.

## Features
- Basic setup of a Pygame window with OpenGL context.
- Example of vertex and fragment shaders in GLSL.
- Creation and rendering of a simple triangle.
- Clean and commented code for easy understanding and modification.

## Requirements
- Python
- Pygame
- PyOpenGL
- Pycharm (Recommended)

## Setup and Installation
To run this template, ensure you have the above requirements installed. You can install Pygame and PyOpenGL using pip:

```
pip install pygame PyOpenGL
```

## Usage
Run the script in your preferred Python environment. This will open a window displaying a red triangle rendered using OpenGL. The program is set up to handle window close events gracefully.

## Code Structure
- `VERTEX_SHADER`: GLSL code for the vertex shader. It processes vertex positions and transforms them to clip coordinates.
- `FRAGMENT_SHADER`: GLSL code for the fragment shader. It sets the color of each pixel fragment. Currently set to red.
- `main()`: Initializes the Pygame window, sets up OpenGL context, compiles shaders, and runs the render loop.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

## Author
- Noah Kahn - December 15, 2023
