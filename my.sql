-- CREATE TABLE Surat(
-- Name CHAR(50),
-- Age INT,
-- Grade CHAR(1)
-- );

INSERT INTO Surat (Name, Age, Grade)
VALUES ('Alice', 20, 'A'),
('Bob', 22, 'B'),
('jyoti', 12, 'B'),
('Booby', 15, 'A'),
('Charlie', 19, 'C');



delete FROM Surat WHERE Age > 21;

SELECT * FROM Surat;