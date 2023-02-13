class Brush:
    def render(self,path,img_draw):
        '''
        render the path
        :param path:
        :return:
        '''
        raise NotImplementedError

    def __init__(self,setting=None):
        if setting:
            for key in setting:
                setattr(self,key,setting[key])
