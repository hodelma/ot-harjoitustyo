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

`repositories`-pakkauksen `ScoreRepository`-luokka huolehtii tietojen tallentamisesta SQLite-tietokantaan. Luokka noudattaa repositorio-suunnittelumallia, joka eristää tietokantatoiminnot muusta sovelluslogiikasta.

Pisteet tallennetaan `scores`-tauluun.







## Tiedostot ja konfiguraatio

Tietokantatiedoston nimi haetaan `.env`-tiedostosta ympäristömuuttujalla `DATABASE_FILENAME`. Mikäli muuttujaa ei ole asetettu, käytetään oletusarvona `database.db`. Testejä varten on erillinen `.env.test`-tiedosto, joka ohjaa testit omaan testitietokantaansa. Tietokantayhteys luodaan `db/database_connection.py`-moduulissa ja sen konfiguraatio sijaitsee `db/config.py`-tiedostossa. Tietokantataulut alustetaan `db/initialize_database.py`-moduulin `initialize_database()`-funktiolla, jota kutsutaan ohjelman käynnistyksen yhteydessä `main.py`:ssä.









## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat `Game`, `Level` ja peliobjektien luokat (`Player`, `Coin`, `Monster`), jotka mallintavat pelin tilaa ja objekteja.

<img src="kuvat/class_diagram.png" width="590">

Toiminnallisista kokonaisuuksista vastaa pääosin `Level`-luokan olio, joka hallinnoi kaikkia peliobjekteja ja pelilogiikkaa. `Game`-luokka pitää yllä pelitilaa, jossa on esim. pistemäärä ja elämät. Luokka tarjoaa metodeja pelilogiikan toiminnoille:

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
      +collect_coin(value)
      +hit_monster()
      +has_won()
      +reset()
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
      +int speed
      +int value
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
    }

    class Renderer {
      +render()
    }

    class EventQueue {
      +get()
    }

    class ScoreRepository {
      +save_score(score)
      +get_high_score()
      +get_recent_scores(limit)
    }

    Level --> Game
    Level --> Player
    Level "1" o-- "many" Coin : coins
    Level "1" o-- "many" Monster : monsters
    GameLoop --> Level
    GameLoop --> Renderer
    GameLoop --> EventQueue
    Renderer --> Game
    Game --> ScoreRepository
```









## Päätoiminnallisuudet

### Kolikon kerääminen

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Game
    participant ScoreRepository

    User->>GameLoop: Press arrow key
    GameLoop->>Level: update(keys_pressed)
    Level->>Level: player.move(dx, dy)
    Level->>Level: _check_collisions()
    Level->>Game: collect_coin(coin.value)
    Game->>Game: score += value
    Game->>ScoreRepository: Potentially save score
    Game-->>Level: return
    Level->>Level: Create new Coin
    Level-->>GameLoop: return
    GameLoop->>Renderer: render()
```



### Hirviöön törmääminen

Kun pelaaja törmää hirviöön:

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Game

    User->>GameLoop: Press arrow key
    GameLoop->>Level: update(keys_pressed)
    Level->>Level: player.move(dx, dy)
    Level->>Level: _check_collisions()
    Level->>Game: hit_monster()
    Game->>Game: lives -= 1
    Game-->>Level: return
    Level->>Level: Remove monster, create new one
    Level-->>GameLoop: return
```



### Pelin tilanvaihto

Pelaaja voi siirtyä eri pelitilaan painamalla näppäimiä:

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Game

    User->>GameLoop: Press key (ENTER, S, ESCAPE, Q)
    GameLoop->>GameLoop: _handle_keydown(event)
    GameLoop->>Level: reset() / change state
    Level->>Game: Update game state
    Game-->>Level: return
    Level-->>GameLoop: return
```
