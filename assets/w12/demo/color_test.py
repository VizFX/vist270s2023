from Canvas import Canvas
from RectangleBrush import RectangleBrush
def process_file_name(name):
    name=name.replace("(","_")
    name=name.replace(")","_")
    name=name.replace("/","_")
    return name

def transparency_test(start_alpha,canvas,rect_brush,rgba):
    total_step = 10
    alpha_gap = int((255 - start_alpha) / total_step)
    margin = 20
    shape_gap = int((canvas.width / 2 - margin * 2) / total_step)
    for i in range(1, 1 + total_step):
        path = [(shape_gap * i, shape_gap * i), (canvas.width - shape_gap * i, canvas.height - shape_gap * i)]
        rect_brush.render_2D(
            path,
            canvas.img_draw
        )
        rgba[-1] += alpha_gap
        rect_brush.stroke_color = tuple(rgba)

def rgb_color_test(canvas,rect_brush,rgba_original):
    margin = 20
    stripe_ct=10
    rect_width=(canvas.width-2*margin)/stripe_ct
    rect_height=canvas.height-2*margin
    x=margin
    overlap_height=canvas.height/5
    hor_rect=[

            (margin,canvas.height/2-overlap_height/2),(canvas.width-margin,canvas.height/2+overlap_height/2)

    ]
    rect_brush.render_2D(
        hor_rect,
        canvas.img_draw
    )
    rect_brush.stroke_color = tuple(rgba_original)

    rgba=rgba_original.copy()
    for i in range(stripe_ct):
        rgba[0]=(rgba[0]+10)%255
        rgba[1]=(rgba[1]+1)%255
        rgba[2]=(rgba[1]+5)%255
        path = [
            (x, margin),
            (x+rect_width, margin+rect_height)
        ]
        rect_brush.render_2D(
            path,
            canvas.img_draw
        )

        rect_brush.stroke_color = tuple(rgba)
        x+=rect_width

def produce_one_image(color_info_str,start_alpha=30):

    color_info=color_info_str.split(",")
    name_idx=0
    name=color_info[name_idx]
    # hex_idx=1
    # r_idx=2
    # g_idx=3
    # b_idx=4
    #
    # rgb=(
    #     int(float(color_info[r_idx][:-1])/100*255),
    #     int(float(color_info[g_idx][:-1])/100*255),
    #     int(float(color_info[b_idx][:-1])/100*255)
    # )

    rgba=[int(float(color_info[i][:-1])/100*255) for i in range(2,5)]
    rgba.append(start_alpha)
    rgba_t=tuple(rgba)

    canvas=Canvas(
        {
            # "img_mode":"RGBA",
            # "bg_color":(255,255,255,255),
            "img_draw_mode":"RGBA",
            "img_name":process_file_name(name)
        }
    )
    rect_brush=RectangleBrush({"stroke_color":rgba_t})
    # transparency_test(start_alpha, canvas, rect_brush, rgba)
    rgb_color_test(canvas,rect_brush,rgba)

    # canvas.export()
    canvas.img.show()
def extract_and_produce():
    with open ("color_data.csv","r") as data_file:
        data=data_file.read()

    lines=data.split("\n")
    for i,line in enumerate(lines):
        if i<10:
            continue
        # print(i,line)
        produce_one_image(line,start_alpha=150)
        return

extract_and_produce()

