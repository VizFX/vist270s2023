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




# width=500
# height=500
# img=Image.new(
#         mode="RGB",
#         size=(width,height),
#         color=(200,215,255)
#     )
#
# img_draw=ImageDraw.Draw(img)
def draw_circle(A,radius,img_draw,fill=(0,0,255)):
    B=A[0]+radius,A[1]+radius
    img_draw.ellipse([A,B],fill=fill)
# O=(200,200)
# P=(300,305)
# radius=10
# draw_circle(P,radius,img_draw)
# draw_circle(O,radius,img_draw,fill=(0,255,0))
#
# theta=-30
def rotate(P,O,theta_degree):
    theta=math.radians(theta_degree)
    x0,y0=P
    xc,yc=O
    x1=(x0-xc)*math.cos(theta)-(y0-yc)*math.sin(theta)+xc
    y1=(x0-xc)*math.sin(theta)+(y0-yc)*math.cos(theta)+yc
    return x1,y1

# T=rotate(P,O,theta)
# draw_circle(T,radius,img_draw,fill=(255,0,0))
#
# print(T)
# img.show()
def pattern():
    width=500
    height=500
    img=Image.new(
        mode="RGB",
        size=(width,height),
        color=(200,215,255)
    )
    starting_pt=(0,0)
    ending_pt=(width,height)

    # line=[starting_pt,ending_pt]


    img_draw=ImageDraw.Draw(img)

    line_ct=random.randint(10,30)
    threshold=200
    blue=(0,0,255)
    red=(255,0,0)
    for i in range(line_ct):
        line=random_line(width,height)
        line_length=math.dist(
            line[0],
            line[1]
        )
        if line_length> threshold:
            color_to_use=red
            #creat a new line that is 90 degrees from the original line
            rot_center=line[0]
            new_line=[
                #rotated line[0],
                rotate(line[0],rot_center,90),
                #rotated line[1]
                rotate(line[1],rot_center,90)
            ]
            img_draw.line(
            new_line,
            fill=(0,255,0)
        )
        else:
            color_to_use=blue
        #if line is longer than 200
        # color it red
        # else, blue
        img_draw.line(
            line,
            fill=color_to_use
        )

    img.show()
pattern()
