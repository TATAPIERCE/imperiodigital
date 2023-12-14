from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Cita
from .forms import CitaForm
from django.contrib import messages
# Create your views here.

def RenderTemplate(request):
    form = CitaForm()
    citas = Cita.objects.all()
    return render(request,'index.html',{'form': form, 'citas': citas})

def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():

            servicio = form.cleaned_data['servicio']
            nombre_del_cliente = form.cleaned_data['nombre_del_cliente']
            direccion = form.cleaned_data['direccion']
            fecha = form.cleaned_data['fecha']
            celular = form.cleaned_data['celular']
            hora_inicio = form.cleaned_data['hora_inicio']
            descripcion = form.cleaned_data['descripcion']

            subject = 'Nueva cita agendada'
            message = f'''
                Servicio: {servicio}
                Nombre del Cliente: {nombre_del_cliente}
                Dirección: {direccion}
                Numero Celular: {celular}
                Fecha: {fecha}
                Hora de Inicio: {hora_inicio}
                Descripción del problema: {descripcion}
            '''
            recipient_list = ['ImperioDigital3315@gmail.com']

            send_mail(subject, message, 'ImperioDigital3315@gmail.com', recipient_list)

            return redirect('index')

    else:
        form = CitaForm()

    return render(request, 'index.html', {'form': form})


def enviar_correo_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')

        subject = 'Mensaje de Contacto'
        message = f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}'
        from_email = 'ImperioDigital3315@gmail.com'
        recipient_list = ['ImperioDigital3315@gmail.com']

        send_mail(subject, message, from_email, recipient_list)

    return render(request, 'index.html')



    


