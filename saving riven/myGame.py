from gamelib import*

game = Game(800,600,"SAVE RIVEN!")
yasuo = Image("images\\ssss.jpg",game)
bk = Image("images\\yasuo2.jpg",game)
crosshair = Image("images\\crosshair.png",game)
riven = Image("images\\riven2.png",game)





crosshair.resizeTo(100,100)
riven.resizeTo(150,150)
riven.moveTo(150,150)

bk.resizeTo(800,600)
yasuo.resizeTo(150,150)
yasuo.setSpeed(6,60)
riven.setSpeed(4,30)


while not game.over:
    game.processInput()
    bk.draw()
    yasuo.move("True")
    riven.move("True")
  
    crosshair.moveTo(mouse.x, mouse.y)
    
    if yasuo.collidedWith(mouse) and mouse.LeftButton:
        game.score+=1
        x = randint(150,650)
        y = randint(150,450)
        yasuo.moveTo(x,y)
        yasuo.speed+=2
        yasuo.resizeBy(-2)

    if riven.health<10:
        game.drawText("You lose!",300,0)
        game.over=True

    if yasuo.collidedWith(riven):

        riven.health-=1
        riven.resizeBy(-2)

    if riven.collidedWith(mouse) and mouse.LeftButton:
        riven.health-=1
        
        

   
        
   
    if game.score>=50:
        game.drawText("You win!",300,0)
        game.over=True

   
   
   
    game.drawText("Health =  " + str(riven.health),500,0)
    game.displayScore()
    game.update(20)
game.wait(K_SPACE)
game.quit()
   


 
   
    


   




    


