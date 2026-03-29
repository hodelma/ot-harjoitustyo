# Kolikkokerääjä -peli

Sovelluksen avulla pelaajan on mahdollista pelata kolikkopeliä, jossa tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä kerätyistä kolikoista, mutta törmätessä hirviöön pisteet nollautuvat. Peli päättyy, kun pelaaja saavuttaa voittoehdon keräämällä 20 kolikkoa tai törmää hirviöön.


## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)<br>
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)<br>
- [Changelog](coin-collecter-app/dokumentaatio/changelog.md)

>[!Important]
>Sinulla täytyy olla Python 3.12. versio ladattuna etukäteen — sovellus on toteutettu 3.12. versiolla. Tutustu asennusohjeisiin [täältä](https://www.python.org/downloads/)


## Asennusohjeet

1. Asenna projektin riippuvuudet:
```bash
poetry install --no-root
```

2. *Alustustoimenpiteet (päivittyy myöhemmin)*


3. Käynnistä sovellus (sovellus ei ns. avaudu, koska ei ole käyttöliittymää vielä):
```bash
poetry run invoke start
```

## Käytössä olevat komennot

### Sovelluksen testaaminen
```bash
poetry run invoke test
```

### Testikattavuuden tarkistaminen coveragella
```bash
poetry run invoke coverage
```

### Testikattavuusraportin generointi
```bash
poetry run invoke coverage-report
``` 
