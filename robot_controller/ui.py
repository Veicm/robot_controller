import customtkinter as ctk
from .transmitter import Transmitter
from .transmitter import TestTransmitter
from .crawly import crawlyButtons

class RobotController(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Robot Controller")
        self.geometry("515x540")
        self.resizable(False, True)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.test_transmitter = TestTransmitter()
        self.transmitter = Transmitter(port=1234)
        

        self.main_content = ctk.CTkFrame(self)
        self.main_content.pack(fill="both", expand=True)

        self.crawly_view()

    def _clear_main_frame(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()


    def _top_bar(self):
        self.label_title = ctk.CTkLabel(self.main_content, text="Robot Controller", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=(10, 2))

        self.label_author = ctk.CTkLabel(self.main_content, text="by Veicm")
        self.label_author.pack(pady=(0, 10))

        self.segment_frame = ctk.CTkFrame(self.main_content)
        self.segment_frame.pack(pady=10)

        self.button1 = ctk.CTkButton(self.segment_frame, text="Crawly", command=self.crawly_view)
        self.button1.grid(row=0, column=0, padx=10)

        self.button2 = ctk.CTkButton(self.segment_frame, text="SMARS (not working)", command=self.smars_view)
        self.button2.grid(row=0, column=1, padx=10)

        self.button3 = ctk.CTkButton(self.segment_frame, text="Walky (not working)", command=self.walky_view)
        self.button3.grid(row=0, column=2, padx=10)

        self.ip_entry = ctk.CTkEntry(self.main_content, placeholder_text="Target IP")
        self.ip_entry.pack(pady=10)

        self.separator_top = ctk.CTkFrame(self.main_content, height=2, fg_color="gray")
        self.separator_top.pack(fill="x", padx=20, pady=(10, 5))



    def _crawly_buttons(self):
        self.crawly_label = ctk.CTkLabel(self.main_content, text="Crawly", font=ctk.CTkFont(size=14))
        self.crawly_label.pack(pady=(0, 10))

        self.button_area = ctk.CTkScrollableFrame(self.main_content)
        self.button_area.pack(padx=5, pady=(0, 10), fill="both", expand=True)

        buttons = [ # for col (the last int) only use numbers from 0 to 2
            ("Toggle curled walking", "curl", 0, 0),
            ("Toggle Dancing", "dance", 0, 1),
            ("Music Mario", "melody_mario", 0, 2)
        ]

        for (text, massage, row, col) in buttons:
            self.button = ctk.CTkButton(self.button_area, text=text, command=lambda m=massage: self.send_massage(m))
            self.button.grid(row=row, column=col, padx=10, pady=5)

    def _smars_buttons(self):
        self.crawly_label = ctk.CTkLabel(self.main_content, text="SMARS", font=ctk.CTkFont(size=14))
        self.crawly_label.pack(pady=(0, 10))

        self.button_area = ctk.CTkScrollableFrame(self.main_content)
        self.button_area.pack(padx=5, pady=(0, 10), fill="both", expand=True)

        buttons = [ # for col (the last int) only use numbers from 0 to 2
            ("Test 1 (nothing)", "test_1", 0, 0),
            ("Test 2 (nothing)", "test_2", 0 ,1)
        ]

        for (text, massage, row, col) in buttons:
            self.button = ctk.CTkButton(self.button_area, text=text, command=lambda: self.send_massage(massage))
            self.button.grid(row=row, column=col, padx=10, pady=5)

    def _walky_buttons(self):
        self.crawly_label = ctk.CTkLabel(self.main_content, text="Walky", font=ctk.CTkFont(size=14))
        self.crawly_label.pack(pady=(0, 10))

        self.button_area = ctk.CTkScrollableFrame(self.main_content)
        self.button_area.pack(padx=5, pady=(0, 10), fill="both", expand=True)

        buttons = [ # for col (the last int) only use numbers from 0 to 2
            ("Test 1 (nothing)", "test_1", 0, 0),
            ("Test 2 (nothing)", "test_2", 0 ,1)
        ]
        
        for (text, massage, row, col) in buttons:
            self.button = ctk.CTkButton(self.button_area, text=text, command=lambda: self.send_massage(massage))
            self.button.grid(row=row, column=col, padx=10, pady=5)



    def _debug_button(self):
        self.separator_bottom = ctk.CTkFrame(self.main_content, height=2, fg_color="gray")
        self.separator_bottom.pack(fill="x", padx=20, pady=(10, 5))

        self.bottom_segment = ctk.CTkFrame(self.main_content)
        self.bottom_segment.pack(pady=20)

        self.debug_button = ctk.CTkButton(self.bottom_segment, text="Debug", command=lambda: self.send_massage("debug"))
        self.debug_button.pack()
    
    def crawly_view(self):
        self._clear_main_frame()

        self._top_bar()
        crawlyButtons()._crawly_buttons(self.main_content)
        self._debug_button()
        
        self.mainloop()

    def smars_view(self):
        self._clear_main_frame()

        self._top_bar()
        self._smars_buttons()
        self._debug_button()
        
        self.mainloop()

    def walky_view(self):
        self._clear_main_frame()

        self._top_bar()
        self._walky_buttons()
        self._debug_button()
        
        self.mainloop()

    def send_massage(self, massage:str):
        self.ip = self.ip_entry.get()
        if self.ip == "":
            self.test_transmitter.send_massage(massage, self.ip)
        else:
            try:
                self.transmitter.send_massage(massage, self.ip)
            except Exception:
                self.test_transmitter.send_massage(massage, self.ip)


if __name__ == "__main__":
    robot_controller = RobotController()
    robot_controller.mainloop()