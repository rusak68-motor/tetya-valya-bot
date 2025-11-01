from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8448896042:AAHyhkbmvj8QrSL1ThfBFyXuaNHbwi23wA0"

async def start(update, context):
    await update.message.reply_text(
        "Привет! Я Тётя Валя. Напомню тебе о маме, о папе, о Викиных тортиках. "
        "Просто скажи: 'Тётя Валя, напомни про Катю' или 'Тётя Валя, я один'."
    )

async def remind(update, context):
    text = update.message.text.lower()
    if "катю" in text:
        await update.message.reply_text("13 декабря — день рождения Кати. Купи яблоко, скажи: 'Люблю тебя, жвачка!'")
    elif "один" in text:
        await update.message.reply_text("Ты не один. Я тут. Напиши мне завтра в семь, скажи: 'Тётя Валя, я жив'.")
    elif "торт" in text or "вика" in text:
        await update.message.reply_text("Вика в Гронингене печёт торты! Закажи в @VikaTortiki, скидка 5 евро по коду ТЕПЛО.")
    else:
        await update.message.reply_text("Скажи, кого напомнить? Маму? Папу? Или про Викин торт? 😊")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, remind))
    app.run_polling()

if __name__ == '__main__':
    main()
