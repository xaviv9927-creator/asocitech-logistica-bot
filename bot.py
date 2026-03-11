import telebot
from flask import Flask
import threading
import os

# --- CONFIGURACIÓN OFICIAL ---
TOKEN = "8760433292:AAGPqzL1JLlmfJn9faWdlILV2LycoCr9xPk"
MI_CHAT_ID = "7501019675" 

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Ruta para que Render y Cron-job vean que el sistema está vivo
@app.route('/')
def home():
    return "SISTEMA ASOCITECH ACTIVO 🦾"

# --- EL MENSAJE TÉCNICO ---
MENSAJE_LOGISTICA = """
Holaaaaa 👋🏻, soy el asistente virtual oficial de **ASOCITECH Montes**. Este sistema ha sido diseñado exclusivamente para la gestión y consulta de tu logística institucional.

El equipo técnico de **ASOCITECH Montes** efectuará el abordaje en su institución en la fecha establecida en la invitación oficial.

**Requerimientos logísticos para la jornada:**

**1:** Concentración de la población estudiantil interesada para una **disertación técnica** de 15 a 20 minutos.

**2:** Designación de personal directivo o docentes coordinadores para una **sesión de trabajo** donde se **solventarán** dudas técnicas e **indicarán** los lineamientos.

**3:** Habilitación de un **espacio de alta capacidad y techado** (Cancha o Salón Multiusos).

**4:** Se requiere la **cooperación integral** del personal docente para asegurar el cumplimiento del protocolo de disciplina.

**5:** Posterior a la disertación, se llevará a cabo una **reunión de articulación técnica** con los docentes asignados.

⏳ **TIEMPO ESTIMADO:** Duración de **2 a 2.5 horas**.

⚠️ **NOTA:** No se requiere la consignación de prototipos o proyectos físicos en esta etapa.

💬 Si requiere asistencia adicional, ingrese su consulta a continuación.
"""

@bot.message_handler(commands=['start'])
def enviar_logistica(message):
    bot.send_message(message.chat.id, MENSAJE_LOGISTICA, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def gestionar_consultas(message):
    if str(message.chat.id) == MI_CHAT_ID:
        if message.reply_to_message and "ID_USUARIO:" in message.reply_to_message.text:
            try:
                target_id = message.reply_to_message.text.split("ID_USUARIO: ")[1].split("\n")[0]
                bot.send_message(target_id, f"<b>🔹 RESPUESTA DEL EQUIPO TÉCNICO:</b>\n\n{message.text}", parse_mode="HTML")
                bot.send_message(MI_CHAT_ID, "✅ Enviado.")
            except:
                bot.send_message(MI_CHAT_ID, "❌ Error al enviar.")
    else:
        reporte = (
            f"❓ <b>NUEVA CONSULTA</b>\n"
            f"ID_USUARIO: {message.chat.id}\n"
            f"NOMBRE: {message.from_user.first_name}\n"
            f"--------------------------------\n"
            f"MENSAJE: {message.text}\n"
            f"--------------------------------\n"
            f"💡 <i>Responde para contestar.</i>"
        )
        bot.send_message(MI_CHAT_ID, reporte, parse_mode="HTML")

# Función para correr el servidor web
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Lanzamos Flask en un hilo para que no bloquee al bot
    threading.Thread(target=run_flask).start()
    print("ASOCITECH Montes Online... 🦾")
    bot.polling(non_stop=True)
