from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# --------------------
# CONFIGURACIÓN
# --------------------
TOKEN = "8284829820:AAFFqdjrUzHjKMRCzM2MZUX1XZ-TCD0mgzU"
IMAGEN_BIENVENIDA = "https://i.postimg.cc/xjmWCdgv/5807651020014816783.jpg"

# --------------------
# FUNCION DE BIENVENIDA
# --------------------
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_user in update.message.new_chat_members:
        # Mensaje de texto
        # Mensaje con imagen
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=IMAGEN_BIENVENIDA,
            caption=f"Hola {new_user.full_name}!!  \nBienvenido a XPEGaming , el grupo de los frikis.\nEntra y ponte cómodo! , dinos que plataformas juegas y a que estas jugando últimamente .\n\n PD: No se admite gente que haya tocado más de una teta "
        )

# --------------------
# INICIALIZAR BOT
# --------------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))
app.run_polling()


