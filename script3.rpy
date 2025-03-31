label xx:
scene bg 2
show kail 10:
    zoom 0.35
    xalign 0.9
    yalign 1.2
show edmond 2:
    zoom 0.3
    xalign 0.7
    yalign 1.25
show bekki 6:
    zoom 0.3
    xalign 0.4
    yalign 1.25
show mori 9:
    zoom 0.3
    xalign 0.2
    yalign 1.52
m "О, ну всё, пошли тогда."
hide mori 8 with moveoutleft
hide kail 10 with moveoutleft
scene bg 6
show kail 10 with moveinright:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 8 with moveinright:
    zoom 0.3
    xalign 0.4
    yalign 1.52
show kail 8:
    zoom 0.35
    xalign 0.6
    yalign 1.2
k "Чо мы ищем то?"
show kail 10:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.4
    yalign 1.52
m "Что-нибудь интересненькое."
show mori 8:
    zoom 0.3
    xalign 0.4
    yalign 1.52
show kail 6:
    zoom 0.35
    xalign 0.6
    yalign 1.2
k "И зачем тебе это интересненькое?"
show kail 7:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.4
    yalign 1.52
m "В смысле зачем?! Это же прикольно!"
show mori 8:
    zoom 0.3
    xalign 0.4
    yalign 1.52
show kail 6:
    zoom 0.35
    xalign 0.6
    yalign 1.2
k "Нет."
show kail 7:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.4
    yalign 1.52
m "Ну ты.. Как всегда."
m "Ты правда не помнишь, что тебе снилось?"
show mori 8:
    zoom 0.3
    xalign 0.4
    yalign 1.52
show kail 6:
    zoom 0.35
    xalign 0.6
    yalign 1.2
k "Да. Постоянно так."
show kail 7:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.4
    yalign 1.52
m "А мне заброшка снилась. И на меня там тварь кинулась."
show mori 8:
    zoom 0.3
    xalign 0.4
    yalign 1.52
show kail 6:
    zoom 0.35
    xalign 0.6
    yalign 1.2
k "Говорила уже."
show kail 7:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.4
    yalign 1.52
m "Ещё раз послушаете! Что ты сегодня такой занудный??!"
show mori 6:
    zoom 0.3
    xalign 0.4
    yalign 1.52
show kail 6:
    zoom 0.35
    xalign 0.6
    yalign 1.2
k "Не выспался просто."
show kail 7:
    zoom 0.35
    xalign 0.6
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.4
    yalign 1.52
m "Ой, ладно. Продолжим!"
m "Мне снилась заброшенная комната, прям как эта.."
m "Ой.. Бэкки! Эдмонд! Идите сюда!!"
show mori 8:
    zoom 0.3
    xalign 0.4
    yalign 1.52
menu:
    "Ты что-то нашла?":
        jump vmeste
return

label konec:

play music napr
scene bg 1
show mori 5:
    zoom 0.3
    xalign 0.2
    yalign 1.52
show kail 1:
    zoom 0.35
    xalign 0.4
    yalign 1.2
show bekki 16:
    zoom 0.3
    xalign 0.6
    yalign 1.25
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show mori 1:
    zoom 0.3
    xalign 0.2
    yalign 1.52
m "Эдмонд, иди, ты же знаешь, что нужно делать.."
show mori 5:
    zoom 0.3
    xalign 0.2
    yalign 1.52
show edmond 18:
    zoom 0.3
    xalign 0.9
    yalign 1.25
e "Ещё не знаю.."
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show bekki 18:
    zoom 0.3
    xalign 0.6
    yalign 1.25
b "Я боюсь туда идти, там демон.."
show bekki 16:
    zoom 0.3
    xalign 0.6
    yalign 1.25
show kail 6:
    zoom 0.35
    xalign 0.4
    yalign 1.2
k "Да нет там никого."
show kail 1:
    zoom 0.35
    xalign 0.4
    yalign 1.2
hide kail 1 with moveoutright
show mori 1:
    zoom 0.3
    xalign 0.2
    yalign 1.52
m "Кайл! Там же демон!!"
m "И что нам делать?"
show mori 5:
    zoom 0.3
    xalign 0.2
    yalign 1.52 
show edmond 18:
    zoom 0.3
    xalign 0.9
    yalign 1.25
e "Пока что неизвестно."
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show mori 1:
    zoom 0.3
    xalign 0.2
    yalign 1.52
m "Бэк, [q], идём искать Кайла!"
show mori 6:
    zoom 0.3
    xalign 0.2
    yalign 1.52 
hide mori 6 with moveoutright
scene bg 7
show mori 6:
    zoom 0.3
    xalign 0.6
    yalign 1.52
show bekki 16:
    zoom 0.3
    xalign 0.3
    yalign 1.25
show mori 1:
    zoom 0.3
    xalign 0.6
    yalign 1.52
m "И где его искать?"
show mori 6:
    zoom 0.3
    xalign 0.6
    yalign 1.52
q "Где-то тут."
show mori 1:
    zoom 0.3
    xalign 0.6
    yalign 1.52
m "Спасибо, капитан-очевидность."
m "Кайл!!! Ты где!!?? Иди к нам!!!"
show mori 6:
    zoom 0.3
    xalign 0.6
    yalign 1.52
show kail 2 with moveinright:
    zoom 0.35
    xalign 0.9
    yalign 1.2
show kail 3:
    zoom 0.35
    xalign 0.9
    yalign 1.2
k "Ты чо орёшь?"
show kail 2:
    zoom 0.35
    xalign 0.9
    yalign 1.2
show mori 9:
    zoom 0.3
    xalign 0.6
    yalign 1.52
m "Кайл! Ты живой!!"
show mori 6:
    zoom 0.3
    xalign 0.6
    yalign 1.52
show kail 8:
    zoom 0.35
    xalign 0.9
    yalign 1.2
k "Конечно. Я умирать и не собирался."
show kail 2:
    zoom 0.35
    xalign 0.9
    yalign 1.2
show mori 1:
    zoom 0.3
    xalign 0.6
    yalign 1.52
m "Пошлите к Эдмонду. Он придумает, что делать."
show mori 6:
    zoom 0.3
    xalign 0.6
    yalign 1.52
show kail 6:
    zoom 0.35
    xalign 0.9
    yalign 1.2
k "Вы понимаете, что убегаете от ничего? Дурдом какой-то.."
show kail 2:
    zoom 0.35
    xalign 0.9
    yalign 1.2
#тут страшный звук, у демона голосок прорезался
play sound strasna
show kail 1:
    zoom 0.35
    xalign 0.9
    yalign 1.2
show mori 4:
    zoom 0.3
    xalign 0.6
    yalign 1.52
show bekki 17:
    zoom 0.3
    xalign 0.3
    yalign 1.25
show bekki 18:
    zoom 0.3
    xalign 0.3
    yalign 1.25
b "Идём к Эдмонду!!"
show bekki 17:
    zoom 0.3
    xalign 0.3
    yalign 1.25
scene bg 1
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show mori 4 with moveinright:
    zoom 0.3
    xalign 0.2
    yalign 1.52 
show kail 1 with moveinright:
    zoom 0.35
    xalign 0.4
    yalign 1.2
show bekki 17 with moveinright:
    zoom 0.3
    xalign 0.6
    yalign 1.25
show mori 1:
    zoom 0.3
    xalign 0.2
    yalign 1.52 
m "Оно убьёт нас!!!"
m "От ничего убегаем, да, Кайл??!"
show mori 5:
    zoom 0.3
    xalign 0.2
    yalign 1.52 
show kail 6:
    zoom 0.35
    xalign 0.4
    yalign 1.2
k "Не истери."
show kail 2:
    zoom 0.35
    xalign 0.4
    yalign 1.2
show edmond 18:
    zoom 0.3
    xalign 0.9
    yalign 1.25
e "Успокойтесь, я что-нибудь придумаю."
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show kail 6:
    zoom 0.35
    xalign 0.4
    yalign 1.2
k "Может у кого-нибудь уже есть идеи?"
show kail 2:
    zoom 0.35
    xalign 0.4
    yalign 1.2
if karma < 0: # and karma < = 3:
    menu:
        "У меня есть идея.":
            jump koncovka1
elif karma > 0: # and karma > = -3:
    menu:
        "Наверно нет?":
            jump koncovka2

return