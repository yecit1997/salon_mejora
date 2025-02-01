from django.core.paginator import Paginator



def paginador(objeto,request):
    paginador = Paginator(objeto, 10)
    num_pagina = request.GET.get('page')
    objeto = paginador.get_page(num_pagina)
    return objeto

