import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
PUBLIC_PAGES = (ROOT / "index.html", ROOT / "anna-tx.html")


class WhataburgerAnnaListingContract(unittest.TestCase):
    def test_first_party_contact_facts_are_consistent(self):
        expected = (
            '<h3><a href="https://locations.whataburger.com/tx/anna/601-s-central-expy.html" '
            'target="_blank" rel="noopener">Whataburger</a></h3>'
            '<div class="biz-cat">American · Fast Food</div>'
            '<div class="biz-addr">📍 601 S Central Expy, Anna, TX 75409</div>'
            '<div class="biz-phone"><a href="tel:14694253825">📞 (469) 425-3825</a></div>'
        )
        stale = (
            '<h3>Whataburger</h3><div class="biz-cat">American · Fast Food</div>'
            '<div class="biz-addr">📍 1101 N Powell Pkwy, Anna, TX 75409</div>'
            '<div class="biz-phone">📞 (972) 924-6200</div>'
        )
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertEqual(source.count(expected), 1)
                self.assertNotIn(stale, source)

    def test_listing_is_not_duplicated(self):
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertEqual(source.count(">Whataburger</a></h3>"), 1)
                self.assertEqual(source.count("601 S Central Expy, Anna, TX 75409"), 1)


if __name__ == "__main__":
    unittest.main()
