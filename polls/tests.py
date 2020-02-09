from django.test import TestCase
from django.utils import timezone

import datetime

from .models import Question

# application tests is placed here (in tests.py),the testing
# system will automatically find tests in any file whose name
# begins with test.
# testing system will create special database for testing 
# when we run the test, then it will look for test methods
# whose names begin with test.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() returns False for questions
        whose pub_date is in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # assertIs(a,b) checks if a object is b object,if 
        # failed it will raise an AssertionError
        self.assertIs(future_question.was_published_recently(),False)