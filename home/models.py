from django.db import models

class menu(models.Model):
    menu_name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/%Y/%M/%D', default='img/ahiface.png')

    def __str__(self):
        return '{}'.format(self.menu_name)