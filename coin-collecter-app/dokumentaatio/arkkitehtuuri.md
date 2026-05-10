# Arkkitehtuurikuvaus



## Rakenne

Alla näkyy koodin suurpiirteinen pakkausrakenne:

<img src="kuvat/pakkauskaavio.png" width="420">

Pakkaus *ui* sisältää käyttöliittymästä eli pelisilmukasta ja piirtämisestä, *repositories* tietojen pysyväistallennuksesta, *sprites* ja *db* tietokannan hallinnasta vastaavan koodin. *game_logic.py* sisältää pelilogiikan ja *level.py* pelin tason objektit sekä törmäystarkistukset.











## Käyttöliittymä

Käyttöliittymä koostuu neljästä eri näkymästä:

- Päävalikko
- Pelinäkymä
- Taukovalikko
- Pelin lopetus
- Tulostaulu

Jokainen näkymä on toteutettu `Renderer`-luokassa omana piirtometodina (`_draw_menu`, `_draw_scoreboard`, `_draw_pause_menu`, `_draw_game_over`). Käyttöliittymä ei vastaa sovelluslogiikasta, vaan ainoastaan nykyisen tilan piirtämisestä.

`Renderer` pitää kirjaa sen hetkisistä napin sijainneista, jota `GameLoop` hyödyntää hiiren klikkauksien käsittelyssä.
<br>

Pelitilan muutokset tapahtuvat Game-olion state-attribuutin kautta. Mahdolliset tilat ovat "menu", "playing", "paused", "game_over" ja "scoreboard".









## Tietojen pysyväistallennus

`repositories`-pakkauksen `ScoreRepository`-luokka huolehtii tietojen tallentamisesta SQLite-tietokantaan. Luokka noudattaa repositorio-suunnittelumallia.

Pisteet tallennetaan `scores`-tauluun.







### Tiedostot ja konfiguraatio

Tietokantatiedoston nimi haetaan `.env`-tiedostosta ympäristömuuttujalla `DATABASE_FILENAME`. Jos muuttujaa ei ole asetettu, käytetään oletusarvona `database.db`. Testejä varten on erillinen `.env.test`-tiedosto, joka ohjaa testit omaan testitietokantaansa. Tietokantayhteys luodaan `db/database_connection.py`-moduulissa ja sen konfiguraatio sijaitsee `db/config.py`-tiedostossa. Tietokantataulut alustetaan `db/initialize_database.py`-moduulin `initialize_database()`-funktiolla, jota kutsutaan ohjelman käynnistyksen yhteydessä `main.py`:ssä.









## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat `Game`, `Level` ja peliobjektien luokat (`Player`, `Coin`, `Monster`), jotka mallintavat pelin tilaa ja objekteja.

<img src="kuvat/class_diagram.png" width="590">

Toiminnallisista kokonaisuuksista vastaa pääosin `Level`-luokan olio, joka hallinnoi kaikkia peliobjekteja ja pelilogiikkaa. `Game`-luokka pitää yllä pelitilaa, jossa on esim pistemäärä ja elämät. Luokalla on pelilogiikan toimintoja:

- `collect_coin(value)` lisää pisteen saldoon kun kolikko kerätään
- `hit_monster()` vähentää elämiä kun hirviö osuu pelaajaan
- `has_won()` tarkistaa voittoehdot

`Level`-luokka hallinnoi `all_sprites`, `coins`, `monsters` ja päivittää pelaajan liikettä, tarkistaa törmäykset ja hallinnoi peliobjektien luomista ja poistamista.










### Pelin luokkakaavio

```mermaid
classDiagram
    class Game {
      +int score
      +bool is_over
      +bool won
      +str state
      +int high_score
      +int lives
      -ScoreRepository _score_repository
      +collect_coin(value)
      +hit_monster()
      +has_won()
      +reset()
      -_save_score()
    }
 
    class Level {
      +Game game
      +Player player
      +Group all_sprites
      +Group coins
      +Group monsters
      +update(keys_pressed)
      +reset()
      -_check_boundaries()
      -_check_collisions()
    }
 
    class Player {
      +int speed
      +move(dx, dy)
      +reset_position(x, y)
    }
 
    class Coin {
      +int value
      +int speed
      +update()
      +randomize_position()
    }
 
    class Monster {
      +int speed
      +update()
      +reset_position()
    }
 
    class GameLoop {
      +start()
      -_handle_events()
      -_handle_keydown(event)
      -_handle_click(pos)
      -_click_menu(pos)
      -_click_scoreboard(pos)
      -_click_paused(pos)
      -_click_game_over(pos)
    }
 
    class Renderer {
      +dict button_rects
      +render()
      -_render_ui(mouse_position)
      -_draw_score()
      -_draw_menu(mouse_position)
      -_draw_pause_menu(mouse_position)
      -_draw_game_over(mouse_position)
      -_draw_scoreboard(mouse_position)
    }
 
    class Clock {
      +tick(fps)
      +get_ticks()
    }
 
    class EventQueue {
      +get()
    }
 
    class ScoreRepository {
      +save_score(score)
      +get_high_score()
      +get_recent_scores(limit)
      +delete_all()
    }
 
    Level --> Game
    Level --> ScoreRepository
    Level --> Player
    Level "1" o-- Coin : coins
    Level "1" o-- Monster : monsters
    GameLoop --> Level
    GameLoop --> Renderer
    GameLoop --> EventQueue
    GameLoop --> Clock
    Renderer --> Game
    Renderer --> ScoreRepository
    Game --> ScoreRepository
```









## Päätoiminnallisuudet

### Kolikon kerääminen

Pelaaja osuu kolikkoon. `GameLoop` kutsuu `Level`-olion `update()`, joka ensin siirtää pelaajaa painettujen näppäinten mukaan ja tarkistaa sitten törmäykset. Törmäyksen havaitessaan `Level` kutsuu `Game`-olion `collect_coin()`, joka kasvattaa pistesaldoa ja päivittää mahd. ennätyksen. Sitten `Level` arpoo kolikolle uuden sijainnin `(roll_coin())`.

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Game
    participant ScoreRepository
    participant Renderer

    User ->> GameLoop: 
    GameLoop ->> Level: update(keys_pressed)

    Level ->> Level: player.move(dx, dy)
    Level ->> Level: _check_collisions()

    Level ->> Game: collect_coin(coin.value)
    Game ->> Game: score += value
    Game ->> Game: high_score = max(high_score, score)

    Game -->> Level: return

    Level ->> Level: roll_coin()
    Level -->> GameLoop: return

    GameLoop ->> Renderer: render()
```



### Hirviöön törmääminen

Pelaaja törmää hirviöön. `GameLoop` kutsuu `Level`-olion `update()`, joka siirtää pelaajaa ja tarkistaa törmäykset. Törmäyksen havaitessaan `Level` kutsuu `Game` olion `hit_monster()`, joka vähentää pelaajan elämäpisteitä yhdellä.

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Game
    participant ScoreRepository
 
    User->>GameLoop:
    GameLoop->>Level: update(keys_pressed)
    Level->>Level: player.move(dx, dy)
    Level->>Level: _check_collisions()
    Level->>Game: hit_monster()
    Game->>Game: lives -= 1
    Game-->>Level: return
    Level->>Level: monster.kill()
    Level-->>GameLoop: return
    GameLoop->>Renderer: render()
```



### Pelin tilanvaihto

Pelaaja painaa päävalikossa "Start"-nappia. `GameLoop` käsittelee hiiren klikkauksen ja tunnistaa sen. Sitten `GameLoop` kutsuu `Level`-olion `reset()`-metodia, joka ketjuttaa kutsun `Game`-olion `reset()`-metodille.

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Game
 
    User->>GameLoop:
    GameLoop->>GameLoop: _handle_click(pos)
    GameLoop->>GameLoop: _click_menu(pos)
    GameLoop->>Level: reset()
    Level->>Game: reset()
    Game->>Game: state = "playing", score = 0, lives = 3
    Game-->>Level: return
    Level->>Level: player.reset_position()
    Level->>Level: roll_coin()
    Level->>Level: monster.reset_position()
    Level-->>GameLoop: return
    GameLoop->>Renderer: render()
```




## Sovelluksen rakenteen mahdolliset laatuongelmat

### Käyttöliittymä

Sovelluksen näytön resoluutio on kovakoodattu eri paikkoihin koodissa.
