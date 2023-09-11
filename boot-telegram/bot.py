from telegram.ext import *
import responses, constants

print('Starting a bot....')

async def start_command(update, context):
    await update.message.reply_text(f"Hello {update.message.from_user['first_name']} Welcome!")

async def help_command(update, context):
    await update.message.reply_text("Hi or Hello -> return 'Hey, what's up\nchannel -> return Youtube link: https://youtube.com")

async def handle_message(update, context):
    txt = str(update.message.text).lower()
    response = responses.sample_responses(txt)
    await update.message.reply_text(response)

async def error(update, context):
    await print(f"Update: {update} caused error: {context.error}")

if __name__ == '__main__':
    application = Application.builder().token(constants.API_KEY).build()

    # Commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Run bot
    application.run_polling(1.0)