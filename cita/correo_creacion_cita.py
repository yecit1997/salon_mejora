from django.core.mail import send_mail


def enviar_correo(cliente, cita):
    destinatarios = [cliente.user.email, cita.estilista.user.email]
    asunto = "Nueva Cita Programada"
    mensaje = f"""Se ha generado una nueva cita. 
            Servicio: {cita.servicio.nombre} 
            Cliente: {cliente.user.get_full_name()} 
            Estilista: {cita.estilista.user.get_full_name()} 
            Fecha: {cita.fecha} Hora: {cita.hora} """
    send_mail(asunto, mensaje, "tusitioweb@correo.com", destinatarios)
