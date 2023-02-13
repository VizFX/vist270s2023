from ParametricGenerator import ParametricGenerator

class CubicBezierCurveGenerator(ParametricGenerator):
    center=(0,0)
    two_dim=True
    p0=(0,0)
    p3=(100,0)
    p1=(25,-25)
    p2=(75,25)
    t_total_step=30
    def calculate(self,v0,v1,v2,v3,t):
        one_minus_t=1-t
        return one_minus_t**3*v0+3*one_minus_t**2*t*v1+3*one_minus_t*t**2*v2+t**3*v3

    def produce_design(self):
        t_step=1/self.t_total_step
        coordinates=[]
        for i in range(self.t_total_step+1):
            #generate the point on the curve
            t=i*t_step

            x=self.calculate(
                v0=self.p0[0],
                v1=self.p1[0],
                v2=self.p2[0],
                v3=self.p3[0],
                t=t
            )
            y=self.calculate(
                v0=self.p0[1],
                v1=self.p1[1],
                v2=self.p2[1],
                v3=self.p3[1],
                t=t
            )
            pt=(x,y)
            coordinates.append(pt)
        return coordinates
