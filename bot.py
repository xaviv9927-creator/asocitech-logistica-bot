import telebot

# --- CONFIGURACIÓN OFICIAL ASOCITECH ---
TOKEN = "8760433292:AAGPqzL1JLlmfJn9faWdlILV2LycoCr9xPk"
MI_CHAT_ID = "7501019675" 

bot = telebot.TeleBot(TOKEN)

# --- MENSAJE DE PROTOCOLO TÉCNICO ---
MENSAJE_LOGISTICA = """
Holaaaaa 👋🏻, soy el asistente virtual oficial de **ASOCITECH Montes**. Este sistema ha sido diseñado exclusivamente para la gestión y consulta de tu logística institucional.

El equipo técnico de **ASOCITECH Montes** efectuará el abordaje en su institución en la fecha establecida en la invitación oficial.

**Requerimientos logísticos para la jornada:**

**1:** Concentración de la población estudiantil interesada para una **disertación técnica** de 15 a 20 minutos. En este espacio se expondrá el alcance de la ruta científica, las áreas de investigación y las metodologías de trabajo.

**2:** Designación de personal directivo o docentes coordinadores para una **sesión de trabajo** con el equipo de **ASOCITECH MONTES**. En este encuentro se **solventarán** dudas técnicas y se **indicarán** los lineamientos y protocolos a seguir para la participación en las EXPOCIENCIAS municipales.

**3:** Habilitación de un **espacio de alta capacidad y techado** (Cancha o Salón Multiusos) para la agrupación de los alumnos, garantizando la organización, el orden y la disciplina necesarios para el desarrollo de la actividad.

**4:** Se requiere la **cooperación integral** del personal docente para asegurar el cumplimiento del protocolo de disciplina durante la disertación general. El orden es un factor determinante para el éxito de la operación.

**5:** Posterior a la disertación general, se llevará a cabo una **reunión de articulación técnica** con los docentes asignados. El objetivo es profundizar en los procesos de registro, cronogramas de evaluación y criterios específicos de ingeniería.

⏳ **TIEMPO ESTIMADO:** El despliegue completo (Disertación + Reunión de Articulación) contempla una duración de **2 a 2.5 horas**.

⚠️ **NOTA:** Esta jornada es de carácter organizativo y técnico. No se requiere la consignación de prototipos o proyectos físicos en esta etapa.

💬 Si requiere asistencia adicional, ingrese su consulta a continuación y nuestro equipo técnico le responderá a la brevedad.
"""

@bot.message_handler(commands=['start'])
def enviar_logistica(message):
    bot.send_message(message.chat.id, MENSAJE_LOGISTICA, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def gestionar_consultas(message):
    # Si tú respondes a un reporte del bot desde tu Telegram
    if str(message.chat.id) == MI_CHAT_ID:
        if message.reply_to_message and "ID_USUARIO:" in message.reply_to_message.text:
            try:
                # Extraer el ID del usuario para mandarle tu respuesta
                target_id = message.reply_to_message.text.split("ID_USUARIO: ")[1].split("\n")[0]
                bot.send_message(target_id, f"<b>🔹 RESPUESTA DEL EQUIPO TÉCNICO:</b>\n\n{message.text}", parse_mode="HTML")
                bot.send_message(MI_CHAT_ID, "✅ Respuesta enviada con éxito.")
            except Exception as e:
                bot.send_message(MI_CHAT_ID, f"❌ Error al procesar respuesta: {e}")
    else:
        # Si un chamo o profe escribe, te llega a ti
        reporte = (
            f"❓ <b>NUEVA CONSULTA LOGÍSTICA</b>\n"
            f"ID_USUARIO: {message.chat.id}\n"
            f"NOMBRE: {message.from_user.first_name}\n"
            f"--------------------------------\n"
            f"MENSAJE: {message.text}\n"
            f"--------------------------------\n"
            f"💡 <i>Responde a este mensaje para contestar al usuario.</i>"
        )
        bot.send_message(MI_CHAT_ID, reporte, parse_mode="HTML")

print("ASOCITECH Montes Online... 🦾")
bot.polling()
