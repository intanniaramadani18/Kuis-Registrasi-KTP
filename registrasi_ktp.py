import json
import os

NAMA_FILE = "data_biodata.json"

def muat_data():
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r", encoding="utf-8") as file:
          return json.load(file)
    return []

def simpan_data(data):
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def tambah_data(data):
    print("\n==== TAMBAH DATA PRIBADI ====")

    nik = input("NIK (16 digit): ").strip()

    if not nik.isdigit() or len(nik) != 16:
        print("NIK harus 16 digit angka!")
        return

    if any(orang["NIK"] == nik for orang in data):
        print("NIK sudah tedaftar!")
        return

    kolom = [
        ("Nama Lengkap", "Nama lengkap"),
        ("Tempat Lahir", "Tempat lahir"),
        ("Tanggal Lahir", "Tanggal lahir"),
        ("Jenis Kelamin", "Jenis kelamin"),
        ("Alamat", "Alamat"),
        ("Agama", "Agama"),
        ("Status Perkawaninan", "Status Perkawaninan"),
        ("Nomor HP", "Nomor HP"),
        ("Pekerjaan", "Pekerjaan"),
        ("Kewarganegaraan", "Kewarganegaraan"),
        ("Email", "Email"),
        ("Pendidikan Terakhir", "Pendidikan Terakhir"),
        ("Hobi", "Hobi")  
    ]

    biodata = {"NIK": nik}

    for kunci, pertanyaan in kolom:
        nilai = input(pertanyaan + ": ").strip()

        if not nilai:
            print("Data tidak boleh kosong!")
            return

        biodata[kunci] = nilai

    data.append(biodata)
    simpan_data(data)
    print("\nRegistrasi berhasil!")

def lihat_data(data):
    if not data:
        print("\nBelum ada data terdaftar.")
        return

    for nomor, orang in enumerate(data, start=1):
        print(f"\n==== PROFIL ORANG KE-{nomor} ====")
        for kunci, nilai in orang.items():
            print(f"{kunci:<22}: {nilai}")

def cari_profil(data):
    nik = input("Masukkan NIK yang dicari: ").strip()

    for orang in data:
        if orang["NIK"] == nik:
            print("\n=== PROFIL DITEMUKAN ===")
            for kunci, nilai in orang.items():
                print(f"{kunci:<22}: {nilai}")
            return

    print("Profil tidak ditemukan.")


def menu():
    data = muat_data()

    while True:
        print("\n=== SISTEM REGISTRASI BIODATA ===")
        print("1. Tambah Data Pribadi")
        print("2. Lihat Semua Profil")
        print("3. Cari Profil")
        print("4. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            lihat_data(data)
        elif pilihan == "3":
            cari_profil(data)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


menu()
