from utils.CPoint import Point

def save_modules_in_neighbourhood(qr, point, radius, colour):
    """
    radius=1: 8 nearest modules will be saving
    """
    x, y = point.x, point.y
    for delta_x in range(-radius, radius + 1):
        for delta_y in range(-radius, radius + 1):
            if abs(delta_x) < radius and abs(delta_y) < radius:
                continue
            if ((1 <= x + delta_x <= qr.num_of_modules) and
                (1 <= y + delta_y <= qr.num_of_modules)): 
                qr.colour_for_module[x + delta_x][y + delta_y] = colour


def save_colour_for_module(qr, point, colour):
    qr.colour_for_module[point.x][point.y] = colour


def save_colours_for_finder_patterns_modules(qr):
    finder_patterns_centers = [Point(4, 4), 
                               Point(4, qr.num_of_modules - 3), 
                               Point(qr.num_of_modules - 3, 
                                     qr.num_of_modules - 3)]
    
    for point in finder_patterns_centers:
        save_modules_in_neighbourhood(qr, point, radius=4, colour='white')
        save_modules_in_neighbourhood(qr, point, radius=3, colour='black')
        save_modules_in_neighbourhood(qr, point, radius=2, colour='white')
        save_modules_in_neighbourhood(qr, point, radius=1, colour='black')
        save_colour_for_module(qr, point, colour='black')


def save_colours_for_alignment_patterns(qr):
    if qr.version == 'Version 1 (21 x 21)':
        return 0
    
    alignment_pattern_center = Point(19, 7)
    save_modules_in_neighbourhood(qr, alignment_pattern_center, 
                                  radius=2, colour='black')
    save_modules_in_neighbourhood(qr, alignment_pattern_center, 
                                  radius=1, colour='white')
    save_colour_for_module(qr, alignment_pattern_center, colour='black')
    

def save_colours_for_timing_patterns(qr):
    finder_patterns = [Point(4, 4), Point(4, qr.num_of_modules - 3), 
                       Point(qr.num_of_modules - 3, qr.num_of_modules - 3)]
    
    # vertical timing_pattern
    x_const = finder_patterns[0].x + 3
    y_min = finder_patterns[0].y + 5
    y_max = finder_patterns[1].y - 5
    black_modules = [Point(x_const, y) for y in range(y_min, y_max + 1, 2)]
    white_modules = [Point(x_const, y) for y in range(y_min + 1, y_max, 2)]
    
    # horizontal timing_pattern
    y_const = finder_patterns[1].y - 3
    x_min = finder_patterns[1].x + 5
    x_max = finder_patterns[2].x - 5
 
    black_modules.extend([Point(x, y_const) for x in range(x_min, x_max + 1, 2)])
    white_modules.extend([Point(x, y_const) for x in range(x_min + 1, x_max, 2)])

    for black_point in black_modules:
        save_colour_for_module(qr, black_point, colour='black')
    for white_point in white_modules:
        save_colour_for_module(qr, white_point, colour='white')


def save_format_info_modules(qr):
    x_const = 9
    y_const = qr.num_of_modules - 8

    format_info_1 = [Point(x_const, y) for y in range(1, 8)]
    format_info_1.extend([Point(x, y_const) 
                         for x in range(qr.num_of_modules - 7, 
                                        qr.num_of_modules + 1)])

    format_info_2 = [Point(x, y_const) for x in range(1, 7)]
    format_info_2 += [Point(8, y_const)]
    format_info_2.extend([Point(x_const, y_const)] + 
                         [Point(x_const, y_const + 1)] + 
                         [Point(x_const, y) 
                         for y in range(qr.num_of_modules - 5, 
                                        qr.num_of_modules + 1)])
    
    qr.format_info.extend(format_info_1)
    qr.format_info.extend(format_info_2)



def save_all_no_data_modules(qr):
    """
    no_data_modules includes finder, alignment, timing patterns
    and always black point(9, 8) 
    """
    for x in range(1, qr.num_of_modules + 1):
        for y in range(1, qr.num_of_modules + 1):
            if qr.colour_for_module[x][y] != -1:
                qr.modules_with_no_data.append(Point(x, y))


def save_colours_for_template_modules(qr):
    save_colours_for_finder_patterns_modules(qr)
    save_colours_for_alignment_patterns(qr)
    save_colours_for_timing_patterns(qr)
    save_colour_for_module(qr, Point(9, 8), colour='black') # always black point
    save_all_no_data_modules(qr)