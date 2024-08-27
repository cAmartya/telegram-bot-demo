from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application, MessageHandler, filters

import os, re
# from try_handler import Driver
from core.handler import Driver

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

text = []

driver = Driver()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  text.clear()
  await update.message.reply_text(f'Hello {update.effective_user.first_name}, you can send the reports now.')

async def end_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  print("recieved till now", len(text),text)

  with open("./tmp.txt", "w") as f:
    f.write('#'.join(text))

  await update.message.reply_text(f'preparing report')
  # driver.extract(text)
  try:
    driver.extract(text)
  except Exception as e:
    print(e)
  with open("./try.xlsx", "rb") as f:
    await update.message.reply_document(document=f)
  await update.message.reply_text(f'thank you')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  msg_type = update.message.chat.type
  msg_txt = update.message.text
  terminal = "#"
  # replace `=======` with "#" 
  msg_txt = re.sub(r'==+', terminal, msg_txt)
  for msg_block in msg_txt.split(terminal):
    if len(msg_block)>0:
      cleaned_block = msg_block.replace("*", " ").strip().lower()
      # remove whatsapp timestamp
      cleaned_block = re.sub(r'\[[^\]]*\]\s[^\:]*:\s*', "#", cleaned_block)
      for item in cleaned_block.split(terminal):
        if len(item)>0:
          text.append(item)

  print(f"user: {update.effective_user.first_name}, {update.message.chat.id} in {msg_type}: {msg_txt}")


async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f"update {update} caused error: {context.error}")
  await update.message.reply_text("Internal Error")


if __name__ == "__main__":

  app = ApplicationBuilder().token(TOKEN).build()

  # commands
  app.add_handler(CommandHandler("start", start_command))
  app.add_handler(CommandHandler("end", end_command))

  # messages
  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  # errors
  app.add_error_handler(handle_error)

  print("started polling, waiting for messages...")

  app.run_polling(poll_interval=1)