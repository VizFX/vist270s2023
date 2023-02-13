# defines my pixel system


def my_pixel_system(gray_scale_val,img_draw, x, y, pixel_size):
    '''

    Given a gray-scale value,
    Produce a drawing in the designed location that as the rendering of that pixel.

    :param gray_scale_val: an integer that represents the grayscale value. 0 is black, 255 is white.
    :param img_draw: img_draw object used to perform the drawing
    :param x: top left corner of the original pixel
    :param y: top left corner of the original pixel
    :param pixel_size: the width and height of a pixel
    :return:
    '''

    #TODO
    # example: draw a rectangle with the given gray color.
    coor=[
        (x,y),
        (x+pixel_size,y),
        (x+pixel_size,y+pixel_size),
        (x,y+pixel_size),
        (x,y)
    ]
    img_draw.polygon(coor,gray_scale_val)




