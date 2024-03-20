from vkbottle import Keyboard, KeyboardButtonColor, Text

k_start = (
    Keyboard(one_time=True, inline=True)
    .add(Text("Старт🚀"), color=KeyboardButtonColor.POSITIVE)
).get_json()

k_main = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Мой профиль👤",payload = {"btn_menu": "profile"}), color=KeyboardButtonColor.PRIMARY)
    .row()
    .add(Text("Ферма🌾",payload = {"btn_menu": "farm"}), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Склад📦",payload = {"btn_menu": "storage"}),color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Рынок🛒", payload = {"btn_menu": "shop"}),color=KeyboardButtonColor.SECONDARY) 
    ).get_json()