import sys
import time


def train_model():
    """Simulasi pelatihan model."""


    print("--- Memulai Pelatihan Model ---")
    time.sleep(2) 
    
    
    accuracy = 0.85 
    print(f"Model berhasil dilatih. Akurasi: {accuracy}")
    
    
    with open("model_artifact.txt", "w") as f:
        f.write(f"Model version: {time.time()}\nAccuracy: {accuracy}")

    print("--- Pelatihan Model Selesai ---")


if __name__ == '__main__':


    if len(sys.argv) > 1 and sys.argv[1] == 'train':
        train_model()
    else:
        print("Panggil skrip ini dengan 'python src/model.py train'")

