import datetime
from django.shortcuts import render, redirect
from .models import Alumnos, Comentario, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
from django.db.models import Q


# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def comentarios(request):
    comentarios_lista = ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios': comentarios_lista})

def contacto(request):
    return render(request,"registros/contacto.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Comentarios')
    form = ComentarioContactoForm()
    return render(request,'registros/contacto.html',{'form': form})

def eliminarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html", {'comentarios':comentarios})
    return render(request, 'registros/confirmarEliminacion.html', {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})
def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
    return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultar3(request):
    alumnos=Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultar6(request):
    fechaInicio = datetime.date(2025, 7, 8)
    fechaFin = datetime.date(2025, 7, 12)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='Prueba de comentario')
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultaFirma1(request):
    fechaInicio = datetime.date(2025, 7, 8)
    fechaFin = datetime.date(2025, 7, 9)
    comentarios = ComentarioContacto.objects.filter(created__date__range=(fechaInicio, fechaFin))
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})
def consultaFirma2(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="servicio")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})
def consultaFirma3(request): #listo
    alumnos=Alumnos.objects.filter(nombre__in=["Monica"])
    return render(request, "registros/consultas.html", {'alumnos':alumnos})
def consultaFirma4(request):
    comentarios_solo_mensaje = ComentarioContacto.objects.only('mensaje')
    return render(request, "registros/comentarios.html", {'comentarios': comentarios_solo_mensaje})

def consultaFirma5(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__istartswith="Hola")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})


def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, "registros/seguridad.html", {'nombre': nombre})