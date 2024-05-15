from Paketler.samit import samitleri_al

if __name__ == "__main__":
    cumle = input("Bir cümle girin: ")
    samitler = samitleri_al(cumle)
    print("Sonuç:", samitler)
