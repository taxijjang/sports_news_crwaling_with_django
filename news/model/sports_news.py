from django.db import models


class SportsNews(models.Model):
    id = models.IntegerField(primary_key=True)
    flatform = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    rank = models.IntegerField()
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.rank}위 {self.title}"

    class Meta:
        managed= False
        db_table = 'sports_news'