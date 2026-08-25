import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARKS_PAGE = ROOT / "blog" / "anna-parks.html"


class ParksParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.links = {}
        self._href = None
        self._link_text = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._link_text = []

    def handle_data(self, data):
        normalized = " ".join(data.split())
        if normalized:
            self.text.append(normalized)
            if self._href:
                self._link_text.append(normalized)

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links[" ".join(self._link_text)] = self._href
            self._href = None
            self._link_text = []


class OfficialParksPlanningContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = ParksParser()
        parser.feed(PARKS_PAGE.read_text(encoding="utf-8"))
        cls.text = " ".join(parser.text)
        cls.links = parser.links

    def test_official_planning_section_explains_current_and_future_status(self):
        self.assertIn("Plan your park visit with official City sources", self.text)
        self.assertIn("currently in development", self.text)
        self.assertIn("confirm current access, hours, and amenities", self.text)

    def test_official_city_links_cover_park_details_reservations_and_projects(self):
        expected = {
            "City parks and trails directory": "https://www.annatexas.gov/266/Parks-and-Trails",
            "Pavilion reservations and applications": "https://www.annatexas.gov/1180/Reservations-and-Applications",
            "Parks capital improvement projects": "https://www.annatexas.gov/1368/Parks-Capital-Improvement-Projects",
        }
        for label, url in expected.items():
            with self.subTest(label=label):
                self.assertEqual(url, self.links.get(label))

    def test_official_directory_examples_are_anna_specific(self):
        for place in (
            "Baldwin Park",
            "Bryant Park",
            "Johnson Park",
            "Natural Springs Park",
            "Sherley Heritage Park",
            "Slayter Creek Park",
        ):
            with self.subTest(place=place):
                self.assertIn(place, self.text)


if __name__ == "__main__":
    unittest.main()
