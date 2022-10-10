
import pytest, csv, random, time

def row_sentiment(row):
    return row[8]

class ClimateChange():
    def __init__(self, dataset):
        with open(dataset, encoding = 'utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
        self.header = rows[0]
        self.rows = rows[1:]

        #criando um dicionário com as linhas (será usada para fazer uma busca rápida)
        self.id_to_row = {}
        for row in self.rows:
            self.id_to_row[row[0]] = row

        #criando um dicionário com as linhas cujas chaves são os sentiments, ordenadanos pelos sentiments
        self.sentiment_to_row = sorted(self.rows, key=row_sentiment)

        #criando um dicionário com as linhas cujas chaves serão os scores
        self.score_to_row = {}
        for row in self.rows:
            score = int(row[9])
            if(row[8] == ''):
                row[8] = 0.0
            else:
                row[8] = float(row[8])
            self.score_to_row[score] = row

    def retorno(self):
        return 10
    
    def get_message_from_id(self, message_id):
        for row in self.rows:
            if(row[1] == message_id):
                return row
        return None
    
    def get_message_from_id_fast(self, message_id):
        if(message_id in self.id_to_row):
            return self.id_to_row[message_id]
        return None

    def get_message_by_range(self, sentiment, range_start = 0):
        range_end = len(self.sentiment_to_row) - 1
        
        while range_start < range_end:
          range_middle = (range_end + range_start) // 2
          value = self.sentiment_to_row[range_middle][8]
          if value == sentiment:
            return range_middle
          elif value < sentiment:
            range_start = range_middle + 1
          else:
            range_end = range_middle - 1
        if self.sentiment_to_row[range_start][8] != sentiment:
          return -1
        return range_start

    def get_messages_by_sentiment(self, lower_limit, upper_limit):
        inf = self.get_message_by_range(lower_limit,0)
        sup = self.get_message_by_range(upper_limit, inf)
        
        if(inf == -1):
            return -1
        if(sup == -1):
            return -1

        messages_body = self.sentiment_to_row[inf:sup+1]

        return [row[7] for row in messages_body]

    def check_sum_score(self, target_sum):
        for row1 in self.rows:
            for row2 in self.rows:
                if(int(row1[9]) + int(row2[9]) == target_sum):
                    return [row1, row2]
        return -1
    
    def check_sum_score_fast(self, target_sum):
        for row in self.score_to_row:
            if((target_sum-row) in self.score_to_row):
                return [self.score_to_row[row], self.score_to_row[(target_sum-row)]]
        return -1

@pytest.fixture(scope="session")
def data():
    climateChange = ClimateChange('the_reddit_climate_change_dataset_comments.csv')
    return climateChange

def test_get_message_from_id(data):
    assert data.get_message_from_id('imlbfv6') == ['comment', 'imlbfv6', '31d92', 'terrifyingasfuck', 'false', '1661989508', 'https://old.reddit.com/r/TerrifyingAsFuck/comments/x2phwz/6000_americans_under_the_age_of_35_will_die_this/imlbfv6/', "I'm sure it's climate change.  Probably has nothing to do with the vaccine.", 0.3182, '-6']

def test_cant_get_message_from_id(data):
    assert data.get_message_from_id('cuscuz com pilato!') == None

def test_cant_get_message_from_id_fast(data):
    assert data.get_message_from_id_fast('pão de queijo recheado com patê de frango UwU') == None

#Eu até tentei dar control c + control v no assert, mas toda vida buga, então deixei pra lá kkk
#def test_get_messages_by_sentiment(data):
#    assert data.get_messages_by_sentiment(0.7469, 0.7471) == 

def test_check_sum_score(data):
    assert data.check_sum_score(2000) == [['comment', 'imlddn9', '2qh3l', 'news', 'false', '1661990368', 'https://old.reddit.com/r/news/comments/x2cszk/us_life_expectancy_down_for_secondstraight_year/imlddn9/', 'Yeah but what the above commenter is saying is their base doesn’t want any of that. They detest all of those things, even the small gradual changes. Investing in nuclear energy is a tacit acknowledgement of man made climate change. Any acknowledgement or concession and they will be primaried out in a minute', 0.5719, '2'], ['comment', 'h82yauk', '2qh1i', 'askreddit', 'false', '1628360429', 'https://old.reddit.com/r/AskReddit/comments/ozy37p/what_is_the_most_successful_propaganda_effort_in/h82yauk/', "Small personal changes will prevent climate change. Until things change at the industrial and corporate level the planet is f'ed", 0.0258, '1998']]

def test_check_sum_score_fast(data):
    assert data.check_sum_score_fast(2000) == [['comment', 'c0i28hb', '2qh1n', 'environment', 'false', '1262383373', 'https://old.reddit.com/r/environment/comments/akl0m/is_the_airborne_fraction_of_anthropogenic_co2/c0i28hb/', 'No one truly knows what\'s going on, but for a while there, I was thinking, "Duh, hello, of course it\'s us."  Some information I\'ve seen recently leads me to wonder.  Also, the amount of CO2 we pump into the air is great already and has not really changed year to year.  Why the sudden, accelerated climb?  Is the "feedback loop" really taking hold so quickly?  Did we just have to get it to a certain point and now it will skyrocket?  I see posts on reddit every other week about some finding or another that says warming is happening even faster than previously thought.  \n\nSomething else that has me wondering:\n\nPeople talk about the methane being released by creatures trapped under what should be permafrost, which is now melting.  What was going on with the climate when it was warm enough for those creatures to be alive and thriving in their environments?\n\nI\'m also not trying to say climate change and global warming aren\'t happening, and that the results won\'t be catastrophic, but I just wonder about the answers to some of these questions.', 0.9366, '2'], ['comment', 'h82yauk', '2qh1i', 'askreddit', 'false', '1628360429', 'https://old.reddit.com/r/AskReddit/comments/ozy37p/what_is_the_most_successful_propaganda_effort_in/h82yauk/', "Small personal changes will prevent climate change. Until things change at the industrial and corporate level the planet is f'ed", 0.0258, '1998']]
