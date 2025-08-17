from qr_extra_data import alpha_num_dict, total_max_data_in_bytes

def get_encoding_mode_bites(qr_code):
    encoding_modes = ['numeric', 'alphanumeric', 'binary']
    encoding_mode_bytes = ['0001', '0010', '0100']
    index = encoding_modes.index(qr_code.encoding_mode)
    return encoding_mode_bytes[index]


def get_user_msg_length_bites(qr_code):
    encoding_modes = ['numeric', 'alphanumeric', 'binary']
    user_msg_length_bytes_format = ['010b', '09b', '08b']
    index = encoding_modes.index(qr_code.encoding_mode)
    format_len = user_msg_length_bytes_format[index]
    return format(len(qr_code.user_msg), format_len)


def do_numeric_encoding(msg):
    chunk_len = 3
    binary_msg = '' 
    for i in range(len(msg) // chunk_len):
        chunk = msg[chunk_len * i:chunk_len * i + chunk_len]
        binary_msg += format(int(chunk), '010b')

    if (len(msg) % chunk_len == 1):
        binary_msg += format(int(msg[-1]), '04b')
    elif (len(msg) % chunk_len == 2):
        binary_msg += format(int(msg[-2:]), '07b')

    return binary_msg


def do_alphanumeric_encoding(msg):
    chunk_len = 2
    binary_msg = ''

    for i in range(len(msg) // chunk_len):
        chunk = msg[chunk_len * i:chunk_len * i + chunk_len]
        num = alpha_num_dict[chunk[0]] * 45 + alpha_num_dict[chunk[1]]
        binary_msg += format(num, '011b')    
    
    if len(msg) % chunk_len == 1:
        num = alpha_num_dict[msg[-1]]
        binary_msg += format(num, '06b')
    return binary_msg


def do_binary_encoding(msg):
    return ''.join(format(ord(char), '08b') for char in msg)


def get_encoding_user_msg(qr_code):
    encoding_msg = ''
    if qr_code.encoding_mode == 'numeric':
        encoding_msg = do_numeric_encoding(qr_code.user_msg)
    elif qr_code.encoding_mode == 'alphanumeric':
        encoding_msg = do_alphanumeric_encoding(qr_code.user_msg)
    else:
        encoding_msg = do_binary_encoding(qr_code.user_msg)
    return encoding_msg


def get_needed_zeroes(qr, msg_bin_length):
    """
    if user input is too short for current qr version 
    and error correction level, or(and) length of user input
    in binary form is not a multiple of 8
    """
    qr_ver_and_err_correction_lvl = (qr.version, qr.error_correction_lvl)
    max_capacity = total_max_data_in_bytes[qr_ver_and_err_correction_lvl]
    
    needed_bites = max_capacity * 8 - msg_bin_length
    needed_zeroes_num = min(needed_bites, 4)
    
    if (msg_bin_length + needed_zeroes_num) % 8 != 0:
        needed_zeroes_num += (8 - (msg_bin_length + needed_zeroes_num) % 8)
    return '0' * needed_zeroes_num


def get_padding_bytes(qr, msg_bin):
    """
    if user input after adding zeroes is still too short
    """
    qr_ver_and_err_correction_lvl = (qr.version, qr.error_correction_lvl)
    max_capacity = total_max_data_in_bytes[qr_ver_and_err_correction_lvl]
    pad_bytes = ['11101100', '00010001']
    padding_bytes = ''

    for i in range(max_capacity - len(msg_bin) // 8):
        padding_bytes += pad_bytes[i % 2]
    return padding_bytes


def encode_data(qr):
    user_msg_bin = ''
    user_msg_bin += get_encoding_mode_bites(qr)
    user_msg_bin += get_user_msg_length_bites(qr)
    user_msg_bin += get_encoding_user_msg(qr)
    user_msg_bin += get_needed_zeroes(qr, len(user_msg_bin))
    user_msg_bin += get_padding_bytes(qr, user_msg_bin)
    return user_msg_bin