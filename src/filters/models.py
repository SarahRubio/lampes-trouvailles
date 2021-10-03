from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(
        "Nom de la catégorie d'objet",
        max_length=70)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    short_description = models.TextField(
        'description courte',
        blank=True)

    class Meta:
        verbose_name = "Catégorie d'objet"
        verbose_name_plural = "Catégories d'objet"

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    name = models.CharField(
        "Nom de la sous catégorie d'objet",
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    category = models.ForeignKey(
        'Category',
        verbose_name='Categorie',
        related_name='categories',
        on_delete=models.PROTECT)
    description = RichTextField(
        "description du type d'objet",
        null=True, blank=True)

    date_created = models.DateTimeField(
        'Date de création',
        default=timezone.now)

    class Meta:
        verbose_name = "Sous catégorie d'objet"
        verbose_name_plural = "Sous catégories d'objet"

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]


class Color(models.Model):

    name = models.CharField(
        "Nom de la couleur",
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    code = models.CharField(
        'Code de la couleur',
        max_length=256,
        db_index=True)

    date_created = models.DateTimeField(
        'Date de création',
        default=timezone.now)

    class Meta:
        verbose_name = 'Couleur'
        verbose_name_plural = 'Couleurs'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]


class Designer(models.Model):

    name = models.CharField(
        'Nom du designer',
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    description = RichTextField(
        'description du designer',
        null=True, blank=True)

    date_created = models.DateTimeField(
        'Date de création',
        default=timezone.now)

    class Meta:
        verbose_name = 'Designer'
        verbose_name_plural = 'Designers'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]


class Material(models.Model):

    name = models.CharField(
        'Nom du matériau',
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    description = RichTextField(
        'description du matériau',
        null=True, blank=True)

    date_created = models.DateTimeField(
        'Date de création',
        default=timezone.now)

    class Meta:
        verbose_name = 'Matériau'
        verbose_name_plural = 'Matériaux'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]


class State(models.Model):

    name = models.CharField(
        "Etat de l'objet",
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)

    class Meta:
        verbose_name = "Etat de l'objet"
        verbose_name_plural = "Etat de l'objet"

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]


class Style(models.Model):

    name = models.CharField(
        'Nom du style',
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    description = RichTextField(
        'description du style',
        null=True, blank=True)

    date_created = models.DateTimeField(
        'Date de création',
        default=timezone.now)

    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]
