# Testausdokumentti

Ohjelmaa on testattu automatisoiduilla yksikkö- ja integraatiotesteillä unittestiä hyödyntäen sekä järjestelmätason testeillä manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

### Repositorio-luokat

Tietokantaoperaatioista vastaavaa repositorio-luokkaa `ScoreRepository` testataan `TestScoreRepository`-testiluokalla.

### Testauskattavuus

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu README.md tiedoston ja käyttöohjeen kuvaamalla tavalla sekä Linux-ympäristöön että yliopiston Cubbli Linux-virtuaalikoneella. Sovellusta on myös testattu tilanteessa, jossa käyttäjä unohtaisi tehdä alustustoimenpiteet komennolla `poetry run invoke build`. Tällöin `database.db`-tietokanta luodaan aina automaattisesti.

### Toiminnallisuudet

Kaikki määrittelydokumentissa ja käyttöohjeessa kerrotut toiminnallisuudet on käyty läpi manuaalisesti. Yllättäviä ongelmia tai bugeja ei ilmennyt testauksessa.

## Sovellukseen jääneet laatuongelmat

Kun käyttäjä testaa sovellusta, `test-database.db`-testitiedosto jää lojumaan repositorioon eikä poistu automaattisesti testauksen päättyessä.
