import pygame
import random
import math

WIDTH, HEIGHT = 1000, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping_Pong_2Players")
Running = True

class Game:
    def __init__(self, player_1, player_2, ball):
        self.player_1 = player_1
        self.player_2 = player_2
        self.ball = ball
        self.score_1 = 0
        self.score_2 = 0
        self.winner=None
        self.small_font = pygame.font.SysFont("impact", 30)
        self.big_font = pygame.font.SysFont("impact", 50)
        self.score_1_text = self.small_font.render(f"score_1 : {self.score_1}", True, "white")
        self.score_1_text_rect = self.score_1_text.get_rect(topleft=(10, 20))
        self.score_2_text = self.small_font.render(f"score_2 : {self.score_2}", True, "white")
        self.score_2_text_rect = self.score_2_text.get_rect(topright=(WIDTH - 10, 20))
        self.score_title_text = self.big_font.render(f"Ping Pong", True, "white")
        self.score_title_text_rect = self.score_title_text.get_rect(center=(WIDTH // 2, 40))
        self.score_winner_text = self.small_font.render(f"{self.winner}", True, "silver")
        self.score_winner_text_rect = self.score_winner_text.get_rect(center=(WIDTH // 2-40, HEIGHT//2+40))
        self.score_game_over_text = self.small_font.render(f"Game Overr! press Enter to continue ", True, "silver")
        self.score_game_over_text_rect = self.score_game_over_text.get_rect(center=(WIDTH // 2+60, HEIGHT//2-80))

    def update(self):
        self.draw()
        self.check_winner()
        self.check_collision()
        self.player_1.move()
        self.player_2.move()
        self.ball.move()
        self.update_score()
        
    def game_over(self):
        global Running
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   Running = False
                   return
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        self.reset()
                        self.score_1 = 0
                        self.score_2 = 0
                        self.winner=None
                        return


    def check_winner(self):
        if self.score_1==5:
            self.winner="player one is the winner "
            self.score_winner_text = self.small_font.render(self.winner, True, "silver")
            self.draw()
            pygame.display.flip()
            self.game_over()
        if self.score_2==5:
            self.winner="player two is the winner "
            self.score_winner_text = self.small_font.render(self.winner, True, "silver")
            self.draw()
            pygame.display.flip()
            self.game_over()

    def reset(self):
        self.ball.reset()

    def update_score(self):
        if self.ball.rect.left <= 0:
            self.score_2 += 1
            self.reset()
        if self.ball.rect.right >= WIDTH:
            self.score_1 += 1
            self.reset()
        self.score_1_text = self.small_font.render(f"score_1 : {self.score_1}", True, "white")
        self.score_2_text = self.small_font.render(f"score_2 : {self.score_2}", True, "white")

    def check_collision(self):
        if self.player_1.my_pad.colliderect(self.ball.rect):
            self.ball.bounce_x()
        elif self.player_2.my_pad.colliderect(self.ball.rect):
            self.ball.bounce_x()
        if self.ball.rect.top <= 100 or self.ball.rect.bottom >= HEIGHT:
            self.ball.bounce_y()

    def draw(self):
        pygame.draw.line(screen, "white", (0, 100), (WIDTH, 100))
        screen.blit(self.score_1_text, self.score_1_text_rect)
        screen.blit(self.score_2_text, self.score_2_text_rect)
        screen.blit(self.score_title_text, self.score_title_text_rect)
        if self.winner:
             screen.blit(self.score_game_over_text, self.score_game_over_text_rect)
             screen.blit(self.score_winner_text, self.score_winner_text_rect)
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()

class Ball:
    def __init__(self):
        self.radius = 10
        self.speed = 1
        self.reset()

    def reset(self):
        self.pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
        angle = random.uniform(math.radians(20), math.radians(60))
        if random.choice([True, False]):
            angle = -angle
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * self.speed
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.radius * 2, self.radius * 2)

    def move(self):
        self.pos += self.velocity
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

    def bounce_x(self):
        self.velocity.x *= -1
        self.velocity.y += random.uniform(-0.3, 0.3)
        self.velocity = self.velocity.normalize() * self.speed

    def bounce_y(self):
        self.velocity.y *= -1
        self.velocity = self.velocity.normalize() * self.speed

    def draw(self):
        pygame.draw.ellipse(screen, "white", self.rect)

class Paddle:
    def __init__(self, x, y, is_player1):
        self.my_pad = pygame.Rect(x, y, 10, 100)
        self.speed = 4
        self.is_player1 = is_player1

    def move(self):
        keys = pygame.key.get_pressed()
        if self.is_player1:
            if keys[pygame.K_w] and self.my_pad.top > 100:
                self.my_pad.y -= self.speed
            if keys[pygame.K_s] and self.my_pad.bottom < HEIGHT:
                self.my_pad.y += self.speed
        else:
            if keys[pygame.K_UP] and self.my_pad.top > 100:
                self.my_pad.y -= self.speed
            if keys[pygame.K_DOWN] and self.my_pad.bottom < HEIGHT:
                self.my_pad.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, "white", self.my_pad)

my_game = Game(Paddle(0, HEIGHT // 2 - 50, True), Paddle(WIDTH - 10, HEIGHT // 2 - 50, False), Ball())

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    screen.fill("black")
    my_game.update()
    pygame.display.flip()

pygame.quit()
