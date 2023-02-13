class ParametricGenerator:
    def produce_design(self):
        '''
        :return: a list of coordinate
        '''
        raise NotImplementedError
    def scale_and_translate(self,scale_factors,translates):
        '''
        generate a base design using the produce_design method. Scale this design according to the center using the scale factors. Then, translate the design using values stored in the translates variable.
        :param scale_factors:a sequence for scale factors. If the coordinates are 2D, the sequence should have 2 value (sx, sy).
        :param translates:
        :return:
        '''

        original_design=self.produce_design()
        transformed_design=[]
        # scaleX,scaleY=scale_factors
        # tx,ty=translates

        for pt in original_design:
            # pt=(0,0,0)
            transformed_pt=[]
            for dim_i in range(len(pt)):
                val_dim=pt[dim_i]
                scaled_v=val_dim*scale_factors[dim_i]
                translated_v=(1-scale_factors[dim_i])*self.center[dim_i]
                scaled_v+=translated_v
                s_t_value=scaled_v+translates[dim_i]
                transformed_pt.append(s_t_value)
            transformed_design.append( tuple(transformed_pt))
        return transformed_design
    def produce_2d_design(self):
        # todo:
        raise NotImplementedError
    def produce_3d_design(self,scale_factors,translates,add_dim):
        '''
        produce a scaled, translated 3d design.
        If the generator produces 2d designs, add a default value to the additional dimension.

        :param scale_factors:
        :param translates:
        :param add_dim:
        :return:
        '''
        design=self.scale_and_translate(scale_factors,translates)
        if self.two_dim:
            #add additional dim
            three_dim_design=[]
            for pt in design:
                #create a new point with the additional dimension
                new_pt=[pt[0],pt[1]]
                new_pt.insert(add_dim,self.dim_value)
                new_pt=tuple(new_pt)
                three_dim_design.append(new_pt)
            return three_dim_design
        return design



    dim_value=0
    def __init__(self,setting=None):
        if setting:
            for key in setting:
                value=setting[key]
                setattr(self,key,value)
