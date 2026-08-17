import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AdvertisingOfferContract(unittest.TestCase):
    def test_homepage_links_to_advertising_offer(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('<a href="/advertising.html">Advertise Here</a>', html)

    def test_offer_is_disclosed_and_source_attributable(self):
        html = (ROOT / "advertising.html").read_text(encoding="utf-8")
        self.assertIn("Paid placement does not buy a review, rating, endorsement", html)
        self.assertIn("No audience size, results, or response volume is guaranteed", html)
        match = re.search(r'href="(mailto:[^"]+)">Email an advertising inquiry</a>', html)
        if match is None:
            self.fail("Missing source-attributable advertising inquiry link")
        self.assertEqual(
            match.group(1),
            "mailto:entempsllc@gmail.com?subject=Anna%20TX%20Directory%20-%20Advertising%20Inquiry%20-%20Advertising%20Page",
        )


if __name__ == "__main__":
    unittest.main()
