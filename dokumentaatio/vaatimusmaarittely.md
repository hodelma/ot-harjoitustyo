# Vaatimusmäärittely

## Sovelluksen tarkoitus ja yleiskuva
Pelin tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä keräämistään kolikoista, mutta jos osuu hirviöön, pisteet nollautuvat ja peli päättyy. Pelaaja voittaa, kun hän kerää 20 kolikkoa osumatta hirviöihin.

## Suunnitellut toiminnallisuudet

### Perusversio (ydintoiminnallisuus)
- [ ] Pelaajan hahmon liikkuminen ruudulla
- [ ] Kolikoiden kerääminen kasvattaa pistesaldoa
- [ ] Hirviöön osuminen johtaa pisteiden nollaamiseen ja pelin päättymiseen
- [ ] Pelin voittaminen: 20 kolikkoa kerätty, niin pelaaja voittaa
- [ ] Osumatarkistus: pelaaja vs. kolikko, pelaaja vs. hirviö
- [ ] Pelin tilan seuranta: pisteet, peli päättynyt/käynnissä, voitto

### Etusivu / valikko
- [ ] Start-nappi aloittaa pelin
- [ ] Scoreboard-nappi näyttää pelaajan parhaat pisteet
- [ ] Vaikeustasot (Easy/Medium/Hard) tai levelit (esim. hirviöiden nopeus)
- [ ] Quit-nappi sulkee pelin

### Peli-ikkuna
- [ ] Peli käynnissä ja hahmon ohjaus
- [ ] Game Over -näkymä - pelaaja häviää
- [ ] You Win -näkymä - pelaaja voittaa
- [ ] Esc-näppäin avaa valikon, jossa vaihtoehdot:
  - "Resume" jatkaa peliä
  - "Quit" palaa etusivulle tai sulkee pelin

## Jatkokehitysideoita
- [ ] Eri vaikeustasoilla esim. enemmän hirviöitä/nopeampi tahti <br>
- [ ] Eri pistearvot kolikoille <br>
- [ ] Pelaaja ei kuole yhdestä törmäyksestä <br>
- [ ] Ajastettu peli / aikaraja <br>
- [ ] Graafisten tehosteiden ja animaatioiden lisääminen
