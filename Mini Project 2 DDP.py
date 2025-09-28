users = {
    "Rama": {"password": "12345", "role": "Manager"},
    "Dani": {"password": "54321", "role": "Karyawan"}
}

files = [
    {'nama': 'Tugas 1.pdf', 'ekstensi': 'pdf'},
    {'nama': 'Gambar 1.jpg', 'ekstensi': 'jpg'},
    {'nama': 'Tugas 3.pdf', 'ekstensi': 'pdf'},
    {'nama': 'Tugas 2.pdf', 'ekstensi': 'pdf'},
    {'nama': 'Arteri.mp3', 'ekstensi': 'mp3'},
    {'nama': 'Gambar 2.jpg', 'ekstensi': 'jpg'},
]

def login():
    print("=" * 68)
    print("LOGIN SISTEM PENYORTIRAN FILE SESUAI EXTENSI")
    print("=" * 68)
    while True:
        try:
            print("Pilih role untuk login:")
            print("1. Manager")
            print("2. Karyawan")
            print("3. Keluar Program")
            role_pilih = input("Masukkan pilihan (1 - 3): ").strip()
            if role_pilih == '1':
                role_dipilih = "Manager"
            elif role_pilih == '2':
                role_dipilih = "Karyawan"
            elif role_pilih == '3':
                print("Terima kasih, program selesai.")
                exit()  # keluar program langsung
            else:
                raise ValueError("Input harus berupa angka 1 - 3.")
            
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if username in users:
                user = users[username]
                if user["password"] == password and user["role"] == role_dipilih:
                    print(f"\nLogin berhasil! Selamat datang {username} ({user['role']})\n")
                    return user['role']
                else:
                    print("Username atau password salah.\n")
            else:
                print("Username atau password salah.\n")
        except KeyboardInterrupt:
            print("\nTidak boleh menggunakan Ctrl + C saat login.\n")
        except Exception as e:
            print(f"Error : {e}\n")

def tambah_file():
    try:
        while True:
            nama = input("Masukkan nama file (contoh: Tugas Minpro 1.pdf): ").strip()
            if not nama:
                print("Nama file tidak boleh kosong.")
                continue
            if '.' not in nama:
                print("Nama file harus mengandung ekstensi, contoh: Tugas Minpro 1.pdf")
                continue
            ekstensi = nama.split('.')[-1]
            files.append({'nama': nama, 'ekstensi': ekstensi})
            print(f"\nFile '{nama}' berhasil ditambahkan!\n")
            break
    except KeyboardInterrupt:
        print("\nEror: Tidak boleh menggunakan Ctrl+C saat menambah file.")

def tampilkan_files():
    if not files:
        print("Daftar file kosong.")
    else:
        print("-" * 68)
        print("No | Nama File                                          | Ekstensi")
        print("-" * 68)
        for index, f in enumerate(files):
            print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
        print("-" * 68)

def edit_file():
    try:
        tampilkan_files()
        if not files:
            return
        index = input("Pilih nomor file yang ingin diedit: ").strip()
        if not index.isdigit():
            print("Input harus berupa angka.")
            return
        index = int(index) - 1
        if index < 0 or index >= len(files):
            print("Nomor file tidak valid.")
            return
        while True:
            nama_baru = input(f"Masukkan nama baru (contoh: Tugas Minpro 1.pdf): ").strip()
            if not nama_baru:
                print("Nama file tidak boleh kosong.")
                continue
            if '.' not in nama_baru:
                print("Nama file harus mengandung ekstensi, contoh: Tugas Minpro 1.pdf")
                continue
            ekstensi = nama_baru.split('.')[-1].lower()
            files[index]['nama'] = nama_baru
            files[index]['ekstensi'] = ekstensi
            print(f"\nFile berhasil diperbarui menjadi '{nama_baru}'\n")
            break
    except KeyboardInterrupt:
        print("\nError: Tidak boleh menggunakan Ctrl+C saat edit file.")

def hapus_file():
    tampilkan_files()
    try:
        index = int(input("Pilih nomor file yang ingin dihapus: ")) - 1
        if 0 <= index < len(files):
            hapus = files.pop(index)
            print(f"\nFile '{hapus['nama']}' berhasil dihapus!\n")
        else:
            print("Nomor file tidak valid.")
    except ValueError:
        print("Eror: Input harus berupa angka yang tertera")
    except KeyboardInterrupt:
        print("\nError: Tidak boleh menggunakan Ctrl+C saat menghapus file.")

def sortir_file():
    if not files:
        print("Daftar file kosong.")
    else:
        sorted_files = sorted(files, key=lambda x: x['ekstensi'])
        print("\nDaftar file setelah disortir berdasarkan ekstensi:")
        print("-" * 68)
        print("No | Nama File                                          | Ekstensi")
        print("-" * 68)
        for index, f in enumerate(sorted_files):
            print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
        print("-" * 68)

def menu(role):
    while True:
        try:
            if role == "Karyawan":
                print("=" * 68)
                print("MENU SISTEM PENYORTIRAN FILE SESUAI EXTENSI")
                print("=" * 68)
                print("1. Tambah File")
                print("2. Tampilkan Daftar File")
                print("3. Keluar Program")
                
                pilih = input("Pilih menu: ").strip()
                
                if pilih == '1':
                    tambah_file()
                elif pilih == '2':
                    tampilkan_files()
                elif pilih == '3':  
                    print("Terima kasih, program selesai.")
                    break
                else:
                    raise ValueError("Input harus berupa angka 1 - 3.")

            elif role == "Manager":
                print("=" * 68)
                print("MENU SISTEM PENYORTIRAN FILE SESUAI EXTENSI")
                print("=" * 68)
                print("1. Tambah File")
                print("2. Tampilkan Daftar File")
                print("3. Edit File")
                print("4. Hapus File")
                print("5. Sortir File")
                print("6. Keluar Program")
                
                pilih = input("Pilih menu: ").strip()
                
                if pilih == '1':
                    tambah_file()
                elif pilih == '2':
                    tampilkan_files()
                elif pilih == '3':
                    edit_file()
                elif pilih == '4':
                    hapus_file()
                elif pilih == '5':
                    sortir_file()
                elif pilih == '6':
                    print("Terima kasih, program selesai.")
                    break
                else:
                    raise ValueError("Input harus berupa angka 1 - 6.")
            
            else:
                print("Role tidak dikenali. Program dihentikan.")
                break
        
        except KeyboardInterrupt:
            print("\nError: Tidak boleh menggunakan Ctrl+C saat di tampilan menu.")
        except Exception as e:
            print(f"Error : {e}\n")

if __name__ == "__main__":
    role = login()
    if role:
        menu(role)
