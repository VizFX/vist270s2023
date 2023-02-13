from PIL import Image,ImageDraw

class Canvas:
    def export(self,file_format=".jpg"):
        self.img.save(self.output_loc+self.img_name+file_format)
    def __init__(self,width=500,height=500,output_loc="output/",img_name="test_img",bg_color=(255,255,255)):
        '''
        Create an image
        :param width:
        :param height:
        :param output_loc:
        :param img_name:
        '''
        self.width=width
        self.height=height
        self.output_loc=output_loc
        self.img_name=img_name
        self.center = [width / 2, height / 2]
        self.img = Image.new("RGB", (width, height), color=bg_color)
        self.img_draw = ImageDraw.Draw(self.img)