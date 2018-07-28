# -*- coding: UTF-8 -*-
import pygame
import random

def main():
    pygame.init()
    width = 1500
    height = 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("rain")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    clock = pygame.time.Clock()
    running = True
    # drops = []

    class Drop:
        def __init__(self):
            self.x = random.randrange(width)
            self.y = 10
            self.yspeed = random.uniform(2,3)
            self.rgb = (0,0,random.randint(0, 255))
            self.size = random.randint(1, 20)

        def fall(self):
            self.y = self.y + self.yspeed

        def draw(self):
            # pygame.draw.rect(screen, self.rgb, (self.x, self.y, random.choice(self.size)))
            pygame.draw.rect(screen, self.rgb, (self.x, self.y, self.size/4, self.size))

    drops = [Drop() for i in range(500)]

    while running:
        clock.tick(30)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_DOWN:
                    for i in drops:
                        i.yspeed = i.yspeed + 1


        for i in drops:
            i.draw()
            i.fall()
            if i.y >= height:
                i.y = random.randint(-200, -10)


        pygame.display.flip()


if __name__ == '__main__':

    main()
