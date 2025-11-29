import re
import time
print("LOADING DATA............")
print("")
from data import emails, phone_numbers
from black_list import blacklist_phones, blacklist_emails
print("DATA LOADED")


blacklist_phones = set(blacklist_phones)
blacklist_emails = set(blacklist_emails)


#PHONE REGEX PATTERN:
phone_regex = re.compile(r"""
                         ((\d{3})|(\(\d{3}\)))? #Area code is optional
                         [\s-]?             #First separator space or dash or dot
                         \d{3}                  #Three digit prefix
                         [-\s]                #Second separator space or dash or dot
                         \d{4}                  #Four digit number
                         (\s(ext(\.)?\s\d{2,5})|(\sx\d{2,5}))?                
                        """, re.VERBOSE)

email_regex = re.compile(r"""
                        \b                      #Word boundary
                        [a-zA-Z0-9_%+-]+        #Name part
                        @                       #At symbol
                        [a-zA-Z0-9_.-]+          #Domain name
                        \.                      #.
                        [a-zA-Z0-9]{2,}         #Top level domain
                        \b                      #Word boundary
""", re.VERBOSE)

time.sleep(3)
print("SCRAPING STARTED..............")
print("")
phone_nos = re.finditer(phone_regex, phone_numbers)
emailss = re.finditer(email_regex, emails)
phone_no_hits = []
email_hits = []
print("SCRAPING COMPLETED")

time.sleep(3)
print("CROSSREFERENCING, PLEASE WAIT.............")
print("")
for phone_no in phone_nos:
    phone_no = phone_no.group().strip()
    if phone_no in blacklist_phones:
        phone_no_hits.append(phone_no)
for email in emailss:
    email = email.group().strip()
    if email in blacklist_emails:
        email_hits.append(email)

print("CROSSREFERENCE COMPLETED")
print("")
print(f"{len(phone_no_hits)} phone number hits found: \n{"\n".join(phone_no_hits)}")
print("")
print(f"{len(email_hits)} email hits found: \n{"\n".join(email_hits)}")
