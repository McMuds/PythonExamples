DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    artist_name varchar(255)
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    album_name varchar(255),
    year_released int,
    artist_id int REFERENCES artists(id) ON DELETE CASCADE
);