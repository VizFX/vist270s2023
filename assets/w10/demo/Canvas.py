from PIL import Image, ImageDraw
# handle all canvas information
# hold properties
# handle export

class Canvas:
    def export(self,file_type=".jpg"):
        self.img.save(
            self.output_loc+self.name+file_type
        )
    def __init__(self,width=500,height=500,bg_color=(255,255,255),output_loc="output/",name="canvas"):
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.center=[self.width/2,self.height/2]
        self.output_loc=output_loc
        self.name=name
        self.img=Image.new(
            "RGB",
            (self.width,self.height),
            color=self.bg_color
        )
        self.img_draw=ImageDraw.Draw(
            self.img
        )

