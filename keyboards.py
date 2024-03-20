from vkbottle import Keyboard, KeyboardButtonColor, Text

k_start = (
    Keyboard(one_time=True, inline=True)
    .add(Text("Старт"), color=KeyboardButtonColor.POSITIVE)
).get_json()

k_main = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Мой профиль"), color=KeyboardButtonColor.PRIMARY, payload = {"command": "userinfo"})
    .row
    .add(Text("Ферма"), color=KeyboardButtonColor.POSITIVE, payload = {"command": "farminfo"})
    .add(Text("Склад"),color=KeyboardButtonColor.SECONDARY, payload={"command":"storageinfo"})
    .row
    .add(Text("Рынок"), color=KeyboardButtonColor.NEGATIVE, payload={"command":"shopdef"})  
    ).get_json()