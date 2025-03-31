
# Вы можете расположить сценарий своей игры в этом файле.
# музыка и звуки
# Определение персонажей игры.


define e = Character(u'Эдмонд', color="#1900AB")
define m = Character(u'Мори', color="#C21000")
define k = Character(u'Кайл', color="#468F43")
define b = Character(u'Бэкки', color="#C29E75")
define q = Character("[name]", color="#FFD73A")
define audio.fon = "audio/fon.mp3"
define audio.napr = "audio/napr.mp3"
define audio.screamer = "audio/screamer.mp3"
define audio.strasna = "audio/strasna.mp3"
define audio.krik = "audio/krik.mp3"
default karma = 0
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
# define x
# Игра начинается здесь:
label start:
    jump prog
return
label prog:
    play music fon
    scene bg 1
    $ q = renpy.input("как вас зовут?")
    "приятной игры, [q]"
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show kail 10:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show edmond 4:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    e "Мы на месте."
    e "Где бэк?"
    show edmond 2:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Под кустом где-то валяется поди."
    show kail 7:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "У-у-у... А мы что? Приехали в пятизвёздочный отель?"
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show kail 8:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Естественно."
    show kail 5:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "Вау."
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show bekki 8 with moveinleft:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "А есть что-нибудь покушать?"
    show bekki 4:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    e "Нет. Если вы закончили свои переговоры, то мы можем заходить."
    scene bg 2 with fade
    show kail 7:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 7:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    show bekki 8:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "Что за дом бомжа?"
    show bekki 4:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "Скорее харомы."
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    e "Вы прекрасно понимали куда идёте.."
    hide mori 8 with moveoutright
    hide kail 7 with moveoutright
    e "Вы даже не слушали меня..Ладно. Бэк, что насчёт тебя?"
    show edmond 2:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    show bekki 8:
        zoom 0.3
        xalign 0.3
        yalign 1.25 
    b "Я хочу ходить с тобой и помогать."
    show bekki 4:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    e "Отлично, тогда идём."
    scene bg 3 with fade
    show edmond 1:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    b "Нагадала женщине на улице цыганка 'в твоём ребенке смерть твоя будет' за то, что та не дала милостыню. "
    b "Женщина не поверила ей и забыла про этот случай. Пришло время родов и родила она маленького болезненного сына. "
    b "Как только мать выписали с ребенком из роддома, она заметила одну странную вещь - ребенок не улыбался, не кричал и вообще не издавал звуки. Она ухаживала за ним и пыталась кормить, но получалось только через силу."
    b "Через время он стал ещё более странным. Издевался над животными, никогда не разговаривал и научился только страшно хрипеть, и пугал мать этим по ночам."
    b "Однажды на утро она не обнаружила сына в кровати, придя на кухню увидела полный разгром и сына с мертвым псом, которого он ел. С этого момента все стало невыносимым."
    b "Ребенок не прекращал хрипеть и делал это без остановки. Хватал мать и сильно кусал ее. "
    b "Так продолжалось несколько месяцев и однажды мать не выдержала, взяла сына, пришла с ним на заброшку, зарезала его, а труп спрятала под обломками. И больше никто его не видел. А дух сына стал обитать на заброшке, ходить по ней и ужасно хрипеть..."
    show bekki 5:
        zoom 0.3 
        xalign 0.4
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    e "Ты помогать собираешься?"  
    show edmond 1:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show mori 9 with moveinleft:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    m "О Бэкки! Хочешь с нами побегать!?"
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    b "Да!"
    show bekki 5:
        zoom 0.3 
        xalign 0.4
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    m "Ура! Тогда беги!!"
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    hide bekki 5 with moveoutleft
    hide mori 8 with moveoutleft
    scene bg 2 with fade
    show mori 8 with moveinright:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show bekki 5 with moveinright:
        zoom 0.3
        xalign 0.1
        yalign 1.25
    window hide

    scene poster 2 with fade

    pause
    scene bg 4
    show mori 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 18:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "Ай-ай-ай..Как больно.."
    show bekki 17:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Нифига ты взломщик."
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show edmond 14 with moveinleft:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show edmond 18:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    e "Не думал, что ты всё таки поможешь. Но спасибо, что хоть что-то ты сделал."
    show edmond 14:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "О Эдмонд, ты прям как дед ходун."
    show bekki 19:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Уф, Эмонд, хочешь тут жить?"
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 7 with moveinleft:
        zoom 0.35
        xalign 0.1
        yalign 1.2
    show kail 8:
        zoom 0.35
        xalign 0.1
        yalign 1.2
    k "Прикольно. Вы в расхитителей гробниц играете?"
    show kail 5:
        zoom 0.35
        xalign 0.1
        yalign 1.2
    show edmond 4:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    e "Оставьте свои шутки при себе."
    show edmond 14:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "А мне понравились."
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    e "Всё равно. На сегодня мы можем закончить."
    show edmond 14:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Ура домой!"
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    scene bg 5 with fade
    show bekki 4:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 2:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Ну Эдмонд вообще. Ходец по заброшкам."
    show bekki 4:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Тварина глупая, как так можно."
    show mori 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Выгоните его на заброшку."
    show kail 2:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Щас выгоним."
    show mori 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Вы, конечно, здесь шутите, но там реально могут быть демоны."
    show bekki 7:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Не придуривайся. Или ты как Эдмонд?"
    show kail 2:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 10:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "АААААА демоны!"
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    menu:
        "Мне кажется, что на этой заброшке может быть что-то подобное.":
            $ karma = karma + 1
            jump da
        "Что за ересь? Демонов не существует.":
            $ karma = karma - 1
            jump net

    return
    
    label da:

    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Серьёзно? Я думал, что хоть ты не будешь верить в этот бред."
    show kail 2:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show bekki 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Да, я тоже считаю, что там есть демоны всякие."
    show bekki 4:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Теперь демоны придут за нами."
    show mori 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Можно пойти разузнать у Эдмонда."
    show bekki 4:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Пойдёмте конечно."
    show mori 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    scene bg 13 with fade
    show edmond 1:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    show mori 8 with moveinleft:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show bekki 5 with moveinleft:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "Привет Эдмонд.Расскажи нам про демонов! Мы боимся, что они нас убьют!"
    show bekki 5:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    e "Демоны не причинят вам вреда, если не тревожить их."
    show edmond 1:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "Давайте вызовем демона?!"
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "О, давайте!"
    show bekki 5:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    e "Вы разве не боитесь, что они вас убьют?"
    show edmond 1:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "Нужно смотреть страху в глаза."
    show bekki 5:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "Да, Эдмонд, давай вызывать по твоей книжонке."
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    e "Нет.Это слишком опасно."
    show edmond 1:
        zoom 0.3
        xalign 0.9
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "Фу, Эдмонд, какая ты бяка, зануда."
    show mori 8:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    b "Эдмонд,ну ты как всегда."
    show bekki 5:
        zoom 0.3
        xalign 0.3
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    m "Пошли от него..."
    show mori 7:
        zoom 0.3
        xalign 0.6
        yalign 1.25
    scene bg 12 with fade
    show bekki 5 with moveinleft:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 7 with moveinleft:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show bekki 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "О, уже дрыхнет, тварь ненасытная."
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1 with moveinleft:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Сейчас демона будем вызывать."
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Ура, я нашла книжку!!"
    show bekki 8:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "[q],ты точно с нами?"
    menu:
        "Да.":
            $ karma = + 1
            jump om
        "Я думаю,что это плохая идея..":
            $ karma = - 1
            jump nom

    return

    label net:
    
    scene bg 5
    show bekki 4:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 8:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Вот. Ещё одна светлая голова! Я доволен."
    show kail 4:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Да вы ваще."
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Можете не верить,но потом.. Демоны придут за вами!"
    show bekki 4:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "За тобой бы кто пришёл. Иди со своими демонами к Эдмонду."
    show kail 7:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show bekki 15:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "И пойду!"
    show bekki 15:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    hide bekki 15 with moveoutright
    show kail 8:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Одним идиотом меньше. Мори, родная, ты, надеюсь, с нами?"
    show kail 10:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "И чем я тут должна с вами заниматься?"
    show mori 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Говоришь так, будто скучнее нас никого нет."
    show kail 7:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    q "Можем пойти посмотреть, как там Бэк и Эдмонд."
    show mori 9:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    m "Давайте!"
    show mori 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    k "Да что вам неймётся..?"
    show kail 7:
        zoom 0.35
        xalign 0.8
        yalign 1.2
    scene bg 10
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Бэк, если не вызывать, то он не навредит тебе."
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 7 with moveinleft:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 8 with moveinleft:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "А мы вызывать демона хотим!"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Нет. Это опасно."
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Пф. Будто что-то произойдёт. Хватит верить во всякий бред. Давайте вызовем."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Кайлик!! Ты.. Ты.. Ты просто друг!! С большой буквы!!"
    show kail 10:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Бэки, Эдмонд, вы с нами же?"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Да!"
    show bekki 6:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "[q], а ты?"
    menu:
        "Я тоже.":
            $ karma = + 1
            jump cho
        "Может займёмся чем нибудь другим?.":
            $ karma = - 1
            jump omg

    return

    label omg:

    scene bg 10
    show kail 10:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 6:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Ты серьёзно!??"
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show kail 8:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Да ладно тебе, [q], не слушай Мори. Если не хочешь вызывать, то можешь рядом постоять. Но я тебе гарантирую, ничего не произойдёт, демонов же не существует."
    show kail 10:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    q "Тогда я посмотрю."
    show edmond 13:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Я против этой затеи. Прекращайте, это не шутки."
    show edmond 14:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Да мне всё равно."
    show mori 17:
        zoom 0.29
        xalign 0.8
        yalign 1.52
    m "Audi me, Domine inferni, misericordiam ostende et votum meum imple!"
    window hide

    scene poster 3 with fade

    pause
    scene bg 10
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Ну и? Ничего не произошло."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Вот же... Не свезло.."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Вы в своём уме!? А если бы ритуал прошёл успешно?!"
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Я бы исполнила своё желание."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Никто бы не пришёл. Демонов не существует."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Существуют! И вообще-то демон пришёл! Теперь он нас всех убьёт!!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Не, он, судя по всему, не пришёл."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Пришёл!! Вы скоро сами убедитесь!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Думаю, Мори и Кайл правы. Сейчас мы все должны отдохнуть,завтра,по крайней мере меня, ждёт много дел, поэтому, я считаю,что нужно ложиться спать."
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Точно! Завтра нас ждёт заброшка!"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Опять эта помойка?"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "А тебе, что? Не нравится? Если хочешь, то можешь не идти. Никто не заставляет."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    hide mori 8 with moveoutleft
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Я тоже с Эдмондом пойду."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Так себе у вас развлечения."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Ты просто не понимаешь."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Да, конечно"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    scene bg 9 with fade
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 8 with moveinleft:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Всем доброе утро."
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Угу..Самая первая ушла спать и самая последняя проснулась."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да блин, я всю ночь мучилась с кошмарами."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Тебе тоже снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да! Я же говорю, всю ночь мучилась."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show bekki 8:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    b "Мне тоже снились кошмары."
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Хм.. [q], Кайл, вам снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Мне не снятся сны."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    menu:
        "Мне тоже снились кошмары.":
            jump chego
        "Я не помню, что мне снилось.":
            jump ee

    return

    label cho:

    scene bg 10
    show kail 10:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 6:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Ура! Давайте вызывать!"
    show edmond 13:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Я против этой затеи. Прекращайте, это не шутки."
    show edmond 14:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Да мне всё равно."
    show mori 17:
        zoom 0.29
        xalign 0.8
        yalign 1.52
    m "Audi me, Domine inferni, misericordiam ostende et votum meum imple!"
    window hide

    scene poster 3 with fade

    pause
    scene bg 10
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Ну и? Ничего не произошло."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Вот же... Не свезло.."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Вы в своём уме!? А если бы ритуал прошёл успешно?!"
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Я бы исполнила своё желание."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Никто бы не пришёл. Демонов не существует."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Существуют! И вообще-то демон пришёл! Теперь он нас всех убьёт!!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Не, он, судя по всему, не пришёл."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Пришёл!! Вы скоро сами убедитесь!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Думаю, Мори и Кайл правы. Сейчас мы все должны отдохнуть,завтра,по крайней мере меня, ждёт много дел, поэтому, я считаю,что нужно ложиться спать."
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Точно! Завтра нас ждёт заброшка!"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Опять эта помойка?"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "А тебе, что? Не нравится? Если хочешь, то можешь не идти. Никто не заставляет."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    hide mori 8 with moveoutleft
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Я тоже с Эдмондом пойду."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Так себе у вас развлечения."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Ты просто не понимаешь."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Да, конечно"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    scene bg 9 with fade
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 8 with moveinleft:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Всем доброе утро."
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Угу..Самая первая ушла спать и самая последняя проснулась."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да блин, я всю ночь мучилась с кошмарами."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Тебе тоже снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да! Я же говорю, всю ночь мучилась."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show bekki 8:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    b "Мне тоже снились кошмары."
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Хм.. [q], Кайл, вам снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Мне не снятся сны."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    menu:
        "Мне тоже снились кошмары.":
            jump chego
        "Я не помню, что мне снилось.":
            jump ee
    

    return

    label om:

    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Вот и умничка! Давайте вызывать!!"
    scene bg 10
    show mori 7:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Чем вы тут занимаетесь?"
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Ой.."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Доброе утро, Эдмонд."
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Вы отвечать собираетесь?"
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Демона вызываем."
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Я ведь говорил вам, что это опасно. Это не шутки."
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Давай ты с нами вызовешь? Ты же профессионал, с таким бояться нечего."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Да, Эдмонд, мы всё равно вызовем его."
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Ладно.."
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Ура!! Давайте ещё и Кайла позовём?? Будет веселее."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Да, давайте!"
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Вы тогда всё подготовьте, а я за ним!"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    hide mori 8 with moveoutleft 
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Ну, Эдмонд, говори,что делать."
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Нужно начертить пентаграмму, расставить свечи.. Обычно демонов призывают для исполнения желания. У вас есть желание?"
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 20:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Желание? Мы просто на демона посмотреть хотим."
    show bekki 5:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Вызвать демона - не в зоопарк сходить, придётся заплатить больше чем деньгами. В любом случае, я против вашей затеи."
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 7  with moveinleft:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 8  with moveinleft:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Вообще-то есть желание."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52 
    show edmond 17:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Всё равно не стоит."
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Ты серьёзно в это веришь?"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Конечно верит!!!"
    show mori 17:
        zoom 0.29
        xalign 0.8
        yalign 1.52
    m "Audi me, Domine inferni, misericordiam ostende et votum meum imple!"
    window hide

    scene poster 3 with fade

    pause
    scene bg 10
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Ну и? Ничего не произошло."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Вот же... Не свезло.."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Вы в своём уме!? А если бы ритуал прошёл успешно?!"
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Я бы исполнила своё желание."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Никто бы не пришёл. Демонов не существует."
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Существуют! И вообще-то демон пришёл! Теперь он нас всех убьёт!!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Не, он, судя по всему, не пришёл."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Пришёл!! Вы скоро сами убедитесь!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Думаю, Мори и Кайл правы. Сейчас мы все должны отдохнуть,завтра,по крайней мере меня, ждёт много дел, поэтому, я считаю,что нужно ложиться спать."
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Точно! Завтра нас ждёт заброшка!"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Опять эта помойка?"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "А тебе, что? Не нравится? Если хочешь, то можешь не идти. Никто не заставляет."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    hide mori 8 with moveoutleft
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Я тоже с Эдмондом пойду."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Так себе у вас развлечения."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Ты просто не понимаешь."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Да, конечно"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    scene bg 9 with fade
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 8 with moveinleft:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Всем доброе утро."
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Угу..Самая первая ушла спать и самая последняя проснулась."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да блин, я всю ночь мучилась с кошмарами."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Тебе тоже снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да! Я же говорю, всю ночь мучилась."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show bekki 8:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    b "Мне тоже снились кошмары."
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Хм.. [q], Кайл, вам снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Мне не снятся сны."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    menu:
        "Мне тоже снились кошмары.":
            jump chego
        "Я не помню, что мне снилось.":
            jump ee
    
    return

    label nom:

    scene bg 12
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.25
    m "Иди тогда отсюда."
    scene bg 9
    show kail 10:
        zoom 0.35
        xalign 0.5
        yalign 1.2
    show kail 8:
        zoom 0.35
        xalign 0.5
        yalign 1.2
    k "О, привет. Не сидится с этими?"
    show kail 10:
        zoom 0.35
        xalign 0.5
        yalign 1.2
    q "Они там демона вызывают."
    show kail 6:
        zoom 0.35
        xalign 0.5
        yalign 1.2
    k "Боже.. Им заняться нечем?"
    show kail 7:
        zoom 0.35
        xalign 0.5
        yalign 1.2
    q "..."
    k "..."
    show kail 6:
        zoom 0.35
        xalign 0.5
        yalign 1.2
    k "Пошли посмотрим на этих дебилов."
    scene bg 10
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 4:
        zoom 0.3
        xalign 0.7
        yalign 1.52
    show kail 7 with moveinleft:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Заняться нечем?"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.7
        yalign 1.52
    m "Привет, а мы тут демона вызываем."
    show mori 4:
        zoom 0.3
        xalign 0.7
        yalign 1.52
    show edmond 13:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Я против этой затеи. Прекращайте, это не шутки."
    show edmond 14:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    m "Да мне всё равно."
    show mori 17:
        zoom 0.29
        xalign 0.7
        yalign 1.52
    m "Audi me, Domine inferni, misericordiam ostende et votum meum imple!"
    window hide

    scene poster 3 with fade

    pause
    scene bg 10
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 1:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Ну и? Ничего не произошло."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Вот же... Не свезло.."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show edmond 6:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Вы в своём уме!? А если бы ритуал прошёл успешно?!"
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Я бы исполнила своё желание."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Никто бы не пришёл. Демонов не существует."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Существуют! И вообще-то демон пришёл! Теперь он нас всех убьёт!!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Не, он, судя по всему, не пришёл."
    show mori 4:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Пришёл!! Вы скоро сами убедитесь!"
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show edmond 7:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    e "Думаю, Мори и Кайл правы. Сейчас мы все должны отдохнуть,завтра,по крайней мере меня, ждёт много дел, поэтому, я считаю,что нужно ложиться спать."
    show edmond 8:
        zoom 0.3
        xalign 0.5
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "Точно! Завтра нас ждёт заброшка!"
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Опять эта помойка?"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    m "А тебе, что? Не нравится? Если хочешь, то можешь не идти. Никто не заставляет."
    show mori 8:
        zoom 0.3
        xalign 0.8
        yalign 1.52
    hide mori 8 with moveoutleft
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Я тоже с Эдмондом пойду."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Так себе у вас развлечения."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 14:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    b "Ты просто не понимаешь."
    show bekki 1:
        zoom 0.3
        xalign 0.2
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Да, конечно"
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    #hide edmond 8 #with fade
    #hide kail 7 #with fade
    #hide bekki 1 #with fade
    #hide bg 10 
    scene bg 9 with fade
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 8 with moveinleft:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Всем доброе утро."
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Угу..Самая первая ушла спать и самая последняя проснулась."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да блин, я всю ночь мучилась с кошмарами."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Тебе тоже снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 1:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Да! Я же говорю, всю ночь мучилась."
    show mori 6:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show bekki 8:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    b "Мне тоже снились кошмары."
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 4:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    e "Хм.. [q], Кайл, вам снились кошмары?"
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show kail 6:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "Мне не снятся сны."
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    
    menu:
        "Мне тоже снились кошмары.":
            jump chego
        "Я не помню, что мне снилось.":
            jump ee

    return

    label chego:

    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "О, а что вам снилось? Мне вот.. Щас расскажу!"
    menu:
        "Рассказывай.":
            jump son

    return

    label ee:

    scene bg 9 #sswith fade
    show kail 7:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show bekki 1:
        zoom 0.3
        xalign 0.4
        yalign 1.25
    show edmond 2:
        zoom 0.3
        xalign 0.7
        yalign 1.25
    show mori 8:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    show kail 8:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    k "С чего вдруг нам всем поголовно должны сниться кошмары?"
    show kail 10:
        zoom 0.35
        xalign 0.9
        yalign 1.2
    show mori 9:
        zoom 0.3
        xalign 0.2
        yalign 1.52
    m "Не знаю. Ну щас я расскажу,что мне снилось! "
    menu:
        "Рассказывай.":
            jump son
    return
return