label zabroshka1:
scene bg 2
show kail 7:
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
show mori 8:
    zoom 0.3
    xalign 0.2
    yalign 1.52
show kail 3:
    zoom 0.35
    xalign 0.9
    yalign 1.2
k "И надолго мы здесь?"
show kail 7:
    zoom 0.35
    xalign 0.9
    yalign 1.2
show edmond 17:
    zoom 0.3
    xalign 0.7
    yalign 1.25
e "Точно не знаю."
show edmond 2:
    zoom 0.3
    xalign 0.7
    yalign 1.25
show mori 9:
    zoom 0.3
    xalign 0.2
    yalign 1.52
m "Кайл, пошли со мной на прогулочку?"
show mori 8:
    zoom 0.3
    xalign 0.2
    yalign 1.52
show kail 8:
    zoom 0.35
    xalign 0.9
    yalign 1.2
k "Пошли. Всяко лучше чем с этими чудиками."
k "[q], ты с нами или с Бэком и Эдмондом?"
show kail 10:
    zoom 0.35
    xalign 0.9
    yalign 1.2
menu:
    "Я с тобой и Мори.":
        jump xx 
    "Я с Бэком и Эдмондом.":
        jump xz
return