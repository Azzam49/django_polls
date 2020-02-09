import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    #uses 'date published' as a human-readable name for pub_date
    pub_date = models.DateTimeField('date published')

    #represents model by question_text
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #checks if was published in last 24 hour
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #one-to-many relation ship with Question modal and cascade is delete
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #represents model by its choice_text
    def __str__(self):
        return self.choice_text




# Some Django API commands:
# Question.objects.filter(question_text__startswith='What')

# Question.objects.get(pub_date__year=current_year)

# The following is identical to Question.objects.get(id=1).
#>>> Question.objects.get(pk=1)

# accessing our custom method
#>>> q.was_published_recently()
#True

# Question table have One-To-Many relation with Choice
# q = Question.objects.get(id=1)
# q.choice_set.all() # this returns all choices for q question
# _set : is the set of related records

#c = q.choice_set.create(choice_text='Just hacking again', votes=0)
# c.question # c is the choice, returns its forgien key question

#q.choice_set.count() # returns count