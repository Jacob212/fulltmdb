import unittest
from fulltmdb import people


class PeopleTest(unittest.TestCase):
    def test_details(self):
        result = people.details(287)
        self.assertTrue(result['name'] == "Brad Pitt")

    def test_changes(self):
        result = people.changes(287)
        self.assertTrue('changes' in result)

    def test_movie_credits(self):
        result = people.movie_credits(287)
        self.assertTrue('cast' in result)

    def test_tv_credits(self):
        result = people.tv_credits(287)
        self.assertTrue('cast' in result)

    def test_combined_credits(self):
        result = people.combined_credits(287)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = people.external_ids(287)
        self.assertTrue('id' in result)

    def test_images(self):
        result = people.images(287)
        self.assertTrue('profiles' in result)

    def test_tagged_images(self):
        result = people.tagged_images(287)
        self.assertTrue('results' in result)

    def test_translations(self):
        result = people.translations(287)
        self.assertTrue('translations' in result)

    def test_latest(self):
        result = people.latest()
        self.assertTrue('id' in result)

    def test_popular(self):
        result = people.popular()
        self.assertTrue('results' in result)
