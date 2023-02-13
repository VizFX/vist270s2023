from Canvas import Canvas
from EyeGenerator import EyeGenerator

canvas=Canvas()
eg=EyeGenerator()
p0=100,350
p3=400,350
eg.render_2D(
    [p0,p3],
    canvas.img_draw
)
canvas.img.show()
