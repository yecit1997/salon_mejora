from django.core.paginator import Paginator



def paginador(objeto,f):
    paginador = Paginator(objeto, 12)
    num_pagina = f.GET.get('page')
    objeto = paginador.get_page(num_pagina)
    return objeto

