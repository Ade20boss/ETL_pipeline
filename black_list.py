import random
from faker import Faker

fake = Faker('en_US')

# --- 1. GENERATE BLACKLISTED EMAILS ---
# We use specific domains often associated with spam/burners for realism
spam_domains = ['spam-service.com', 'burner-mail.io', 'fake-inbox.net', 'temp-mail.org', 'bad-actor.biz']

blacklist_emails = []
for _ in range(7000):
    # Mix of normal looking emails and obvious spam domains
    if random.random() < 0.5:
        email = fake.email()
    else:
        email = f"{fake.user_name()}@{random.choice(spam_domains)}"
    blacklist_emails.append(email)

# --- 2. GENERATE BLACKLISTED PHONE NUMBERS ---
blacklist_phones = []

for _ in range(6780):
    # We use the same US formatting logic to ensure your regex matches these
    format_type = random.choice(['standard', 'no_parens', 'no_area_code', 'extension'])

    if format_type == 'standard':
        p = f"({fake.numerify('###')}) {fake.numerify('###-####')}"
    elif format_type == 'no_parens':
        sep = random.choice(['-', '.', ' '])
        p = f"{fake.numerify('###')}{sep}{fake.numerify('###')}{sep}{fake.numerify('####')}"
    elif format_type == 'no_area_code':
        p = f"{fake.numerify('###-####')}"
    elif format_type == 'extension':
        base = f"({fake.numerify('###')}) {fake.numerify('###-####')}"
        ext_sep = random.choice([' x', ' ext. ', ' #'])
        p = f"{base}{ext_sep}{fake.numerify('####')}"

    blacklist_phones.append(p)