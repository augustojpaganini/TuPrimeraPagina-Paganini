from django.shortcuts import render, redirect
from .models import Camiseta, Equipo, Cliente
from .forms import CamisetaForm, EquipoForm, ClienteForm


def inicio(request):
    return render(request, 'tienda/inicio.html')


# ---------- FORMULARIOS ----------
def camiseta_form(request):
    if request.method == 'POST':
        form = CamisetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_camisetas')
    else:
        form = CamisetaForm()
    return render(request, 'tienda/camiseta_form.html', {'form': form})


def equipo_form(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'tienda/equipo_form.html', {'form': form})


def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = ClienteForm()
    return render(request, 'tienda/cliente_form.html', {'form': form})


# ---------- LISTADOS ----------
def lista_camisetas(request):
    camisetas = Camiseta.objects.all()
    return render(request, 'tienda/lista_camisetas.html', {'camisetas': camisetas})


def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'tienda/lista_equipos.html', {'equipos': equipos})

def camisetas_por_equipo(request, slug):
    equipo = Equipo.objects.get(slug=slug)
    camisetas = Camiseta.objects.filter(equipo=equipo)
    return render(request, 'tienda/camisetas_por_equipo.html', {
        'equipo': equipo,
        'camisetas': camisetas
    })

# ---------- CARRITO ----------
from django.shortcuts import redirect

def agregar_al_carrito(request, camiseta_id):
    """Agrega una camiseta al carrito usando la sesión."""
    carrito = request.session.get('carrito', [])
    if camiseta_id not in carrito:
        carrito.append(camiseta_id)
    request.session['carrito'] = carrito
    return redirect('ver_carrito')


def ver_carrito(request):
    """Muestra las camisetas agregadas al carrito."""
    carrito = request.session.get('carrito', [])
    from .models import Camiseta
    camisetas = Camiseta.objects.filter(id__in=carrito)
    return render(request, 'tienda/ver_carrito.html', {'camisetas': camisetas})


def eliminar_del_carrito(request, camiseta_id):
    """Elimina una camiseta del carrito."""
    carrito = request.session.get('carrito', [])
    if camiseta_id in carrito:
        carrito.remove(camiseta_id)
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def buscar_camisetas(request):
    form = BusquedaCamisetaForm(request.GET or None)
    camisetas = []
    if form.is_valid():
        consulta = form.cleaned_data['consulta']
        camisetas = Camiseta.objects.filter(jugador__icontains=consulta)
    return render(request, 'tienda/buscar_camisetas.html', {'form': form, 'camisetas': camisetas})

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Camiseta, Equipo, Cliente
from .forms import CamisetaForm, EquipoForm, ClienteForm, BusquedaCamisetaForm

def buscar_camisetas(request):
    form = BusquedaCamisetaForm(request.GET or None)
    camisetas = Camiseta.objects.all()

    if form.is_valid():
        consulta = form.cleaned_data.get('consulta')
        if consulta:
            camisetas = camisetas.filter(
                Q(jugador__icontains=consulta) |
                Q(equipo__nombre__icontains=consulta) |
                Q(numero__icontains=consulta)
            )

    contexto = {
        'form': form,
        'camisetas': camisetas,
    }
    return render(request, 'tienda/buscar_camisetas.html', contexto)



