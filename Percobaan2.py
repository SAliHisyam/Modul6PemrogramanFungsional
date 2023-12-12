from PIL import Image

# Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open(
    "C:\\Users\\Administrator\\Documents\\Semester V\\Pemrograman Fungsional\\Modul 6\\white.png")
overlay_image = Image.open(
    "C:\\Users\\Administrator\\Documents\\Semester V\\Pemrograman Fungsional\\Modul 6\\Test.jpg")

# Pastikan kedua gambar memiliki mode warna yang sama (misalnya, mode RGB)
background_image = background_image.convert("RGB")
overlay_image = overlay_image.convert("RGB")

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))

# Simpan gambar hasil edit dalam format yang sama seperti gambar latar belakang (misalnya, JPEG)
background_image.save("hasil_edit_gambar.jpg")

# Tampilkan gambar hasil edit
background_image.show()
