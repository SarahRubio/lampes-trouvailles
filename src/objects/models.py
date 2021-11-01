
from os.path import splitext

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


from ckeditor.fields import RichTextField


def logo_upload_to(instance, filename):
    """Rename uploaded files with the object's slug."""

    _, extension = splitext(filename)
    name = instance.slug
    object_name = instance.__class__.__name__
    filename = '{}/{}_logo{}'.format(object_name, name, extension)
    return filename

def logo_upload_to_2(instance, filename):
    """Rename uploaded files with the object's slug."""

    _, extension = splitext(filename)
    name = instance.slug
    object_name = instance.__class__.__name__
    filename = '{}/{}_logo_2{}'.format(object_name, name, extension)
    return filename

def logo_upload_to_3(instance, filename):
    """Rename uploaded files with the object's slug."""

    _, extension = splitext(filename)
    name = instance.slug
    object_name = instance.__class__.__name__
    filename = '{}/{}_logo_3{}'.format(object_name, name, extension)
    return filename


class Light(models.Model):

    name = models.CharField(
        "Nom de la lampe",
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        "Slug",
        help_text="Laissez vide pour que le champ se remplisse seul",
        blank=True)
    reference = models.CharField(
        "référence de la lampe",
        max_length=256,
        null=True, blank=True,)
    description = RichTextField(
        "description de la lampe",
        null=True, blank=True)
    first_image = models.FileField(
        'photo n°1',
        null=True, blank=True,
        upload_to=logo_upload_to,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    second_image = models.FileField(
        'photo n°2',
        null=True, blank=True,
        upload_to=logo_upload_to_2,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    third_image = models.FileField(
        'photo n°3',
        null=True, blank=True,
        upload_to=logo_upload_to_3,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    price = models.IntegerField(
        "prix de la lampe",
        blank=True)
    designer = models.ManyToManyField(
        'filters.Designer',
        blank=True,
        related_name='lights',
        verbose_name="designer de la lampe")
    categories = models.ManyToManyField(
        'filters.Category',
        verbose_name="catégorie d'objets",
        related_name='lights',
        blank=True)
    subcategories = models.ManyToManyField(
        'filters.SubCategory',
        verbose_name="Sous catégorie d'objets",
        related_name='lights',
        blank=True)
    style = models.ManyToManyField(
        'filters.Style',
        verbose_name="Style de la lampe",
        related_name='lights',
        blank=True)
    materials = models.ManyToManyField(
        'filters.Material',
        verbose_name="Matériaux de la lampe",
        related_name='lights',
        blank=True)
    colors = models.ManyToManyField(
        'filters.Color',
        verbose_name="Couleurs de la lampe",
        related_name='lights',
        blank=True)
    weight = models.IntegerField(
        "poids de la lampe en kg",
        blank=True)
    height = models.IntegerField(
        "hauteur de la lampe en cm",
        blank=True)
    width = models.IntegerField(
        "largeur de la lampe en cm",
        blank=True)
    depth = models.IntegerField(
        "profondeur de la lampe en cm",
        blank=True)
    state = models.ManyToManyField(
        'filters.State',
        verbose_name="Etat de la lampe",
        related_name='lights',
        blank=True)
    key_words = RichTextField(
        "mots clés pouvant être associé à la lampe",
        null=True, blank=True)

    is_negotiable =  models.BooleanField(
        "Prix négociable?",
        default=False,
        help_text="Le prix de cet objet est-il négociable?")
    is_outstanding = models.BooleanField(
        "Pièce exceptionnelle?",
        default=False,
        help_text="Cet objet est-il une pièce exceptionnelle?")
    is_hightlighted =  models.BooleanField(
        "Pièce mise en avant?",
        default=False,
        help_text="Cet objet doit-il être mis en avant?")

    date_updated = models.DateTimeField(
        "Date de mise à jour",
        auto_now=True)
    date_created = models.DateTimeField(
        "Date de création",
        default=timezone.now)

    class Meta:
        verbose_name = 'Lampe'
        verbose_name_plural = 'Lampes'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]

    def get_absolute_url(self):
        url_args = [self.id]
        if self.slug:
            url_args.append(self.slug)
        return reverse('light-detail', args=url_args)


class Finding(models.Model):

    name = models.CharField(
        "Nom de la trouvaille",
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        "Slug",
        help_text="Laissez vide pour que le champ se remplisse seul",
        blank=True)
    reference = models.CharField(
        "référence de la trouvaille",
        max_length=256,
        null=True, blank=True,)
    description = RichTextField(
        "description de la trouvaille",
        null=True, blank=True)
    first_image = models.FileField(
        'photo n°1',
        null=True, blank=True,
        upload_to=logo_upload_to,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    second_image = models.FileField(
        'photo n°2',
        null=True, blank=True,
        upload_to=logo_upload_to_2,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    third_image = models.FileField(
        'photo n°3',
        null=True, blank=True,
        upload_to=logo_upload_to_3,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    price = models.IntegerField(
        "prix de la trouvaille",
        blank=True)
    designer = models.ManyToManyField(
        'filters.Designer',
        blank=True,
        related_name='findings',
        verbose_name="designer de la trouvaille")
    categories = models.ManyToManyField(
        'filters.Category',
        verbose_name="catégorie d'objets",
        related_name='findings',
        blank=True)
    subcategories = models.ManyToManyField(
        'filters.SubCategory',
        verbose_name="Sous catégorie d'objets",
        related_name='findings',
        blank=True)
    style = models.ManyToManyField(
        'filters.Style',
        verbose_name="Style de la trouvaille",
        related_name='findings',
        blank=True)
    materials = models.ManyToManyField(
        'filters.Material',
        verbose_name="Matériaux de la trouvaille",
        related_name='findings',
        blank=True)
    colors = models.ManyToManyField(
        'filters.Color',
        verbose_name="Couleurs de la trouvaille",
        related_name='findings',
        blank=True)
    weight = models.IntegerField(
        "poids de la trouvaille en kg",
        blank=True)
    height = models.IntegerField(
        "hauteur de la trouvaille en cm",
        blank=True)
    width = models.IntegerField(
        "largeur de la trouvaille en cm",
        blank=True)
    depth = models.IntegerField(
        "profondeur de la trouvaille en cm",
        blank=True)
    state = models.ManyToManyField(
        'filters.State',
        verbose_name="Etat de la trouvaille",
        related_name='findings',
        blank=True)
    key_words = RichTextField(
        "mots clés pouvant être associés à la trouvaille",
        null=True, blank=True)

    is_negotiable =  models.BooleanField(
        "Prix négociable?",
        default=False,
        help_text="Le prix de cet objet est-il négociable?")
    is_outstanding = models.BooleanField(
        "Pièce exceptionnelle?",
        default=False,
        help_text="Cet objet est-il une pièce exceptionnelle?")
    is_hightlighted =  models.BooleanField(
        "Pièce mise en avant?",
        default=False,
        help_text="Cet objet doit-il être mis en avant?")

    date_updated = models.DateTimeField(
        "Date de mise à jour",
        auto_now=True)
    date_created = models.DateTimeField(
        "Date de création",
        default=timezone.now)

    class Meta:
        verbose_name = 'Trouvaille'
        verbose_name_plural = 'Trouvailles'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]

    def get_absolute_url(self):
        url_args = [self.id]
        if self.slug:
            url_args.append(self.slug)
        return reverse('finding-detail', args=url_args)


class Furniture(models.Model):

    name = models.CharField(
        "Nom du meuble",
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        "Slug",
        help_text="Laissez vide pour que le champ se remplisse seul",
        blank=True)
    reference = models.CharField(
        "référence du meuble",
        max_length=256,
        null=True, blank=True,)
    description = RichTextField(
        "description du meuble",
        null=True, blank=True)
    first_image = models.FileField(
        'photo n°1',
        null=True, blank=True,
        upload_to=logo_upload_to,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    second_image = models.FileField(
        'photo n°2',
        null=True, blank=True,
        upload_to=logo_upload_to_2,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    third_image = models.FileField(
        'photo n°3',
        null=True, blank=True,
        upload_to=logo_upload_to_3,
        help_text="Assurez vous que l'image n'est pas trop lourde.")
    price = models.IntegerField(
        "prix du meuble",
        blank=True)
    designer = models.ManyToManyField(
        'filters.Designer',
        blank=True,
        related_name='furnitures',
        verbose_name="designer du meuble")
    categories = models.ManyToManyField(
        'filters.Category',
        verbose_name="catégorie d'objets",
        related_name='furnitures',
        blank=True)
    subcategories = models.ManyToManyField(
        'filters.SubCategory',
        verbose_name="Sous catégorie d'objets",
        related_name='furnitures',
        blank=True)
    style = models.ManyToManyField(
        'filters.Style',
        verbose_name="Style du meuble",
        related_name='furnitures',
        blank=True)
    materials = models.ManyToManyField(
        'filters.Material',
        verbose_name="Matériaux du meuble",
        related_name='furnitures',
        blank=True)
    colors = models.ManyToManyField(
        'filters.Color',
        verbose_name="Couleurs du meuble",
        related_name='furnitures',
        blank=True)
    weight = models.IntegerField(
        "poids du meuble en kg",
        blank=True)
    height = models.IntegerField(
        "hauteur du meuble en cm",
        blank=True)
    width = models.IntegerField(
        "largeur du meuble en cm",
        blank=True)
    depth = models.IntegerField(
        "profondeur du meuble en cm",
        blank=True)
    state = models.ManyToManyField(
        'filters.State',
        verbose_name="Etat du meuble",
        related_name='furnitures',
        blank=True)
    key_words = RichTextField(
        "mots clés pouvant être associés au meuble",
        null=True, blank=True)

    is_negotiable =  models.BooleanField(
        "Prix négociable?",
        default=False,
        help_text="Le prix de cet objet est-il négociable?")
    is_outstanding = models.BooleanField(
        "Pièce exceptionnelle?",
        default=False,
        help_text="Cet objet est-il une pièce exceptionnelle?")
    is_hightlighted =  models.BooleanField(
        "Pièce mise en avant?",
        default=False,
        help_text="Cet objet doit-il être mis en avant?")

    date_updated = models.DateTimeField(
        "Date de mise à jour",
        auto_now=True)
    date_created = models.DateTimeField(
        "Date de création",
        default=timezone.now)

    class Meta:
        verbose_name = 'Meuble'
        verbose_name_plural = 'Meubles'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]
    
    def get_absolute_url(self):
        url_args = [self.id]
        if self.slug:
            url_args.append(self.slug)
        return reverse('furniture-detail', args=url_args)
