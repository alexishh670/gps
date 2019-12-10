from django.http import HttpResponse


def consular_gps(request):
    mensaje = request.GET['mensaje']
    return HttpResponse(mensaje)