from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.postgres.fields import ArrayField

User = settings.AUTH_USER_MODEL
class Quiz(models.Model):
    question = models.CharField(max_length = 2500)
    option1 = models.CharField(max_length = 2000)
    option2 = models.CharField(max_length = 2000)
    option3 = models.CharField(max_length = 2000)
    option4 = models.CharField(max_length = 2000)
    answer = models.CharField(max_length = 2000)


    def __str__(self):
        return self.question
class QuizId(models.Model):
    quizid = models.CharField(max_length=12, default=0)

    def __str__(self):
        return self.quizid

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length = 50,default='name')
    mobileNumber=models.CharField(max_length = 12)
    TvashId = models.CharField(max_length=12,default=0)
    score=models.IntegerField(default=0)
    percentile=models.FloatField(default=0)
    ch1 = models.IntegerField(default=0)
    ch2 = models.IntegerField(default=0)
    ch3 = models.IntegerField(default=0)
    ch4 = models.IntegerField(default=0)
    ch5 = models.IntegerField(default=0)
    ch6 = models.IntegerField(default=0)
    ch7 = models.IntegerField(default=0)
    ch8 = models.IntegerField(default=0)
    ch9 = models.IntegerField(default=0)
    ch10 = models.IntegerField(default=0)

    ch11 = models.IntegerField(default=0)
    ch12 = models.IntegerField(default=0)
    ch13 = models.IntegerField(default=0)
    ch14 = models.IntegerField(default=0)
    ch15 = models.IntegerField(default=0)
    ch16 = models.IntegerField(default=0)
    ch17 = models.IntegerField(default=0)
    ch18 = models.IntegerField(default=0)
    ch19 = models.IntegerField(default=0)
    ch20 = models.IntegerField(default=0)

    ch21 = models.IntegerField(default=0)
    ch22 = models.IntegerField(default=0)
    ch23 = models.IntegerField(default=0)
    ch24 = models.IntegerField(default=0)
    ch25 = models.IntegerField(default=0)
    ch26 = models.IntegerField(default=0)
    ch27 = models.IntegerField(default=0)
    ch28 = models.IntegerField(default=0)
    ch29 = models.IntegerField(default=0)
    ch30 = models.IntegerField(default=0)

    ch31 = models.IntegerField(default=0)
    ch32 = models.IntegerField(default=0)
    ch33 = models.IntegerField(default=0)
    ch34 = models.IntegerField(default=0)
    ch35 = models.IntegerField(default=0)
    ch36 = models.IntegerField(default=0)
    ch37 = models.IntegerField(default=0)
    ch38 = models.IntegerField(default=0)
    ch39 = models.IntegerField(default=0)
    ch40 = models.IntegerField(default=0)

    ch41 = models.IntegerField(default=0)
    ch42 = models.IntegerField(default=0)
    ch43 = models.IntegerField(default=0)
    ch44 = models.IntegerField(default=0)
    ch45 = models.IntegerField(default=0)
    ch46 = models.IntegerField(default=0)
    ch47 = models.IntegerField(default=0)
    ch48 = models.IntegerField(default=0)
    ch49 = models.IntegerField(default=0)
    ch50 = models.IntegerField(default=0)

    ch51 = models.IntegerField(default=0)
    ch52 = models.IntegerField(default=0)
    ch53 = models.IntegerField(default=0)
    ch54 = models.IntegerField(default=0)
    ch55 = models.IntegerField(default=0)
    ch56 = models.IntegerField(default=0)
    ch57 = models.IntegerField(default=0)
    ch58 = models.IntegerField(default=0)
    ch59 = models.IntegerField(default=0)
    ch60 = models.IntegerField(default=0)


    login_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'UserProfile of user: {}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            try:
                instance.userprofile.save()
            except ObjectDoesNotExist:
                UserProfile.objects.create(user=instance)
#
    def save(self, *args, **kwargs):
        # calculate sum before saving.
        self.score = self.calculate_sum()

        super(UserProfile, self).save(*args, **kwargs)

    def calculate_sum(self):
        """ Calculate a numeric value for the model instance. """
        try:
            sum=self.ch1+self.ch2+self.ch3+self.ch4+self.ch5+self.ch6+self.ch7+self.ch8+self.ch9+self.ch10\
                +self.ch11+self.ch12+self.ch13+self.ch14+self.ch15+self.ch16+self.ch17+self.ch18+self.ch19+self.ch20\
                +self.ch21+self.ch22+self.ch23+self.ch24+self.ch25+self.ch26+self.ch27+self.ch28+self.ch29+self.ch30\
                +self.ch31+self.ch32+self.ch33+self.ch34+self.ch35+self.ch36+self.ch37+self.ch38+self.ch39+self.ch40\
                +self.ch41+self.ch42+self.ch43+self.ch44+self.ch45+self.ch46+self.ch47+self.ch48+self.ch49+self.ch50\
                +self.ch51+self.ch52+self.ch53+self.ch54+self.ch55+self.ch56+self.ch57+self.ch58+self.ch59+self.ch60

            return sum
        except KeyError:
            # Value_a or value_b is not in the VALUES dictionary.
            # Do something to handle this exception.
            # Just returning the value 0 will avoid crashes, but could
            # also hide some underlying problem with your data.
            return 0
