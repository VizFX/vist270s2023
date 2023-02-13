'''

stores predefined layout and helper functions

'''
import random
import turtle as T_mod

def make_rect(turtle,x,y,width,height):

    turtle.penup()
    turtle.home()
    turtle.setpos(x, y)
    turtle.pendown()
    for j in range(4):
        s=width if j%2==0 else height
        turtle.forward(s)
        turtle.right(90)



def generate_screen_turtle():
    '''
    generate turtle and screen
    :return:
    '''
    screen = T_mod.Screen()
    turtle=T_mod.Turtle()
    turtle.ht()
    screen.tracer(0)
    return turtle,screen

def setup_screen(screen):
    '''
    calculate width and height according to settings stored in layout_settings
    :param screen:
    :return: width,height,margin,col_ct,row_ct,margin,cell_size
    '''
    col_ct=layout_settings["col_ct"]
    cell_size=layout_settings["cell_size"]
    margin=layout_settings["margin"]
    row_ct=layout_settings["row_ct"]

    width=col_ct*cell_size+margin*2
    height= row_ct*cell_size+margin*2
    screen.setup(
        width,height
    )
    return width,height,margin,col_ct,row_ct,margin,cell_size

layout_settings={
    "col_ct":10,
    "row_ct":10,
    "cell_size":random.randint(30,80),
    "margin":50
}

def basic_setup(display_canvas_boundary):
    turtle, screen = generate_screen_turtle()
    width, height, margin, col_ct, row_ct, margin, cell_size = setup_screen(screen)
    start_x = -width / 2 + margin
    start_y = height / 2 - margin
    if display_canvas_boundary:
        make_rect(turtle, -width / 2, height / 2, width, height)
        make_rect(turtle, start_x, start_y, width - 2 * margin, height - 2 * margin)
    return turtle, screen,width, height, margin, col_ct, row_ct, margin, cell_size,start_x,start_y

def basic_grid_layout(tile_func,rotate_func,show_result,display_canvas_boundary,display_cell_boundary):

    turtle, screen, width, height, margin, col_ct, row_ct, margin, cell_size, start_x, start_y=basic_setup(display_canvas_boundary)

    for i in range(col_ct):
        x = cell_size * i - col_ct * cell_size / 2
        for j in range(row_ct):
            y = start_y - j * cell_size
            if display_cell_boundary:
                make_rect(turtle, x, y, cell_size, cell_size)
            tile_func(turtle, screen, x, y, cell_size, rotation=rotate_func(i,j))
    screen.update()
    if show_result:
        T_mod.done()


def layout0(tile_func,show_result=True,display_canvas_boundary=True,display_cell_boundary=True):
    '''
    basic grid layout without any rotation
    :param tile_func:
    :param show_result:
    :param display_canvas_boundary:
    :param display_cell_boundary:
    :return:
    '''

    rotate_func=lambda i,j:0
    basic_grid_layout(tile_func, rotate_func, show_result, display_canvas_boundary, display_cell_boundary)


def layout1(tile_func, show_result=True, display_canvas_boundary=True, display_cell_boundary=True):
    '''
    basic grid layout with alternating rotation
    :param tile_func:
    :param show_result:
    :param display_canvas_boundary:
    :param display_cell_boundary:
    :return:
    '''

    def rotate_func(i,j):
        if i%2==0:
            return 0 if j%2==0 else 45
        return 0 if j%2==1 else 45
    basic_grid_layout(tile_func, rotate_func, show_result, display_canvas_boundary, display_cell_boundary)


def layout2(tile_func, show_result=True, display_canvas_boundary=True, display_cell_boundary=True):
    '''
    a layout with randomized size, location, and rotation

    :param tile_func:
    :param show_result:
    :param display_canvas_boundary:
    :param display_cell_boundary:
    :return:
    '''
    turtle, screen, width, height, margin, col_ct, row_ct, margin, cell_size, start_x, start_y=basic_setup(display_canvas_boundary)
    rRange = [-10, 10]
    for i in range(col_ct):
        x = cell_size * i+start_x
        for j in range(row_ct):
            y = start_y-cell_size * j+ random.uniform(rRange[0], rRange[1])
            x_use = x + random.uniform(rRange[0], rRange[1])
            if display_cell_boundary:
                make_rect(turtle, x_use, y, cell_size, cell_size)
            tile_func(turtle, screen, x_use, y, cell_size, rotation=random.uniform(-90,90))
    screen.update()
    if show_result:
        T_mod.done()