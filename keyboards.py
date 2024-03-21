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

k_profile = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Назад ↩️", payload={"btn_profile":"exit"}), color=KeyboardButtonColor.SECONDARY)
)

k_Farm = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Собрать всё 🥕",payload={"btn_farm":"collect_all"}), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Назад ↩️", payload={"btn_farm":"exit"}), color=KeyboardButtonColor.SECONDARY)
)

k_Storage = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Назад ↩️", payload={"btn_storage":"exit"}), color=KeyboardButtonColor.SECONDARY)
)
k_Market = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Купить курицу\n🐤300", payload={"btn_market":"buy_chicken"}), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Купить корову\n🐄1000", payload={"btn_market":"buy_cow"}), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Продать всё 💰", payload={"btn_market":"sell_all"}), color=KeyboardButtonColor.PRIMARY)
    .row()
    .add(Text("Назад ↩️", payload={"btn_market":"exit"}), color=KeyboardButtonColor.SECONDARY)

)
