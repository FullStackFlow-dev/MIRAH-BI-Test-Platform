-- CLEANUP

DROP TABLE IF EXISTS avis CASCADE;
DROP TABLE IF EXISTS paiements CASCADE;
DROP TABLE IF EXISTS commandes CASCADE;
DROP TABLE IF EXISTS clients CASCADE;
DROP TABLE IF EXISTS restaurants CASCADE;


-- RESTAURANTS

CREATE TABLE restaurants (

    restaurant_id INTEGER PRIMARY KEY,

    name VARCHAR(255) NOT NULL,

    quartier VARCHAR(100),

    ville VARCHAR(100),

    pays VARCHAR(100),

    categorie VARCHAR(100),

    telephone VARCHAR(20),

    rating NUMERIC(3,1),

    review_count INTEGER,

    latitude NUMERIC(10,6),

    longitude NUMERIC(10,6)
);

=
-- CLIENTS

CREATE TABLE clients (

    client_id BIGINT PRIMARY KEY,

    nom VARCHAR(255) NOT NULL,

    email VARCHAR(255),

    telephone VARCHAR(20),

    ville VARCHAR(100),

    pays VARCHAR(100)
);


-- COMMANDES

CREATE TABLE commandes (

    commande_id BIGINT PRIMARY KEY,

    restaurant_id INTEGER NOT NULL,

    client_id BIGINT NOT NULL,

    montant NUMERIC(12,2),

    devise VARCHAR(10),

    statut_commande VARCHAR(50),

    canal_commande VARCHAR(50),

    date_commande TIMESTAMP,

    CONSTRAINT fk_commande_restaurant
        FOREIGN KEY (restaurant_id)
        REFERENCES restaurants (restaurant_id),

    CONSTRAINT fk_commande_client
        FOREIGN KEY (client_id)
        REFERENCES clients (client_id)
);


-- PAIEMENTS

CREATE TABLE paiements (

    paiement_id BIGINT PRIMARY KEY,

    commande_id BIGINT NOT NULL,

    mode_paiement VARCHAR(50),

    montant NUMERIC(12,2),

    devise VARCHAR(10),

    date_paiement TIMESTAMP,

    CONSTRAINT fk_paiement_commande
        FOREIGN KEY (commande_id)
        REFERENCES commandes (commande_id)
);


-- AVIS

CREATE TABLE avis (

    avis_id BIGINT PRIMARY KEY,

    restaurant_id INTEGER NOT NULL,

    client_id BIGINT NOT NULL,

    note INTEGER CHECK (
        note BETWEEN 1 AND 5
    ),

    commentaire TEXT,

    date_avis TIMESTAMP,

    CONSTRAINT fk_avis_restaurant
        FOREIGN KEY (restaurant_id)
        REFERENCES restaurants (restaurant_id),

    CONSTRAINT fk_avis_client
        FOREIGN KEY (client_id)
        REFERENCES clients (client_id)
);


-- INDEXES

CREATE INDEX idx_commandes_restaurant
ON commandes(restaurant_id);

CREATE INDEX idx_commandes_client
ON commandes(client_id);

CREATE INDEX idx_commandes_date
ON commandes(date_commande);

CREATE INDEX idx_paiements_commande
ON paiements(commande_id);

CREATE INDEX idx_avis_restaurant
ON avis(restaurant_id);

CREATE INDEX idx_clients_email
ON clients(email);


-- COMMENTS

COMMENT ON TABLE restaurants IS
'Données restaurants simulées pour MIRAH-BI Sandbox';

COMMENT ON TABLE clients IS
'Données clients simulées pour MIRAH-BI Sandbox';

COMMENT ON TABLE commandes IS
'Données de commandes simulées en FCFA';

COMMENT ON TABLE paiements IS
'Données de paiements simulées en FCFA';

COMMENT ON TABLE avis IS
'Données de satisfaction client simulées';