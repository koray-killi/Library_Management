#   Wrap-up Project
#   Title: Library Management System
#   by: koraykilli

class kitap: # Class of Books
    ID = 0
    def __init__(self,KitapAdi,Yazar,genre,BasimTarihi):
        self.ID = kitap.ID
        kitap.ID +=1
        self.KitapAdi = KitapAdi
        self.Yazar = Yazar
        self.genre = genre
        self.BasimTarihi = BasimTarihi
    def ozellikler(self):
        return print(f"ID: {self.ID}, Kitap Adı: {self.KitapAdi}, Yazar: {self.Yazar}, Tür: {self.genre}, Basım Tarihi: {self.BasimTarihi}")

# Data-get Functions
def kitap_get():
    kitaplist = []
    with open("books.txt","r") as books:
        for i in books.readlines():
            ilist = i.strip().split(",")
            kitaplist.append(kitap(ilist[0],ilist[1],ilist[2],ilist[3]))
    return kitaplist
def userkey_get(location_of_text,split_character):
    with open(location_of_text,"r") as acc:
        accounts = dict()
        damn = bool()
        for i in acc.readlines():
            accs = ""
            passa = ""
            for j in i:
                j = j.strip()
                if damn == True:
                    passa+= j
                else:
                    if j != split_character:
                        accs+= j
                        
                    else:
                        damn = True
            accounts[accs] = passa
            damn = False
    return accounts
kitap_list = kitap_get() # To get books information as class(kitap).
account_dict = userkey_get("accounts.txt",";") # To get accounts information as dictionary.
# Main Menu's Functions
def kitaplari_listele(kitapliste):
    print("ID\tKitap Adı\tYazar\tTür\tBasım Tarihi")
    for i in kitapliste:
            print(f"{i.ID}\t{i.KitapAdi}\t{i.Yazar}\t{i.genre}\t{i.BasimTarihi}")
    return
def kitap_ekle(kitapliste):
    yeni = []
    parametre = ["isim","yazar","tür","basım tarihi"]
    for i in parametre:
        x = input(f"Lütfen yeni kitabın {i} bilgisini giriniz: ")
        if x == "":
            print(f"Kısım: '{i}' boş bırakılamaz!")
            return
        else:
            yeni.append(x)
    kitapliste.append(kitap(yeni[0],yeni[1],yeni[2],yeni[3]))
    return kitapliste
def kitap_sil(kitapliste):
    x = int(input("Lütfen Silinecek kitabın ID'sini yazınız:"))
    if len(kitapliste)<x+1:
        print("\033[91mSayı ID'lerden büyük olamaz!\033[0m")
        return
    else:
        kitapliste.remove(kitapliste[x])
        return kitapliste
def kitap_ara(kitapliste):
    aranacak = input("Lütfen anahtar kelimeyi yazınız: ")
    if aranacak == "":
        print("\033[91mAranacak alan boş bırakılamaz!\033[0m")
        return
    else:
        no_result = 1
        for i in kitapliste:
            if aranacak in i.KitapAdi:
                print(f"\033[92m{i.ID}\t{i.KitapAdi}\t{i.Yazar}\t{i.genre}\t{i.BasimTarihi}\033[0m")
                no_result = 0
            elif aranacak in i.Yazar:
                print(f"\033[92m{i.ID}\t{i.KitapAdi}\t{i.Yazar}\t{i.genre}\t{i.BasimTarihi}\033[0m")
                no_result = 0
            elif aranacak in i.genre:
                print(f"\033[92m{i.ID}\t{i.KitapAdi}\t{i.Yazar}\t{i.genre}\t{i.BasimTarihi}\033[0m")
                no_result = 0
            elif aranacak in i.BasimTarihi:
                print(f"\033[92m{i.ID}\t{i.KitapAdi}\t{i.Yazar}\t{i.genre}\t{i.BasimTarihi}\033[0m")
                no_result = 0
        if no_result == 1:
            print("\033[91mKitap bulunamadı!\033[0m")
        return
def kaydet_ve_cik(accounts,kitapliste):
    with open("accounts.txt","w") as accs:
        for i in accounts.keys():
            if list(accounts.keys())[-1] == i:
                accs.write(f"{i};{accounts[i]}")
            else:
                accs.write(f"{i};{accounts[i]}\n")
    with open("books.txt","w") as book:
        for i in kitapliste:
            if i == kitapliste[-1]:
                book.write(f"{i.KitapAdi},{i.Yazar},{i.genre},{i.BasimTarihi}")
            else:
                book.write(f"{i.KitapAdi},{i.Yazar},{i.genre},{i.BasimTarihi}\n")
    return       
# Login Function and Main Menu Loop
def login(x):
    username = input("Lütfen Kullanıcı adınızı giriniz (0 to exit): ")
    password = input("Lütfen şifrenizi giriniz (0 to exit): ")
    if username == "0" and password == "0":
        return quit()
    for i in x.keys():
        if username == i:
            if password == x[i]:
                print(f"\033[92mGiriş Başarılı, Hoşgeldin {i}!\033[0m")
                return
    print("\033[91mGeçersiz şifre veya kullanıcı adı, lütfen tekrar deneyiniz!\033[0m")
    return login(x)       
print("\033[93mKütüphane Yönetim Sistemine Hoşgeldiniz!\033[0m")
login(account_dict)
while True:
    print("1. Tüm Kitapları Listele") ##
    print("2. Kitap Ara") ##
    print("3. Yeni Kitap Ekle") ##
    print("4. Kitap Sil") ##
    print("7. Sistemi Kaydet ve Çık") ##

    secim = input("Lütfen bir işlem seçiniz (1-7): ")
        
    if secim == '1':
        kitaplari_listele(kitap_list)
    elif secim == '2':
        kitap_ara(kitap_list)
    elif secim == '3':
        kitap_list = kitap_ekle(kitap_list)
    elif secim == '4':
        kitap_list = kitap_sil(kitap_list)
    elif secim == '5':
        # kitap_odunc_al()
        print("")
    elif secim == '6':
        # kitap_iade_et()
        print("")
    elif secim == '7':
        kaydet_ve_cik(account_dict,kitap_list)
        print("Sistemden çıkılıyor...")
        break
    else:
        print("Geçersiz giriş! Lütfen 1 ile 7 arasında bir seçim yapınız.")
