import random
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from PIL import Image, ImageTk

# Simulovaná data příspěvků
posts = [
    {"text": "Ráno s kávou a západem slunce – nejlepší start dne!", "time": "20.02.2025 08:00", "likes": 150, "comments": 25, "shares": 10, "sentiment": "pozitivní"},
    {"text": "Nový produkt je tu!", "time": "21.02.2025 15:00", "likes": 20, "comments": 2, "shares": 0, "sentiment": "neutrální"},
    {"text": "Co děláte o víkendu?", "time": "22.02.2025 18:00", "likes": 80, "comments": 15, "shares": 5, "sentiment": "pozitivní"},
    {"text": "Nový vtip dne – zkus to!", "time": "23.02.2025 19:00", "likes": 120, "comments": 18, "shares": 8, "sentiment": "pozitivní"},
    {"text": "Ráno bez kávy? Žádný den!", "time": "19.02.2025 07:30", "likes": 130, "comments": 22, "shares": 12, "sentiment": "pozitivní"}
]

# Funkce pro přidání vlastního příspěvku
def add_post(text, time):
    new_post = {"text": text, "time": time, "likes": 0, "comments": 0, "shares": 0, "sentiment": "neutrální"}
    posts.append(new_post)

class SocialPulseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SocialPulse – Analýza sociálních sítí")
        self.root.geometry("700x600")

        # Nadpis aplikace
        self.title_label = ttk.Label(root, text="SocialPulse", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.subtitle_label = ttk.Label(root, text="Tvůj týdenní report", font=("Arial", 14))
        self.subtitle_label.pack(pady=5)

        # Rámeček pro obsah
        self.report_frame = ttk.Frame(root, padding=10)
        self.report_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Textové pole pro report
        self.report_text = scrolledtext.ScrolledText(self.report_frame, wrap="word", width=70, height=10, font=("Arial", 12))
        self.report_text.pack(fill="both", expand=True)

        # Vstupní pole pro nový příspěvek
        self.entry_label = ttk.Label(root, text="Přidat nový příspěvek:")
        self.entry_label.pack()
        
        self.post_entry = ttk.Entry(root, width=50)
        self.post_entry.pack(pady=5)
        
        self.time_entry = ttk.Entry(root, width=20)
        self.time_entry.insert(0, "HH:MM")
        self.time_entry.pack(pady=5)
        
        self.add_post_button = ttk.Button(root, text="Přidat příspěvek", command=self.add_new_post)
        self.add_post_button.pack(pady=5)
        
        # Oddělovač
        self.separator = ttk.Separator(root, orient="horizontal")
        self.separator.pack(fill="x", padx=20, pady=10)
        
        # Tlačítka
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        
        self.detailed_button = ttk.Button(button_frame, text="Podrobný report", command=self.show_detailed_report)
        self.detailed_button.pack(side="left", padx=10, pady=5)
        
        self.summary_button = ttk.Button(button_frame, text="Shrnutí", command=self.show_summary)
        self.summary_button.pack(side="left", padx=10, pady=5)
        
        self.train_button = ttk.Button(button_frame, text="Naučit se z dat", command=self.train_and_show)
        self.train_button.pack(side="left", padx=10, pady=5)
        
        self.upload_button = ttk.Button(button_frame, text="Nahrát screenshot", command=self.upload_screenshot)
        self.upload_button.pack(side="left", padx=10, pady=5)
        
        self.exit_button = ttk.Button(button_frame, text="Zavřít", command=root.quit)
        self.exit_button.pack(side="left", padx=10, pady=5)

        self.image_label = ttk.Label(root)
        self.image_label.pack()

    def add_new_post(self):
        text = self.post_entry.get()
        time = self.time_entry.get()
        if text and time:
            add_post(text, time)
            self.report_text.insert("end", f"Nový příspěvek přidán: {text} v {time}\n")
            self.post_entry.delete(0, "end")
            self.time_entry.delete(0, "end")

    def show_detailed_report(self):
        self.report_text.insert("end", "Podrobný report není zatím implementován.\n")

    def show_summary(self):
        self.report_text.insert("end", "Shrnutí není zatím implementováno.\n")

    def train_and_show(self):
        self.report_text.insert("end", "Trénování modelu není zatím implementováno.\n")

    def upload_screenshot(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((300, 200), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
            self.report_text.insert("end", "Screenshot byl nahrán a připraven k analýze.\n")

# Spuštění aplikace
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialPulseApp(root)
    root.mainloop()
