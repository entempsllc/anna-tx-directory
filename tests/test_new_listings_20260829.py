
import pytest
from bs4 import BeautifulSoup
import os

def test_texas_roadhouse_anna_listing_contract():
    """Verify Texas Roadhouse Anna listing exists with correct first-party facts."""
    for path in ['index.html', 'anna-tx.html']:
        if not os.path.exists(path):
            continue
        with open(path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        # Find the link to Texas Roadhouse
        link = soup.find('a', href='https://www.texasroadhouse.com/locations/anna')
        assert link is not None, f"Texas Roadhouse link missing in {path}"
        assert "Texas Roadhouse" in link.text
        
        # Verify container facts
        card = link.find_parent('div', class_='biz-card') or link.find_parent('div', class_='biz-info')
        assert card is not None
        card_text = card.get_text()
        assert "201 S Central Expressway" in card_text
        assert "(945) 777-3409" in card_text
        assert "Steakhouse" in card_text

def test_brookshires_anna_listing_contract():
    """Verify Brookshire's Anna listing exists with correct first-party facts."""
    for path in ['index.html', 'anna-tx.html']:
        if not os.path.exists(path):
            continue
        with open(path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        # Find the link to Brookshire's
        link = soup.find('a', href='https://www.brookshires.com/store-information/Anna/131')
        assert link is not None, f"Brookshire's link missing in {path}"
        assert "Brookshire's" in link.text
        
        # Verify container facts
        card = link.find_parent('div', class_='biz-card') or link.find_parent('div', class_='biz-info')
        assert card is not None
        card_text = card.get_text()
        assert "1325 W White St" in card_text
        assert "(972) 924-8088" in card_text
        assert "Grocery Store" in card_text
        
        # Verify section id
        section = card.find_parent('div', class_='section')
        assert section is not None
        assert section.get('id') == 'grocery'
