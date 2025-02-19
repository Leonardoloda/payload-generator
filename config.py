CREW = "crew"
HOTELS = "hotels"
MONTHLY_BLOCK_LIMIT = "monthly"

APPLICATION_CHOICES = [CREW, HOTELS, MONTHLY_BLOCK_LIMIT]

INT = "int"
BAT = "bat"

ENVIRONMENT_CHOICES = [INT, BAT]

CREW_DIRECTORY = "./samples/crew"
HOTELS_DIRECTORY = "./samples/hotels"
MONTHLY_BLOCK_LIMIT_DIRECTORY = "./samples/monthly"

PATHS_CONFIG = {
    CREW: CREW_DIRECTORY,
    HOTELS: HOTELS_DIRECTORY,
    MONTHLY_BLOCK_LIMIT: MONTHLY_BLOCK_LIMIT_DIRECTORY,
}

APPLICATION_CONFIG = {
    CREW: {
        "QUEUE_NAME": "RAW-ROSTER-JCT-%s-0",
        "TOPIC": "RAW-ROSTER-JCT-%s",
    },
    HOTELS: {
        "QUEUE_NAME": "emh-dev.ACES-HCD-%s-0",
        "TOPIC": "emh-dev.ACES-HCD-%s",
    },
    MONTHLY_BLOCK_LIMIT: {
        "QUEUE_NAME": "emh-dev.JCT-MBL-%s-0",
        "TOPIC": "emh-dev.JCT-MBL-%s",
    },
}
