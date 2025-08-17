class QR:
    def __init__(self, 
                 version='Version 1 (21 x 21)', 
                 error_correction_lvl='15 % error correction (M)',
                 encoding_mode='binary',
                 mask_pattern='Auto'):
        self._version = version
        self._error_correction_lvl = error_correction_lvl
        self._encoding_mode = encoding_mode
        self._mask_pattern = mask_pattern
        self._user_msg = ''
        self._modules_with_no_data = []
        self._format_info = []
        self._num_of_modules = 21
        self._colour_for_module = [[-1] * (self.num_of_modules + 1) 
                                   for _ in range(self.num_of_modules + 1)]


    #-----versions, error_correction_lvls and mask patterns-----
    @property
    def versions(self):
        qr_versions = ['Auto', 
                       'Version 1 (21 x 21)', 
                       'Version 2 (25 x 25)']
        return qr_versions

    @property
    def error_correction_lvls(self):
        error_correction_lvls = ['Auto', 
                                 '7 % error correction (L)', 
                                 '15 % error correction (M)', 
                                 '25 % error correction (Q)', 
                                 '30 % error correction (H)']
        return error_correction_lvls

    @property
    def mask_patterns(self):
        mask_patterns = ['Auto', 'Mask Pattern 0', 'Mask Pattern 1', 
                         'Mask Pattern 2', 'Mask Pattern 3','Mask Pattern 4', 
                         'Mask Pattern 5', 'Mask Pattern 6', 'Mask Pattern 7']
        return mask_patterns


    #-----version, error_correction_lvl, encoding_mode 
    # and mask pattern for this qr-----
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value
        if value == 'Version 1 (21 x 21)':
            self._num_of_modules = 21
        elif value == 'Version 2 (25 x 25)':
            self._num_of_modules = 25
        self._colour_for_module = [[-1] * (self.num_of_modules + 1) 
                                   for _ in range(self.num_of_modules + 1)]
        
        
    @property
    def error_correction_lvl(self):
        return self._error_correction_lvl

    @error_correction_lvl.setter
    def error_correction_lvl(self, value):
        self._error_correction_lvl = value

    @property
    def encoding_mode(self):
        return self._encoding_mode
    
    @encoding_mode.setter
    def encoding_mode(self, value):
        self._encoding_mode = value

    def get_configuration(self):
        return (self._version, self._error_correction_lvl, self._encoding_mode)
    
    def set_configuration(self, config):
        self.version = config[0]
        self._error_correction_lvl = config[1]
        self._encoding_mode = config[2]

    @property
    def mask_pattern(self):
        return self._mask_pattern
    
    @mask_pattern.setter
    def mask_pattern(self, value):
        self._mask_pattern = value

    
    #-----matrixes-----
    @property
    def modules_with_no_data(self):
        return self._modules_with_no_data
    
    @modules_with_no_data.setter
    def modules_with_no_data(self, value):
        self._modules_with_no_data.append(value)

    @property
    def format_info(self):
        return self._format_info
    
    @format_info.setter
    def format_info(self, value):
        self._format_info.extend(value)

    @property
    def colour_for_module(self):
        return self._colour_for_module

    @colour_for_module.setter
    def colour_for_module(self, i, j, value):
        self._colour_for_module[i][j] = value


    #-----for canvas-----
    @property
    def num_of_modules(self):
        return self._num_of_modules
    
    @num_of_modules.setter
    def num_of_modules(self, value):
        self._num_of_modules = value

    @property
    def module_length(self):
        return round(600 / self.num_of_modules)


    #-----user_input-----
    @property
    def user_msg(self):
        return self._user_msg
    
    @user_msg.setter
    def user_msg(self, value):
        self._user_msg = value