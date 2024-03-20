from vkbottle.bot import BotLabeler, Message, rules
from vkbottle_types.objects import UsersUserFull

admin_labeler = BotLabeler()
admin_labeler.auto_rules = [rules.FromPeerRule(284629059)] # Допустим, вы являетесь Павлом Дуровым

@admin_labeler.message(command="halt")
async def halt(_):
    exit(0)


@admin_labeler.message(command="userinfo")
async def userinfo_handler(message: Message):
    userid = message.reply_message.from_id if message.reply_message else message.from_id
    user: UsersUserFull = (await message.ctx_api.users.get(userid))[0]
    await message.reply(f"Имя: {user.first_name}\n"
                        f"Фамилия: {user.last_name}\n"
                        f"Ссылка: https://vk.com/id{userid}\n"
                        f"id: {user.id}")
    
