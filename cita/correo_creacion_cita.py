from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def enviar_correo(cliente, cita):
    destinatarios = [cliente.user.email, cita.estilista.user.email]
    asunto = "Nueva Cita Programada"
    mensaje = f"""
    
______________________________
Se ha generado una nueva cita. 
______________________________

Cliente: {cliente.user.get_full_name()}
Estilista: {cita.estilista.user.get_full_name()}

Servicio: {cita.servicio.nombre}

Descipción: {cita.servicio.descripcion}


Fecha: {cita.fecha} Hora: {cita.hora} 

"""
    send_mail(asunto, mensaje, "tyecit@gmail.com", destinatarios)
    
   