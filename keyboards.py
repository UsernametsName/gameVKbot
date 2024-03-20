from vkbottle import Keyboard, KeyboardButtonColor, Text

k_start = (
    Keyboard(one_time=True, inline=True)
    .add(Text("Старт🚀"), color=KeyboardButtonColor.POSITIVE)
).get_json()

k_main = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Мой профиль👤"), color=KeyboardButtonColor.PRIMARY)
    .row()
    .add(Text("Ферма🌾"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Склад📦"),color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Рынок🛒"), color=KeyboardButtonColor.NEGATIVE) 
    ).get_json()