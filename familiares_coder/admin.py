from django.contrib import admin
from .models import*
#from .models import Familiar
#from .models import Mascota
#from .models import PeliculaFavorita
# Register your models here.

admin.site.register(Familiar)
admin.site.register(Mascota)
admin.site.register(PeliculaFavorita)
admin.site.register(Avatar)
admin.site.register(Mensaje)

#class FamiliarAdmin(admin.ModelAdmin):
#    list_display = ('nombre','apellido')
    
    
#admin.site.register(Familiar,FamiliarAdmin)

#class MascotaAdmin(admin.ModelAdmin):
#    list_display = ('nombre','edad','animal')
    
    
#admin.site.register(Mascota,MascotaAdmin)

#class PeliculaFavoritaAdmin(admin.ModelAdmin):
#    list_display = ('nombre','genero','estreno')
    
    
#admin.site.register(PeliculaFavorita,PeliculaFavoritaAdmin)

