# Vaatimusmäärittely

## Sovelluksen tarkoitus ja yleiskuva
Pelin tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä keräämistään kolikoista, mutta jos osuu hirviöön, pisteet nollautuvat ja peli päättyy. Pelaaja voittaa, kun hän kerää 20 kolikkoa osumatta hirviöihin.

## Suunnitellut toiminnallisuudet

### Perusversio (ydintoiminnallisuus)
- [x] Pelaajan hahmon liikkuminen ruudulla
- [x] Kolikoiden kerääminen kasvattaa pistesaldoa
- [x] Hirviöön osuminen johtaa pisteiden nollaamiseen ja pelin päättymiseen
- [x] Pelin voittaminen: 20 kolikkoa kerätty, niin pelaaja voittaa
- [ ] Eri pistearvot kolikoille
- [ ] Graafisten tehosteiden ja animaatioiden lisääminen
- [ ] Pelaaja ei kuole yhdestä törmäyksestä

### Etusivu / valikko
- [x] Start-toiminto aloittaa pelin
- [ ] Scoreboard-toiminto näyttää pelaajan pisteet eri pelikerroilta
- [ ] Vaikeustasot (Easy/Medium/Hard) tai levelit (hirviöiden nopeus/liikesuunta)
- [x] Quit-toiminto sulkee pelin

### Peli-ikkuna
- [x] Game Over -näkymä - pelaaja häviää
- [x] You Win -näkymä - pelaaja voittaa
- [x] Ohje takaisin menuun pelin päättyessä
- [ ] Play again/Restart game-toiminto, kun peli päättyy
- [x] Esc-näppäin avaa valikon, jossa resume ja quit

## Jatkokehitysideoita
- [ ] Ajastettu peli / aikaraja <br>
- [ ] Boss-hahmo
- [ ] Kolikkomagneetti vetää kolikot pelaajaan
- [ ] Eri hirviötyypit
- [ ] Useita kenttiä (erilainen teema joka kentässä)
- [ ] Hirviöiden lisäksi esteitä pelikentällä
- [ ] Ääniefektit
- [ ] Käyttäjän luominen mahdollista (kirjautuminen, kisaaminen muita pelaajia vastaan)
