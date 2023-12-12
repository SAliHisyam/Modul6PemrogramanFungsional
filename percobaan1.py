from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# Pastikan untuk mengganti 'path_to_image' dengan direktori file gambar yang ingin Anda gunakan
path_to_image = "C:\\Users\\Administrator\\Documents\\Semester V\\Pemrograman Fungsional\\Modul 6\\Test.jpg"
gambarku = Image.open(path_to_image)

# TODO 2: Ubah gambar menjadi hitam-putih
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
nama = "SAYID MUHAMMAD ALI HISYAM FAHLEVI"  # Ganti dengan nama Anda
nim = "202110370311422"    # Ganti dengan NIM Anda
# Ganti dengan direktori font Arial yang Anda unduh
direktoriFont = "C:/Windows/Fonts/arial.ttf"
ukuranFont = 24

draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype(direktoriFont, ukuranFont)
text = f"{nama}\n{nim}"

# Mendapatkan ukuran text menggunakan ImageFont.getsize
text_width, text_height = draw.textbbox((0, 0), text, font=font)[
    2:]  # Mengambil width dan height saja

text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
nama_file_hasil = "percobaan_satu.jpg"
gambarBW.save(nama_file_hasil)

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
