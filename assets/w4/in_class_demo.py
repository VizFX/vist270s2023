import turtle as T_mod
def draw_rect(turtle,width,height,starting_pt,filled=False):
    # go to the starting point
    turtle.penup()
    turtle.goto(starting_pt[0],starting_pt[1])
    turtle.pendown()
    if filled:
        turtle.begin_fill()
    for i in range(4):
        if i%2==0:
            length=width
        else:
            length=height

        turtle.forward(length)
        # turn right 90 degrees
        turtle.right(90)
    if filled:
        turtle.end_fill()

def tile0(turtle,screen,x,y,cell_size,rotation=0):
    starting_pt=[x,y]
    draw_rect(
        turtle=turtle,
        width=cell_size,
        height=cell_size,
        starting_pt=starting_pt,
        filled=False
    )
    # draw the smaller rect
    # define the size by ratio to the larger rectangle
    r_to_R_ratio=0.5
    r=cell_size*r_to_R_ratio
    margin=(cell_size-r)/2
    # sp[0]+m,sp[1]-m
    sp_r=[
        starting_pt[0]+margin,
        starting_pt[1]-margin,
    ]

    draw_rect(
        turtle=turtle,
        width=r,
        height=r,
        starting_pt=sp_r,
        filled=True
    )



#generate a drawing grid
def canvas_building(turtle,screen,x,y,width,height):
    starting_pt=[x,y]
    draw_rect(
        turtle=turtle,
        width=width,
        height=height,
        starting_pt=starting_pt,
        filled=False
    )
    # draw the smaller rect
    # define the size by ratio to the larger rectangle
    r_to_R_ratio=0.5
    r_width=width*r_to_R_ratio
    r_height=height*r_to_R_ratio
    margin_width=(width-r_width)/2
    margin_height=(height-r_height)/2
    # sp[0]+m,sp[1]-m
    sp_r=[
        starting_pt[0]+margin_width,
        starting_pt[1]-margin_height,
    ]

    draw_rect(
        turtle=turtle,
        width=r_width,
        height=r_height,
        starting_pt=sp_r,
        filled=True
    )


screen=T_mod.Screen()
tina=T_mod.Turtle()
canvas_width=800
canvas_height=400
screen.setup(canvas_width,canvas_height)

canvas_building(tina,screen,-canvas_width/2,canvas_height/2,canvas_width,canvas_height)
T_mod.done()
