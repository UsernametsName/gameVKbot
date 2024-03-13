from vkbottle.bot import BotLabeler, Message, rules
from vkbottle_types.objects import MessagesConversation, UsersUser
from vkbottle_types.events import MessageTypingState


class ChatInfoRule(rules.ABCRule[Message]):
    async def check(self, message: Message) -> dict:
        chats_info = await message.ctx_api.messages.get_conversations_by_id(message.peer_id)
        return {"chat": chats_info.items[0]}


chat_labeler = BotLabeler()
chat_labeler.vbml_ignore_case = True
chat_labeler.auto_rules = [rules.PeerRule(from_chat=True), ChatInfoRule()]

@chat_labeler.message(command="самобан")
async def kick(message: Message, chat: MessagesConversation):
    await message.ctx_api.messages.remove_chat_user(message.chat_id, message.from_id)
    await message.answer(f"Участник самоустранился из {chat.chat_settings.title} по собственному желанию")

@chat_labeler.message(text="где я")
async def where_am_i(message: Message, chat: MessagesConversation):
    await message.answer(f"Вы в <<{chat.chat_settings.title}>>")

@chat_labeler.raw_event(MessageTypingState)
async def typing_state(event: MessageTypingState):
    user: UsersUser = (await event.ctx_api.users.get(event.user_id))[0]
    await event.ctx_api.messages.send(peer_id=event.user_id, message=f"Чё пишим?, {user.first_name} {user.last_name}", random_id=0)