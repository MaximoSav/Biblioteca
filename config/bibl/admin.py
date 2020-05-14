from django.contrib import admin
from bibl.models import Autor
from bibl.models import Libro
from bibl.models import Ejemplar
from bibl.models import Usuarios
# Register your models here.

admin.site.register(Autor,)
admin.site.register(Libro,)
admin.site.register(Ejemplar,)
admin.site.register(Usuarios,)
