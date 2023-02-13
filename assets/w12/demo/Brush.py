class Brush:
    stroke_color=(0,0,0)
    def render_2D(self,path,img_draw):
        '''
        render the path
        :param path:
        :return:
        '''
        img_draw.line(
            path,
            fill=self.stroke_color
        )
    def render_3D(self,path):
        cmds.curve(p=path)


    def __init__(self,setting=None):
        if setting:
            for key in setting:
                setattr(self,key,setting[key])