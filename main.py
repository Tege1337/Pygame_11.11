import pygame
import sys
import random
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
p_color = (0, 128, 255)

scr_width = 800
scr_height = 600

clock = pygame.time.Clock()

screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Pygame ASD")

class Player:
    def __init__(self, x, y, c_width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.movement = {"left": False, "right": False, "up": False, "down": False}

        def moving(self):
            if self.movement["left"]:
                self.x -= self.speed
            elif self.movement["right"]:
                self.x += self.speed
            elif self.movement["up"]:
                self.y -= self.speed
            elif self.movement["down"]:
                self.y += self.speed
            self.rect.topleft = (self.x, self.y)

        def draw(self, screen):
            pygame.draw.rect(screen, p_color, self.rect)
        
        def handle_input(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movement["left"] = True
                if event.key == pygame.K_RIGHT:
                    self.movement["right"] = True
                if event.key == pygame.K_UP:
                    self.movement["up"] = True
                if event.key == pygame.K_DOWN:
                    self.movement["down"] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement["left"] = False
                elif event.key == pygame.K_RIGHT:
                    self.movement["right"] = False
                elif event.key == pygame.K_UP:
                    self.movement["up"] = False
                elif event.key == pygame.K_DOWN:
                    self.movement["down"] = False


