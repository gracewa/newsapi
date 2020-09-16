import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(
            'Formidable challenges await as Suga set to take over as Japan PM',
            'The 71-year-old will need all his political skills to deal with COVID-19, a ravaged economy and an ageing population.',
            'https://www.aljazeera.com/mritems/Images/2020/9/16/f255185330504915b6d027e446a63dbf_18.jpg',
            '2020-09-16T01:51:00Z'
            'https://www.gsmarena.com/sony_denies_cutting_playstation_5_production_targets-news-45291.php'
            "(CNN)President Donald Trump said in March that he didn't consider the coronavirus pandemic a once-in-a-lifetime leadership challenge, even as the country was going through historic shutdowns to fight… [+4458 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()
