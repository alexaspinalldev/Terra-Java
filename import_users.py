from django.contrib.auth.models import User

users = [
    {"username": "roaster1", "email": "roaster1@example.com", "first_name": "Roaster's Delight", "last_name": "", "password": "password123"},
    {"username": "supplier2", "email": "supplier2@example.com", "first_name": "Global Coffee Supply", "last_name": "", "password": "password123"},
    {"username": "beanmaster", "email": "beanmaster@example.com", "first_name": "Bean Masters", "last_name": "", "password": "password123"},
    {"username": "javaexpert", "email": "javaexpert@example.com", "first_name": "Java Experts", "last_name": "", "password": "password123"},
    {"username": "brewcraft", "email": "brewcraft@example.com", "first_name": "Brew Craft", "last_name": "", "password": "password123"},
    {"username": "caffeineco", "email": "caffeineco@example.com", "first_name": "Caffeine Co", "last_name": "", "password": "password123"},
    {"username": "lattepro", "email": "lattepro@example.com", "first_name": "Latte Pro", "last_name": "", "password": "password123"},
    {"username": "espressox", "email": "espressox@example.com", "first_name": "Espresso X", "last_name": "", "password": "password123"},
    {"username": "javaworld", "email": "javaworld@example.com", "first_name": "Java World", "last_name": "", "password": "password123"},
    {"username": "coffeeroast", "email": "coffeeroast@example.com", "first_name": "Coffee Roast Co.", "last_name": "", "password": "password123"},
]

for user_data in users:
    user, created = User.objects.get_or_create(
        username=user_data["username"],
        defaults={
            "email": user_data["email"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
        }
    )
    if created:
        user.set_password(user_data["password"])
        user.save()
        print(f"User '{user.username}' created.")
    else:
        print(f"User '{user.username}' already exists.")
