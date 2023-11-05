import pygame

class Pipeline(pygame.sprite.Sprite):
    def __init__(self,orientation,x_pos,y_pos):
        super().__init__()
        self.image = pygame.image.load("Art/pipe-green.png").convert_alpha()
        self.orientation = orientation
        if self.orientation == "upwards":       #If the pipe is at ground level
            self.rect = self.image.get_rect(topright = (x_pos, y_pos))
        elif self.orientation == "downwards":       #If the pipe is at sky level
            self.image = pygame.transform.flip(self.image, False, True) #Inverts the image
            self.rect = self.image.get_rect(bottomright = (x_pos, y_pos - 100))
    
    def destroy(self):
        if self.rect.x <= -60:
            self.kill()
    
    def update(self):
        self.destroy()
        self.rect.x -= 2

#When the player hits a CheckPoint rectangle, its score will increase by 1 and the checkPoint will disappear
class CheckPoint(pygame.sprite.Sprite):
    def __init__(self,x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((5,100)).convert_alpha()
        self.image.fill((255,0,0,120))
        self.rect = self.image.get_rect(bottomright = (x_pos, y_pos))
    def destroy(self):
        if self.rect.x <= -60:
            self.kill()
    def update(self):
        self.destroy()
        self.rect.x -= 2
