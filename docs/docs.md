# Kalenterilmoittautumis-sovellus

Eventie on kalenterisovellu missä voi luoda uusia tapahtumia ja ilmota olemassa oleviin tapahtumiin. Sovellus on toteutettu pythonin flaskilla, postgreSQL-tietokannalla ja Reactilla.

## Puutteeliset toiminnallisuudet
Sovelluksesta puuttuu uloskirjautuminen, käyttäjän datan muokkaus, ilmoittautumisen peruutus ja ilmoittautumisjono.

## Käyttöohje

### Perustoiminallisuus

Ensimmäisellä sivulla löydät tulevat tapahtumat. Tapahtumia ja niiden tietoja voi katsella vaikka käyttäjä ei ole sisäänkirjautunut. 

Tapahtumien listaus tapahtuu seuraavalla kyselyllä:

`SELECT events.*, users.id as user_id, users.name as user_name FROM events left join users on (events.author_id = users.id) where time >= now();`

### Kirjautuminen tai uuden käyttäjän luonti

Yläkulmassa on linkki kirjautumiseen. Jos käyttäjällä ei ole olemassa olevaa käyttäkjää voi hän luoda uuden painamalla 'Register' -nappia. Tällöin näkyviin tulee lomake missä kysytään käyttäjän perustiedot. Käyttäjää pyydetään vielä kirjautumaan sisään uusilla tunnuksilla käyttäjän luonnin jälkeen. Kirjautumisen jälkeen käyttäjä voi luoda uusia tapahtumia ja ilmoittautua toisiin tapahtumiin.

Käyttäjän luonti tapahtuu seuraavalla kyselyllä:

`INSERT INTO users VALUES (%s,%s,%s,%s,%s);`

Käyttäjän autentikointi tapahtuu seuraavalla kyselyllä:

`SELECT id, username, password_salt FROM users where username = %s;`

### Tapahtuman luonti, muokkaaminen ja poistaminen

Tapahtumalistan pohjalla on laatikko, mistä voi luoda uuden tapahtuman. Painamalla nappia avautuu uusi modali missä kysytään käyttäjältä tapahtuman tietoja.

Käyttäjä pystyy myös muokkaamaan omia tapahtumiaan. Kun käyttäjä painaa omaa tapahtumaa, esille tulee tapahtuman perustiedot. Modalista löytyy myös nappi 'Edit event' minkä painamalla käyttäjä pystyy muuttamaan tapahtumaa. Modalista löytyy myös nappi 'Delete event' joka poistaa tapahtuman kokonaan tietokannasta.

Tapahtuman luonti tapahtuu seuraavalla kyselyllä:

`INSERT INTO events VALUES (%s,%s,%s,%s,%s,%s,%s,%s);`

Tapahtuman muokkaaminen tapahtuu seuraavalla kyselyllä:

`UPDATE events SET id  = %s, name = %s, description = %s, registration_start = %s, registration_end = %s, time = %s, max_participants = %s, author_id = %s where id = %s;`

Tapahtuman poistaminen tapahtuu seuraavalla transaktiolla:

`DELETE FROM registrations WHERE event_id = %s`
`DELETE FROM events WHERE id = %s`







