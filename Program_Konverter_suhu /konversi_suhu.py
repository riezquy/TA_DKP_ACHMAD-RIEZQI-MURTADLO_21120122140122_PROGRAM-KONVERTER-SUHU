import tkinter as tk
from tkinter import ttk
from riwayat_konversi import RiwayatKonversi


class SuhuConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.riwayat_konversi = RiwayatKonversi()
        
        # Background color
        bg_color = "#00BFFF"
        
        # frame utama
        main_frame = tk.Frame(root, bg=bg_color)
        main_frame.pack(padx=30, pady=30)
        
        # judul label
        title_label = tk.Label(main_frame, text="Konversi Suhu", font=("Courier new", 24, "bold"), fg="black", bg=bg_color)
        title_label.grid(row=0, columnspan=3, pady=10)
        
        # Combo box pertama
        self.combo_box1 = ttk.Combobox(main_frame, values=["Celcius", "Fahrenheit", "Kelvin"], font=("Arial", 12))
        self.combo_box1.grid(row=1, column=0, padx=10, pady=10)
        self.combo_box1.set("pilih skala")

        # Tombol konversi
        self.button1 = tk.Button(main_frame, text="Konversi", command=self.klik_tombol_konversi, font=("Arial", 12), bg="#c792df", fg="white")
        self.button1.grid(row=1, column=1, padx=10)
        
        # Combo box kedua
        self.combo_box2 = ttk.Combobox(main_frame, values=["Fahrenheit", "Celcius", "Kelvin"], font=("Arial", 12))
        self.combo_box2.grid(row=1, column=2, padx=10, pady=10)
        self.combo_box2.set("pilih skala")
        
        # Input field
        self.entry = tk.Entry(main_frame, font=("Arial", 12))
        self.entry.insert(0, "Masukkan angka")
        self.entry.config(fg="gray")
        self.entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.entry.grid(row=2, column=0, columnspan=3, padx=10)
        
        # Label hasil
        self.result_label = tk.Label(main_frame, text="Hasil", font=("Arial", 14, "bold"), fg="black", bg=bg_color)
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Tombol reset
        self.button2 = tk.Button(main_frame, text="Reset", command=self.klik_tombol_reset, font=("Arial", 12), bg="#c792df", fg="white")
        self.button2.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Riwayat konversi
        self.history_button = tk.Button(main_frame, text="Tampilkan Riwayat Konversi", command=self.tampilkan_riwayat_konversi, font=("Arial", 12), bg="#c792df", fg="white")
        self.history_button.grid(row=5, column=0, columnspan=3, pady=10)

    def on_entry_focus_in(self, event):
        if self.entry.get() == "Masukkan angka":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def on_entry_focus_out(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Masukkan angka")
            self.entry.config(fg="gray")
    
    def klik_tombol_konversi(self):
        selected_item1 = self.combo_box1.get()
        selected_item2 = self.combo_box2.get()
        input_value = self.entry.get()
        try:
            input_value = float(input_value)
            if selected_item1 == "Celcius" and selected_item2 == "Fahrenheit":
                converted_value = input_value * 9/5 + 32
                self.result_label.config(text=f"{input_value} Celcius = {converted_value} Fahrenheit")
            elif selected_item1 == "Celcius" and selected_item2 == "Kelvin":
                converted_value = input_value + 273.15
                self.result_label.config(text=f"{input_value} Celcius = {converted_value} Kelvin")
            elif selected_item1 == "Fahrenheit" and selected_item2 == "Celcius":
                converted_value = (input_value - 32) * 5/9
                self.result_label.config(text=f"{input_value} Fahrenheit = {converted_value} Celcius")
            elif selected_item1 == "Fahrenheit" and selected_item2 == "Kelvin":
                converted_value = (input_value - 32) * 5/9 + 273.15
                self.result_label.config(text=f"{input_value} Fahrenheit = {converted_value} Kelvin")
            elif selected_item1 == "Kelvin" and selected_item2 == "Celcius":
                converted_value = input_value - 273.15
                self.result_label.config(text=f"{input_value} Kelvin = {converted_value} Celcius")
            elif selected_item1 == "Kelvin" and selected_item2 == "Fahrenheit":
                converted_value = (input_value - 273.15) * 9/5 + 32
                self.result_label.config(text=f"{input_value} Kelvin = {converted_value} Fahrenheit")
            else:
                self.result_label.config(text="Jangan Dikonversi lah ya")

            # Menambahkan konversi ke dalam riwayat konversi
            konversi = f"{input_value} {selected_item1} = {converted_value} {selected_item2}"
            self.riwayat_konversi.tambahkan_konversi(konversi)

        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid")
    
    def klik_tombol_reset(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Hasil")
    
    def tampilkan_riwayat_konversi(self):
        riwayat = self.riwayat_konversi.get_riwayat()
        if riwayat:
            self.tampilkan_jendela_riwayat(riwayat)
        else:
            self.tampilkan_jendela_riwayat("Tidak ada riwayat konversi.")
    
    def tampilkan_jendela_riwayat(self, riwayat):
        jendela_riwayat = tk.Toplevel(self.root)
        jendela_riwayat.title("Riwayat Konversi")
        riwayat_label = tk.Label(jendela_riwayat, text=riwayat, font=("Arial", 12))
        riwayat_label.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    
    # Gaya untuk frame dan tombol
    root.style = ttk.Style()
    root.style.configure("My.TFrame", background="#00BFFF")
    root.style.configure("My.TButton", background="#c792df", foreground="white")
    
    app = SuhuConverterApp(root)
    root.mainloop()
