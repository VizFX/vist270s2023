from Brush import Brush
import random
class VerticalBrush(Brush):
    stroke_color=(0,0,255)
    line_length=30
    mode="fixed"
    def make_line(self,pt):
        if self.mode=="fixed":
            tp=(
                    pt[0],
                    pt[1]-self.line_length/2
                )
            bp=(
                    pt[0],
                    pt[1]+self.line_length/2
                )
        elif self.mode=="random":
            random_length=random.randint(10,100)
            tp=(
                    pt[0],
                    pt[1]-random_length/2
                )
            bp=(
                    pt[0],
                    pt[1]+random_length/2
                )

        return [tp,bp]
    def render(self,path,img_draw):
        '''
        Render a path by adding vertical lines to the image
        :param path:
        :param img_draw:
        :return:
        '''
        img_draw.line(
            path,
            fill=self.stroke_color
        )
        for pt in path:
            #draw a vertical line passing through this point
            # tp, bp

            line=self.make_line(pt)
            img_draw.line(
                line,
                fill=self.stroke_color
            )

