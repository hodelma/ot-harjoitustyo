# Vaatimusmäärittely

## Sovelluksen tarkoitus ja yleiskuva
Pelin tavoitteena on kerätä kolikoita ja välttää hirviöitä. Pelaaja saa pisteitä keräämistään kolikoista, mutta jos osuu hirviöön, pisteet nollautuvat ja peli päättyy. Pelaaja voittaa, kun hän kerää 20 kolikkoa osumatta hirviöihin.

## Suunnitellut toiminnallisuudet

### Perusversio (ydintoiminnallisuus)
- [x] Pelaajan hahmon liikkuminen ruudulla
- [x] Kolikoiden kerääminen kasvattaa pistesaldoa
- [x] Hirviöön osuminen johtaa pisteiden nollaamiseen ja pelin päättymiseen
- [x] Pelin voittaminen: 20 kolikkoa kerätty, niin pelaaja voittaa
- [x] Osumatarkistus: pelaaja vs. kolikko, pelaaja vs. hirviö
- [x] Pelin tilan seuranta: pisteet, peli päättynyt/käynnissä, voitto
- [ ] Eri pistearvot kolikoille
- [ ] Graafisten tehosteiden ja animaatioiden lisääminen
- [ ] Pelaaja ei kuole yhdestä törmäyksestä <br>

### Etusivu / valikko
- [x] Start-nappi aloittaa pelin
- [ ] Scoreboard-nappi näyttää pelaajan parhaat pisteet
- [ ] Vaikeustasot (Easy/Medium/Hard) tai levelit (esim. hirviöiden nopeus)
- [x] Quit-nappi sulkee pelin

### Peli-ikkuna
- [x] Peli käynnissä ja hahmon ohjaus
- [x] Game Over -näkymä - pelaaja häviää
- [x] You Win -näkymä - pelaaja voittaa
- [x] Esc-näppäin avaa valikon, jossa vaihtoehdot:
  - "Resume" jatkaa peliä
  - "Quit" palaa etusivulle tai sulkee pelin

## Jatkokehitysideoita
- [ ] Ajastettu peli / aikaraja <br>
- [ ] Boss-hahmo
- [ ] Kolikkomagneetti vetää kolikot pelaajaan
- [ ] Eri hirviötyypit
- [ ] Useita kenttiä (erilainen teema joka kentässä)
- [ ] Hirviöiden lisäksi esteitä pelikentällä
- [ ] Ääniefektit ja musiikki
- [ ] Käyttäjän luominen mahdollista (kirjautuminen, kilpailu muita pelaajia vastaan)
