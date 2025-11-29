import random
from faker import Faker

fake = Faker('en_US')

# --- 1. GENERATE 1500 EMAILS ---
emails = [fake.email() for _ in range(400000)]

# --- 2. GENERATE 1000 COMPLEX US PHONE NUMBERS ---
phone_numbers = []

for _ in range(300000):
    # We roll a dice to see what format this number will be
    format_type = random.choice(['standard', 'no_parens', 'no_area_code', 'extension'])

    if format_type == 'standard':
        # Standard US: (555) 123-4567
        # We manually construct to ensure US area codes
        p = f"({fake.numerify('###')}) {fake.numerify('###-####')}"

    elif format_type == 'no_parens':
        # Separated by dots or dashes: 555.123.4567 or 555-123-4567
        sep = random.choice(["-", " "])
        p = f"{fake.numerify('###')}{sep}{fake.numerify('###')}{sep}{fake.numerify('####')}"

    elif format_type == 'no_area_code':
        # Just local: 555-0199
        p = f"{fake.numerify('###-####')}"

    elif format_type == 'extension':
        # Any format + extension: (555) 123-4567 x1234 or ext. 555
        base = f"({fake.numerify('###')}) {fake.numerify('###-####')}"
        ext_sep = random.choice([' x', ' ext. ', ' ext ', ' #'])
        ext_num = fake.numerify('####')
        p = f"{base}{ext_sep}{ext_num}"

    phone_numbers.append(p)

emails = "\n".join(emails)
phone_numbers = "\n".join(phone_numbers)