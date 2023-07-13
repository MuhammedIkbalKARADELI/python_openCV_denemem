# İkinci program
import birinci_program
print(f"İkinci programın içindeki name: {__name__}")  # __main__

print("Ben ikinci programın içinde if name == main ifadesinin dışındayım")


if __name__ == "__main__":
    print("İkinci programın içinde name != main ")


