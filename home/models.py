from django.db import models
from django.utils.text import slugify

class menu(models.Model):
    menu_name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/%Y/%M/%D', default='img/ahiface.png')
    ratings =  GenericRelation(Rating, related_query_name= 'object_list')
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.menu_name)
        super(menu, self).save()

    def __str__(self):
        return '{}'.format(self.menu_name)