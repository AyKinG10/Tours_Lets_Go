from django.db import models

class Tour(models.Model):
    name = models.CharField('Name', max_length=50, )
    date = models.TimeField('Date', max_length=250,)
    equipment = models.TextField('Equipment')
    country = models.TextField('Country')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'