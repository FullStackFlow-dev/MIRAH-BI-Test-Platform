import json
import random

from datetime import datetime, timedelta
from faker import Faker

from configs.settings import (
    BRONZE_DIR,
    NB_RESTAURANTS,
    NB_CLIENTS,
    NB_COMMANDES,
    NB_AVIS,
    NB_PAIEMENTS
)

# ==========================================================
# INITIALISATION
# ==========================================================

fake = Faker("fr_FR")

# ==========================================================
# DONNÉES DE RÉFÉRENCE
# ==========================================================

QUARTIERS = [
    "Almadies",
    "Ngor",
    "Yoff",
    "Ouakam",
    "Plateau",
    "Mermoz",
    "Sacré-Cœur",
    "Liberté 6",
    "Point E",
    "Fann"
]

VILLES = [
    "Dakar",
    "Pikine",
    "Guédiawaye",
    "Rufisque"
]

CATEGORIES = [
    "Cuisine Sénégalaise",
    "Cuisine Africaine",
    "Cuisine Française",
    "Cuisine Italienne",
    "Cuisine Libanaise",
    "Cuisine Asiatique",
    "Fast Food",
    "Fruits de Mer",
    "Grillades",
    "Pâtisserie"
]

RESTAURANTS_PRESTIGIEUX = [
    "Le Lagon 1",
    "Chez Loutcha",
    "Restaurant Farid",
    "Le Djoloff",
    "La Calebasse",
    "Le Ryad",
    "L'Endroit",
    "Noflaye Beach",
    "La Terrasse",
    "Le Relais Sportif",
    "Terrou-Bi Restaurant",
    "Radisson Blu Restaurant",
    "Pullman Dakar Restaurant",
    "Yoka Lounge",
    "Bideew Restaurant",
    "Melo Patisserie",
    "Le Jardin Thaï",
    "Le Bayékou",
    "Tasty Sénégal",
    "Chez Katia"
]

# ==========================================================
# NOMS SÉNÉGALAIS
# ==========================================================

PRENOMS_HOMMES = [
    "Mamadou",
    "Ibrahima",
    "Ousmane",
    "Moussa",
    "Cheikh",
    "Alioune",
    "Pape",
    "Abdoulaye",
    "Babacar",
    "Modou",
    "Amadou",
    "Serigne",
    "Moustapha",
    "Malick",
    "Mouhamed"
]

PRENOMS_FEMMES = [
    "Awa",
    "Fatou",
    "Aminata",
    "Mariama",
    "Khady",
    "Ndeye",
    "Dior",
    "Astou",
    "Rokhaya",
    "Sokhna",
    "Bineta",
    "Coumba",
    "Yacine",
    "Adama",
    "Fama"
]

NOMS_SENEGALAIS = [
    "Diop",
    "Ndiaye",
    "Fall",
    "Ba",
    "Diallo",
    "Sow",
    "Sy",
    "Ndour",
    "Gueye",
    "Mbaye",
    "Faye",
    "Kane",
    "Cissé",
    "Seck",
    "Thiam",
    "Sarr"
]

CLIENTS_INTERNATIONAUX = [
    "John Smith",
    "Emma Dubois",
    "Pierre Bernard",
    "Maria Silva",
    "Carlos Santos",
    "Michael Johnson",
    "Daniel Wilson",
    "Sophia Martin",
    "Robert Thompson",
    "David Brown"
]

COMMENTAIRES = [
    "Excellent service",
    "Très satisfait",
    "Repas délicieux",
    "Livraison rapide",
    "Bonne expérience",
    "Je recommande",
    "Cuisine excellente",
    "Service professionnel",
    "Bon rapport qualité prix",
    "À améliorer"
]

STATUTS_COMMANDE = [
    "Livrée",
    "En préparation",
    "En cours de livraison",
    "Annulée"
]

CANAUX_COMMANDE = [
    "Application Mobile",
    "Site Web",
    "Téléphone",
    "Sur Place"
]

MODES_PAIEMENT = [
    "Wave",
    "Orange Money",
    "Free Money",
    "Carte Bancaire",
    "Espèces"
]

# ==========================================================
# FONCTIONS
# ==========================================================

def save_ndjson(filename, data):

    filepath = BRONZE_DIR / filename

    with open(filepath, "w", encoding="utf-8") as file:

        for row in data:

            file.write(
                json.dumps(
                    row,
                    ensure_ascii=False
                ) + "\n"
            )

    print(f"{filepath.name} généré")


def generate_phone():

    prefixe = random.choice(
        ["70", "75", "76", "77", "78"]
    )

    numero = random.randint(
        1000000,
        9999999
    )

    return f"+221{prefixe}{numero}"


def generate_client_name():

    if random.random() <= 0.80:

        prenom = random.choice(
            PRENOMS_HOMMES +
            PRENOMS_FEMMES
        )

        nom = random.choice(
            NOMS_SENEGALAIS
        )

        return f"{prenom} {nom}"

    return random.choice(
        CLIENTS_INTERNATIONAUX
    )


def generate_restaurant_name(index):

    if index <= len(RESTAURANTS_PRESTIGIEUX):

        return RESTAURANTS_PRESTIGIEUX[
            index - 1
        ]

    return (
        f"{random.choice(CATEGORIES)} "
        f"{random.choice(QUARTIERS)} "
        f"{index}"
    )


def generate_amount():

    return random.choices(
        population=[
            5000,
            7000,
            10000,
            12000,
            15000,
            20000,
            25000,
            30000,
            40000,
            50000,
            75000,
            100000
        ],
        weights=[
            20,
            18,
            16,
            14,
            12,
            10,
            8,
            6,
            5,
            4,
            2,
            1
        ]
    )[0]

# ==========================================================
# RESTAURANTS
# ==========================================================

restaurants = []

for i in range(1, NB_RESTAURANTS + 1):

    restaurants.append({

        "restaurant_id": i,

        "name": generate_restaurant_name(i),

        "quartier": random.choice(QUARTIERS),

        "ville": "Dakar",

        "pays": "Sénégal",

        "categorie": random.choice(CATEGORIES),

        "telephone": generate_phone(),

        "rating": round(
            random.uniform(3.0, 5.0),
            1
        ),

        "review_count": random.randint(
            20,
            5000
        ),

        "latitude": round(
            random.uniform(14.650, 14.800),
            6
        ),

        "longitude": round(
            random.uniform(-17.550, -17.300),
            6
        )
    })

# ==========================================================
# CLIENTS
# ==========================================================

clients = []

for i in range(1, NB_CLIENTS + 1):

    nom = generate_client_name()

    email = (
        nom.lower()
           .replace(" ", ".")
           .replace("é", "e")
           .replace("è", "e")
        + str(random.randint(1, 999))
        + "@gmail.com"
    )

    clients.append({

        "client_id": i,

        "nom": nom,

        "email": email,

        "telephone": generate_phone(),

        "ville": random.choice(VILLES),

        "pays": "Sénégal"
    })

# ==========================================================
# COMMANDES
# ==========================================================

commandes = []

for i in range(1, NB_COMMANDES + 1):

    date_commande = (
        datetime.now()
        - timedelta(
            days=random.randint(0, 365)
        )
    )

    commandes.append({

        "commande_id": i,

        "restaurant_id": random.randint(
            1,
            NB_RESTAURANTS
        ),

        "client_id": random.randint(
            1,
            NB_CLIENTS
        ),

        "montant": generate_amount(),

        "devise": "FCFA",

        "statut_commande": random.choice(
            STATUTS_COMMANDE
        ),

        "canal_commande": random.choice(
            CANAUX_COMMANDE
        ),

        "date_commande": date_commande.isoformat()
    })

# ==========================================================
# PAIEMENTS
# ==========================================================

paiements = []

for i in range(1, NB_PAIEMENTS + 1):

    date_paiement = (
        datetime.now()
        - timedelta(
            days=random.randint(0, 365)
        )
    )

    paiements.append({

        "paiement_id": i,

        "commande_id": i,

        "mode_paiement": random.choice(
            MODES_PAIEMENT
        ),

        "montant": generate_amount(),

        "devise": "FCFA",

        "date_paiement": date_paiement.isoformat()
    })

# ==========================================================
# AVIS
# ==========================================================

avis = []

for i in range(1, NB_AVIS + 1):

    avis.append({

        "avis_id": i,

        "restaurant_id": random.randint(
            1,
            NB_RESTAURANTS
        ),

        "client_id": random.randint(
            1,
            NB_CLIENTS
        ),

        "note": random.randint(1, 5),

        "commentaire": random.choice(
            COMMENTAIRES
        ),

        "date_avis": (
            datetime.now()
            - timedelta(
                days=random.randint(0, 365)
            )
        ).isoformat()
    })

# ==========================================================
# EXPORT BRONZE
# ==========================================================

save_ndjson("restaurants.json", restaurants)
save_ndjson("clients.json", clients)
save_ndjson("commandes.json", commandes)
save_ndjson("paiements.json", paiements)
save_ndjson("avis.json", avis)

# ==========================================================
# STATISTIQUES
# ==========================================================

print()
print("=" * 60)
print("DATASET BRONZE GÉNÉRÉ")
print("=" * 60)

print(f"Restaurants : {len(restaurants):,}")
print(f"Clients     : {len(clients):,}")
print(f"Commandes   : {len(commandes):,}")
print(f"Paiements   : {len(paiements):,}")
print(f"Avis        : {len(avis):,}")

print("=" * 60)