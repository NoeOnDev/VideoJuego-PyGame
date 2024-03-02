import pygame

# entities.py
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 50
        self.height = 50
        self.color = (0, 0, 255)
        self.vel = 1
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

# main.py
def main ():
    pygame.init()
    win = pygame.display.set_mode((1000, 800))
    player = Player()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player.vel > 0:
            player.x -= player.vel
        if keys[pygame.K_RIGHT] and player.x + player.vel < 1000 - player.width:
            player.x += player.vel
        if keys[pygame.K_UP] and player.y - player.vel > 0:
            player.y -= player.vel
        if keys[pygame.K_DOWN] and player.y + player.vel < 800 - player.height:
            player.y += player.vel
        
        win.fill((0, 0, 0))
        player.draw(win)
        pygame.display.update()
        
    pygame.quit()
if __name__ == "__main__":
    main()

# render.py

# input.py

# physics.py

# audio.py

# gui.py

# scenes.py