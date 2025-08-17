def fill_colour_for_module(canvas, qr, point, colour):
    x, y = point.x, point.y
    shift = (700 - 600) / 2
    
    x_min = (x - 1) * qr.module_length
    y_min = (qr.num_of_modules - y) * qr.module_length

    x_max = x * qr.module_length
    y_max = (qr.num_of_modules - y + 1) * qr.module_length
    
    canvas.create_rectangle(x_min + shift, y_min + shift, 
                            x_max + shift, y_max + shift, 
                            fill=colour, outline="")
    

def clear_all(qr_code):
    qr_code.format_info.clear()
    qr_code.modules_with_no_data.clear()
    for x in range(1, qr_code.num_of_modules + 1):
        for y in range(1, qr_code.num_of_modules + 1):
            qr_code.colour_for_module[x][y] = -1
