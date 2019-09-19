from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
# Create your models here.


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    user_id = models.ForeignKey(User, related_name='User_Category', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255,)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField()

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return 'Category: {}'.format(self.nom)

class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    auteur = models.ForeignKey(User, related_name='User_Article', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', related_name='Category_Article', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    titre = models.CharField(max_length=255)
    Description = models.TextField(null=True)
    contenu = HTMLField('Contenu', default="null")
    image_cat = models.ImageField(upload_to='Article/')
    image_detail = models.ImageField(upload_to='Article/')
    article_acceuil = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField()

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return 'Article : {} by {}'.format(self.titre, self.auteur)



class Tag(models.Model):
    """Model definition for Tag."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return 'Tag: {}'.format(self.nom)


class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    user_id = models.ForeignKey(User, related_name='User_Comment', on_delete=models.CASCADE)
    article_id = models.ForeignKey('Article', related_name='Article_Comment', on_delete=models.CASCADE)
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField()



    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        pass
