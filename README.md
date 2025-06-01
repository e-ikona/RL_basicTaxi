```markdown
# Smart Taxi RL

Proyek ini adalah implementasi algoritma Q-Learning pada environment Taxi dengan visualisasi menggunakan Pygame.  
Tujuan proyek ini adalah melatih agent pintar untuk menjemput dan mengantar penumpang di grid dengan rintangan.

## Fitur

- Simulasi environment Taxi dengan rintangan dan lokasi penumpang/tujuan berbeda  
- Q-Learning agent untuk pelatihan dan pengambilan keputusan  
- Visualisasi langkah agent menggunakan Pygame dengan tampilan grid, posisi taxi, penumpang, dan status keberhasilan  
- Logging hasil simulasi dan akurasi agent  

## Struktur Proyek

```

.
├── model/
│   └── qtable.pkl            # File model Q-Table hasil training
├── taxi\_env.py               # Environment Taxi dengan grid, rintangan, dan state
├── q\_learning\_agent.py       # Implementasi Q-Learning Agent
├── pygame\_visual.py          # Visualisasi grid dan simulasi menggunakan Pygame
├── test.py                   # Script utama untuk menjalankan simulasi dan visualisasi
├── README.md                 # Dokumentasi proyek ini
└── requirements.txt          # Dependencies Python yang diperlukan

```

## Cara Menjalankan

1. Pastikan Python 3.8+ sudah terinstall di sistem Anda.  
2. Install dependencies dengan menjalankan:

```

pip install -r requirements.txt

```

3. Jalankan script `test.py` untuk memulai simulasi dan visualisasi:

```

python test.py

```

4. Jendela visualisasi Pygame akan terbuka dan menunjukkan langkah agent hingga selesai.

## Dependencies

- `pygame` : Untuk membuat visualisasi grid dan agent  
- `numpy` : Untuk komputasi numerik (jika digunakan dalam agent)  
- `pickle` : Modul bawaan Python untuk load/save Q-Table  

## Catatan

- Pastikan file `model/qtable.pkl` sudah tersedia sebagai model hasil training, atau buat dan latih Q-Table terlebih dahulu.  
- Anda dapat mengubah parameter grid dan rintangan di file `test.py` sesuai kebutuhan.

## Lisensi

Proyek ini bersifat open-source dan dapat digunakan untuk pembelajaran dan pengembangan lebih lanjut.

---

Selamat mencoba dan bereksperimen dengan Smart Taxi RL! 🚖✨
```
