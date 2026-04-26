# Vaatimusmäärittely

## Sovelluksen tarkoitus ja yleiskuva
Pelin tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä keräämistään kolikoista, mutta jos osuu hirviöön, pisteet nollautuvat ja peli päättyy. Pelaaja voittaa, kun hän kerää 20 kolikkoa osumatta hirviöihin.

## Suunnitellut toiminnallisuudet

### Perusversion ydintoiminnallisuus
- [x] Pelaajan hahmon liikkuminen ruudulla
- [x] Kolikoiden kerääminen kasvattaa pistesaldoa
- [x] Hirviöön osuminen johtaa pisteiden nollaamiseen ja pelin päättymiseen
- [x] Pelin voittaminen: 20 kolikkoa kerätty, niin pelaaja voittaa
- [x] Eri pistearvot kolikoille
- Graafisten tehosteiden ja animaatioiden lisääminen:
  - [x] You win/Game over tekstien vilkkuminen
  - [ ] HP-sydämet näkyvissä hienommin vain "lives left" tekstin sijaan
- [ ] Näytöllä olevien nappien painaminen näppäimen painamisen sijaan
- [x] Pelaaja ei kuole yhdestä törmäyksestä

### Etusivu / valikko
- [x] Start-toiminto aloittaa pelin
- [x] Scoreboard-toiminto näyttää pelaajan pisteet eri pelikerroilta
- [ ] Vaikeustasot (Easy/Medium/Hard) tai levelit (hirviöiden nopeus/liikesuunta)
- [x] Quit-toiminto sulkee pelin

### Peli-ikkuna
- [x] Game Over -näkymä - pelaaja häviää
- [x] You Win -näkymä - pelaaja voittaa
- [x] Ohje takaisin menuun pelin päättyessä
- [x] Play again/Restart game-toiminto, kun peli päättyy
- [x] Esc-näppäin avaa valikon, jossa resume ja quit

## Jatkokehitysideoita
- [ ] Ajastettu peli
- [ ] Boss-hirviöhahmo
- [ ] Eri hirviötyypit
- [ ] Useita teemakenttiä
- [ ] Hirviöiden lisäksi esteitä pelikentällä
- [ ] Ääniefektit
- [ ] Käyttäjän luominen mahdollista
- [ ] Uusien pelihahmojen unlockaaminen mitä pidemmälle pelissä pääsee
