from utility import *


def multiple_dots():
    img,img_draw,center,width,height=makeImg()
    pair_ct=20
    tx=200
    ty=-100
    radius=10

    for i in range(pair_ct):
        P=generate_random_pt(width,height)
        Q=translate(P,tx,ty)
        point_info=[
            [P,(0,0,255)],
            [Q,(255,0,255)]
        ]
        for pt_info in point_info:
            pt,color=pt_info
            draw_circle(pt,radius,img_draw,fill=color)

    show = img.show()
def translation_animation():

    startPt=(100,100)
    tx=400
    ty=300
    step_ct=10
    tx_step=tx/step_ct
    ty_step=ty/step_ct
    radius=10
    img_lst=[]
    for iter in range(step_ct):
        #generate an image that has the dot in the correct location
        pt=translate(
            startPt,
            iter*tx_step,
            iter*ty_step
        )

        img,img_draw,center,width,height=makeImg()
        draw_circle(
            pt,
            img_draw=img_draw,
            radius=radius,
            fill=(255,0,255)
        )
        img_lst.append(img)

        # img.save(
        #     "output/ta_"+str(iter)+".jpg"
        # )
    # print(img_lst)
    img_lst[0].save(
        "output/test.gif",
        append_images=img_lst[1:],
        save_all=True,
        duration=50,
        loop=0
    )

# translation_animation()

def scale_demo():
    img,img_draw,center,width,height=makeImg()
    r=45

    hor_line=[
        (0,height/2),
        (width,height/2)
    ]
    vert_line=[
        (width/2,0),
        (width/2,height)
    ]
    img_draw.line(hor_line,fill=(0,0,0))
    img_draw.line(vert_line,fill=(0,0,0))
    #before scale
    A=(width/2,height/2)
    B=translate(A,r*2,r*2)
    img_draw.ellipse(
        [A,B],
        fill=None,
        outline=(0,0,255)
    )
    scale_factor=2
    #scale according to origin
    A_p=scale_pt(A,center,scale_factor,scale_factor)
    B_p=scale_pt(B,center,scale_factor,scale_factor)

    img_draw.ellipse(
        [A_p,B_p],
        fill=None,
        outline=(0,255,255)
    )
    circle_center=translate(A,r,r)
    A_p2=scale_pt(A,circle_center,scale_factor,scale_factor)
    B_p2=scale_pt(B,circle_center,scale_factor,scale_factor)

    img_draw.ellipse(
        [A_p2,B_p2],
        fill=None,
        outline=(255,0,255)
    )

    img.show()
