label koncovka1:

play music napr
scene bg 1
show kail 2:
    zoom 0.35
    xalign 0.4
    yalign 1.2
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show mori 4:
    zoom 0.3
    xalign 0.2
    yalign 1.52 
show bekki 17:
    zoom 0.3
    xalign 0.6
    yalign 1.25
q "Давайте от него убежим?"
show kail 6:
    zoom 0.35
    xalign 0.4
    yalign 1.2
k "А давайте."
show kail 2:
    zoom 0.35
    xalign 0.4
    yalign 1.2
show edmond 17:
    zoom 0.3
    xalign 0.9
    yalign 1.25
e "Ужасная идея."
show edmond 20:
    zoom 0.3
    xalign 0.9
    yalign 1.25
show kail 6:
    zoom 0.35
    xalign 0.4
    yalign 1.2
k "Если хотите, то дальше тут стойте. Если вы жить хотите, надо действовать."
show kail 2:
    zoom 0.35
    xalign 0.4
    yalign 1.2

window hide

scene poster8 with fade

pause

scene bg 14
show kail 2:
    zoom 0.35
    xalign 0.5
    yalign 1.2
show kail 8:
    zoom 0.35
    xalign 0.5
    yalign 1.2
k "Я думаю, что мы достаточно далеко убежали."
show kail 10:
    zoom 0.35
    xalign 0.5
    yalign 1.2
#страшный звук
play sound krik
window hide

scene poster 1 with fade

#if karma > 0 and karma < 10:
#    "fff"
#elif karma >=10 and karma <20:
#    "dddd"
#else:
#    "оооо"

pause

"Видимо твои решения были недостаточно хороши, но не волнуйся, всегда можно попробовать с начала!"
"Или такой конец тебя устроит?"

return