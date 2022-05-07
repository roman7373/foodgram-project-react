from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from online_service.models import (Ingredient, Recipe,
                                   RecipeIngredient, Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')


class IngredientResource(resources.ModelResource):

    class Meta:
        model = Ingredient


class IngredientAdmin(ImportExportActionModelAdmin):
    resource_class = IngredientResource
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name',)


# class IngredientAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'measurement_unit')
#    list_filter = ('name',)


class RecipeIgredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIgredientInline,)
    list_display = ('id', 'name', 'author')
    list_filter = ('name', 'author', 'tags')
    readonly_fields = ('favorites',)

    def favorites(self, obj):
        return obj.favorites.count()

    favorites.short_description = 'В избранном'


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
