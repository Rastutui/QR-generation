from qr_template import save_colours_for_template_modules, save_format_info_modules
from qr_extra_data import *
from utils.CPoint import Point
from utils.helper import clear_all, fill_colour_for_module
from encoding import encode_data

def get_error_correction_bytes(qr, user_msg_bin):
    user_msg_decimal = []
    
    for i in range(8, len(user_msg_bin) + 1, 8):
        user_msg_decimal.append(int(user_msg_bin[i - 8:i], 2))

    key = (qr.version, qr.error_correction_lvl)
    num_of_correction_bytes = num_of_correction_bytes_dict[key]
    polynom_coeffs = generator_polynomial_coeffs[num_of_correction_bytes]
    
    new_lst = user_msg_decimal.copy()
    new_lst.extend([0] * (len(polynom_coeffs) - len(user_msg_decimal)))
    
    for i in range(len(user_msg_decimal)):
        new_lst.append(0)
        A = new_lst.pop(0)
        if A == 0:
            continue
        for index in range(len(polynom_coeffs)):
            B = (polynom_coeffs[index] + galois_field_inverse[A]) % 255
            new_lst[index] ^= galois_field[B]

    correction_bytes_decimal = new_lst[:num_of_correction_bytes]
    correction_bytes = ''.join(format(num, '08b') 
                               for num in correction_bytes_decimal)
    return correction_bytes


def get_remainder_bites(qr_version, user_msg_bin_length):
    if qr_version == 'Version 1 (21 x 21)':
        total_modules_for_data = 21 ** 2 - 64 * 3 - 15 * 2 - 1 - 5 * 2
    else:
        total_modules_for_data = 25 ** 2 - 64 * 3 - 15 * 2 - 1 - 9 * 2 - 5 ** 2

    num_of_remainder_bits = total_modules_for_data - user_msg_bin_length
    remainder_bits = '0' * num_of_remainder_bits
    return remainder_bits


def fill_format_info_modules(canvas, qr):
    key = (qr.error_correction_lvl, qr.mask_pattern)
    format_info_bites = codes_for_format_information[key] * 2
    for digit, point in zip(format_info_bites, qr.format_info):
        if digit == '1':
            fill_colour_for_module(canvas, qr, point, colour='black')
            qr.colour_for_module[point.x][point.y] = 'black'
        else:
            fill_colour_for_module(canvas, qr, point, colour='white')
            qr.colour_for_module[point.x][point.y] = 'white'


def fill_qr_template(canvas, qr):
    for x in range(1, qr.num_of_modules + 1):
        for y in range(1, qr.num_of_modules + 1):
            module_colour = qr.colour_for_module[x][y]
            if module_colour != -1:
                fill_colour_for_module(canvas, qr, Point(x, y), 
                                       colour=module_colour)


def fill_qr_data_modules(canvas, qr, user_msg_bin):
    i = 0
    point = Point(qr.num_of_modules, 1)
    step = 0
    fl_up = True
    while i < len(user_msg_bin):
        if (point in qr.modules_with_no_data
            or point in qr.format_info):
            point, fl_up = get_next_coords(qr, point, step, fl_up)
        else:
            if user_msg_bin[i] == '1':
                fill_colour_for_module(canvas, qr, point, colour='black')
                qr.colour_for_module[point.x][point.y] = 'black'
            else:
                fill_colour_for_module(canvas, qr, point, colour='white')
                qr.colour_for_module[point.x][point.y] = 'white'
            i += 1
            point, fl_up = get_next_coords(qr, point, step, fl_up)
        step += 1


def fill_qr(canvas, qr, user_msg_bin):
    fill_qr_template(canvas, qr)
    fill_format_info_modules(canvas, qr)
    fill_qr_data_modules(canvas, qr, user_msg_bin)


def generate_qr(canvas, qr_code):
    clear_all(qr_code)

    save_colours_for_template_modules(qr_code)
    save_format_info_modules(qr_code)

    user_msg_bin = encode_data(qr_code)
    user_msg_bin += get_error_correction_bytes(qr_code, user_msg_bin)
    user_msg_bin += get_remainder_bites(qr_code.version, len(user_msg_bin))

    fill_qr(canvas, qr_code, user_msg_bin)
    
    do_mask(canvas, qr_code)


def get_next_coords(qr, point, step, fl_up):
    x, y = point.x, point.y
    if fl_up:
        if y == qr.num_of_modules and step % 2 == 1:
            x, fl_up = x - 1, False
        elif step % 2 == 0:
            x -= 1
        else:
            x, y = x + 1, y + 1
    else:
        if x == 7:
            x -= 1 # для пропуска вертикального timing_pattern-а
        if y == 1 and step % 2 == 1:
            x, fl_up = x - 1, True
        elif step % 2 == 0:
            x -= 1
        else:
            x, y = x + 1, y - 1
    step += 1
    return (Point(x, y), fl_up) 


def inverse_colour(canvas, qr, point):
    x, y = point.x, point.y
    if qr.colour_for_module[x][y] == 'black':
        fill_colour_for_module(canvas, qr, point, colour='white')
    elif qr.colour_for_module[x][y] == 'white':
        fill_colour_for_module(canvas, qr, point, colour='black')


def do_mask(canvas, qr):
    masks = {
        'Mask Pattern 0': lambda x, y: (x + y) % 2,
        'Mask Pattern 1': lambda x, y: y % 2,
        'Mask Pattern 2': lambda x, y: x % 3,
        'Mask Pattern 3': lambda x, y: (x + y) % 3,
        'Mask Pattern 4': lambda x, y: (x // 3 + y // 2) % 2,
        'Mask Pattern 5': lambda x, y: (x * y) % 2 + (x * y) % 3,
        'Mask Pattern 6': lambda x, y: ((x * y) % 2 + (x * y) % 3) % 2,
        'Mask Pattern 7': lambda x, y: ((x + y) % 2 + (x * y) % 3) % 2
    }

    mask = masks[qr.mask_pattern]

    for x in range(qr.num_of_modules):
        for y in range(qr.num_of_modules):
            if mask(x, y) == 0:
                point = Point(x + 1, qr.num_of_modules - y)
                if (point not in qr.modules_with_no_data 
                    and point not in qr.format_info):
                    inverse_colour(canvas, qr, point)