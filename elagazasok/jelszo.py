"""
6️ Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.

"""
print("enter the password")
password = input()
if password == "titok" :
    print("correct password")
else : 
    print("password incorrect")