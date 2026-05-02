import re

def pridej_vlnovky(vstupni_soubor, vystupni_soubor):
    try:
        with open(vstupni_soubor, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Chyba: Soubor '{vstupni_soubor}' nebyl nalezen.")
        return

    # 1. POUZE jednopísmenné předložky a spojky (k, s, v, z, o, u, a, i)
    # (?i) ignoruje velikost písmen, takže chytne i "V lese", "A proto"
    text = re.sub(r'(?i)(?<![a-zA-Z\\])\b(k|s|v|z|o|u|a|i)\s+', r'\1~', text)

    # 2. Čísla a jednotky/symboly (např. 10 kg, 100 %, 5 °C)
    text = re.sub(r'\b(\d+)\s+([a-zA-Z%°])', r'\1~\2', text)

    # 3. Křížové odkazy (Obr. X, Tab. Y, kapitola Z)
    text = re.sub(r'\b(Obr\.|Tab\.|Kap\.|Příloha|kapitola|kapitole|obrázku|tabulce)\s+(\d+|[A-Z]|\\ref)', r'\1~\2', text)

    # 4. Mezery uvnitř zkratek (tzn., atd., apod.)
    text = re.sub(r'\b(tzv\.|tzn\.|atd\.|apod\.)\s+', r'\1~', text)

    with open(vystupni_soubor, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Hotovo! Vlnovky byly úspěšně doplněny (dle striktních pravidel) a soubor uložen jako '{vystupni_soubor}'.")

if __name__ == "__main__":
    # Zde si uprav názvy souborů
    pridej_vlnovky('dp.tex', 'dp_s_vlnovkami.tex')