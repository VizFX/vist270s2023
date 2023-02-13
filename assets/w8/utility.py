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
def rotate_around_pt(P,O,theta_degree):
    theta=math.radians(theta_degree)
    x0,y0=P
    xc,yc=O
    x1=(x0-xc)*math.cos(theta)-(y0-yc)*math.sin(theta)+xc
    y1=(x0-xc)*math.sin(theta)+(y0-yc)*math.cos(theta)+yc
    return x1,y1

def makeImg(width=500,height=500,bg_color=(255,255,255)):
    center=[width/2,height/2]
    img=Image.new("RGB",(width,height),color=bg_color)
    img_draw=ImageDraw.Draw(img)
    return img,img_draw,center,width,height


##########################################
def findMidPt(p0,p1):
    return ((p0[0]+p1[0])/2,(p0[1]+p1[1])/2)
def translatePoint(pt,tx,ty):
    return (pt[0]+tx,pt[1]+ty)
def scalePointAccordingToCenter(p,center,scale,scaleY=None):
    if scaleY is  None:
        scaleY=scale
    scaleX=scale
    scalePoints=[p[0]*scaleX,p[1]*scaleY]
    translateX=(1-scaleX)*center[0]
    translateY=(1-scaleY)*center[1]
    return (scalePoints[0]+translateX,scalePoints[1]+translateY)


def makeGif(img_list,addr,duration=40,loop=0):
    img_list[0].save(
            addr,
            save_all=True,
            append_images=img_list[1:],
            loop=loop,
            duration=duration
    )

