import csv, requests

class Profile:
    """Represents a profile to enter."""

    def __init__(self, row):
        self.email = row[0]
        self.first = row[1]
        self.last = row[2]
        self.zip = row[3]
        self.phone = row[4]

def load_profiles():
    """Loads profiles from a CSV format."""

    profile_list = []

    with open("./data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_id = 0

        for row in csv_reader:
            if row_id != 0:
                profile_list.append(Profile(row))
            row_id += 1

    return profile_list

def enter_raffle(email, first, last, zip, phone, size):
    """Enters raffle"""

    headers = {
        'authority': 'f1eb5xittl.execute-api.us-east-1.amazonaws.com',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'dnt': '1',
        'origin': 'https://shop.travisscott.com',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://shop.travisscott.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('a', 'm'),
        ('email', email),
        ('first', first),
        ('last', last),
        ('zip', zip),
        ('telephone', phone),
        ('product_id', phone),
        ('kind', 'shoe'),
        ('size', size),
    )

    response = requests.get('https://f1eb5xittl.execute-api.us-east-1.amazonaws.com/fragment/submit', headers=headers, params=params)
    if response.status_code == 200:
        print(f"Successfully entered {email}")
    else:
        print(f"Failed enter {email} ({str(response.status_code)})")

if __name__ == "__main__":
    size = input("Size: ")
    profiles = load_profiles()

    for profile in profiles:
        enter_raffle(
            email=profile.email,
            first=profile.first,
            last=profile.last,
            zip=profile.zip,
            phone=profile.phone,
            size=size
        )
