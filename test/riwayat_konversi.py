from collections import deque

class RiwayatKonversi:
    def __init__(self):
        self.riwayat = deque(maxlen=3)  # Membuat deque dengan batas maksimum riwayat konversi
    
    def tambahkan_konversi(self, konversi):
        self.riwayat.append(konversi)
    
    def get_riwayat(self):
        return "\n".join(self.riwayat)

    def ambil_konversi_terbaru(self):
        if self.riwayat:
            return self.riwayat.popleft()
        else:
            return None

