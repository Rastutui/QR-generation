import customtkinter as ctk
from QR import QR
from qr_extra_data import *
from generate_qr import generate_qr
import random

class QRGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('QR code generator')

        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')

        self.update_idletasks()  
        main_window_width = self.winfo_screenwidth() * 0.8
        main_window_height = self.winfo_screenheight() * 0.8
        self.geometry(f"{main_window_width}x{main_window_height}")
        self.minsize(main_window_width, main_window_height)
 
        self._setup_ui()

    def _setup_ui(self):
        big_font=("Arial", 20)
        medium_font=("Arial", 17)
        small_font=("Arial", 14)       

        qr_code = QR()

        # -----Methods-----
        def set_too_many_chars_warning():
            warning_too_many_chars = 'Использовано слишком большое\n'
            warning_too_many_chars += 'количество символов!\n'
            warning_too_many_chars += '(Возможно в будущем это\n'
            warning_too_many_chars += 'не будет проблемой...)'
            warning_too_many_chars_label.configure(text=warning_too_many_chars)
        
        
        def set_cyrillic_used_warning():
            warning_cyrillic_used = 'Использование кириллицы запрещено!'
            warning_cyrillic_used_label.configure(text=warning_cyrillic_used)

        
        def set_optimal_encoding_mode(msg, qr_code):
            if msg.isnumeric():
                qr_code.encoding_mode = 'numeric'
            else:
                qr_code.encoding_mode = 'alphanumeric'
    
            for i in range(len(msg)):
                if msg[i] not in alpha_num_dict:
                    qr_code.encoding_mode = 'binary'


        def check_possibility_qr_generation(len_msg, qr_code):
            qr_config = qr_code.get_configuration()
            max_char_capacity = character_capacities[qr_config]
            if len_msg <= max_char_capacity:
                warning_too_many_chars_label.configure(text='')   
                return True
            else:
                return False
        

        def set_qr_configuration(e):
            len_msg = len(textbox.get(0.0, 'end-1c'))
            qr_code.version = qr_version_combo_box.get()
            qr_code.error_correction_lvl = error_correction_combo_box.get()
            
            fl_qr_ver_auto, fl_error_correction_auto = False, False
            if qr_code.version == 'Auto':
                fl_qr_ver_auto, qr_code.version = True, 'Version 1 (21 x 21)'
            if qr_code.error_correction_lvl == 'Auto':
                fl_error_correction_auto = True 
                qr_code.error_correction_lvl = '15 % error correction (M)'
            
            if fl_qr_ver_auto and fl_error_correction_auto:
                for error_correction_auto in qr_code.error_correction_lvls[2:0:-1]:
                    for qr_ver_auto in qr_code.versions[1:]:
                        qr_code.error_correction_lvl = error_correction_auto
                        qr_code.version = qr_ver_auto
                        if check_possibility_qr_generation(len_msg, qr_code):
                            return True          
            elif fl_qr_ver_auto:
                for qr_ver_auto in qr_code.versions[1:]:
                    qr_code.version = qr_ver_auto
                    if check_possibility_qr_generation(len_msg, qr_code):
                        return True
            elif fl_error_correction_auto:
                for error_correction_auto in qr_code.error_correction_lvls[2:0:-1]:
                    qr_code.error_correction_lvl = error_correction_auto
                    if check_possibility_qr_generation(len_msg, qr_code):
                        return True
            else:
                if check_possibility_qr_generation(len_msg, qr_code):
                    return True
           
            generate_qr_button._state = 'disable'
            set_too_many_chars_warning()
            return False


        def text_box_scaner(e):
            msg = textbox.get(0.0, 'end-1c')
            if not len(msg):
                generate_qr_button._state = 'disable'
            elif not msg.isascii():
                set_cyrillic_used_warning()
                generate_qr_button._state = 'disable'
            else:
                warning_cyrillic_used_label.configure(text='')

            set_optimal_encoding_mode(msg, qr_code)

            if not set_qr_configuration(e):
                set_too_many_chars_warning()
                generate_qr_button._state = 'disable'  
            else:
                warning_too_many_chars_label.configure(text='') 

            if (len(msg) and len(warning_too_many_chars_label._text) == 0
                and len(warning_cyrillic_used_label._text) == 0):
                generate_qr_button._state = 'normal'


        def set_mask_pattern():
            if mask_pattern_combo_box.get() == 'Auto':
                not_auto_mask_patterns = qr_code.mask_patterns[1:]
                qr_code.mask_pattern = random.choice(not_auto_mask_patterns)
            else:
                qr_code.mask_pattern = mask_pattern_combo_box.get()


        def _generate_qr():
            msg = textbox.get(0.0, 'end-1c')
            if (not len(msg) or len(warning_too_many_chars_label._text) != 0 
                or len(warning_cyrillic_used_label._text) != 0):
                generate_qr_button._state = 'disable'
            else:
                generate_qr_button._state = 'normal'
                qr_code.user_msg = msg

                if 'canvas' in locals():
                    del canvas
                canvas = ctk.CTkCanvas(master=self, bg='white')
                canvas.place(relx=0.45, rely=0.12, width=700, height=700)
                
                set_mask_pattern()
                generate_qr(canvas, qr_code)


        # -----Widgets-----
        # Frame
        left_panel = ctk.CTkFrame(master=self)
        left_panel.place(x=0, relheight=1, relwidth=0.32)
        
        # Comboxes
        error_correction_lvl = ctk.StringVar(value='Auto')
        qr_version = ctk.StringVar(value='Auto')
        mask_pattern = ctk.StringVar(value='Auto')

        combo_box_common_fields = {
            'master': left_panel,
            'height': 60,
            'state': 'readonly',
            'dropdown_font': small_font,
            'font': medium_font
        }

        error_correction_combo_box = ctk.CTkComboBox(
            **combo_box_common_fields)
        error_correction_combo_box.configure(
            values=qr_code.error_correction_lvls,
            variable=error_correction_lvl,
            command=set_qr_configuration)

        mask_pattern_combo_box = ctk.CTkComboBox(**combo_box_common_fields)
        mask_pattern_combo_box.configure(values=qr_code.mask_patterns,
                                         variable=mask_pattern)

        qr_version_combo_box = ctk.CTkComboBox(**combo_box_common_fields)
        qr_version_combo_box.configure(values=qr_code.versions,
                                       variable=qr_version,
                                       command=set_qr_configuration)   

        combo_box_common_geometry = {
            'relx': 0.05, 
            'relwidth': 0.8, 
            'relheight': 0.05
        }
        
        # geometry
        error_correction_combo_box.place(**combo_box_common_geometry, 
                                         rely=0.55)
        mask_pattern_combo_box.place(**combo_box_common_geometry, 
                                     rely=0.65)
        qr_version_combo_box.place(**combo_box_common_geometry, 
                                   rely=0.75)


        # Textbox
        textbox = ctk.CTkTextbox(left_panel,
                                corner_radius=10, 
                                font=medium_font)
        textbox.place(relx=0.05, rely=0.15, relwidth=0.8, relheight=0.15)
        textbox.bind("<KeyRelease>", text_box_scaner)

        # Warning labels
        warning_common_fields = {
            'master': left_panel, 
            'text': '',
            'text_color': 'red', 
            'font': small_font
        }
        warning_too_many_chars_label = ctk.CTkLabel(**warning_common_fields)
        warning_cyrillic_used_label = ctk.CTkLabel(**warning_common_fields)

        # geometry
        warning_too_many_chars_label.place(x=0, rely=0.4, 
                                           relwidth=0.9, relheight=0.1)

        warning_cyrillic_used_label.place(x=0, rely=0.3, 
                                          relwidth=0.9, relheight=0.06)

        # Enter text label
        enter_text_label = ctk.CTkLabel(master=left_panel, 
                                        text='Введите текст для генерации:', 
                                        font=big_font)
        enter_text_label.place(relx=0.05, rely=0.1)

        # Choose labels
        choose_label_common_fields = {
            'master': left_panel, 
            'font': big_font
        }

        choose_error_correction_lvl_label = ctk.CTkLabel(
            **choose_label_common_fields)
        choose_error_correction_lvl_label.configure(
            text='Выберите уровень коррекции ошибок:') 
        
        choose_mask_label = ctk.CTkLabel(**choose_label_common_fields)
        choose_mask_label.configure(text='Выберите маску:')
        
        choose_qr_version_label = ctk.CTkLabel(**choose_label_common_fields)
        choose_qr_version_label.configure(text='Выберите версию qr кода:')    
        
        # geometry
        choose_error_correction_lvl_label.place(relx=0.05, rely=0.51)
        choose_mask_label.place(relx=0.05, rely=0.61)
        choose_qr_version_label.place(relx=0.05, rely=0.71)


        # Button
        generate_qr_button = ctk.CTkButton(master=left_panel, 
                                           text='Сгенерировать QR код',
                                           state='disable',
                                           command=_generate_qr, 
                                           font=big_font)
        generate_qr_button.place(relx=0.05, rely=0.85, 
                                 relwidth=0.8, relheight=0.07)