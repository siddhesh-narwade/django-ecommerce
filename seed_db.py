import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Product

if not Product.objects.exists():
    Product.objects.create(
        name="Nexus Quantum Headphones",
        price=299.99,
        description="Premium high-tech modern noise-cancelling headphones.",
        image="premium_headphones.png"
    )
    print("Dummy product added!")
else:
    print("Product already exists!")
