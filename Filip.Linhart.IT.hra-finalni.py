
#barvy
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

#cena opravy a seznam nazvu achievmentu
oprava_lodi = 100
achievmenty = {
    "Našel jsi opuštěnou bednu!",
    "Našel jsi mince!",
    "Klíček ti teď patří.",
    "Zámečník!",
}

#funkce na nacteni a kontrolu hodnot
def nacti_volbu(text, povolene_hodnoty):
    while True:
        volba = input(text).strip().lower()

        if volba in povolene_hodnoty:
            return volba

        print("Neplatná hodnota.")
        print("Povolené hodnoty jsou:", ", ".join(povolene_hodnoty))

#funkce na nacteni jmena
def nacti_jmeno():
    while True:
        jmeno = input("Jak se jmenuješ? ").strip()

        if jmeno:
            return jmeno

        print("Jméno nesmí být prázdné.")

#funkce pro aktualizaci stavu
def novy_stav():
    return {
        "zivoty": 100,
        "penize": 20,
        "jidlo": 3,
        "energie": 100,
        "inventar": [],
        "achievementy": set(),
        "nalezy": set(),
    }


def nalez(stav, nazev):
    if nazev in stav["nalezy"]:
        return False

    stav["nalezy"].add(nazev)
    return True

#funkce achievmentu
def achievment(stav, nazev):
    if nazev not in stav["achievementy"]:
        stav["achievementy"].add(nazev)
        print(yellow + "ACHIEVEMENT: " + nazev + reset)

#funkce konce cesty
def konec_cesty(stav):
    """Vyhodnotí vyčerpání a jídlo pouze u živého hráče."""
    if stav["zivoty"] <= 0:
        return

    if stav["energie"] <= 0:
        stav["zivoty"] = max(0, stav["zivoty"] - 10)

        if stav["zivoty"] <= 0:
            print("Byl jsi až moc vyřízený, až jsi z toho zkolaboval.")
            return

        print()
        print("Jsi velmi unavený.")
        print("Ztratil jsi 10 životů.")
        print("Zbývá ti:", stav["zivoty"])
        stav["energie"] = 20

    if stav["jidlo"] > 0:
        stav["jidlo"] -= 1
        stav["energie"] = min(100, stav["energie"] + 10)
        print("Najedl ses.")
        print("Zbývá jídla:", stav["jidlo"])

#funkce lesu
def les(stav):
    print()
    print("Po chvíli přemýšlení ses rozhodl, že prozkoumáš les.")
    print("Vstoupil jsi do tajemného temného lesa a rozhlédl ses.")
    print()
    print("Vidíš tři cesty.")
    print("1 - Jít doleva")
    print("2 - Jít doprava")
    print("3 - Jít rovně")

    cesta = nacti_volbu("Vyber cestu (1-3): ", ["1", "2", "3"])
    stav["energie"] = max(0, stav["energie"] - 40)

    if cesta == "1":
        print("Rozhodl ses jít doleva.")

        if nalez(stav, "bedna"):
            print("Po chvíli chůze jsi narazil na opuštěnou bednu.")
            print("Otevřel jsi ji a našel jsi uvnitř mince.")
            achievment(stav, "Našel jsi opuštěnou bednu!")
            achievment(stav, "Našel jsi mince!")
            stav["penize"] += 10
            print("Získal jsi 10 mincí.")
        else:
            print("Opuštěná bedna je už prázdná. Mince z ní už máš.")

    elif cesta == "2":
        print("Rozhodl ses jít doprava.")
        print("Po chvíli chůze jsi uslyšel divné zvuky.")
        print("Ale najednou se před tebou objevila divoká zvěř.")
        print("Podařilo se ti utéct, ale ztratil jsi energii.")
        achievment(stav, "Divoký nepřítel.")
        print("Utekl jsi mezi stromy a myslel sis, že jsi v bezpečí.")
        print("Ale najednou jsi uklouzl po mokrém listí a spadl jsi do hluboké jámy.")
        print("Dopadl jsi na kámen a vykrvácel jsi.")
        stav["zivoty"] = 0

    else:
        print("Rozhodl ses jít rovně.")

        if nalez(stav, "klic"):
            print("Jdeš už dlouho a najednou se ti něco leskne mezi stromy.")
            print("Je to starý klíč, který leží na zemi.")
            print("Sebral jsi ho a teď je tvůj.")
            stav["inventar"].append("klic")
            print("Klíč byl přidán do inventáře.")
            achievment(stav, "Klíček ti teď patří.")
        else:
            print("Místo, kde ležel klíč, je už prázdné.")
            print("Tento klíč už máš.")

#funkce prozkoumavani steny v jeskyni
def prozkoumej_steny(stav):
    odpoved = nacti_volbu(
        "Chceš prozkoumat stěny jeskyně? ano/ne: ",
        ["ano", "ne"],
    )

    if odpoved == "ne":
        print("Rozhodl ses odejít.")
        return

    if "svíčka" not in stav["inventar"]:
        print("V jeskyni je příliš tma a bez svíčky stěny nejde prozkoumat.")
        print("Možná by se nějaká svíčka dala najít v chatě.")
        return

    if nalez(stav, "mapa"):
        print("Díky světlu svíčky jsi našel starou kresbu.")
        print("Kresba ukazuje směr k majáku.")
        print("Získal jsi mapu.")
        stav["inventar"].append("mapa")
    else:
        print("Tuto část jeskyně už znáš. Mapu máš v inventáři.")

#funkce jeskyne
def jeskyne(stav):
    print()
    print("Chtěl ses podívat do jeskyně.")
    print("Vstoupil jsi do tajemné jeskyně.")
    print("Je zde velká kamenná brána.")
    stav["energie"] = max(0, stav["energie"] - 40)

    if "klic" in stav["inventar"]:
        if nalez(stav, "poklad"):
            print("Přišel jsi k bráně a všiml sis, že je tam zámek.")
            print("Vytáhl jsi klíč a dal ho do zámku.")
            print("Brána se otevřela!")
            achievment(stav, "Zámečník!")
            print("Vstoupil jsi dovnitř a na zemi jsi našel starou truhlu.")
            print("Vedle truhly ležela hora zlatých mincí.")
            print("Všechny jsi je posbíral.")
            stav["inventar"].append("poklad")
            stav["penize"] += 100
            print("Získal jsi 100 mincí.")
        else:
            print("Kamenná brána je už otevřená.")
            print("Místo, kde ležel poklad, je prázdné. Poklad už máš.")
    else:
        print("Brána je zamčena.")
        print("Nemáš klíč, třeba bys ho někde našel.")

    print()
    prozkoumej_steny(stav)


def chata(stav):
    print()
    print("Došel jsi ke staré chatě.")
    print("Dveře jsou otevřené.")
    print("1 - Prohledat stůl")
    print("2 - Prohledat skříň")
    print("3 - Odejít")

    volba = nacti_volbu("Vyber co uděláš (1-3): ", ["1", "2", "3"])

    if volba == "1":
        if nalez(stav, "svíčka"):
            print("Na stole leží svíčka.")
            stav["inventar"].append("svíčka")
            print("Získal jsi svíčku.")
        else:
            print("Stůl je prázdný. Svíčku už máš.")

    elif volba == "2":
        print("Ve skříni jsi našel konzervu jídla.")
        stav["jidlo"] += 2
        print("Získal jsi 2 kusy jídla.")

    else:
        print("Opouštíš chatu.")


def zobraz_inventar(stav):
    print()
    print("========== INVENTÁŘ ==========")

    if not stav["inventar"]:
        print("Tvůj inventář je prázdný.")
    else:
        for predmet in stav["inventar"]:
            print("-", predmet)

    print("Počet předmětů:", len(stav["inventar"]))


def zobraz_stav(stav, jmeno):
    print()
    print("========== TVŮJ STAV ==========")
    print("Jméno:", jmeno)
    print("Životy:", stav["zivoty"])
    print("Energie:", stav["energie"])
    print("Peníze:", stav["penize"])
    print("Jídlo:", stav["jidlo"])
    print("Splněné úkoly:", len(stav["achievementy"]))


def odpocinek(stav):
    print()
    print("Našel jsi bezpečné místo k odpočinku.")
    odpoved = nacti_volbu("Chceš si odpočinout? ano/ne: ", ["ano", "ne"])

    if odpoved == "ano":
        stav["energie"] = min(100, stav["energie"] + 30)
        print("Odpočinul sis.")
        print("Energie:", stav["energie"])
    else:
        print("Rozhodl ses pokračovat.")


def odjezd(stav):
    print()
    print("Došel jsi k přístavu.")
    print("Před tebou je stará loď.")

    chybi = []

    if "poklad" not in stav["inventar"]:
        chybi.append("- Chybí ti poklad.")

    if "mapa" not in stav["inventar"]:
        chybi.append("- Chybí ti mapa.")

    if stav["penize"] < oprava_lodi:
        chybi.append("- Na opravu lodi potřebuješ 100 mincí.")

    if chybi:
        print("Zatím nemáš vše potřebné.")
        for polozka in chybi:
            print(polozka)
        return False

    stav["penize"] -= oprava_lodi
    print("Máš poklad i mapu.")
    print("Použil jsi 100 mincí na opravu lodi.")
    print()
    print("GRATULUJEME!")
    print("Podařilo se ti opustit ostrov živý!")

    if achievmenty.issubset(stav["achievementy"]):
        print(yellow + "BONUS: Získal jsi všechny průzkumnické achievementy!" + reset)

    return True


def vypis_pribeh():
    print("13.7. Jsi vyrazil na loď.")
    print("Zapál jsi motor lodi a vyjel.")
    print("Najednou se ti začala třást loď, ale řekl sis, že to je jenom nějaká vlna.")
    print("Vlnu jsi přešel a přišla noc.")
    print("V noci tě vzbudila veliká bouřka a blesk ti udeřil do lodě.")
    print("Přišla obrovská vlna, která ti převrátila loď.")
    print("Otevřel jsi oči a zjistil jsi, že ses probudil na neznámém ostrově.")
    print("Musíš najít cestu domů.")
    print("Dokážeš to živý?")
    print()


def vypis_menu():
    print(blue + "-----------------------------------" + reset)
    print(green + "           KAM SE VYDÁŠ?" + reset)
    print(blue + "-----------------------------------" + reset)
    print("1 - Prozkoumat les")
    print("2 - Navštívit jeskyni")
    print("3 - Prozkoumat chatu")
    print("4 - Zkontrolovat inventář")
    print("5 - Zkontrolovat stav")
    print("6 - Odpočinout si")
    print("7 - Pokusit se o odjezd")
    print("8 - Ukončit hru")
    print("-----------------------------------")


def hra(jmeno):
    vypis_pribeh()
    stav = novy_stav()

    print("Hra začíná. Hodně štěstí!")
    print("Máš", stav["zivoty"], "životů, snaž se žádný neztratit.")
    print()
    print("Před tebou je les, jeskyně a stará chata.")
    print("Musíš se rozhodnout, kam půjdeš, nebo zemřeš.")

    while stav["zivoty"] > 0:
        print()
        vypis_menu()
        volba = nacti_volbu(
            "Jak se rozhodneš? ",
            ["1", "2", "3", "4", "5", "6", "7", "8"],
        )

        if volba == "1":
            les(stav)
            konec_cesty(stav)
        elif volba == "2":
            jeskyne(stav)
            konec_cesty(stav)
        elif volba == "3":
            chata(stav)
        elif volba == "4":
            zobraz_inventar(stav)
        elif volba == "5":
            zobraz_stav(stav, jmeno)
        elif volba == "6":
            odpocinek(stav)
        elif volba == "7":
            if odjezd(stav):
                print("Dokázal jsi opravit loď a vydat se domů,", jmeno, "gratuluji!")
                break
        else:
            print()
            print("Rozhodl ses ukončit hru.")
            print("Děkujeme za hraní!")
            break

    if stav["zivoty"] <= 0:
        print()
        print(red + "==============================" + reset)
        print(red + "          THE END" + reset)
        print(red + "==============================" + reset)
        print("Došly ti životy.")
        print("Ostrov se stal tvým novým domovem.")

    print()
    print("Děkuju za hraní,", jmeno)
    print("Pokud se ti hra líbila, neváhej mi napsat recenzi na GitHubu!")
    print()


def main():
    print(blue + "=" * 37 + reset)
    print(green + "       DOSTANEŠ SE DOMŮ ŽIVÝ?" + reset)
    print(blue + "=" * 37 + reset)

    jmeno = nacti_jmeno()
    print("Vítej ve hře,", jmeno)
    print()

    while True:
        start = nacti_volbu(
            "Chceš spustit hru? ano/ne: ",
            ["ano", "ne"],
        )

        if start == "ne":
            break

        hra(jmeno)

    print()
    print(red + "===================================" + reset)
    print(green + "          KONEC HRY" + reset)
    print(red + "===================================" + reset)


if __name__ == "__main__":
    main()
