
import os
from bs4 import BeautifulSoup

def verify():
    errors = []
    for path in ['index.html', 'anna-tx.html']:
        if not os.path.exists(path):
            errors.append(f"File missing: {path}")
            continue
        with open(path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        # Texas Roadhouse
        link_tr = soup.find('a', href='https://www.texasroadhouse.com/locations/anna')
        if not link_tr:
            errors.append(f"Texas Roadhouse link missing in {path}")
        else:
            card = link_tr.find_parent('div', class_='biz-card') or link_tr.find_parent('div', class_='biz-info')
            if not card:
                errors.append(f"Texas Roadhouse card missing in {path}")
            else:
                text = card.get_text()
                if "201 S Central Expressway" not in text: errors.append(f"TR Address missing in {path}")
                if "(945) 777-3409" not in text: errors.append(f"TR Phone missing in {path}")
        
        # Brookshire's
        link_b = soup.find('a', href='https://www.brookshires.com/store-information/Anna/131')
        if not link_b:
            errors.append(f"Brookshire's link missing in {path}")
        else:
            card = link_b.find_parent('div', class_='biz-card') or link_b.find_parent('div', class_='biz-info')
            if not card:
                errors.append(f"Brookshire's card missing in {path}")
            else:
                text = card.get_text()
                if "1325 W White St" not in text: errors.append(f"Brookshire's Address missing in {path}")
                if "(972) 924-8088" not in text: errors.append(f"Brookshire's Phone missing in {path}")
                section = card.find_parent('div', class_='section')
                if not section or section.get('id') != 'grocery':
                    errors.append(f"Brookshire's grocery section ID missing in {path}")

    if errors:
        for e in errors: print(f"FAIL: {e}")
        exit(1)
    else:
        print("PASS")

if __name__ == "__main__":
    verify()
