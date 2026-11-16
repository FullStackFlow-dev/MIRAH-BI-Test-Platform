-- DATABASE
CREATE DATABASE IF NOT EXISTS restaurant_bi
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE restaurant_bi;

-- CLEANUP
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS avis;
DROP TABLE IF EXISTS paiements;
DROP TABLE IF EXISTS commandes;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS restaurants;

SET FOREIGN_KEY_CHECKS = 1;

-- RESTAURANTS
CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quartier VARCHAR(100),
    ville VARCHAR(100),
    pays VARCHAR(100),
    categorie VARCHAR(100),
    telephone VARCHAR(20),
    rating DECIMAL(3,1),
    review_count INT,
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6)
) ENGINE=InnoDB
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT='Donnees restaurants simulees pour MIRAH-BI Sandbox';

-- CLIENTS
CREATE TABLE clients (
    client_id BIGINT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telephone VARCHAR(20),
    ville VARCHAR(100),
    pays VARCHAR(100)
) ENGINE=InnoDB
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT='Donnees clients simulees pour MIRAH-BI Sandbox';

-- COMMANDES
CREATE TABLE commandes (
    commande_id BIGINT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    client_id BIGINT NOT NULL,
    montant DECIMAL(12,2),
    devise VARCHAR(10),
    statut_commande VARCHAR(50),
    canal_commande VARCHAR(50),
    date_commande DATETIME,
    CONSTRAINT fk_commande_restaurant
        FOREIGN KEY (restaurant_id)
        REFERENCES restaurants (restaurant_id),
    CONSTRAINT fk_commande_client
        FOREIGN KEY (client_id)
        REFERENCES clients (client_id)
) ENGINE=InnoDB
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT='Donnees de commandes simulees en FCFA';

-- PAIEMENTS
CREATE TABLE paiements (
    paiement_id BIGINT PRIMARY KEY,
    commande_id BIGINT NOT NULL,
    mode_paiement VARCHAR(50),
    montant DECIMAL(12,2),
    devise VARCHAR(10),
    date_paiement DATETIME,
    CONSTRAINT fk_paiement_commande
        FOREIGN KEY (commande_id)
        REFERENCES commandes (commande_id)
) ENGINE=InnoDB
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT='Donnees de paiements simulees en FCFA';

-- AVIS
CREATE TABLE avis (
    avis_id BIGINT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    client_id BIGINT NOT NULL,
    note INT,
    commentaire TEXT,
    date_avis DATETIME,
    CONSTRAINT chk_avis_note
        CHECK (note BETWEEN 1 AND 5),
    CONSTRAINT fk_avis_restaurant
        FOREIGN KEY (restaurant_id)
        REFERENCES restaurants (restaurant_id),
    CONSTRAINT fk_avis_client
        FOREIGN KEY (client_id)
        REFERENCES clients (client_id)
) ENGINE=InnoDB
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT='Donnees de satisfaction client simulees';

-- INDEXES
CREATE INDEX idx_commandes_restaurant
    ON commandes (restaurant_id);
CREATE INDEX idx_commandes_client
    ON commandes (client_id);
CREATE INDEX idx_commandes_date
    ON commandes (date_commande);
CREATE INDEX idx_paiements_commande
    ON paiements (commande_id);
CREATE INDEX idx_avis_restaurant
    ON avis (restaurant_id);
CREATE INDEX idx_clients_email
    ON clients (email);

-- VALIDATION
SHOW TABLES;
