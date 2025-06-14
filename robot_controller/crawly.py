import customtkinter as ctk
from .transmitter import Transmitter
from .transmitter import TestTransmitter

class crawlyButtons(ctk.CTk):
    def __init__(self):
        self.test_transmitter = TestTransmitter()
        self.transmitter = Transmitter(port=1234)
        

    def _crawly_buttons(self, meta):
        self.crawly_label = ctk.CTkLabel(meta, text="Crawly", font=ctk.CTkFont(size=14))
        self.crawly_label.pack(pady=(0, 10))

        self.button_area = ctk.CTkScrollableFrame(meta)
        self.button_area.pack(padx=5, pady=(0, 10), fill="both", expand=True)

        buttons = [ # for col (the last int) only use numbers from 0 to 2
            ("Toggle curled walking", "curl", 0, 0),
            ("Toggle Dancing", "dance", 0, 1),
            ("Music Mario", "melody_mario", 0, 2)
        ]

        for (text, massage, row, col) in buttons:
            self.button = ctk.CTkButton(self.button_area, text=text, command=lambda m=massage: self.send_massage(m))
            self.button.grid(row=row, column=col, padx=10, pady=5)