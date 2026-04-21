# Projektin changelog

## Viikko 3

- Implementoitu Game-pelilogiikka
- Rakennettu testit pelilogiikka funktioille ja varmistettu pelimekaniikkojen toimivuus
- Konfiguroitu tietokanta ja avattu SQLite-yhteys
- Tkinterillä toteutettu alustava UI ja ikkuna aukeaa

## Viikko  4
- Vaihdettu käyttöliittymä Tkinteristä kokonaisuudessaan Pygameen
- Käyttäjä voi liikuttaa pelihahmoa ja kasvattaa pistesaldoaan keräämällä kolikoita
- Käyttäjä näkee etusivun, peli-ikkunan ja pause menu -ikkunan
- Käyttäjä näkee voitto- tai häviönäkymän
- Lisätty `GameLoop` ja `Level` luokat sekä niille testejä
- Otettu pylint käyttöön

## Viikko 5
- Käyttäjä voi aloittaa pelin heti uudelleen pelin päättymisen jälkeen
- Testattu, että kolmen elämän loppuessa score ja elämät resetoituvat, kun pelin aloittaa uudelleen
- Käyttäjä voi kerätä eri arvoisia kolikoita
- Käyttäjä ei kuole yhdestä hirviöön törmäyksestä (voi seurata elämiään)
