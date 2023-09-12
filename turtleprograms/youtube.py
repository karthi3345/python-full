from turtle import*
fillcolor("red")
begin_fill()
for i in [300,200,300,200]:
    forward(i)
    circle(10,90)

end_fill()
fillcolor("white")
begin_fill()
up()
goto(130,50)
down()
for i in (30,120,120):
   left(i)
   forward(100)
end_fill()
