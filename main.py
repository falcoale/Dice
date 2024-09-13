# Spero vi piaccia :)

import json
import os
import random
import time

ascii_intro = """
▓█████▄  ██▓ ▄████▄  ▓█████     ▄▄▄▄ ▓██   ██▓     █████▒▄▄▄       ██▓     ▄████▄   ▒█████   ▄▄▄       ██▓    ▓█████ 
▒██▀ ██▌▓██▒▒██▀ ▀█  ▓█   ▀    ▓█████▄▒██  ██▒   ▓██   ▒▒████▄    ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▒████▄    ▓██▒    ▓█   ▀ 
░██   █▌▒██▒▒▓█    ▄ ▒███      ▒██▒ ▄██▒██ ██░   ▒████ ░▒██  ▀█▄  ▒██░    ▒▓█    ▄ ▒██░  ██▒▒██  ▀█▄  ▒██░    ▒███   
░▓█▄   ▌░██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ░▓█▒  ░░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░░██▄▄▄▄██ ▒██░    ▒▓█  ▄ 
░▒████▓ ░██░▒ ▓███▀ ░░▒████▒   ░▓█  ▀█▓░ ██▒▓░   ░▒█░    ▓█   ▓██▒░██████▒▒ ▓███▀ ░░ ████▓▒░ ▓█   ▓██▒░██████▒░▒████▒
 ▒▒▓  ▒ ░▓  ░ ░▒ ▒  ░░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒     ▒ ░    ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░
 ░ ▒  ▒  ▒ ░  ░  ▒    ░ ░  ░   ▒░▒   ░▓██ ░▒░     ░       ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░   ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░
 ░ ░  ░  ▒ ░░           ░       ░    ░▒ ▒ ░░      ░ ░     ░   ▒     ░ ░   ░        ░ ░ ░ ▒    ░   ▒     ░ ░      ░   
   ░     ░  ░ ░         ░  ░    ░     ░ ░                     ░  ░    ░  ░░ ░          ░ ░        ░  ░    ░  ░   ░  ░
 ░          ░                        ░░ ░                                 ░                                                                                                                                                                                                                                                                                            
"""
def intro():
    print(ascii_intro)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(intro())
    print("Lancia il dado premento invio. Crediti scrivendo 1.")
    lancio = input(">> ")

    if str(lancio) == "":
        try:
            with open("dadi.json", "r") as f:
                dado = json.load(f)
                dado = random.choice(dado)
                print(f"{dado}")
                print("Per rilanciare aspetta un secondo.")
                time.sleep(1)
                main()
        except Exception as e:
            print(f"Errore nel caricamento del dado: {e}")
    elif lancio == "1":
        print("Profilo GitHub ↪ https://github.com/falcoale")
        print(f"↩ Torna indietro premendo invio")
        scelta = input(">> ")
        try:
            if scelta == "":
                main()
        except Exception as e:
            print(f"Errore: {e}")
    else:
        print(f"Riprova.")


if __name__ == "__main__":
    main()



