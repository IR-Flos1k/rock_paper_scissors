import pygame as lib
from logik import AIBot

lib.init()

# screen set
WIDTH, HEIGHT = 800, 600
screen = lib.display.set_mode((WIDTH, HEIGHT))
lib.display.set_caption('Rock-Paper-Scissors with AI')

#images
bg_size = (800, 600)
paper_size = (250, 250)
scissors_size = (325, 250)
rock_size = (325, 250)

bg = lib.transform.scale(lib.image.load('background/background.jpg'), bg_size)
paper = lib.transform.scale(lib.image.load('background/paper.png'), paper_size)
rock = lib.transform.scale(lib.image.load('background/rock.png'), rock_size)
scissors = lib.transform.scale(lib.image.load('background/scissors.png'), scissors_size)

paper_player = lib.transform.scale(lib.image.load('background/paper.png'), paper_size)
rock_player = lib.transform.scale(lib.image.load('background/rock.png'), rock_size)
scissors_player = lib.transform.scale(lib.image.load('background/scissors.png'), scissors_size)

paper_player = lib.transform.flip(paper_player, True, False)
rock_player = lib.transform.flip(rock_player, True, False)
scissors_player = lib.transform.flip(scissors_player, True, False)

#dictionary
images_dict_bot = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

images_dict_players = {
    "rock_player": rock_player,
    "paper_player": paper_player,
    "scissors_player": scissors_player
}

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (160, 82, 45)

class Button:
    def __init__(self, x, y, width, height, text, value1, value2):
        self.rect = lib.Rect(x, y, width, height)
        self.text = text
        self.value1 = value1
        self.value2 = value2
        self.font = lib.font.SysFont(None, 40)

    def draw(self, surface):
        lib.draw.rect(surface, BROWN, self.rect)
        lib.draw.rect(surface, BLACK, self.rect, 2) 
        
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

btn_rock = Button(100, 500, 150, 50, "Камінь", "rock", "rock_player")
btn_paper = Button(325, 500, 150, 50, "Папір", "paper", "paper_player")
btn_scissors = Button(550, 500, 150, 50, "Ножиці", "scissors", "scissors_player")
buttons = [btn_rock, btn_paper, btn_scissors]

bot = AIBot()

current_player_image = None
current_bot_image = None

running = True
while running:
    screen.blit(bg, (0, 0))
    
    for event in lib.event.get():
        if event.type == lib.QUIT:
            running = False
            
        if event.type == lib.MOUSEBUTTONDOWN:
            if event.button == 1:
                for btn in buttons:
                    if btn.is_clicked(event.pos):
                        player_move = btn.value2
                        bot_move = bot.predict_move()
                        
                        print(f"Ви обрали: {player_move} | Бот обрав: {bot_move}")
                        
                        current_player_image = images_dict_players[player_move]
                        current_bot_image = images_dict_bot[bot_move]
                        
                        bot.update_memory(player_move)
                        
    if current_player_image:
        screen.blit(current_player_image, (75, 150)) 
    if current_bot_image:
        screen.blit(current_bot_image, (450, 150))

    for btn in buttons:
        btn.draw(screen)

    lib.display.flip()

lib.quit()