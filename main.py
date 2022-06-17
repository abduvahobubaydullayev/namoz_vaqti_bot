from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import requests
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)
from namoz import TOKEN, namoz, malNam

btn_data = 'salom'
STATE_REGION = 1
STATE_CALENDAR = 2
btn_today, btn_tomorrow, btn_week, btn_region, btn_duo, btn_vaqt = (
    '⏳ Bugun', '⏳ Erta', '📆 Bir haftalik', '🇸🇱  Mintaqa', '🤲 Duo', '🕋 Vaqt')

rest = []
date_time = ''
data_week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
date_day = ''
buttons = ReplyKeyboardMarkup([
    [btn_today, btn_tomorrow], [btn_week, btn_region], [btn_duo, btn_vaqt],
], resize_keyboard=True)


def start(update, context):
    user = update.message.from_user

    buttons = [
        [
            InlineKeyboardButton('Toshkent', callback_data='Tashkent'),
            InlineKeyboardButton('Andijon', callback_data='Andijan'),
            InlineKeyboardButton('Namangan', callback_data='Namangan')
        ],
        [
            InlineKeyboardButton('Samarqand', callback_data='Samarkand'),
            InlineKeyboardButton('Farg`ona', callback_data='Kokand'),
            InlineKeyboardButton('Sirdaryo', callback_data='Gulistan')
        ],
        [
            InlineKeyboardButton('Surxondaryo', callback_data='Termez'),
            InlineKeyboardButton('Qashqadaryo', callback_data='Qarshi'),
            InlineKeyboardButton('Xorazm', callback_data='Khiva')
        ],
        [
            InlineKeyboardButton('Jizzax', callback_data='Jizzakh'),
            InlineKeyboardButton('Navoiy', callback_data='Navoi'),
            InlineKeyboardButton('Buxoro', callback_data='Bukhara')
        ],
        [
            InlineKeyboardButton('Qoraqalpog`iston', callback_data='Nukus'),
        ]
    ]
    update.message.reply_html(
        f'Assalomu aleykum <b>{user["first_name"]}!</b>\n \n Namoz vaqtlari botiga hush kelibsiz!!\n '
        f'\n Sizga qaysi mintaqa bo`yicha '
        'ma`lumot beray!', reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION


def inline_callback(update, context):
    global btn_data
    try:
        query = update.callback_query
        btn_data = query.data
        query.message.delete()
        query.message.reply_html(text=f'<b>{query.data}</b>dagi namoz vaqti!!! \n Quyidagilardan birini tanlang!',
                                 reply_markup=buttons)
        return STATE_CALENDAR
    except Exception as e:
        print('error : ', str(e))
    # print(query.data)


def calendar_today(update, context):
    url = f'https://api.pray.zone/v2/times/today.json?city={btn_data}&school=1'

    query = update.callback_query

    res = requests.get(url)

    r = res.json()
    # print(r)

    r_time = r['results']['datetime'][0]['date']['gregorian']
    rest0 = namoz(btn_data)
    c = 0
    for i in range(7):
        if r_time == rest0[i][7]:
            c = i

    update.message.reply_html(f'<b>{rest0[c][7]}y.milodiy. {rest0[c][8]}y.hijriy\n {data_week[c]}. \n'
                              f'{btn_data} vaqti bilan.</b>\n\n'
                              f'<b>{rest0[c][0]}</b>  Tong     Saharlik tugashi  \n  \n'
                              f'<b>{rest0[c][1]}</b>  Bomdod                     \n  \n'
                              f'<b>{rest0[c][2]}</b> Quyosh                      \n  \n'
                              f'<b>{rest0[c][3]}</b>  Peshin                     \n  \n'
                              f'<b>{rest0[c][4]}</b>  Asr                        \n  \n'
                              f'<b>{rest0[c][5]}</b>  Shom    Iftorlik vaqti     \n  \n'
                              f'<b>{rest0[c][6]}</b>  Xufton                     \n  \n'
                              )


def calendar_tomorrow(update, context):
    url = f'https://api.pray.zone/v2/times/today.json?city={btn_data}&school=2'
    query = update.callback_query

    res = requests.get(url)
    rest0 = namoz(btn_data)
    r = res.json()
    # print(r)
    r_time = r['results']['datetime'][0]['date']['gregorian']
    c = 0
    for i in range(7):
        if r_time == rest0[i][7]:
            c = i + 1

    update.message.reply_html(f'<b>{rest0[c][7]}y.milodiy. {rest0[c][8]}y.hijriy  \n{data_week[c]}. \n'
                              f'{btn_data} vaqti bilan.</b>\n\n'
                              f'<b>{rest0[c][0]}</b>  Tong     Saharlik tugashi  \n  \n'
                              f'<b>{rest0[c][1]}</b>  Bomdod                     \n  \n'
                              f'<b>{rest0[c][2]}</b> Quyosh                      \n  \n'
                              f'<b>{rest0[c][3]}</b>  Peshin                     \n  \n'
                              f'<b>{rest0[c][4]}</b>  Asr                        \n  \n'
                              f'<b>{rest0[c][5]}</b>  Shom    Iftorlik vaqti     \n  \n'
                              f'<b>{rest0[c][6]}</b>  Xufton                     \n  \n'
                              )


def calendar_week(update, context):
    rest0 = namoz(btn_data)
    for i in range(7):
        update.message.reply_html(f'<b>{rest0[i][7]}y.milodiy. {rest0[i][8]}y.hijriy  \n{data_week[i]}. \n'
                                  f'{btn_data} vaqti bilan.</b>\n\n'
                                  f'<b>{rest0[i][0]}</b>  Tong     Saharlik tugashi  \n  \n'
                                  f'<b>{rest0[i][1]}</b>  Bomdod                     \n  \n'
                                  f'<b>{rest0[i][2]}</b> Quyosh                      \n  \n'
                                  f'<b>{rest0[i][3]}</b>  Peshin                     \n  \n'
                                  f'<b>{rest0[i][4]}</b>  Asr                        \n  \n'
                                  f'<b>{rest0[i][5]}</b>  Shom    Iftorlik vaqti     \n  \n'
                                  f'<b>{rest0[i][6]}</b>  Xufton                     \n  \n'
                                  )


def calendar_region(update, context):
    user = update.message.from_user

    buttons = [
        [
            InlineKeyboardButton('Toshkent', callback_data='Tashkent'),
            InlineKeyboardButton('Andijon', callback_data='Andijan'),
            InlineKeyboardButton('Namangan', callback_data='Namangan')
        ],
        [
            InlineKeyboardButton('Samarqand', callback_data='Samarkand'),
            InlineKeyboardButton('Farg`ona', callback_data='Kokand'),
            InlineKeyboardButton('Sirdaryo', callback_data='Gulistan')
        ],
        [
            InlineKeyboardButton('Surxondaryo', callback_data='Termez'),
            InlineKeyboardButton('Qashqadaryo', callback_data='Qarshi'),
            InlineKeyboardButton('Xorazm', callback_data='Khiva')
        ],
        [
            InlineKeyboardButton('Jizzah', callback_data='Jizzakh'),
            InlineKeyboardButton('Navoi', callback_data='Navoi'),
            InlineKeyboardButton('Buxoro', callback_data='Bukhara')
        ],
        [
            InlineKeyboardButton('Qoraqalpog`iston', callback_data='Nukus'),
        ]
    ]
    update.message.reply_html(
        f'Assalomu aleykum <b>{user["first_name"]}!</b>\n \n Namoz vaqtlari botiga hush kelibsiz!!\n \n Sizga qaysi mintaqa bo`yicha '
        'ma`lumot beray!', reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION


def calendar_duo(update, context):
    dua = \
        [
            [
                "SANO DUOSI\nSubhanakallouhumma va bihamdika va tabarokasmuka va taa’la jadduka "
                "va la ilaha g‘oyruk.\nMa`nosi: «Allohim! Sening noming muborakdir. Shon-sharafing "
                "ulug'dir. Sendan o'zga iloh yo'qdir».\n"

            ],
            [
                "FOTIHA SURASi\nA`uzu billahi minash shaytonir rojiym. Bismillahir rohmanir rohiym. "
                "Al hamdulillahi robbil ‘alamiyn. Ar-rohmanir rohiym. \nMaliki yavmiddiyn. Iyyaka na’budu "
                "va iyyaka nasta’iyn. Ihdinas sirotol mustaqiym. Sirotollaziyna an’amta ‘alayhim g‘oyril "
                "mag‘zubi ‘alayhim valazzolliyn.\nMazmuni: Allohning dargohidan quvilgan shayton yomonligidan "
                "Allohning panohiga qochaman. Mehribon va rahmli Alloh nomi bilan (boshlayman). \n"
                "Hamd olamlar rabbi Allohgakim, (U) mehribon, rahmli va hisob-kitob kuni (Qiyomat)ning egasidir. "
                "Sengagina ibodat qilamiz va Sendangina yordam so'raymiz! \nBizni shnday to'g'ri yo'lga boshlaginki, "
                "(U) Sen in'om (hidoyat) etganlarning (payg'ambarlar, siddiq va shahidlarning) yo'lidir, \ng'azabga "
                "uchragan (Muso qavmidan itoatsizlarining) "
                "va adashgan (Iso qavmining «Allohning farzandi bor» deydigan)larning emas!\n"
            ],
            [
                "KAVSAR SURASI\nInna a’toynakal-kavsar. Fa solli lirobbika vanhar. Inna shaniaka huval abtar."
                "Mazmuni: «(Ey Muhammad,) darhaqiqat, Biz Sizga Kavsarni* berdik. Bas, Rabbingiz uchun namoz "
                "o'qing va (tuya) so'yib qurbonlik qiling! Albatta, g'animingizning o'zi (barcha yaxshiliklardan) "
                "mahrumdir».(Kavsar — jannatdagi bir ajib daryo yoki hovuzning nomi. Uning suvi asaldan totli, "
                "qor va suvdan oq. Undan ichgan kishi abadiy chanqoqlik ko'rmaydi.)"
            ],
            [
                'IXLOS SURASI\nQul huvallohu ahad. Allohus-somad. Lam yalid. Va lam yuvlad va lam yakullahu kufuvan ahad.\n'
                'Mazmuni: (Ey Muhammad,) ayting: «U — Alloh yagonadir. Alloh behojat, (lekin) hojatbarordir. U tug`magan va '
                'tug`ilmagan ham. Shuningdek, Unga teng biror zot yo`qdir»."'
            ],
            [
                'FALAQ SURASI\nQul a’uzu birobbil falaq. Min sharri ma xolaq. Va min sharri g‘osiqin iza vaqob. '
                'Va min sharrin-naffasati fil ‘uqod. Va min sharri hasidin iza hasad.\nMa`nosi: «(Ey Muhammad,) '
                'ayting: "Panoh tilab iltijo qilurman tong Parvardigoriga yaratgan narsasi yovuzligidan, '
                'tugunchaga dam uruvchi ayollar yovuzligidan hamda hasadchining hasadi yovuzligidan"».'
            ],
            [
                'AN-NOS SURASI\nQul a’uzu birrobin-nasi malikin-nasi ilahin-nasi min sharril vasvasil xonnas. '
                'Allaziy yuvasvisu fiy sudurin-nasi minal jinnati van-nas.\nMa`nosi: «(Ey Muhammad,) ayting: '
                '"Panoh tilab iltijo qilurman odamlar Parvardigoriga, odamlar Podshohiga, odamlar Ilohiga '
                'yashirin vasvasachi (shayton) yovuzligidanki, (u) odamlarning dillariga vasvasa solur. '
                '(O`zi) jinlar va odamlardandir"».'
            ],
            [
                '«ATTAHIYYAT» DUOSI\nAttahiyyatu lillahi vas-solavatu vattoyyibat. Assalamu ‘alayka '
                'ayyuhan-nabiyyu va rohmatullohi va barokatuh. Assalamu ‘alayna va ‘ala ibadillahis-solihiyn. '
                'Ashhadu alla ilaha illallohu va ashhadu anna Muhammadan ‘abduhu va rosuluh.\nMazmuni: '
                'Mol, badan, til bilan ado etiladigan butun ibodatlar Alloh uchundir. Ey Nabiy! Allohning rahmati '
                'va barakoti Sizga bo`lsin. Sizga va solih qullarga Allohning salomi bo`lsin. Iqrormanki, '
                'Allohdan o`zga iloh yo`q. Va yana iqrormanki, Muhammad, alayhissalom, Allohning quli va '
                'elchisidirlar.'
            ],
            [
                'SALOVOT\nAllohumma solli ‘ala Muhammadiv-va ‘ala ali Muhammad. Kama sollayta ‘ala Ibrohima '
                'va ‘ala ali Ibrohim. Innaka hamidum-majid. Allohumma barik ‘ala Muhammadiv-va ‘ala ali Muhammad. '
                'Kama barokta ‘ala Ibrohima va ‘ala ali Ibrohim. Innaka hamidum-majid.\nMazmuni: Allohim, Ibrohim '
                'va uning oilasiga rahmat etganing kabi, Muhammad va ul zotning oilasiga rahmat ayla, Sen hamdu '
                'maqtovga loyiq va buyuk Zotsan.Allohim, Ibrohim va uning oilasiga barakotingni ehson etganing '
                'kabi Muhammad va ul zotning oilasi ustiga ham barakotingni ehson ayla. Sen hamdu maqtovga loyiq '
                'va buyuk Zotsan'
            ],
            [
                'DUO\nRobbana atina fid-dunya hasanatav-va fil axiroti hasanatav-va qina azaban-nar.\n'
                'Mazmuni: «Ey Robbimiz, bizga bu dunyoda ham, oxiratda ham yaxshilikni bergin va bizni do`zax '
                'olovi azobidan saqlagin».'
            ]
        ]

    for i in dua:
        update.message.reply_text(i[0])


def Vaqt(update, context):
    url = f'http://worldtimeapi.org/api/timezone/Asia/tashkent'
    r = requests.get(url)
    res = r.json()
    btn_day = res['datetime'][:10]
    vaq = res['datetime'][11:13] + res['datetime'][13:16]
    mal = malNam(btn_data, vaq, btn_day)
    update.message.reply_text(mal)


def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_REGION: [CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR: [
                MessageHandler(Filters.regex('^(' + btn_today + ')$'), calendar_today),
                MessageHandler(Filters.regex('^(' + btn_tomorrow + ')$'), calendar_tomorrow),
                MessageHandler(Filters.regex('^(' + btn_week + ')$'), calendar_week),
                MessageHandler(Filters.regex('^(' + btn_region + ')$'), calendar_region),
                MessageHandler(Filters.regex('^(' + btn_duo + ')$'), calendar_duo),
                MessageHandler(Filters.regex('^(' + btn_vaqt + ')$'), Vaqt),

            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


main()
