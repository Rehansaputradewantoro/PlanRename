from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**PENGGUNA GRATIS**
	Pemakaian  Batas Unggahan 2GB
	Harga 0
	
	**VIP 1 ** 
	Pemakaian  Batas Unggahan 30GB
	Harga Rp 30.000  🇮🇩/🌎 2.14$  per Month
	
	**VIP 2 **
	Pemakaian Batas Unggahan 65GB
	Harga Rp 55.000  🇮🇩/🌎 3.93$  per Month
	
	Pembayaran bisa melalui Dana Atau Qris ```089652345702```
	
	Tolong Setelah Melakukan Pembayaran Harap Kirim Bukti Transfer Tersebut. 
        Pembayaran melalui Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Revans505")], 
        			[InlineKeyboardButton("Paypal 🌎",url = "https://t.me/Revans505"),
        			InlineKeyboardButton("Qris ",url = "https://t.me/Revas505")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**PENGGUNA GRATIS**
	Pemakaian  Batas Unggahan 2GB
	Harga 0
	
	**VIP 1 ** 
	Pemakaian  Batas Unggahan 40GB
	Harga Rp 30.000  🇮🇩/🌎 2.14$  per Month
	
	**VIP 2 **
	Pemakaian Batas Unggahan 65GB
	Harga Rp 55.000  🇮🇩/🌎 3.93$  per Month
	
	Pembayaran bisa melalui Dana Atau Qris ```089652345702```
	
	Tolong Setelah Melakukan Pembayaran Harap Kirim Bukti Transfer Tersebut. 
        Pembayaran melalui Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Revans505")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Revans505"),
        			InlineKeyboardButton("Qris",url = "https://t.me/Revans505")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
