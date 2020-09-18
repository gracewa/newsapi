import unittest
from .models import sources
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(
            'abc-news',
            'ABC',
            "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
            'https://abcnews.go.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))

if __name__ == '__main__':
    unittest.main()
