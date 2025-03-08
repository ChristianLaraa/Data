use ModaEmergente;

show tables;

INSERT INTO Marcas (
    id_marca,
    nombre,
    ano_creacion,
    categoria,
    ciudad_base,
    disponibilidad,
    precios_promedio,
    seguidores_ig,
    seguidores_tt,
    engagement_redes
)
VALUES
("31", "RAZZA", "2020", "Handmade Jewerly", "Ciudad de México",
 "Ambos", "2900", "1261", "129", "00"),
("32", "INDUSTRIAL", "2019", "Streatwear", "Ciudad de México",
 "Online", "900", "5810", "00", "00"),
("33", "CUEVA", "2020", "Slow Fashion", "Ciudad de México",
 "Ambos", "2600", "20800", "1936", "00");

SELECT * FROM Marcas;

ALTER TABLE Marcas CHANGE COLUMN año_creacion ano_creacion YEAR;




-- update categoria de marca 5
UPDATE Marcas SET categoria = "Streatwear" WHERE id_marca = 5;

UPDATE Marcas SET ciudad_base = "Nezahualcoyotl, Estado de México" WHERE id_marca = 1;