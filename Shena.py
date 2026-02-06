import os # Wajib import ini di paling atas

username = "Freya"
password = "26fgil24t89bvjq354g45obn"

while True:
    username_input = input("masukkan username anda: ")
    
    if username_input != username:
        print('maaf username tidak valid')
        continue 
        
    password_input = input(f"masukkan password {username}: ")
    
    if password_input == password:
        print("Selamat Anda telah berhasil!")
        
        # --- BAGIAN MEMBUKA FOLDER ---
        path_folder = "D:/dekstop 2/private" # <--- Ganti dengan alamat folder kamu
        
        try:
            # os.startfile hanya jalan di Windows
            os.startfile(path_folder) 
            print(f"Folder {path_folder} berhasil dibuka.")
        except FileNotFoundError:
            print("Folder tidak ditemukan. Cek lagi alamat path-nya!")
        # -----------------------------
        
        break 
    else:
        print("password salah")
