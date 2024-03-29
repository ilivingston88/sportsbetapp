from django.db import models

# member model. not in use until login functionality complete.
class Member(models.Model):
  email = models.EmailField(max_length=125)
  firstname = models.CharField(max_length=125)
  lastname = models.CharField(max_length=125)
  phone = models.PositiveBigIntegerField()

class Sport(models.Model):
    key = models.CharField(max_length=100, unique=True, primary_key=True)  # Assuming the 'key' is unique for each sport
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Game(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="games", null=True)  # This establishes the relationship
    commence_time = models.DateTimeField()
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    outcomes = models.JSONField(null=True)

class Bookmaker(models.Model):
    key = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=200)

class Market(models.Model):
    key = models.CharField(max_length=100)
    last_update = models.DateTimeField()
    bookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE, related_name='markets')

class Outcome(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='outcome_set')
    bookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE, related_name='outcomes')
    name = models.CharField(max_length=200)  # Team name
    price = models.FloatField()
    point = models.FloatField(null=True, blank=True)  # Optional field for spreads
    
class TheOddsAPIData(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


