from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
image = Image.open(
    "C:\\Users\\Administrator\\Documents\\Semester V\\Pemrograman Fungsional\\Modul 6\\Test.jpg")

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer_brightness = ImageEnhance.Brightness(image)
enhancer_contrast = ImageEnhance.Contrast(image)

# Kali 1.5 untuk tingkat kecerahan dan 1.2 untuk tingkat kontras
brightness_factor = 1.5
contrast_factor = 1.2

brightened_image = enhancer_brightness.enhance(brightness_factor)
final_image = enhancer_contrast.enhance(contrast_factor)

# TODO 3: Simpan gambar hasil edit
final_image.save("brightness_contrast_image.jpg")

# TODO 4: Tampilkan
final_image.show()
