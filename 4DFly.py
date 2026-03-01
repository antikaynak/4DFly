from pyfiglet import Figlet
from colorama import init, Fore, Style
import os
import time

init(autoreset=True)


P = 1.225
N_VISCOSITY = 0.00001781
G_GRAVITY = 9.81


os.system('cls' if os.name == 'nt' else 'clear')
f = Figlet(font='big')
print(Fore.CYAN + f.renderText('\== 4DFLY ==/') + Style.RESET_ALL)
print(Fore.CYAN + """⠀⠀⠀⣖⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⡆⠹⡀⣠⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⡧⢤⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡧⢄⣹⣅⣜⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⢹⠚⠃⠀⠀⠀⠀⠀
⠀⣀⠴⢒⣉⡹⣶⣤⣀⡉⠉⠒⠒⠒⠒⠤⠤⣀⣀⣀⠇⠀⠀⢸⠠⣄⠀⠀⠀⠀⠀
⠀⠈⠉⠁⠀⠀⠀⠉⠒⠯⣟⣲⠦⣤⣀⡀⠀⠀⠈⠉⠉⠉⠛⠒⠻⢥⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣲⡬⠭⠿⢷⣦⣤⢄⣀⠀⠀⠚⠛⠛⠓⢦⡀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠚⠉⠁⠀⠀⠀⠀⣀⣉⡽⣕⣯⡉⠉⠉⠑⢒⣒⡾
⠀⠀⣀⡠⠴⠒⠉⠉⠀⢀⣀⣀⠤⡤⢶⣶⣋⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀
⣖⣉⣁⣠⠤⠶⡶⡶⢍⡉⠀⠀⠀⠙⠒⠯⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠁⠀⠀⠀⠀⠑⢦⣯⠇""")


print(Fore.YELLOW + "=" * 50)
print(Fore.GREEN + "          ANA MENÜ          ".center(50))
print(Fore.YELLOW + "=" * 50)
print(Fore.WHITE + "1. Reynolds Hesabı")
print(Fore.WHITE + "2. Drag Hesabı")
print(Fore.WHITE + "3. Vektör ve Kanat Alanı Hesabı")
print(Fore.WHITE + "4. Lift Hesabı")
print(Fore.WHITE + "5. V Stall Hesabı")
print(Fore.WHITE + "6. kg to N")
print(Fore.WHITE + "7. Sonuç Analiz")
print(Fore.WHITE + "8. m/s to kmh")
print(Fore.WHITE + "9. m/s to knot")
print(Fore.RED + "10. Çıkış")
print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)

secenekler = {
    "1": "Reynolds Hesabı", "2": "Drag Hesabı", "3": "Vektör ve Kanat Alanı Hesabı",
    "4": "Lift Hesabı", "5": "V Stall Hesabı", "6": "kg to N",
    "7": "Sonuç Analiz", "8": "m/s to kmh", "9": "m/s to Knot", "10": "çıkış"
}


def güvenli_input(mesaj, tip=float):
    while True:
        try:
            return tip(input(mesaj))
        except ValueError:
            print(Fore.RED + "Hata: Lütfen geçerli bir sayı giriniz!" + Style.RESET_ALL)

while True:
    secim = input(Fore.CYAN + "Seçiminizi yapın (1-10): " + Style.RESET_ALL)
    
    if secim in secenekler:
        if secim == "10":
            print(Fore.RED + "Çıkış yapılıyor..." + Style.RESET_ALL)
            break
            
        print(Fore.GREEN + f"\n{secenekler[secim]} seçildi!" + Style.RESET_ALL)
        
        if secim == "1":
            print(Fore.LIGHTMAGENTA_EX + "=" * 50)
            c = güvenli_input(Fore.LIGHTBLACK_EX + "c değeriniz: " + Style.RESET_ALL)
            hizlar = []
            for i in range(1, 6):
                v = güvenli_input(f"{i}. hız (m/s): ")
                hizlar.append(v)
            
            for v in hizlar:
                reynold = (P * v * c) / N_VISCOSITY
                print(f"{Fore.WHITE}{v} M/S reynoldunuz: {Fore.YELLOW}{reynold:.2f}")
            print(Fore.LIGHTMAGENTA_EX + "=" * 50)

        elif secim == "2":
            print(Fore.LIGHTRED_EX + "=" * 50)
            V = güvenli_input(Fore.LIGHTBLACK_EX + "m/s hız: " + Style.RESET_ALL)
            S = güvenli_input(Fore.LIGHTBLACK_EX + "kanat alanı: " + Style.RESET_ALL)
            cd = güvenli_input(Fore.LIGHTBLACK_EX + "Cd değeri: " + Style.RESET_ALL)
            D = 0.5 * P * (V**2) * S * cd
            print(Fore.LIGHTRED_EX + f"Drag değeriniz: {D:.4f}")
            print(Fore.LIGHTRED_EX + "=" * 50)

        elif secim == "3":
            print(Fore.LIGHTYELLOW_EX + "=" * 50)
            kalin = güvenli_input(Fore.LIGHTBLACK_EX + "kanadın kök kordu: " + Style.RESET_ALL)
            ince = güvenli_input(Fore.LIGHTBLACK_EX + "kanadın uc kordu: " + Style.RESET_ALL)
            span = güvenli_input(Fore.LIGHTBLACK_EX + "kanat açıklığı: " + Style.RESET_ALL)
            c_avg = (kalin + ince) / 2
            alan = c_avg * span
            print(Fore.LIGHTYELLOW_EX + f"kanat veter (c): {c_avg}\nkanat alan: {alan}")
            print(Fore.LIGHTYELLOW_EX + "=" * 50)

        elif secim == "4":
            print(Fore.LIGHTCYAN_EX + "=" * 50)
            V = güvenli_input(Fore.LIGHTBLACK_EX + "m/s hız: " + Style.RESET_ALL)
            S = güvenli_input(Fore.LIGHTBLACK_EX + "kanat alanı: " + Style.RESET_ALL)
            cl = güvenli_input(Fore.LIGHTBLACK_EX + "Cl değeri: " + Style.RESET_ALL)
            L = 0.5 * P * (V**2) * S * cl
            print(Fore.LIGHTYELLOW_EX + f"lift değeriniz: {L:.4f}")
            print(Fore.LIGHTCYAN_EX + "=" * 50)

        elif secim == "5":
            print(Fore.LIGHTBLUE_EX + "=" * 50)
            W = güvenli_input(Fore.LIGHTBLACK_EX + "W değeri: " + Style.RESET_ALL)
            S = güvenli_input(Fore.LIGHTBLACK_EX + "kanat alanı: " + Style.RESET_ALL)
            cl = güvenli_input(Fore.LIGHTBLACK_EX + "Cl değeri: " + Style.RESET_ALL)
            v_stall = ((2 * W) / (P * S * cl))**0.5
            print(Fore.LIGHTBLUE_EX + f"V-stall: {v_stall:.2f}")
            print(Fore.LIGHTBLUE_EX + "=" * 50)

        elif secim == "6":
            print(Fore.MAGENTA + "-" * 50)
            kg = güvenli_input("kilo: ")
            print(f"W değeriniz: {kg * G_GRAVITY:.2f} N")
            print(Fore.MAGENTA + "-" * 50)

        elif secim == "7":
            print(Fore.MAGENTA + "■" * 50)
            kgton = güvenli_input("kilogram ağırlığınız: ") * G_GRAVITY
            hizlar = [güvenli_input(f"{i+1}. M/s hız: ") for i in range(5)]
            Vstall2 = güvenli_input("Vstall: ")
            lift2 = güvenli_input("Lift değeriniz: ")
            
            print(Fore.LIGHTYELLOW_EX + "Analiz ediliyor..." + Style.RESET_ALL)
            time.sleep(1.5)
            print(Fore.GREEN + "Analiz başarılı ✓" + Style.RESET_ALL)
            print(Fore.MAGENTA + "-" * 70)

            for v in hizlar:
                if v > Vstall2:
                    print(f"{Fore.GREEN}| {v} M/s uçmaya uygun ✓")
                elif v < Vstall2:
                    print(f"{Fore.RED}| {v} M/s uçmaya uygun değil ✕")
                else:
                    print(f"{Fore.YELLOW}| {v} M/s Havada asılı kalma sınırı")
            
            print(Fore.MAGENTA + "-" * 70)
            if lift2 >= kgton:
                print(Fore.GREEN + "Lift değeriniz ağırlığınızı taşıyabilir ✓")
            else:
                print(Fore.RED + "Lift yetersiz! Kanat alanını büyütmek veya ağırlık azaltmak çözüm olabilir.")
            print(Fore.MAGENTA + "■" * 50)

        elif secim == "8":
            ms = güvenli_input("metre saniye: ")
            print(f"kmh: {ms * 3.6}")

        elif secim == "9":
            ms = güvenli_input("metre saniye: ")
            print(f"m/s: {ms}\nknot: {ms * 1.9438}")
    else:
        print(Fore.RED + "Geçersiz seçim, 1-10 arası bir sayı girin." + Style.RESET_ALL)