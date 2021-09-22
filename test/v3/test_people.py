import unittest
from fulltmdb import People


class PeopleTest(unittest.TestCase):
    def test_details(self):
        result = People.details(287)
        self.assertTrue(result['name'] == "Brad Pitt")

    def test_changes(self):
        result = People.changes(287)
        self.assertTrue('changes' in result)

    def test_movie_credits(self):
        result = People.movie_credits(287)
        self.assertTrue('cast' in result)

    def test_tv_credits(self):
        result = People.tv_credits(287)
        self.assertTrue('cast' in result)

    def test_combined_credits(self):
        result = People.combined_credits(287)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = People.external_ids(287)
        self.assertTrue('id' in result)

    def test_images(self):
        result = People.images(287)
        self.assertTrue('profiles' in result)

    def test_tagged_images(self):
        result = People.tagged_images(287)
        self.assertTrue('results' in result)

    def test_translations(self):
        result = People.translations(287)
        self.assertTrue('translations' in result)

    def test_latest(self):
        result = People.latest()
        self.assertTrue('id' in result)

    def test_popular(self):
        result = People.popular()
        self.assertTrue('results' in result)
