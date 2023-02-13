from PIL import Image, ImageDraw
import random,math

def random_rgb():
    return (
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )
def generate_random_pt(width,height):
    # x >0 and x<width
    x=random.uniform(0,width)
    # y> 0 and y<height
    y=random.uniform(0,height)
    return x,y
def random_line(width,height):
    line=[
        generate_random_pt(width,height),
        generate_random_pt(width,height)
    ]
    return line
def draw_circle(A,radius,img_draw,fill=(0,0,255)):
    B=A[0]+radius,A[1]+radius
    img_draw.ellipse([A,B],fill=fill)
def rotate(P,O,theta_degree):
    theta=math.radians(theta_degree)
    x0,y0=P
    xc,yc=O
    x1=(x0-xc)*math.cos(theta)-(y0-yc)*math.sin(theta)+xc
    y1=(x0-xc)*math.sin(theta)+(y0-yc)*math.cos(theta)+yc
    return x1,y1
def makeImg(width=500,height=500,bg_color=(200,200,255)):
    center=[width/2,height/2]
    img=Image.new("RGB",(width,height),color=bg_color)
    img_draw=ImageDraw.Draw(img)
    return img,img_draw,center,width,height
def translate(P,tx,ty):
    x0,y0=P
    Q=(
        x0+tx,
        y0+ty
    )
    return Q

def scale_pt(pt,scale_center,scale_x,scale_y):
    scaled_pt=(
        pt[0]*scale_x,
        pt[1]*scale_y
    )
    tx=(1-scale_x)*scale_center[0]
    ty=(1-scale_y)*scale_center[1]
    return translate(scaled_pt,tx,ty)


