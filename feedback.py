from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = '8063634034:AAG9xaNnqyLjyLtk8QdF3521uy7TSrTm1EI'
GROUP_CHAT_ID = -4660175120  # замени на chat_id своей беседы

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.forward_message(
            chat_id=GROUP_CHAT_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_message))

if __name__ == '__main__':
    app.run_polling()
