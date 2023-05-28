CREATE TABLE Сотрудник (
    Имя VARCHAR(255),
    Отдел VARCHAR(255),
    Начальник VARCHAR(255),
    FOREIGN KEY (Начальник) REFERENCES Сотрудник(Имя)
);
