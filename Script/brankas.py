import hashlib
import os

SALT = b"GaramRahasiaWarungPakDengklek123!"
HASH_TARGET_HEX = "3071b6b92ca8deff1077448d1a08f4dbd290bf0627986f4fbcb7c3d2cf1623b1"
NAMA_FILE = "../Note/password.txt"

if not os.path.exists(NAMA_FILE):
    print(f"[-] Error: File '{NAMA_FILE}' tidak ditemukan!")
    exit()

print(f"[+] File '{NAMA_FILE}' ditemukan. Memulai proses pemindaian enkripsi...")

status_ketemu = False

with open(NAMA_FILE, "r", encoding="utf-8", errors="ignore") as psw:
    for line in psw:
        password_coba = line.strip()
        
        if not password_coba or password_coba.startswith("#"):
            continue
        
        hash_input = hashlib.pbkdf2_hmac(
            'sha256', 
            password_coba.encode(), 
            SALT, 
            1000
        ).hex()
        
        if hash_input == HASH_TARGET_HEX:
            print("\n" + "="*40)
            print("[+] AKSES BRANKAS DITERIMA!")
            print(f"[+] Password Valid Ditemukan: {password_coba}")
            print("[+] Gunakan password ini untuk membuka rekaman CCTV!")
            print("="*40)
            status_ketemu = True
            break

if not status_ketemu:
    print("\n[-] Proses selesai. Tidak ada password yang cocok di dalam 'password.txt' kamu.")