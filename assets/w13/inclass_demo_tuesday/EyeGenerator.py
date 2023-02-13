from Brush import Brush
from CubicBezierCurveGenerator import CubicBezierCurveGenerator
import math,random
from utility import *

class EyeGenerator(Brush):
    top_eyelid_cp_l_p=[0.2,0.9]
    cp_rot_rg=[-60,60]

    def get_random_val_from_rg(self,key):
        rg=getattr(self,key)
        return random.uniform(
            rg[0],
            rg[1]
        )
    def top_eye_lid(self,p0,p3):

        random_for_p1=random.uniform(
            self.top_eyelid_cp_l_p[0],
            self.top_eyelid_cp_l_p[1]
        )
        rot_p1=random.uniform(
            self.cp_rot_rg[0],
            self.cp_rot_rg[1]
        )
        p1=p0[0],p0[1]-random_for_p1*self.dist
        p1_rot=rotate_around_pt(
            p1,
            p0,
            rot_p1
        )
        random_for_p2=random.uniform(
            self.top_eyelid_cp_l_p[0],
            self.top_eyelid_cp_l_p[1]
        )

        rot_p2=random.uniform(
            self.cp_rot_rg[0],
            self.cp_rot_rg[1]
        )
        p2=p3[0],p3[1]-random_for_p2*self.dist
        p2_rot=rotate_around_pt(
            p2,
            p3,
            rot_p2
        )
        self.cbcg.p0=p0
        self.cbcg.p1=p1_rot
        self.cbcg.p2=p2_rot
        self.cbcg.p3=p3

        self.top_eye_lid=self.cbcg.produce_design()


    def render_2D(self,path,img_draw):
        p0,p3=path
        self.dist=math.dist(p0,p3)
        self.cbcg=CubicBezierCurveGenerator()
        self.top_eye_lid(p0,p3)
        img_draw.line(
            self.top_eye_lid,
            fill=self.stroke_color
        )
        # implement
        return
