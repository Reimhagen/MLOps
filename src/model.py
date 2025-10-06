import sys
import time
import os

def train_model():
    """Simulasi pelatihan model."""
    print("--- Memulai Pelatihan Model ---")
    time.sleep(2) # Simulasi proses yang memakan waktu
    
    # Metrik sederhana (simulasi)
    accuracy = 0.85 
    print(f"Model berhasil dilatih. Akurasi: {accuracy}")
    
    # Simulasi penyimpanan artefak model
    with open("model_artifact.txt", "w") as f:
        f.write(f"Model version: {time.time()}\nAccuracy: {accuracy}")

    print("--- Pelatihan Model Selesai ---")

if __name__ == '__main__':
    # Memastikan skrip dipanggil dengan argumen 'train'
    if len(sys.argv) > 1 and sys.argv[1] == 'train':
        train_model()
    else:
        print("Panggil skrip ini dengan 'python src/model.py train'")