CREATE TABLE Genres (
  genre_id INT PRIMARY KEY,
  genre_name VARCHAR(255)
);

CREATE TABLE Artists (
  artist_id INT PRIMARY KEY,
  artist_name VARCHAR(255)
);

CREATE TABLE Artists_Genres (
  artist_id INT,
  genre_id INT,
  FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
  FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);

CREATE TABLE Albums (
  album_id INT PRIMARY KEY,
  album_name VARCHAR(255),
  release_year INT
);

CREATE TABLE Artists_Albums (
  artist_id INT,
  album_id INT,
  FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
  FOREIGN KEY (album_id) REFERENCES Albums(album_id)
);

CREATE TABLE Tracks (
  track_id INT PRIMARY KEY,
  track_name VARCHAR(255),
  duration INT
);

CREATE TABLE Compilations (
  compilation_id INT PRIMARY KEY,
  compilation_name VARCHAR(255),
  release_year INT
);

CREATE TABLE Tracks_In_Compilations (
  compilation_id INT,
  track_id INT,
  FOREIGN KEY (compilation_id) REFERENCES Compilations(compilation_id),
  FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
);
