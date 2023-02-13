from Brush import Brush

class RectBrush(Brush):
    def render_2D(self,path,img_draw):
        p0=path[0]
        x0,y0=p0
        p1=path[-1]
        x1,y1=p1

        rect=[
            (x0,y0),
            (x1,y0),
            (x1,y1),
            (x0,y1),
            (x0,y0)
        ]
        img_draw.line(
            rect,
            fill=self.stroke_color
        )
