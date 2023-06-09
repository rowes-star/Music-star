import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from YukkiMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(filters.regex("^$"))
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""**اهلين {user} !\n- اضغط الزر عشان تشوف اوامر ستاࢪ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر", callback_data=f"am"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("^الاحصائيات$") & filters.user(2089102006))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"**✧ اهلين مطوري ارحب\n- هذي احصائيات تيبثون ياعيني :\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾**")
    await m_reply_text("")


@app.on_message(filters.command("","بوت"))
def vgdg(client,message):
        message.reply_text(
            f"""✧ Welcome Baby,
ᴅᴇᴠᴇʟᴏᴘᴇʀ -› [RoWeS](t.me/RQ_X0)
ᴄʜᴀɴɴᴇʟ -› [𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍](t.me/S0URCE_STAR)""", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "تحديثات ستاࢪ 🍻", url=f"t.me/S0URCE_STAR")
                    ]
                ]
            ),
            disable_web_page_preview=True

        )




@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )


@app.on_message(filters.command("المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001854546683, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **ابشر ياعيوني ارسلت للمطور هيدخل الجروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت عشان تشوف التحديثات** -› [ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍 •](t.me/S0URCE_STAR)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "- اهلين ياحلو تحكم من الازرار اسفل"




REPLY_MESSAGE_BUTTONS = [

         [

             ("كيفية استخدام البوت"),                   

             ("اوامر ستاࢪ")




          ],

          [

             ("المطور"),

             ("السورس")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^ستاࢪ$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("**- ابشر تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب تيبثون**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("كيفية استخدام البوت"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياعيني عشان تفعل بوت ستاࢪ اتبع الخطوات الي بالاسفل**
1 • ارفعه مشرف بكل الصلاحيات 
2 • لو تبي تشوف الاوامر اكتب [ م الاوامر ] ولو تبي تشغل على طول اكتب شغل + اسم المقطع الصوتي
• مثال : شغل واتنسيت
- لو واجهت مشكله كلم مطور السورس  @RQ_X0""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "RoWeS", user_id=5613406189),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس ستاࢪ ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**
مطور السورس -› [RoWeS](t.me/RQ_X0)
قناة السورس -› [𝘁𝗲𝗽𝘁𝗵𝗼𝗻 𝘁𝗲𝗮𝗺](t.me/S0URCE_STAR)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ستاࢪ 🍻", url=f"https://t.me/S0URCE_STAR"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



REPLY_MESSAGEE = "- هلا فيك في قسم اوامر ستاࢪ"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح التشغيل بمنصات الاغاني")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث"),
             ("طريقة ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.group & command("اوامر تيبثون"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.group & command(""))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.group & command("شرح التشغيل بمنصات الاغاني"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓
• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify
- لو واجهت مشكلة تواصل مع مطور السورس @RQ_X0**
- [「𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍」](t.me/S0URCE_STAR)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & command("اوامر المجموعة"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n╭── • [「𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍」](t.me/S0URCE_STAR) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **شغل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **اسكت**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **الغاء كتم**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n•**استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍](t.me/S0URCE_STAR) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ستاࢪ 🍻", url=f"https://t.me/S0URCE_STAR"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.group & command("اوامر القنوات"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n╭── • [𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍](t.me/S0URCE_STAR) • ──╮\n\n ✧ **اوامر التشغيل بالقنوات**\n\n• **ق تشغيل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني بالقناة\n\n• **ق ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ق تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ق اص**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ق كملي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ق ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ق استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍](t.me/S0URCE_STAR) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ستاࢪ 🍻", url=f"https://t.me/S0URCE_STAR"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & command("طريقة البحث"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلين فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓
[ بحث + اسم المطلوب ..]
مثال -› بحث بحبك وحشتني
- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ستاࢪ 🍻", url=f"https://t.me/S0URCE_STAR"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & command("حفظ التشغيل"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ **اهلين فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( **حفظ التشغيل** )\n\n- عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -› ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق عشان تفهم اكثر ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ستاࢪ 🍻", url=f"https://t.me/S0URCE_STAR"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & command("طريقة ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ستاࢪ 🍻", url=f"https://t.me/S0URCE_STAR"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/R_U_0BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
            )
