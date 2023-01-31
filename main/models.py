from django.db import models



class Car(models.Model):   # Машина
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(
        verbose_name='цена',
    )
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    image = models.ImageField()
    phone = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    url = models.URLField(
        verbose_name='Ссылка на обьявление',
    )

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Продажа авто'



class Apartmentsforrent(models.Model):   # Аренда квартир
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(
        verbose_name='цена',
    )
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    image = models.ImageField()
    phone = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    url = models.URLField(
        verbose_name='Ссылка на обьявление',
    )

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Аренда квартир'






class Saleofapartments(models.Model):   # Продажа квартир
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(
        verbose_name='цена',
    )
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    image = models.ImageField()
    phone = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    url = models.URLField(
        verbose_name='Ссылка на обьявление',
    )

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Продажа квартир'



