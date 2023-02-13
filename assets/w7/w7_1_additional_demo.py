from utility import *
def one_circle_rotate():
    main_img,main_img_draw,center,width,height=makeImg()
    r=3
    p0=translate(center,50,50)
    p1=translate(p0,r,r)
    rotation_ct=20
    degree=360/rotation_ct
    color=random_rgb()
    img_list=[]
    for iter in range(rotation_ct):
        p0_rot=rotate(p0,center,iter*degree)
        p1_rot=(
                    p0_rot[0]+r,
                    p0_rot[1]+r
                )
        main_img_draw.ellipse(
            [p0_rot,p1_rot],
            fill=color
        )
        img,img_draw,center,width,height=makeImg()
        img_draw.ellipse(
            [p0_rot,p1_rot],
            fill=color
        )
        img_list.append(img)

    # main_img.show()
    img_list[0].save(
            "output/rot_one_circle.gif",
            save_all=True,
            append_images=img_list[1:],
            duration=100,
            loop=0
    )

# one_circle_rotate()



def rotate_shapes(export_gif=False):
    width=500
    height=500
    center=[width/2,height/2]
    if export_gif:
        img_list=[]
    else:
        img,img_draw,center,width,height=makeImg()
    circle_count=random.randint(50,250)
    r_range=[10,40]
    rotation_ct=20
    degree=360/rotation_ct
    circle_list=[]
    for i in range(circle_count):
        p0=generate_random_pt(width,height)
        rx=random.randint(r_range[0],r_range[1])
        ry=random.randint(r_range[0],r_range[1])
        p1=(
            p0[0]+rx,
            p0[1]+ry
        )
        rgb=random_rgb()
        circle_list.append(
            [p0,rx,ry,rgb]
        )

    for iter in range(rotation_ct):
        if export_gif:
            img,img_draw,center,width,height=makeImg()
            img_list.append(img)
        for circle_info in circle_list:
            p0,rx,ry,rgb=circle_info
            p0_rot=rotate(p0,center,iter*degree)
            p1_rot=(
                    p0_rot[0]+rx,
                    p0_rot[1]+ry
                )
            img_draw.ellipse(
                    [p0_rot,p1_rot],
                    fill=rgb
            )
    if export_gif:
        img_list[0].save(
            "output/rot_shape.gif",
            save_all=True,
            append_images=img_list[1:],
            duration=100,
            loop=0
        )
    else:
        img.show()
# rotate_shapes(export_gif=True)
