import random

def skor():
    galatasaray_skor = random.randint(1, 10)
    fenerbahce_skor = random.randint(1, 10)
    return galatasaray_skor, fenerbahce_skor

gs_skor, fb_skor = skor()
print(f"Galatasaray Skoru: {gs_skor}")
print(f"Fenerbahçe Skoru: {fb_skor}")

if gs_skor > fb_skor:
    print("Galatasaray kazandı yaşa cimbom !")
elif fb_skor > gs_skor:
    print("Fenerbahçe kazandı")
else:
    print("Maç berabere bitti")
