from django.db import models

class FlatFromList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'flat_form_list'


