from django.db import models
from colorfield.fields import ColorField
from users.models import User
from .validators import validate_value


class Tag(models.Model):
    name = models.CharField('Название тега',
                            unique=True,
                            max_length=100)
    color = models.ColorField('Цвет тега',
                             default='#F000000')
    slug = models.SlugField('Уникальный слаг', unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Название', unique=True, max_length=200)
    measurement_unit = models.CharField('Мера', max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Описание', max_length=200)
    image = models.ImageField('Картинка', upload_to='recipes/images/')
    cooking_time = models.IntegerField(
        'Время приготовления (в минутах)', validators=[validate_value])
    tags = models.ManyToManyField(
        Tag, related_name='recipes', verbose_name='Теги')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes',
        verbose_name='Автор')
    ingredients = models.ManyToManyField(
        Ingredient, related_name='recipes', through='RecipeIngredient',
        verbose_name='Ингредиенты')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    amount = models.IntegerField('Количество', validators=[validate_value])
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.ingredient.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorites')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'], name='unique_favorite')
        ]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='shopping_cart')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='shopping_cart')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'], name='unique_cart')
        ]
