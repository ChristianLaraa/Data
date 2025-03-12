CREATE DATABASE ModaEmergente;
USE ModaEmergente;

--  Tabla de marcas emergentes
CREATE TABLE Marcas (
    id_marca INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    año_creacion YEAR,
    categoria VARCHAR(100),  -- Streetwear, Alternativo, Techwear, etc.
    ciudad_base VARCHAR(100),
    disponibilidad ENUM('Online', 'Tienda Física', 'Ambos'),
    precios_promedio DECIMAL(10,2),  -- Precio medio de productos
    seguidores_ig INT,  -- Seguidores en Instagram
    seguidores_tt INT,  -- Seguidores en TikTok
    engagement_redes DECIMAL(5,2) -- % de interacción
);

-- Tabla de productos de cada marca
CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    id_marca INT,
    nombre VARCHAR(255),
    categoria VARCHAR(100),  -- Sudaderas, Pantalones, etc.
    precio DECIMAL(10,2),
    colores VARCHAR(255),
    FOREIGN KEY (id_marca) REFERENCES Marcas(id_marca) ON DELETE CASCADE
);

-- Tabla de consumidores
CREATE TABLE Consumidores (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    edad INT,
    genero ENUM('Masculino', 'Femenino', 'No Binario', 'Otro'),
    ubicacion VARCHAR(100),  -- Estado (CDMX, Edomex, etc.)
    estilo_preferido VARCHAR(255),  -- Streetwear, Formal, etc.
    frecuencia_compra VARCHAR(50),  -- Cada mes, Cada 3 meses, etc.
    gasto_promedio DECIMAL(10,2),
    fuente_descubrimiento VARCHAR(255)  -- TikTok, Instagram, Recomendación, etc.
);

-- Tabla de influencers que promocionan moda emergente
CREATE TABLE Influencers (
    id_influencer INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    red_social ENUM('Instagram', 'TikTok', 'YouTube', 'X', 'Otro'),
    seguidores INT,
    engagement DECIMAL(5,2),
    marcas_colaboradas TEXT -- Marcas con las que ha trabajado
);

--  Tabla de tendencias en redes sociales
/*CREATE TABLE Tendencias (
    id_trend INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    genero_musical VARCHAR(100),  -- Música más usada en videos con esta moda
    hashtag_popular VARCHAR(255),
    impacto_mensual INT,  -- Cantidad de publicaciones sobre la moda
    crecimiento DECIMAL(5,2)  -- Incremento en la popularidad en %
); */

--  Tabla de relaciones entre marcas e influencers
CREATE TABLE Colaboraciones (
    id_colaboracion INT AUTO_INCREMENT PRIMARY KEY,
    id_marca INT,
    id_influencer INT,
    FOREIGN KEY (id_marca) REFERENCES Marcas(id_marca) ON DELETE CASCADE,
    FOREIGN KEY (id_influencer) REFERENCES Influencers(id_influencer) ON DELETE CASCADE
);


