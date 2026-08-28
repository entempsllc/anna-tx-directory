import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
PUBLIC_PAGES = (ROOT / "index.html", ROOT / "anna-tx.html")


class ChickFilAAnnaListingContract(unittest.TestCase):
    def test_first_party_contact_facts_are_consistent(self):
        expected = (
            '<h3><a href="https://www.chick-fil-a.com/locations/tx/anna-town-center" '
            'target="_blank" rel="noopener">Chick-fil-A — Anna Town Center</a></h3>'
            '<div class="biz-cat">Restaurant · Fast Food</div>'
            '<div class="biz-addr">📍 513 S Central Expy, Anna, TX 75409</div>'
            '<div class="biz-phone"><a href="tel:14698404454">📞 (469) 840-4454</a></div>'
        )
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertEqual(source.count(expected), 1)

    def test_listing_is_not_duplicated_and_has_no_price_claim(self):
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertEqual(source.count(">Chick-fil-A — Anna Town Center</a></h3>"), 1)
                self.assertEqual(source.count("513 S Central Expy, Anna, TX 75409"), 1)
                card_start = source.index(">Chick-fil-A — Anna Town Center</a></h3>")
                card_end = source.index("</div>\n        </div>", card_start)
                self.assertNotIn("biz-badge", source[card_start:card_end])


if __name__ == "__main__":
    unittest.main()
