from PIL import Image,ImageDraw

class Canvas:
    def export(self,file_format=".jpg"):
        self.img.save(self.output_loc+self.img_name+file_format)

    img_mode="RGB"
    img_draw_mode="RGB"
    bg_color = (255, 255, 255)
    width = 500
    height = 500
    output_loc = "output/"
    img_name = "test_img"

    def __init__(self,settings=None):
        '''
        Create an image
        :param width:
        :param height:
        :param output_loc:
        :param img_name:
        '''
        if settings:
            for key in settings:
                setattr(self,key,settings[key])
        self.center = [self.width / 2, self.height / 2]
        self.img = Image.new(self.img_mode, (self.width, self.height), color=self.bg_color)
        self.img_draw = ImageDraw.Draw(self.img,self.img_draw_mode)