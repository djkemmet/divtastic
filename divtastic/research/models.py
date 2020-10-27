from django.db import models

# Create your models here.
class symbol_lookup_model(models.Model):
    symbol = models.CharField(max_length=5, help_text="AAPL,TSLA,SBUX,...")

    class Meta:
        verbose_name_plural='Symbols'

    def __str__(self):
        return self.symbol