from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):

        self.count_is_main_tag = 0
        if len(self.forms) == 0:
            raise ValidationError('Не указаны теги!')
        for form in self.forms:
            if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
                raise ValidationError('Основной тег должен быть один.')
            else:
                if form.cleaned_data.get('is_main'):
                    print(f"{form.cleaned_data.get('tag')} - главный раздел")
                    self.count_is_main_tag += 1
                else:
                    continue

        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ArticleTagsInlineFormset
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = (ScopeInLine,)



