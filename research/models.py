from django.db import models

# Create your models here.
class symbol_lookup_model(models.Model):
    symbol = models.CharField(max_length=5, help_text="AAPL,TSLA,SBUX,...")

    class Meta:
        verbose_name_plural='Symbols'

    def __str__(self):
        return self.symbol

class investment_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Investment Types"

    def __str__(self):
        return self.name

class user_profile_ideas(models.Model):
    idea_name = models.CharField(max_length=256, help_text='What do you want to call this portfolio?')
    investment_type = models.ForeignKey(investment_type, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Portfolio Ideas'

    def __str__(self):
        return self.idea_name


class portfolio_idea_entry(models.Model):
    pass


