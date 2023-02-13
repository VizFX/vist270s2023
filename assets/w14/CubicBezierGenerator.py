#from ParametricGenerator import ParametricGenerator

class CubicBezierGenerator(ParametricGenerator):
    two_dim=True
    p0=0,0
    p3=100,0
    p1=25,25
    p2=75,-25
    t_total_step=40
    def calculate_one_dim(self,v0,v1,v2,v3,t):
        one_minus_t=1-t

        return one_minus_t**3*v0+3*one_minus_t**2*t*v1+3*one_minus_t*t**2*v2+t**3*v3

    def produce_design(self):
        t_step=1/self.t_total_step
        coordinates=[]

        self.center=(0,0) if self.two_dim else (0,0,0)
        dim_ct=2 if self.two_dim else 3
        for i in range(self.t_total_step+1):
            t=i*t_step
            point=[]
            for dim_i in range(dim_ct):
                v=self.calculate_one_dim(
                    self.p0[dim_i],
                    self.p1[dim_i],
                    self.p2[dim_i],
                    self.p3[dim_i],
                    t
                )
                point.append(v)
            coordinates.append(tuple(point))
        return coordinates


