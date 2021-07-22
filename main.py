# Import the pygame library and initialize the pygame (engine).
import pygame
from paddle import Paddle
from ball import Ball

def main():
    pygame.init()
    pygame.mixer.init()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    NEON_GREEN = (10, 242, 41)

    # Open a new window for our game
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PYGAME PONG")
    sound = pygame.mixer.Sound("sound.wav")
    soundMissedShot = pygame.mixer.Sound("missedshot.wav")

    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 195


    #Create a variable that is a list that contains our sprites.
    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # Variable to exit game
    carryOn = True

    # The clock controlling the screen updates
    clock = pygame.time.Clock()

    # Initialize player scores
    scoreA = 0
    scoreB = 0

    gameOn = True

    # |-------------MAIN GAME LOOP--------------------|
    while carryOn:
        # ------MAIN EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()
        #PADDLE A MOVES!
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        # PADDLE B MOVES!
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        if keys[pygame.K_r] and not gameOn:
            main()

        if gameOn:

            # Game Logic Goes Here
            all_sprites_list.update()

            #Check if ball is touching any of the 4 walls:
            if ball.rect.x >= 690:
                soundMissedShot.play()
                scoreA += 1
                ball.rect.x = 350

                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                soundMissedShot.play()
                scoreB += 1
                ball.rect.x = 350
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y >= 490:
                sound.play()
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y <= 0:
                sound.play()
                ball.velocity[1] = -ball.velocity[1]



            #Detect ball collision with our paddles
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                sound.play()
                ball.bounce()

            # ---Drawing on the screen goes here
            screen.fill(BLACK)
            pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
            all_sprites_list.draw(screen)

            # Display Score
            font = pygame.font.SysFont("Showcard Gothic", 74)
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250, 10))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (420, 10))
            #Check for game over with a Score of x
            if scoreA == 3 or scoreB == 3:
                gameOn = False
                screen.fill(BLACK)
                pygame.display.flip()
                fontGameOver = pygame.font.SysFont("Showcard Gothic", 25)

                if scoreA == 3:
                    textGameOver = fontGameOver.render("Player A Wins!" + "  Press R To Play Again!", 1, WHITE)
                    textRect = textGameOver.get_rect()
                    textRect.center = screen.get_rect().center
                    screen.blit(textGameOver, textRect)
                if scoreB == 3:
                    textGameOver = fontGameOver.render("Player B Wins!" + "  Press R To Play Again!", 1, WHITE)
                    textRect = textGameOver.get_rect()
                    textRect.center = screen.get_rect().center
                    screen.blit(textGameOver, textRect)


                pygame.display.flip()
                pygame.time.delay(2000)


        # ---Update the screen with what we drew above
        pygame.display.flip()


        #  ---Frames per second (FPS) using our clock
        clock.tick(60)


    # Code that runs when the user exits the game
    pygame.quit()


if __name__ == '__main__': main()