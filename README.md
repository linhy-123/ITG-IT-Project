# Dostaneš se domů živý?

Krátká textová hra v Pythonu. Po bouřce ztroskotáš na neznámém ostrově a musíš najít způsob, jak se dostat domů.

## Spuštění

Otevři terminál ve složce se souborem hry a spusť:

```bash
python3 Filip.Linhart.IT.hra-finalni.py
```

Zadej své jméno a potom potvrď spuštění hry volbou `ano`.

## Jak hrát

V hlavní nabídce zadej číslo místa nebo činnosti:

- **Les:** Doleva můžeš najít mince, rovně klíč. Cesta doprava končí pádem do jámy a smrtí.
- **Jeskyně:** Klíčem otevřeš bránu a získáš poklad. Se svíčkou můžeš prozkoumat stěny a najít mapu.
- **Chata:** Na stole najdeš svíčku, ve skříni dva kusy jídla.
- **Inventář a stav:** Zkontroluješ nalezené předměty, životy, energii, peníze a jídlo.
- **Odpočinek:** Obnovíš si až 30 energie, nejvýše však na 100.
- **Odjezd:** U přístavu můžeš zkusit opravit loď a opustit ostrov.

Čísla vybírej podle nabídky. U otázek s odpovědí ano/ne napiš `ano` nebo `ne`; při neplatné odpovědi hra požádá o novou.

## Jak vyhrát

Najdi klíč v lese, otevři jím bránu v jeskyni, vezmi poklad a se svíčkou prozkoumej stěny, abys získal mapu. Na opravu lodi potřebuješ 100 mincí. U přístavu pak musíš mít poklad, mapu, svíčku, alespoň 100 mincí a tři achievementy. Pokud splníš také všechny čtyři průzkumnické achievementy, zobrazí se bonusová hláška.

Prozkoumávání lesa a jeskyně stojí energii. Když energie klesne na nulu nebo níže, ztratíš 10 životů; pokud máš jídlo, na konci takového tahu ho sníš a získáš 10 energie. Dávej pozor na životy a vyhýbej se cestě doprava v lese.
