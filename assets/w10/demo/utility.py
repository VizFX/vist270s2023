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
def makeUniformPolygon(x, y, r, sideCt):
    points = []
    for i in range(sideCt):
        points.append((x+r * math.cos(2 * math.pi * i / sideCt), y+r * math.sin(2 * math.pi * i / sideCt)))
    points.append(points[0])
    return points

def makeGif(img_list,addr,duration=40,loop=0):
    img_list[0].save(
            addr,
            save_all=True,
            append_images=img_list[1:],
            loop=loop,
            duration=duration
    )

def makeRectPt(x,y,w,h):
    return [
        (x,y),
        (x+w,y),
        (x+w,y+h),
        (x,y+h),
        (x,y),
    ]

def getPtOnLineByDistPerc(x1,y1,x2,y2,distPerc):
    '''
    get a new ending point base on distance percent
    https://math.stackexchange.com/questions/175896/finding-a-point-along-a-line-a-certain-distance-away-from-another-point
    :param x1: starting point
    :param y1:
    :param x2:
    :param y2:
    :param distPerc:
    :return:
    '''


    pt1=[x1,y1]
    pt2=[x2,y2]
    v=[pt2[0]-pt1[0],pt2[1]-pt1[1]]
    pt3=(pt1[i]+distPerc*v[i] for i in range(2))

    return pt3