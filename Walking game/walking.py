import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Walking Animation")
clock = pygame.time.Clock()

walk1=pygame.image.load("sprite_1.png")
walk2=pygame.image.load("sprite_2.png")
walk3=pygame.image.load("sprite_3.png")

walk1=pygame.transform.scale(walk1,(150,150))
walk2=pygame.transform.scale(walk2,(150,150))
walk3=pygame.transform.scale(walk3,(150,150))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=walk3
        self.rect=self.image.get_rect()
        self.rect.x=300
        self.rect.y=200
        self.speed=5
        self.frame=0
        self.walk_index=0

    def update(self):
        keys=pygame.key.get_pressed()
        moving=False

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            moving=True

        if keys[pygame.K_d]:
            self.rect.x += self.speed
            moving=True 

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            moving=True

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            moving=True


        if moving:
            self.frame +=1

            if self.frame > 10:
                self.walk_index +=1
                self.frame=0

            if self.walk_index > 1:
                self.walk_index=0

            if self.walk_index == 0:
                self.image=walk1

            else:
                self.image=walk2

        else:
            self.image=walk3
            self.frame=0
            self.walk_index=0

player=Player()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=False

    all_sprites.update()
    screen.fill((200, 220, 255))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()