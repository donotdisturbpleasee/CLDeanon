import os

print("\033[33mОбновление python3-pip...\033[0m")
os.system("pip3 install --upgrade pip")
print("")
bib = ["html5lib", "phonenumbers", "requests", "bs4",  "urllib3"]
for i in range(len(bib)):
    print("\033[33mУстановка "+bib[i]+"...\033[0m")
    os.system("pip3 install "+bib[i])
print('\033[32mУстановка завершена!\033[0m')
