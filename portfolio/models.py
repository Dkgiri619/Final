from django.db import models


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/', default= 'NULL' )
    image2 = models.ImageField(upload_to='images/', default= 't')
    image3 = models.ImageField(upload_to='images/', default= 'sds')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=50, default=" ")
    text = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
