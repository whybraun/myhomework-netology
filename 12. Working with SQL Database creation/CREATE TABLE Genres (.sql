CREATE TABLE Genres (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE Artists (
  id INTEGER PRIMARY KEY,
  name TEXT,
  country TEXT
);

CREATE TABLE Albums (
  id INTEGER PRIMARY KEY,
  name TEXT,
  year INTEGER
);

CREATE TABLE Artists_Albums (
  artist_id INTEGER,
  album_id INTEGER,
  FOREIGN KEY(artist_id) REFERENCES Artists(id),
  FOREIGN KEY(album_id) REFERENCES Albums(id)
);

CREATE TABLE Tracks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  duration INTEGER,
  album_id INTEGER,
  FOREIGN KEY(album_id) REFERENCES Albums(id)
);

CREATE TABLE Compilations (
  id INTEGER PRIMARY KEY,
  name TEXT,
  year INTEGER
);

CREATE TABLE Compilations_Tracks (
  compilation_id INTEGER,
  track_id INTEGER,
  FOREIGN KEY(compilation_id) REFERENCES Compilations(id),
  FOREIGN KEY(track_id) REFERENCES Tracks(id)
);
