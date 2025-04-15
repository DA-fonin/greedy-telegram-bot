import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

GREEDY_SITE = "https://greedy.finance/"
HAPI_SCORE_LINK = "http://t.me/herewalletbot/app?startapp=web-score-hapi-mobi"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🍀 Ahoy, seeker of fortune! I’m the Greedy Leprechaun. Ask me about Greedy, Trust Score, or the next drop. Ready when you are!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()

    if "what is greedy" in msg or "greedy?" in msg:
        await update.message.reply_text(
            "🧙‍♂️ Greedy.finance is a drop platform where your patience and Trust Score decide how many tokens you earn. No luck. No whitelists. Just farming magic."
        )
    elif "trust score" in msg:
        await update.message.reply_text(
            f"🧠 Your Trust Score is checked via HAPI Protocol. The higher it is — the more you earn.\nCheck yours here: {HAPI_SCORE_LINK}"
        )
    elif "greed level" in msg:
        await update.message.reply_text(
            "⏳ Greed Level is how long you're willing to wait to claim your reward (1–100 hours). The longer you wait — the bigger the prize!"
        )
    elif "site" in msg or "website" in msg:
        await update.message.reply_text(f"🖥 Greedy portal: {GREEDY_SITE}")
    elif "drop" in msg:
        await update.message.reply_text("🎯 First come, first served! When the drop is live, you’ll see it at greedy.finance. Stay sharp!")
    elif "что такое greedy" in msg or "greedy?" in msg:
        await update.message.reply_text(
            "🧙‍♂️ Greedy.finance — это дроп-платформа, где твой HAPI Trust Score и терпение решают, сколько токенов ты получишь. Без вайтлистов, без рандома — только магия блокчейна."
        )
    elif "trust score" in msg or "траст скор" in msg:
        await update.message.reply_text(
            f"🧠 Trust Score — это твоя репутация в NEAR, проверяется через HAPI. Чем выше — тем жирнее дроп.\nПроверь тут: {HAPI_SCORE_LINK}"
        )
    elif "уровень жадности" in msg or "greed level" in msg:
        await update.message.reply_text(
            "⏳ Уровень жадности — это сколько часов ты готов ждать (от 1 до 100). Чем больше ждёшь — тем больше получаешь!"
        )
    elif "сайт" in msg:
        await update.message.reply_text(f"🖥 Ворота к богатству: {GREEDY_SITE}")
    elif "дроп" in msg:
        await update.message.reply_text("🎯 Кто успел — тот и съел. Следи за дропами на сайте!")
    else:
        await update.message.reply_text("🍀 Ask me anything about Greedy, drops, Trust Score or Greed Level!")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
