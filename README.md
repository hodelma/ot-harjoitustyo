# Kolikkokerääjä peli

Pelaaja voi pelata kolikkopeliä, jossa tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä kerätyistä kolikoista, mutta törmätessä hirviöön pisteet nollautuvat. Peli päättyy, kun pelaaja saavuttaa voittoehdon keräämällä 20 kolikkoa tai törmää hirviöön.


## Dokumentaatio

- [Vaatimusmäärittely](coin-collecter-app/dokumentaatio/vaatimusmaarittely.md)<br>
- [Arkkitehtuuri](coin-collecter-app/dokumentaatio/arkkitehtuuri.md)<br>
- [Työaikakirjanpito](coin-collecter-app/dokumentaatio/tuntikirjanpito.md)<br>
- [Changelog](coin-collecter-app/dokumentaatio/changelog.md)

<br>

>[!Important]
>Sinulla täytyy olla Python 3.12. versio ladattuna etukäteen — sovellus on toteutettu 3.12. versiolla. Tutustu asennusohjeisiin [täältä](https://www.python.org/downloads/)


## Asennusohjeet

**1. Kloonaa repositorio:**
```bash
git clone https://github.com/hodelma/ot-harjoitustyo.git
cd coin-collecter-app
```


**2. Asenna projektin riippuvuudet:**
```bash
poetry install
```


>[!TIP]
>Jos haluat määritellä itse SQLite-tietokantatiedoston nimen, toimi seuraavasti:
>
>Luo projektin juureen tiedosto nimeltä .env
>
>Lisää tiedostoon rivi haluamallasi tiedostonimellä ```DATABASE_FILENAME="OMA_TIEDOSTO_NIMI.db"```


**3. Suorita tarvittavat alustustoimenpiteet:**
```bash
poetry run invoke build
```


**4. Käynnistä sovellus (sovellus ei varsinaisesti avaudu, koska ei ole käyttöliittymää vielä):**
```bash
poetry run invoke start
```



## Käytössä olevat komennot


### Sovelluksen testaaminen
```bash
poetry run invoke test
```

### Testikattavuusraportti
```bash
poetry run invoke coverage-report
```
Coverage raportti generoituu *htmlcov*-hakemistoon


### Pylint
Tiedostossa .pylintrc määriteltyjen tarkistusten suoritus:
```bash
poetry run invoke lint
```

