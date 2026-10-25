# Library of Exercises

Responzivní statický e-shop v češtině: katalog, detaily, košík, digitální materiály a merch, vložené objednávkové formuláře FAPI. Bez animací.

## Spuštění

Bez instalace závislostí a bez sestavení:

```sh
python3 -m http.server 8000
```

Otevřete http://localhost:8000/.

## Úpravy

- `index.html`: hlavička, navigace a patička.
- `app.js`: stránky, košík a propojení s formuláři.
- `products.js`: produkty, ceny, odkazy a kódy FAPI.
- `style.css`: vzhled a responzivita.
- `assets/`: produktové obrázky a fotografie.

Po úpravě JS/CSS spusťte `python3 scripts/version-assets.py` pro aktualizaci verzí souborů v prohlížečové cache.

## Publikování

Celý obsah kořene repozitáře lze nahrát na statický hosting. Relativní cesty podporují i umístění v podadresáři. V GitHub Pages lze vybrat Settings → Pages → větev `main` → složka `/ (root)`. Nahrání repozitáře samotné Pages neaktivuje.

## Objednávky

Digitální produkty mají v košíku nejvýše 1 kus. Vyšší dříve uložené množství se upraví na 1. FAPI formuláři se předává kód produktu, počet kusů a české výchozí nastavení. Jednotlivé produkty se objednávají samostatně.

Objednávky, platby a dodání zajišťují existující formuláře FAPI. Pevný zákaz ruční změny množství uvnitř FAPI je nutné nastavit v jeho administraci. Web neobsahuje API klíče ani vlastní formulář pro platební karty. Platba může pokračovat na zabezpečené bráně. Merch má prodej pozastavený; Tematické hry nemají funkční objednávkový odkaz.

## Indexování a práva

Součástí jsou značka `noindex, nofollow, noarchive, nosnippet` a `robots.txt` s `Disallow: /`. Neomezují přístup a nezaručují úplné vyloučení z vyhledávačů. Soubor `_headers` platí pouze pro podporované hostingy, GitHub Pages jej nepoužívá.

Fotografie, grafika a materiály náleží příslušným autorům; tento repozitář neuděluje novou licenci. Nabídka byla ověřena 25. 10. 2026.
