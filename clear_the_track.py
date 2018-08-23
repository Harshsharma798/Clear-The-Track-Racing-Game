import pygame
import time
import random
pygame.init()

width,height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Clear the track')

def crashed(score):
    font_set = pygame.font.Font('freesansbold.ttf',80)
    text_1 = font_set.render('You crashed',True,(0,0,0))
    text_box_1 = text_1.get_rect()
    text_box_1.center = (width/2,height/3)
    text_2 = font_set.render(('Score = '+str(score)), True, (0, 0, 0))
    text_box_2 = text_2.get_rect()
    text_box_2.center = (width / 2, 2*height /3)
    screen.blit(text_1,text_box_1)
    screen.blit(text_2,text_box_2)
    pygame.display.update()
    time.sleep(1)
    main_game()

def main_game():
    w_change = 0
    clock = pygame.time.Clock()
    char_width, char_height = 60,80
    pos_x,pos_y = (width-char_width)/2 , height-char_height
    character = pygame.transform.scale(pygame.image.load('car_char.png'),(char_width,char_height))
    obs_width,obs_height = 100,200
    obs_pos_x , obs_pos_y = random.randrange(0,width-obs_width) , -obs_height
    speed = 7
    score = 0
    leave = False
    while not leave:
        rect = [obs_pos_x,obs_pos_y,obs_width,obs_height]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    w_change = -10
                elif event.key == pygame.K_RIGHT:
                    w_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    w_change = 0

        pos_x += w_change
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(255,0,0),rect,10)
        obs_pos_y += speed
        screen.blit(character,(pos_x,pos_y))
        font_score = pygame.font.Font('freesansbold.ttf', 40)
        text_score = font_score.render(str(score), False, (0, 0, 0))
        text_box_score = text_score.get_rect()
        text_box_score.center = (width *0.95, height * 0.1)
        screen.blit(text_score,text_box_score)
        if pos_x < 0 or pos_x > width-char_width:
            crashed(score)
        if obs_pos_y > height:
            obs_pos_x , obs_pos_y = random.randrange(0,width-obs_width) , -obs_height
            score += 1
            if score % 5 == 0:
                speed += 1
        if obs_pos_y+obs_height > height - char_height:
            if obs_pos_x > pos_x and obs_pos_x < pos_x+char_width:
                crashed(score)
            elif (obs_pos_x+obs_width) > pos_x and obs_pos_x < pos_x+char_width:
                crashed(score)
            elif obs_pos_x < pos_x and (obs_pos_x+obs_width) > pos_x:
                crashed(score)
        pygame.display.update()
        clock.tick(100)

main_game()
pygame.quit()
quit()