#store all the test scripts
from Canvas import Canvas
from Brush import Brush
from VerticalBrush import VerticalBrush

from test_paths import *


canvas0=Canvas()
path=two_dim_paths["curves"][2]
vb0=VerticalBrush({"stroke_color":(0,255,0)})
vb0.render(
    path,
    canvas0.img_draw
)
vb1=VerticalBrush({
    "stroke_color":(255,0,0),
    "line_length":150,
    "mode":"random"
})
vb1.render(
    two_dim_paths["lines"][1],
    canvas0.img_draw
)
vb1.render(
    two_dim_paths["polygons"][1],
    canvas0.img_draw
)
canvas0.img.show()
# canvas0.export(file_type=".png")
