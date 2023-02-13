from utility import *

def expanding_circle(width=500,height=500,frame_ct=10,fill=(0,0,0),duration=100):

    start_radius=0.25*width
    end_radius=0.8*width
    step=(end_radius-start_radius)/frame_ct
    radius=start_radius
    frame_lst=[]
    for frame_idx in range(frame_ct):
        img, img_draw, center, width, height = makeImg(width, height)
        frame_lst.append(img)

        img_draw.ellipse(
            [
                (center[0]-radius,center[1]-radius),#A
                (center[0]+radius,center[1]+radius),#B
            ],
            fill=fill
        )
        radius +=step
    makeGif(
        frame_lst,
        "output/expanding_circle.gif",
        duration=duration
    )

# expanding_circle()

def rotating_polygon(side_ct,width=500,height=500,frame_ct=10,fill=(0,0,0),duration=100):
    radius=0.25*width
    frame_lst=[]
    base_polygon=[]
    center=width/2,height/2
    P=center[0],center[1]-radius
    rot_degree=360/side_ct
    for i in range(side_ct):
        theta=i*rot_degree
        base_polygon.append(
            rotate_around_pt(P=P,O=center,theta_degree=theta)
        )

    rotation_step=360/frame_ct
    for frame_idx in range(frame_ct):
        img, img_draw, center, width, height = makeImg(width, height)
        frame_lst.append(img)

        img_draw.polygon(
            [rotate_around_pt(pt,center,frame_idx*rotation_step) for pt in base_polygon],
            fill=fill
        )

    makeGif(
        frame_lst,
        "output/rot_polygon.gif",
        duration=duration
    )

# rotating_polygon(7)



