from django.shortcuts import render

from .models import Alumno, Genero
# Create your views here.

#Views de los html del CRUD

#def gestion(request):
#    listaSolicitudes = Solicitud.objects.all()
#    messages.success(request, '¡Solicitudes listadas!')
#    return render(request, "gestionsolicitudes.html", {"solicitudes": listaSolicitudes})

#def RegistrarSolicitud(request):
#    Id=request.POST['txtId']
#    Nombre_solicitud=request.POST['txtNombre_solicitud']
#    Mensaje=request.POST['txtMensaje']

#    solicitud = Solicitud.objects.create(Id=Id, Nombre_solicitud=Nombre_solicitud, Mensaje=Mensaje)
#    messages.success(request, '¡Solicitud registrada!')
#    return redirect('/')

#def editarSolicitud(request, Id):
#    solicitud = Solicitud.objects.get(Id=Id)
#    return render(request, "editarsolicitud.html", {"solicitud: solicitud"})

#def edicionSolicitud(request):
#    Id=request.POST['txtId']
#    Nombre_solicitud=request.POST['txtNombre_solicitud']
#    Mensaje=request.POST['txtMensaje']

#    solicitud = Solicitud.objects.get(Id=Id)
#    solicitud.Nombre_solicitud = Nombre_solicitud
#    solicitud.Mensaje = Mensaje
#    solicitud.save()
#    messages.success(request, '¡Solicitud modificada!')

#    return redirect('/')

#def eliminarSolicitud(request, Id):
#    solicitud = Solicitud.objects.get(Id=Id)
#    solicitud.delete()

#    messages.success(request, '¡Solicitud eliminada!')
#    return redirect('/')

def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)


def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def Nosotros(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Nosotros.html', context)

def Contacto(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Contacto.html', context)

def Fundaciones(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/fundaciones.html', context)

def Tienda(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Tienda.html', context)

def AliTienda(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Tienda subseccion alimentos.html', context)

def AcsTienda(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Tienda subseccion  accesorios.html', context)

def Login(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Login.html', context)

def ComidaPerro(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Comida Perro.html', context)

def ComidaGato(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Comida Gato.html', context)

def Collar(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Collar.html', context)

def Bebedero(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Bebedero.html', context) 

def Registro(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/Registro.html', context)

def gestionsolicitudes(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos\gestionsolicitudes.html', context)

def editarsolicitud(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos\editarsolicitud.html', context) 