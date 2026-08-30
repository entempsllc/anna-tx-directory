import pytest
from bs4 import BeautifulSoup
import os

def test_banks_anna_listing_contract():
    """Verify Cadence, Lamar National, and SouthState Bank Anna listings exist with correct facts."""
    expected_banks = [
        {
            "name": "Cadence Bank",
            "url": "https://cadencebank.com/find-a-location/cadence-anna-branch",
            "address": "402 W White St, Anna, TX 75409",
            "phone": "(972) 924-5626"
        },
        {
            "name": "Lamar National Bank",
            "url": "https://www.lamarnationalbank.com/contact/",
            "address": "1515 W White St, Anna, TX 75409",
            "phone": "(945) 732-4300"
        },
        {
            "name": "SouthState Bank",
            "url": "https://www.southstatebank.com/global/location-detail/801/1427-west-white-street",
            "address": "1427 West White Street, Anna, TX 75409",
            "phone": "(972) 924-3361"
        }
    ]
    
    for path in ['index.html', 'anna-tx.html']:
        full_path = os.path.join('/tmp/anna-listings-20260830', path)
        with open(full_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        # Check if Financial section exists
        financial_section = soup.find('div', id='financial')
        assert financial_section is not None, f"Financial section (id='financial') missing in {path}"
        
        for bank in expected_banks:
            # Find the link
            link = financial_section.find('a', href=bank["url"])
            assert link is not None, f"{bank['name']} link ({bank['url']}) missing in {path}"
            assert bank["name"] in link.text
            
            # Verify container facts
            card = link.find_parent('div', class_='biz-card') or link.find_parent('div', class_='biz-info')
            assert card is not None, f"Could not find biz-card container for {bank['name']} in {path}"
            
            card_text = card.get_text()
            assert bank["address"] in card_text, f"Address mismatch for {bank['name']} in {path}"
            assert bank["phone"] in card_text, f"Phone mismatch for {bank['name']} in {path}"
            
            # Check for tel: link
            tel_link = card.find('a', href=lambda h: h and h.startswith('tel:'))
            assert tel_link is not None, f"Click-to-call link missing for {bank['name']} in {path}"

if __name__ == "__main__":
    pytest.main([__file__])
