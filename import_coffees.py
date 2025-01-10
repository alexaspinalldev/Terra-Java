from django.contrib.auth.models import User
from catalogue.models import Coffee

BEAN_CHOICES = [
    'arabica',
    'excelsa',
    'robusta',
    'liberica',
]

ROAST_LEVELS = [
    'light',
    'medium',
    'dark',
]

coffees = [
    {
        "coffee_name": "Safari Blend",
        "origin": "Ethiopia",
        "bean": "arabica",
        "taste_profile": "Bright and floral with hints of jasmine",
        "roast": "light",
        "description": "A vibrant coffee inspired by the Ethiopian highlands.",
        "vendor_username": "GlobalCoffeeSupply"
    },
    {
        "coffee_name": "Midnight Roast",
        "origin": "Colombia",
        "bean": "robusta",
        "taste_profile": "Bold and smoky with a chocolatey finish",
        "roast": "dark",
        "description": "Perfect for a rich espresso shot.",
        "vendor_username": "GlobalCoffeeSupply"
    },
    {
        "coffee_name": "Golden Hour",
        "origin": "Costa Rica",
        "bean": "arabica",
        "taste_profile": "Sweet and citrusy with a honeyed aroma",
        "roast": "medium",
        "description": "A lively coffee for a morning boost.",
        "vendor_username": "RoastersDelight"
    },
    {
        "coffee_name": "Harvest Moon",
        "origin": "Guatemala",
        "bean": "liberica",
        "taste_profile": "Earthy and complex with nutty undertones",
        "roast": "dark",
        "description": "A coffee blend for cozy evenings.",
        "vendor_username": "RoastersDelight"
    },
    {
        "coffee_name": "Caribbean Gold",
        "origin": "Jamaica",
        "bean": "arabica",
        "taste_profile": "Smooth and buttery with a hint of vanilla",
        "roast": "medium",
        "description": "A luxurious brew for special moments.",
        "vendor_username": "beanmaster"
    },
    {
        "coffee_name": "Jungle Blend",
        "origin": "Vietnam",
        "bean": "robusta",
        "taste_profile": "Rich and earthy with notes of cocoa",
        "roast": "dark",
        "description": "A bold coffee inspired by the tropics.",
        "vendor_username": "beanmaster"
    },
    {
        "coffee_name": "Morning Glory",
        "origin": "Kenya",
        "bean": "arabica",
        "taste_profile": "Bright and tangy with berry notes",
        "roast": "light",
        "description": "A zesty coffee to start the day.",
        "vendor_username": "brewcraft"
    },
    {
        "coffee_name": "Twilight Roast",
        "origin": "Indonesia",
        "bean": "liberica",
        "taste_profile": "Smoky and bold with a hint of spice",
        "roast": "dark",
        "description": "A rich coffee for bold palates.",
        "vendor_username": "brewcraft"
    },
    {
        "coffee_name": "Maple Morning",
        "origin": "Canada",
        "bean": "arabica",
        "taste_profile": "Sweet and smooth with a hint of maple",
        "roast": "medium",
        "description": "A coffee inspired by Canadian mornings.",
        "vendor_username": "caffeineco"
    },
    {
        "coffee_name": "Espresso Luxe",
        "origin": "Italy",
        "bean": "robusta",
        "taste_profile": "Strong and robust with a velvety finish",
        "roast": "dark",
        "description": "An Italian classic for espresso lovers.",
        "vendor_username": "espressox"
    },
    {
        "coffee_name": "Island Bliss",
        "origin": "Hawaii",
        "bean": "arabica",
        "taste_profile": "Tropical and smooth with notes of coconut",
        "roast": "medium",
        "description": "A tropical escape in every cup.",
        "vendor_username": "javaexpert"
    },
    {
        "coffee_name": "Aztec Harvest",
        "origin": "Mexico",
        "bean": "arabica",
        "taste_profile": "Rich and spicy with cinnamon undertones",
        "roast": "medium",
        "description": "A coffee inspired by Aztec traditions.",
        "vendor_username": "javaworld"
    },
    {
        "coffee_name": "Polar Night",
        "origin": "Norway",
        "bean": "robusta",
        "taste_profile": "Smoky and intense with a nutty finish",
        "roast": "dark",
        "description": "A robust blend for long nights.",
        "vendor_username": "javaworld"
    },
    {
        "coffee_name": "Swiss Velvet",
        "origin": "Switzerland",
        "bean": "arabica",
        "taste_profile": "Smooth and creamy with a chocolate hint",
        "roast": "medium",
        "description": "A luxurious blend inspired by Swiss chocolate.",
        "vendor_username": "lattepro"
    },
    {
        "coffee_name": "Sahara Breeze",
        "origin": "Egypt",
        "bean": "liberica",
        "taste_profile": "Floral and aromatic with notes of dates",
        "roast": "light",
        "description": "A delicate coffee inspired by the desert.",
        "vendor_username": "lattepro"
    }
]


for coffee_data in coffees:
    try:
        # Find the vendor using their username
        vendor = User.objects.get(username=coffee_data["vendor_username"])

        # Create the coffee entry
        coffee, created = Coffee.objects.get_or_create(
            coffee_name=coffee_data["coffee_name"],
            defaults={
                "origin": coffee_data["origin"],
                "bean": coffee_data["bean"],
                "taste_profile": coffee_data["taste_profile"],
                "roast": coffee_data["roast"],
                "description": coffee_data["description"],
                "vendor": vendor,
                "listing_approved": True,
            },
        )
        if created:
            print(f"Coffee '{coffee.coffee_name}' created for vendor '{vendor.username}'.")
        else:
            print(f"Coffee '{coffee.coffee_name}' already exists.")
    except User.DoesNotExist:
        print(f"Vendor '{coffee_data['vendor_username']}' does not exist. Coffee not created.")
