-- #1

INSERT INTO Genres (genre_id, genre_name)
VALUES
  (1, 'Pop'),
  (3, 'Hip-Hop'),
  (3, 'Rock');

INSERT INTO Artists (artist_id, artist_name)
VALUES
  (1, 'Ozzy Os'),
  (2, 'Eazy-E'),
  (3, 'Metalica'),
  (4, 'Skrillex');

INSERT INTO Artists_Genres (artist_id, genre_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 1);

INSERT INTO Albums (album_id, album_name, release_year)
VALUES
  (1, 'Album 1', 2020),
  (2, 'Album 2', 2018),
  (3, 'Album 3', 2021);

INSERT INTO Artists_Albums (artist_id, album_id)
VALUES
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 3);

INSERT INTO Tracks (track_id, track_name, duration, album_id)
VALUES
  (1, 'Track 1', 240, 1),
  (2, 'Track 2', 180, 1),
  (3, 'Track 3', 200, 2),
  (4, 'Track 4', 220, 2),
  (5, 'Track 5', 210, 3),
  (6, 'Track 6', 190, 3);

INSERT INTO Compilations (compilation_id, compilation_name, release_year)
VALUES
  (1, 'Compilation 1', 2019),
  (2, 'Compilation 2', 2022),
  (3, 'Compilation 3', 2021),
  (4, 'Compilation 4', 2020);

INSERT INTO Tracks_In_Compilations (compilation_id, track_id)
VALUES
  (1, 1),
  (1, 3),
  (2, 2),
  (2, 4),
  (3, 5),
  (3, 6),
  (4, 1),
  (4, 4);

-- #2
SELECT track_name, duration
FROM Tracks
ORDER BY duration DESC
LIMIT 1;

SELECT track_name, duration
FROM Tracks
WHERE duration >= 210;

SELECT compilation_name
FROM Compilations
WHERE release_year BETWEEN 2018 AND 2020;

SELECT artist_name
FROM Artists
WHERE artist_name NOT LIKE '% %';

SELECT track_name, duration
FROM Tracks
WHERE LOWER(track_name) LIKE '%мой%' OR LOWER(track_name) LIKE '%my%';

-- #3

SELECT g.genre_name, COUNT(ag.artist_id) AS artist_count
FROM Genres g
LEFT JOIN Artists_Genres ag ON g.genre_id = ag.genre_id
GROUP BY g.genre_name;

SELECT COUNT(t.track_id) AS track_count
FROM Tracks t
INNER JOIN Albums a ON t.album_id = a.album_id
WHERE a.release_year BETWEEN 2019 AND 2020;

SELECT a.album_name, AVG(t.duration) AS average_duration
FROM Albums a
INNER JOIN Tracks t ON a.album_id = t.album_id
GROUP BY a.album_name;

SELECT ar.artist_name
FROM Artists ar
LEFT JOIN Artists_Albums aa ON ar.artist_id = aa.artist_id
LEFT JOIN Albums al ON aa.album_id = al.album_id
WHERE al.album_id IS NULL OR al.release_year <> 2020;

SELECT c.compilation_name
FROM Compilations c
INNER JOIN Tracks_In_Compilations tic ON c.compilation_id = tic.compilation_id
INNER JOIN Tracks t ON tic.track_id = t.track_id
INNER JOIN Albums a ON t.album_id = a.album_id
INNER JOIN Artists_Albums aa ON a.album_id = aa.album_id
INNER JOIN Artists ar ON aa.artist_id = ar.artist_id
WHERE ar.artist_name = 'Artist 1';
