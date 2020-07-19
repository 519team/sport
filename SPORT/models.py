from django.db import models

# Create your models here.
class Category(models.Model):
	index_cat=models.IntegerField(unique=True)
	name_category=models.CharField(max_length=50, db_index=True)

class Image(models.Model):
	path=models.FilePathField()

	def __str__(self):
		return self.path

class Size(models.Model):
	colour=models.CharField(max_length=50)
	size=models.CharField(max_length=50)
	table_price=models.IntegerField(null=True)
	count=models.IntegerField(null=True)

class Item(models.Model):
	index_item=models.IntegerField()
	title=models.CharField(max_length=500, db_index=True)
	manufacturer=models.CharField(max_length=500)
	articule=models.CharField(max_length=500, )
	dsc=models.TextField(null=True)
	one_price=models.IntegerField(null=True)
	more_price=models.IntegerField(null=True)
	image=models.ManyToManyField(Image)
	size=models.ManyToManyField(Size)
	id_category = models.ForeignKey(Category,on_delete = models.CASCADE)

	def __str__(self):
		return self.title

