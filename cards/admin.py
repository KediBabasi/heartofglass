from django.contrib import admin
from cards.models import Card


# Register your models here.
class CardAdmin(admin.ModelAdmin):
    """
    """
    list_filter = ('ana_tarife',)
    list_display = ('tarife_adi', 'ana_tarife', 'ucretlendirme', 'tarife_slug', )


admin.site.register(Card, CardAdmin)
