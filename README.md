# Kolikkokerääjä peli

Pelaaja voi pelata kolikkopeliä, jossa tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä kerätyistä kolikoista, mutta törmätessä hirviöön kolme kertaa, pelaaja häviää. Pelaaja voittaa pelin, kun kerää vähintään 20 kolikkoa.


## Dokumentaatio

- [Vaatimusmäärittely](coin-collecter-app/dokumentaatio/vaatimusmaarittely.md)<br>
- [Arkkitehtuuri](coin-collecter-app/dokumentaatio/arkkitehtuuri.md)<br>
- [Käyttöohje](coin-collecter-app/dokumentaatio/kayttoohje.md)<br>
- [Työaikakirjanpito](coin-collecter-app/dokumentaatio/tuntikirjanpito.md)<br>
- [Testausdokumentti](coin-collecter-app/dokumentaatio/testaus.md)<br>
- [Changelog](coin-collecter-app/dokumentaatio/changelog.md)

## Release
[Viikon 5 release](https://github.com/hodelma/ot-harjoitustyo/releases/tag/viikko5)

[Viikon 6 release](https://github.com/hodelma/ot-harjoitustyo/releases/tag/viikko6)

<br>

>[!Important]
>Sinulla täytyy olla Python 3.12. versio ladattuna etukäteen — sovellus on toteutettu 3.12. versiolla. Tutustu asennusohjeisiin [täältä](https://www.python.org/downloads/)


## Asennusohjeet

**1. Kloonaa repositorio:**
```bash
git clone https://github.com/hodelma/ot-harjoitustyo.git
cd ot-harjoitustyo/coin-collecter-app
```


**2. Asenna projektin riippuvuudet:**
```bash
poetry install
```


>[!TIP]
>Jos haluat määritellä itse SQLite-tietokantatiedoston nimen, toimi seuraavasti:
>
>Mene projektin juureen tiedostoon .env
>
>Muokkaa haluamasi tiedostonimi riville ```DATABASE_FILENAME=OMA_TIEDOSTO_NIMI.db```


**3. Suorita tarvittavat alustustoimenpiteet:**
```bash
poetry run invoke build
```


**4. Käynnistä sovellus (käyttöliittymä keskeneräinen):**
```bash
poetry run invoke start
```



## Käytössä olevat komennot


### Sovelluksen testaaminen
```bash
poetry run invoke test
```
Tällöin luodaan myös automaattisesti testitietokanta

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

