from django.db import models

class FlatFrom(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'flat_form_list'

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    flatform = models.ForeignKey(FlatFrom,on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'

