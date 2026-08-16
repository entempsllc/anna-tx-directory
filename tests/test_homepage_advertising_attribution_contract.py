import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HomepageAdvertisingAttributionContract(unittest.TestCase):
    def test_homepage_advertising_inquiry_is_source_attributable(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        match = re.search(r'<a\s+href="([^"]+)">Advertise Here</a>', html)
        self.assertIsNotNone(match, "Missing homepage Advertise Here link")
        href = match.group(1)
        self.assertEqual(
            href,
            "mailto:entempsllc@gmail.com?subject=Anna%20TX%20Directory%20-%20Advertising%20Inquiry%20-%20Homepage",
        )


if __name__ == "__main__":
    unittest.main()
