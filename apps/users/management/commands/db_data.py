users = [
    {"email": "zalalidinovrom@gmail.com", "password": "12345678"},
    {"email": "zr1216@auca.kg", "password": "12345678", "is_staff": True},
]

categories = [
    {"name": "Hair Salon"},
    {"name": "Barber"},
    {"name": "Spa"},
    {"name": "Nail Salon"},
    {"name": "Massage"}
]

businesses = [
    {
        "name": "Elite Hair Studio",
        "description": "Top-notch hair styling and grooming services.",
        "phone_number": "+996555123456",
        "email": "elitehair@example.com",
        "address": "123 Main Street, Bishkek",
        "categories": ["Hair Salon", "Barber"]  # Добавлены категории
    },
    {
        "name": "Grooming Experts",
        "description": "The best place for men's grooming.",
        "phone_number": "+996555654321",
        "email": "groomingexperts@example.com",
        "address": "456 Elm Street, Bishkek",
        "categories": ["Barber", "Massage"]  # Добавлены категории
    },
    {
        "name": "Beauty Haven",
        "description": "Luxury spa services for relaxation and rejuvenation.",
        "phone_number": "+996555987654",
        "email": "beautyhaven@example.com",
        "address": "789 Pine Avenue, Bishkek",
        "categories": ["Spa", "Nail Salon"]  # Добавлены категории
    }
]

specialists = [
    {
        "first_name": "Alina",
        "last_name": "Petrova",
        "business": "Elite Hair Studio"
    },
    {
        "first_name": "Dmitry",
        "last_name": "Ivanov",
        "business": "Grooming Experts"
    },
    {
        "first_name": "Irina",
        "last_name": "Sidorova",
        "business": "Beauty Haven"
    }
]

services = [
    {
        "name": "Haircut",
        "price": 500.00,
        "specialist": "Alina Petrova"
    },
    {
        "name": "Shave",
        "price": 300.00,
        "specialist": "Dmitry Ivanov"
    },
    {
        "name": "Hair Styling",
        "price": 1000.00,
        "specialist": "Alina Petrova"
    },
    {
        "name": "Manicure",
        "price": 600.00,
        "specialist": "Irina Sidorova"
    },
    {
        "name": "Pedicure",
        "price": 700.00,
        "specialist": "Irina Sidorova"
    }
]

time_slots = [
    {
        "specialist": "Alina Petrova",
        "date": "2024-11-29",
        "time": "10:00:00",
        "is_taken": False
    },
    {
        "specialist": "Dmitry Ivanov",
        "date": "2024-11-29",
        "time": "14:00:00",
        "is_taken": False
    },
    {
        "specialist": "Irina Sidorova",
        "date": "2024-11-29",
        "time": "16:00:00",
        "is_taken": False
    }
]
