from Brush import Brush
from CubicBezierCurveGenerator import CubicBezierCurveGenerator
import math,random
from utility import *
from RectBrush import RectBrush

class EyeGenerator(Brush):
    eyelid_cp_l_p=[0.2,0.9]
    cp_rot_rg=[-60,60]
    iris_r_perc=[0.3,0.4]
    pupil_perc=[0.2,0.9]
    p_side_ct=[3,12]
    db_eye_lid_y_dist_perc=[0.1,0.3]
    brow_y_dist_perc=[0.6,0.8]
    brow_length_range=[1.2,1.5]
    brow_rot_rg=[-180,180]

    def get_random_val_from_rg(self,key):
        rg=getattr(self,key)
        return random.uniform(
            rg[0],
            rg[1]
        )

    def generate_curve(self,direction, length_key, rotation_key):
        random_for_p1=self.get_random_val_from_rg(
            length_key
        )
        rot_p1=self.get_random_val_from_rg(
            rotation_key
        )
        p1=self.p0[0],self.p0[1]-direction*random_for_p1*self.dist
        p1_rot=rotate_around_pt(
            p1,
            self.p0,
            rot_p1
        )
        random_for_p2=self.get_random_val_from_rg(
            length_key
        )

        rot_p2=self.get_random_val_from_rg(
            rotation_key
        )
        p2=self.p3[0],self.p3[1]-direction*random_for_p2*self.dist
        p2_rot=rotate_around_pt(
            p2,
            self.p3,
            rot_p2
        )
        self.cbcg.p0=self.p0
        self.cbcg.p1=p1_rot
        self.cbcg.p2=p2_rot
        self.cbcg.p3=self.p3

        return self.cbcg.produce_design()
    def generate_eye_lid_curve(self,direction):
        '''
        return top or bottom eye lid curve
        :param direction:
        :return:
        '''
        return  self.generate_curve(
            direction,
            "eyelid_cp_l_p",
            "cp_rot_rg"
        )

    def generate_top_eye_lid(self):
        self.top_eye_lid=self.generate_eye_lid_curve(direction=1)
    def generate_db_eye_lid(self):
        curve=self.generate_eye_lid_curve(direction=1)
        y_translate=self.get_random_val_from_rg("db_eye_lid_y_dist_perc")*self.dist
        self.db_eye_lid=[
            translatePoint(pt,0,-y_translate) for pt in curve
        ]
        # for pt in curve:
        #     self.db_eye_lid.append(translatePoint(pt,0,-y_translate))
    def generate_brow(self):
        curve=self.generate_curve(
            1,"brow_length_range","brow_rot_rg"
        )
        y_translate=self.get_random_val_from_rg("brow_y_dist_perc")*self.dist
        self.brow=[
            translatePoint(pt,0,-y_translate) for pt in curve
        ]
        # for pt in curve:
        #     self.db_eye_lid.append(translatePoint(pt,0,-y_translate))


    def generate_bottom_eye_lid(self):
        self.bottom_eye_lid=self.generate_eye_lid_curve(direction=-1)
        self.bottom_eye_lid.reverse() #modifying the bottom_eye_lid list in place
        # self.bottom_eye_lid=self.bottom_eye_lid[::-1] # generate a new list

    def generate_iris_and_pupil(self):
        minX,maxX,minY,maxY=self.bbox
        w=maxX-minX
        h=maxY-minY
        center=(
            minX+w/2,
            minY+h/2
        )
        radius=h*self.get_random_val_from_rg("iris_r_perc")
        self.iris=makeUniformPolygon(
            center[0],center[1],radius,30
        )
        p_radius=radius*self.get_random_val_from_rg("pupil_perc")
        p_side_ct=int(self.get_random_val_from_rg("p_side_ct"))

        self.pupil=makeUniformPolygon(
            center[0],center[1],p_radius,p_side_ct
        )

    def render_2D(self,path,img_draw):
        self.p0,self.p3=path
        self.dist=math.dist(self.p0,self.p3)
        self.cbcg=CubicBezierCurveGenerator()
        self.generate_top_eye_lid()
        self.generate_bottom_eye_lid()
        self.eyelid=self.top_eye_lid+self.bottom_eye_lid
        self.bbox=getBbox(self.eyelid)

        self.generate_iris_and_pupil()
        self.generate_db_eye_lid()
        self.generate_brow()
        content_to_draw=[
            self.top_eye_lid,
            self.bottom_eye_lid,
            self.iris,
            self.pupil,
            self.db_eye_lid,
            self.brow
        ]
        for shape in content_to_draw:
            img_draw.line(
                shape,
                fill=self.stroke_color
            )

        # rb=RectBrush()
        #
        # rb.render_2D(
        #     [(minX,minY),(maxX,maxY)],
        #     img_draw
        # )
        # implement
        return
