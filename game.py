import pygame

screen = None
running = True

def main():
    global screen
    global running

    pygame.init()
    pygame.display.set_caption("Game")

    current_screen_info = pygame.display.Info()
    screen = pygame.display.set_mode((current_screen_info.current_w,
                                      current_screen_info.current_h))

    
    player_sprite = sprite(pygame.image.load("player.jpeg"), 50, 50)
    player_sprite.render()
    pygame.display.flip()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

class sprite():
    """
    The sprite class contains all information about a sprite.

    Variables
    ---------
    image:
        The rendered representation of the sprite
    x_position:
        The current x position of the sprite
    y_position:
        The current y position of the sprite
    """
    image = None
    x_position = None
    y_position = None

    def __init__(self, image, x_position, y_position):
        self.image = image
        self.x_position = x_position
        self.y_position = y_position
    def render(self):
        global screen
        screen.blit(self.image, (self.x_position, self.y_position))

    def move(self, new_x_position, new_y_position):
        self.x_position = new_x_position
        self.y_position = new_y_position

if __name__ == '__main__':
    main()
