from Brush import Brush


class RectangleBrush(Brush):
    def render_2D(self,path,img_draw):
        p0=path[0]
        p1=path[-1]
        rect=[
            p0,
            (p1[0],p0[1]),
            p1,
            (p0[0],p1[1]),
            p0
        ]
        img_draw.polygon(
            rect,
            fill=self.stroke_color
        )