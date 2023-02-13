from Canvas import Canvas
from Brush import Brush
from CubicBezierGenerator import CubicBezierGenerator
import math

canvas=Canvas()
base_brush=Brush()
gap=50
start_x=100
length=300
start_y=250
cbg=CubicBezierGenerator(
    {
        "p0":(start_x,start_y),
        "p3":(start_x+length,start_y),
        "p1":(start_x,start_y-gap),
        "p2":(start_x+length,start_y+gap),
    }
)

for i in range(0):
    curve=cbg.produce_design()
    base_brush.stroke_color=(0,0,0)
    base_brush.render_2D(
        path=curve,
        img_draw=canvas.img_draw
    )
    base_brush.stroke_color=(0,0,255)
    base_brush.render_2D(
        path=[cbg.p0,cbg.p3],
        img_draw=canvas.img_draw
    )
    base_brush.stroke_color=(0,255,0)
    base_brush.render_2D(
        path=[cbg.p0,cbg.p1],
        img_draw=canvas.img_draw
    )
    base_brush.render_2D(
        path=[cbg.p1,cbg.p2],
        img_draw=canvas.img_draw
    )
    base_brush.render_2D(
        path=[cbg.p2,cbg.p3],
        img_draw=canvas.img_draw
    )
    cbg.p1=cbg.p1[0],cbg.p1[1]-gap
    cbg.p2=cbg.p2[0],cbg.p2[1]+gap
canvas.img.show()
