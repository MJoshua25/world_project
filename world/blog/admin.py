# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from django.utils.safestring import mark_safe

from . import models

@register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user_id',
        'nom',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'user_id',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'user_id',
        'nom',
        'date_add',
        'date_upd',
        'statut',
    )


@register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image_detail.url))

    list_display = (
        'affiche_image',
        'id',
        'auteur',
        'category_id',
        'titre',
        'Description',
        'article_acceuil',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'auteur',
        'category_id',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'auteur',
        'category_id',
        'titre',
        'image_cat',
        'image_detail',
        'date_add',
        'date_upd',
        'statut',
    )
    raw_id_fields = ('tags',)


@register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add')
    list_filter = ('date_add', 'id', 'nom', 'date_add')


@register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user_id',
        'article_id',
        'content',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'user_id',
        'article_id',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'user_id',
        'article_id',
        'content',
        'date_add',
        'date_upd',
        'statut',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Tag, TagAdmin)
_register(models.Comment, CommentAdmin)