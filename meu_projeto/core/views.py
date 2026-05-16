from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
# from django.shortcuts import render

#ADD

def home(request):
    return render(request, 'home.html')



def home(request):
    produtos = Produto.objects.all()

    return render(request, 'home.html', {
        'produtos': produtos
    })


def criar(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        Produto.objects.create(
            nome=nome,
            preco=preco
        )

        return redirect('/')

    return render(request, 'criar.html')


def editar(request, id):

    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':

        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')

        produto.save()

        return redirect('/')

    return render(request, 'editar.html', {
        'produto': produto
    })


def deletar(request, id):

    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('/')

    return render(request, 'deletar.html', {
        'produto': produto
    })
