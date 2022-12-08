import pyautogui
import os
import time
import copy
import datetime
from PIL import Image
import datetime
import time


#cała mapa = nowy image(RGB, (x/y = kratka x piksele), (cała biała))
cala_mapa = Image.new("RGB", (252 * 32, 252 * 32), (255, 255, 255))

step = 14
time.sleep(0.1)
jedna_kratka_ma_x_piksele = 32
mapa_ma_x_kratek = 252

piksel_w_gornym_lewym_rogu = [15,138]

for file_name in os.listdir("screenshots"):
    img = Image.open(os.path.join("screenshots", file_name))
    gorny_lewy_piksel = copy.copy(piksel_w_gornym_lewym_rogu)
    x = int(file_name[0:2])
    y = int(file_name[2:4])

    if y == 17:
        gorny_lewy_piksel[1] += step * jedna_kratka_ma_x_piksele

    if x == 15:
        gorny_lewy_piksel[0] += 8 * jedna_kratka_ma_x_piksele
    if x == 16:
        gorny_lewy_piksel[0] += (step + 8) * jedna_kratka_ma_x_piksele
    if x == 17:
        gorny_lewy_piksel[0] += (step + step + 8) * jedna_kratka_ma_x_piksele

    dolny_prawy_piksel = [gorny_lewy_piksel[0] + step * jedna_kratka_ma_x_piksele,
                          gorny_lewy_piksel[1] + step * jedna_kratka_ma_x_piksele]

    kafelek = img.crop([gorny_lewy_piksel[0],
                        gorny_lewy_piksel[1],
                        dolny_prawy_piksel[0],
                        dolny_prawy_piksel[1]])

    cala_mapa.paste(kafelek, (x * step * jedna_kratka_ma_x_piksele,
                              y * step * jedna_kratka_ma_x_piksele))


timestamp = time.time()
date_time = datetime.datetime.fromtimestamp(timestamp)
str_date_time = date_time.strftime("%d-%m-%Y_%H-%M-%S")

cala_mapa.save(os.path.join("output", f"homm3_map_scan_{str_date_time}.png"), "PNG")
