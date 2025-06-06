# tugasAkhirAI
Projek Klasifikasi Jenis Kendaraan Menggunakan YOLOv8
Persyaratan Sistem
1. Dependensi Perangkat Lunak

Projek ini membutuhkan paket-paket berikut:
text

Python >= 3.8  
PyTorch >= 2.0  
ultralytics (YOLOv8) >= 8.0  
OpenCV >= 4.7  
numpy >= 1.24  
scikit-learn (untuk evaluasi)  

2. Spesifikasi Perangkat Keras

Minimum:

    CPU: Intel Core i5 (generasi ke-8 atau setara)

    RAM: 8GB (disarankan 16GB untuk training)

    Penyimpanan: 10GB (untuk dataset dan model)

Rekomendasi:

    GPU: NVIDIA GTX 1650 (4GB VRAM) atau setara

    Sistem Operasi: Ubuntu 22.04 (optimasi manajemen memori)

3. Instalasi

    Clone repositori:
    bash

git clone https://github.com/username/projek-klasifikasi-kendaraan.git

Buat environment Python:
bash

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

Install dependensi:
bash

    pip install -r requirements.txt

4. Struktur Dataset

Dataset harus mengikuti struktur YOLOv8:
plaintext

dataset/
├── train/
│   ├── images/  # File gambar (.jpg, .png)
│   └── labels/  # File label YOLO (.txt)
└── valid/       # Struktur sama seperti train

Format label:
text

<class_id> <x_center> <y_center> <width> <height>  # Nilai ternormalisasi [0, 1]

5. Pelatihan Model

Jalankan pelatihan dengan:
bash

yolo detect train \
    data=dataset.yaml \
    model=yolov8n.pt \
    epochs=100 \
    imgsz=640

6. Inference

Contoh penggunaan model terlatih:
python

from ultralytics import YOLO
model = YOLO('best.pt')
results = model.predict('input.jpg', save=True)

Catatan Khusus

    Optimasi CPU: Untuk perangkat terbatas, gunakan argumen imgsz=320 dan batch=4.

    Kompatibilitas: Model ekspor ke format ONNX/TensorRT didukung.

Lisensi: MIT
Kontributor: Gentiaras Teja Samudra