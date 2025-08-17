alpha_num_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 
    'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 
    'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 
    'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 
    'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 
    'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39,
    '+': 40, '-': 41, '.': 42, '/': 43, ':': 44
}


character_capacities = {
    ('Version 1 (21 x 21)', '7 % error correction (L)', 'numeric'): 41, 
    ('Version 1 (21 x 21)', '7 % error correction (L)', 'alphanumeric'): 25, 
    ('Version 1 (21 x 21)', '7 % error correction (L)', 'binary'): 17,
    ('Version 1 (21 x 21)', '15 % error correction (M)', 'numeric'): 34, 
    ('Version 1 (21 x 21)', '15 % error correction (M)', 'alphanumeric'): 20, 
    ('Version 1 (21 x 21)', '15 % error correction (M)', 'binary'): 14,
    ('Version 1 (21 x 21)', '25 % error correction (Q)', 'numeric'): 27, 
    ('Version 1 (21 x 21)', '25 % error correction (Q)', 'alphanumeric'): 16, 
    ('Version 1 (21 x 21)', '25 % error correction (Q)', 'binary'): 11,
    ('Version 1 (21 x 21)', '30 % error correction (H)', 'numeric'): 17, 
    ('Version 1 (21 x 21)', '30 % error correction (H)', 'alphanumeric'): 10, 
    ('Version 1 (21 x 21)', '30 % error correction (H)', 'binary'): 7,
    ('Version 2 (25 x 25)', '7 % error correction (L)', 'numeric'): 77, 
    ('Version 2 (25 x 25)', '7 % error correction (L)', 'alphanumeric'): 47, 
    ('Version 2 (25 x 25)', '7 % error correction (L)', 'binary'): 32,
    ('Version 2 (25 x 25)', '15 % error correction (M)', 'numeric'): 63, 
    ('Version 2 (25 x 25)', '15 % error correction (M)', 'alphanumeric'): 38, 
    ('Version 2 (25 x 25)', '15 % error correction (M)', 'binary'): 26,
    ('Version 2 (25 x 25)', '25 % error correction (Q)', 'numeric'): 48, 
    ('Version 2 (25 x 25)', '25 % error correction (Q)', 'alphanumeric'): 29, 
    ('Version 2 (25 x 25)', '25 % error correction (Q)', 'binary'): 20,
    ('Version 2 (25 x 25)', '30 % error correction (H)', 'numeric'): 34, 
    ('Version 2 (25 x 25)', '30 % error correction (H)', 'alphanumeric'): 20, 
    ('Version 2 (25 x 25)', '30 % error correction (H)', 'binary'): 14,
}


"""
total_max_data includes 4 bites encoding mode, 
(8, 9, or 10) bites of user input length, required zeroes
and user input in binary form
"""
total_max_data_in_bytes = { 
    ('Version 1 (21 x 21)', '7 % error correction (L)'): 19,
    ('Version 1 (21 x 21)', '15 % error correction (M)'): 16,
    ('Version 1 (21 x 21)', '25 % error correction (Q)'): 13,
    ('Version 1 (21 x 21)', '30 % error correction (H)'): 9,
    ('Version 2 (25 x 25)', '7 % error correction (L)'): 34,
    ('Version 2 (25 x 25)', '15 % error correction (M)'): 28,
    ('Version 2 (25 x 25)', '25 % error correction (Q)'): 22,
    ('Version 2 (25 x 25)', '30 % error correction (H)'): 16,
}


num_of_correction_bytes_dict = {
    ('Version 1 (21 x 21)', '7 % error correction (L)'): 7,
    ('Version 1 (21 x 21)', '15 % error correction (M)'): 10,
    ('Version 1 (21 x 21)', '25 % error correction (Q)'): 13,
    ('Version 1 (21 x 21)', '30 % error correction (H)'): 17,
    ('Version 2 (25 x 25)', '7 % error correction (L)'): 10,
    ('Version 2 (25 x 25)', '15 % error correction (M)'): 16,
    ('Version 2 (25 x 25)', '25 % error correction (Q)'): 22,
    ('Version 2 (25 x 25)', '30 % error correction (H)'): 28,
}

# key - number of correction bytes required
generator_polynomial_coeffs = {
    7: [87, 229, 146, 149, 238, 102, 21],
    10: [251, 67, 46, 61, 118, 70, 64, 94, 32, 45],
    13: [74, 152, 176, 100, 86, 100, 106, 104, 130, 218, 206, 140, 78],
    16: [120, 104, 107, 109, 102, 161, 76, 3, 91, 191, 147, 169, 182, 194, 225, 120],
    17: [43, 139, 206, 78, 43, 239, 123, 206, 214, 147, 24, 99, 150, 39, 243, 163, 136],
    22: [210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98, 80, 219, 
         134, 160, 105, 165, 231],
    28: [168, 223, 200, 104, 224, 234, 108, 180, 110, 190, 195, 147, 205, 27, 232, 
         201, 21, 43, 245, 87, 42, 195, 212, 119, 242, 37, 9, 123]
}


codes_for_format_information = {
    ('7 % error correction (L)', 'Mask Pattern 0') : '111011111000100', 
    ('7 % error correction (L)', 'Mask Pattern 1') : '111001011110011', 
    ('7 % error correction (L)', 'Mask Pattern 2') : '111110110101010', 
    ('7 % error correction (L)', 'Mask Pattern 3') : '111100010011101', 
    ('7 % error correction (L)', 'Mask Pattern 4') : '110011000101111', 
    ('7 % error correction (L)', 'Mask Pattern 5') : '110001100011000', 
    ('7 % error correction (L)', 'Mask Pattern 6') : '110110001000001', 
    ('7 % error correction (L)', 'Mask Pattern 7') : '110100101110110', 

    ('15 % error correction (M)', 'Mask Pattern 0') : '101010000010010', 
    ('15 % error correction (M)', 'Mask Pattern 1') : '101000100100101', 
    ('15 % error correction (M)', 'Mask Pattern 2') : '101111001111100', 
    ('15 % error correction (M)', 'Mask Pattern 3') : '101101101001011', 
    ('15 % error correction (M)', 'Mask Pattern 4') : '100010111111001', 
    ('15 % error correction (M)', 'Mask Pattern 5') : '100000011001110', 
    ('15 % error correction (M)', 'Mask Pattern 6') : '100111110010111', 
    ('15 % error correction (M)', 'Mask Pattern 7') : '100101010100000', 

    ('25 % error correction (Q)', 'Mask Pattern 0') : '011010101011111', 
    ('25 % error correction (Q)', 'Mask Pattern 1') : '011000001101000', 
    ('25 % error correction (Q)', 'Mask Pattern 2') : '011111100110001', 
    ('25 % error correction (Q)', 'Mask Pattern 3') : '011101000000110', 
    ('25 % error correction (Q)', 'Mask Pattern 4') : '010010010110100', 
    ('25 % error correction (Q)', 'Mask Pattern 5') : '010000110000011', 
    ('25 % error correction (Q)', 'Mask Pattern 6') : '010111011011010', 
    ('25 % error correction (Q)', 'Mask Pattern 7') : '010101111101101', 

    ('30 % error correction (H)', 'Mask Pattern 0') : '001011010001001', 
    ('30 % error correction (H)', 'Mask Pattern 1') : '001001110111110', 
    ('30 % error correction (H)', 'Mask Pattern 2') : '001110011100111', 
    ('30 % error correction (H)', 'Mask Pattern 3') : '001100111010000', 
    ('30 % error correction (H)', 'Mask Pattern 4') : '000011101100010', 
    ('30 % error correction (H)', 'Mask Pattern 5') : '000001001010101', 
    ('30 % error correction (H)', 'Mask Pattern 6') : '000110100001100', 
    ('30 % error correction (H)', 'Mask Pattern 7') : '000100000111011', 
}


galois_field = [
    1,2,4,8,16,32,64,128,29,58,116,232,205,135,19,38,
    76,152,45,90,180,117,234,201,143,3,6,12,24,48,96,192,
    157,39,78,156,37,74,148,53,106,212,181,119,238,193,159,35,
    70,140,5,10,20,40,80,160,93,186,105,210,185,111,222,161,
    95,190,97,194,153,47,94,188,101,202,137,15,30,60,120,240,
    253,231,211,187,107,214,177,127,254,225,223,163,91,182,113,226,
    217,175,67,134,17,34,68,136,13,26,52,104,208,189,103,206,
    129,31,62,124,248,237,199,147,59,118,236,197,151,51,102,204,
    133,23,46,92,184,109,218,169,79,158,33,66,132,21,42,84,
    168,77,154,41,82,164,85,170,73,146,57,114,228,213,183,115,
    230,209,191,99,198,145,63,126,252,229,215,179,123,246,241,255,
    227,219,171,75,150,49,98,196,149,55,110,220,165,87,174,65,
    130,25,50,100,200,141,7,14,28,56,112,224,221,167,83,166,
    81,162,89,178,121,242,249,239,195,155,43,86,172,69,138,9,
    18,36,72,144,61,122,244,245,247,243,251,235,203,139,11,22,
    44,88,176,125,250,233,207,131,27,54,108,216,173,71,142,1
]


galois_field_inverse = [
    None,0,1,25,2,50,26,198,3,223,51,238,27,104,199,75,
    4,100,224,14,52,141,239,129,28,193,105,248,200,8,76,113,
    5,138,101,47,225,36,15,33,53,147,142,218,240,18,130,69,
    29,181,194,125,106,39,249,185,201,154,9,120,77,228,114,166,
    6,191,139,98,102,221,48,253,226,152,37,179,16,145,34,136,
    54,208,148,206,143,150,219,189,241,210,19,92,131,56,70,64,
    30,66,182,163,195,72,126,110,107,58,40,84,250,133,186,61,
    202,94,155,159,10,21,121,43,78,212,229,172,115,243,167,87,
    7,112,192,247,140,128,99,13,103,74,222,237,49,197,254,24,
    227,165,153,119,38,184,180,124,17,68,146,217,35,32,137,46,
    55,63,209,91,149,188,207,205,144,135,151,178,220,252,190,97,
    242,86,211,171,20,42,93,158,132,60,57,83,71,109,65,162,
    31,45,67,216,183,123,164,118,196,23,73,236,127,12,111,246,
    108,161,59,82,41,157,85,170,251,96,134,177,187,204,62,90,
    203,89,95,176,156,169,160,81,11,245,22,235,122,117,44,215,
    79,174,213,233,230,231,173,232,116,214,244,234,168,80,88,175
]