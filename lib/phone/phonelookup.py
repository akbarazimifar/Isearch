import phonenumbers 
from phonenumbers import timezone, carrier, geocoder
from lib.colors import *
from lib.phone.reputation import *

"""
👁️ Inspector -> https://github.com/N0rz3/Inspector
"""

async def look(phone: str):
    numbers = phonenumbers.parse(phone)
    valid = phonenumbers.is_valid_number(numbers)
    timezones = timezone.time_zones_for_number(numbers)
    carriers = carrier.name_for_number(numbers, None)
    country = geocoder.description_for_number(numbers, 'fr')
    international = phonenumbers.format_number(numbers, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    national = phonenumbers.format_number(numbers, phonenumbers.PhoneNumberFormat.NATIONAL)
    prefix = phonenumbers.format_number(numbers, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(" ")[0]
    country_code = phonenumbers.region_code_for_country_code(int(prefix))

    mobile = phonenumbers.number_type(numbers)
    if mobile == phonenumbers.PhoneNumberType.MOBILE:
                    types = f"[{GREEN}*{WHITE}] Type {GREEN}->{WHITE} Mobile"

    else:
                    types = f"[{GREEN}*{WHITE}] Type {GREEN}->{WHITE} Line fixed "

    print(f"""
{GREEN}> {WHITE}LookUp{GREEN}
---------------------------------------------------{WHITE}

[{GREEN}*{WHITE}] Valid {GREEN}->{WHITE} {valid}
{types}


[{GREEN}+{WHITE}] International phone number {GREEN}->{WHITE} {international}
[{GREEN}+{WHITE}] National phone number {GREEN}->{WHITE} {national}   
[{GREEN}+{WHITE}] Country prefix {GREEN}->{WHITE} {prefix}
[{GREEN}+{WHITE}] Country code {GREEN}->{WHITE} {country_code}
[{GREEN}+{WHITE}] Country {GREEN}->{WHITE} {country}
[{GREEN}+{WHITE}] TimeZone {GREEN}->{WHITE} {timezones}
[{GREEN}+{WHITE}] Carrier {GREEN}->{WHITE} {carriers}
""")
    print(await Main.check(national))