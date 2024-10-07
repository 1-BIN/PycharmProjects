# pip install python-telegram-bot==13.11
import os
import time
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

API_KEY = '7183918209:AAE9tQxHKuBO3KOablRc30XpIZDbomUSo-k'
updater = Updater(token=API_KEY, use_context=True)
f = None
def echo(update, context):
    user_id = update.effective_chat.id
    user_msg = update.message.text
    print(f"{user_id}, {user_msg}")
    context.bot.send_message(chat_id=user_id, text=user_msg)

def my_diary(update, context):
    global f    #전역변수 사용
    print("파일로 저장")
    user_id = update.effective_chat.id
    user_msg = update.message.text

    if '종료' in user_msg:
        if f:
            f.close()
        context.bot.send_message(chat_id= user_id, text='다이어리 종료')
    else:
        f = open('my_diary.txt', 'a', encoding ='utf8')
        f.write(user_msg.replace('/diary', '').strip())
        f.writelines('\n')
        context.bot.send_message(chat_id = user_id, text = '작성중...')

def save_photo(update, context):
    #1. 폴더 췤
    image_dir = '../python_base/img'
    if not os.path.exists(image_dir):  # 해당 경로가 존재하지 않으면
        os.makedirs(image_dir)
    #2. 이름 생성
    time_filename = time.strftime('%Y%m%d%H%M%S') + '.png'  # 이름을 시간으로 설정해줍니다.

    #3. 폴더 + 이름
    img_path = os.path.join(image_dir, time_filename)
    #4. 저장
    photo_id = update.message.photo[-1].file_id     #경로 설정 안해두면 현재 위치에 저장됩니다.
    photo_file = context.bot.getFile(photo_id)
    photo_file.download(img_path)
    update.message.reply_text('photo saved')


# 메세지 리턴
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)
# 일기 저장
diary_handler = CommandHandler('diary', my_diary)
updater.dispatcher.add_handler(diary_handler)
# 사진 저장
photo_handler = MessageHandler(Filters.photo, save_photo)
updater.dispatcher.add_handler(photo_handler)

updater.start_polling()
updater.idle()