import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# ВКЛЮЧАЕМ ЛОГИ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ТВОЙ ТОКЕН — ПРОВЕРЬ, ЧТО ОН ТОЧНЫЙ!
TOKEN = "8448896042:AAHyhkbmvj8QrSL1ThfBFyXuaNHbwi23wA0"

async def start(update, context):
    logger.info("Получена команда /start от %s", update.effective_user.id)
    await update.message.reply_text(
        "Привет! Я Тётя Валя. Напомню тебе о маме, о папе, о Викиных тортиках. "
        "Просто скажи: 'Тётя Валя, напомни про Катю' или 'Тётя Валя, я один'."
    )

async def remind(update, context):
    text = update.message.text.lower()
    logger.info("Сообщение: %s", text)
    if "катю" in text:
        await update.message.reply_text("13 декабря — день рождения Кати. Купи яблоко, скажи: 'Люблю тебя, жвачка!'")
    elif "один" in text:
        await update.message.reply_text("Ты не один. Я тут. Напиши мне завтра в семь, скажи: 'Тётя Валя, я жив'.")
    elif "торт" in text or "вика" in text:
        await update.message.reply_text("Вика в Гронингене печёт торты! Закажи в @VikaTortiki, скидка 5 евро по коду ТЕПЛО.")
    else:
        await update.message.reply_text("Скажи, кого напомнить? Маму? Папу? Или про Викин торт? 😊")

async def error_handler(update, context):
    logger.error("Ошибка: %s", context.error, exc_info=True)

def main():
    logger.info("Запускаю Тётю Валю...")
    try:
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, remind))
        app.add_error_handler(error_handler)
        logger.info("Бот запущен. Ожидаю сообщения...")
        app.run_polling()
    except Exception as e:
        logger.error("КРИТИЧЕСКАЯ ОШИБКА: %s", e)

if __name__ == '__main__':
    main()
