import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
PUBLIC_PAGES = (ROOT / "index.html", ROOT / "anna-tx.html")


class PizzaHutAnnaListingContract(unittest.TestCase):
    def test_first_party_contact_facts_are_consistent(self):
        expected = (
            '<h3><a href="https://locations.pizzahut.com/tx/anna/628-w-white-st" '
            'target="_blank" rel="noopener">Pizza Hut</a></h3>'
            '<div class="biz-cat">Pizza · Delivery &amp; Carryout</div>'
            '<div class="biz-addr">📍 628 W White St, Anna, TX 75409</div>'
            '<div class="biz-phone"><a href="tel:14698405105">📞 (469) 840-5105</a></div>'
        )
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertEqual(source.count(expected), 1)
                self.assertNotIn(
                    "<h3>Pizza Hut Anna</h3><div class=\"biz-cat\">Pizza · Delivery</div>"
                    "<div class=\"biz-addr\">📍 Powell Pkwy, Anna, TX 75409</div>"
                    "<div class=\"biz-phone\">📞 (972) 924-5560</div>",
                    source,
                )

    def test_listing_is_not_duplicated(self):
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertEqual(source.count(">Pizza Hut</a></h3>"), 1)
                self.assertEqual(source.count("628 W White St, Anna, TX 75409"), 1)


if __name__ == "__main__":
    unittest.main()
