from django.db import models


class NaverCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

    class Meta:
        managed = False
        db_table = 'naver_category'


class NaverBaseball(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_baseball'


class NaverBasketball(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_basketball'


class NaverEsports(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_esports'


class NaverFootball(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_football'


class NaverGeneral(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_general'


class NaverGolf(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_golf'


class NaverVolleyball(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_bolleyball'


class NaverWbaseball(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_wbaseball'


class NaverWfootball(models.Model):
    id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'naver_wfootball'
