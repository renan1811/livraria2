from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Editora
from .models import Autor
from .models import Livro


admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
