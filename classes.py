import pygame

def characters_list():
    mainCharacter = main_Character("Harold", 12, 4, pygame.image.load("sprites/Pull Down.png"))
    Ghost = main_Character("Ghost", 12, 4, pygame.image.load("sprites/Pull Down.png"))
    return [mainCharacter, Ghost]


def differentTiles():
    image = pygame.image.load("map/water_and_island_tiles_v2.png")
    #tile1 is big dirt image 0
    #tile2 is skinny dirt image 1
    #tile3 is big grass image 2
    #tile4 is skinny grass image 3
    #grass_only_tile is just grass without the border around it 4


    rect1 = pygame.Rect(3, 0, 93, 93)
    tile1 = image.subsurface(rect1)

    rect2 = pygame.Rect(99, 0, 26, 93)
    tile2 = image.subsurface(rect2)

    rect3 = pygame.Rect(131, 0, 90, 93) #rect3 = pygame.Rect(131, 0, 93, 93)
    tile3 = image.subsurface(rect3)

    rect4 = pygame.Rect(227, 0, 26, 93)
    tile4 = image.subsurface(rect4)
    #-----------Grass Only Square------------------
    grass_only_tile_rect = pygame.Rect(135, 4, 82, 79)
    grass_only_tile = image.subsurface(grass_only_tile_rect)
    #------------Skinny grass variation-------------------
    skinny_grass_variation_rect = pygame.Rect(232, 0, 16, 93)
    skinny_grass_variation_tile = image.subsurface(skinny_grass_variation_rect)
    #-----------------------------------------------------
            #0      1       2       3       4                   5
    return [tile1, tile2, tile3, tile4, grass_only_tile, skinny_grass_variation_tile]

#--------------------Player Movements Animation------------------------
def player_Walk_Up_Images():
    image = pygame.image.load("sprites/Walk Up.png")
    list_images = []
    for i in range(12):
        rect = pygame.Rect(5 + i * 24, 0, 14, 24)
        walk_up_images = image.subsurface(rect)
        list_images.append(walk_up_images)
    return list_images
def player_Walk_Down_Images():
    image = pygame.image.load("sprites/Walk Down.png")
    list_images = []
    for i in range(12):
        rect = pygame.Rect(5 + i * 24, 0, 14, 24)
        walk_up_images = image.subsurface(rect)
        list_images.append(walk_up_images)
    return list_images
def player_Walk_Left_Images():
    image = pygame.image.load("sprites/Walk Left.png")
    list_images = []
    for i in range(12):
        rect = pygame.Rect(5 + i * 24, 0, 14, 24)
        walk_up_images = image.subsurface(rect)
        list_images.append(walk_up_images)
    return list_images
def player_Walk_Right_Images():
    image = pygame.image.load("sprites/Walk Right.png")
    list_images = []
    for i in range(12):
        rect = pygame.Rect(5 + i * 24, 0, 14, 24)
        walk_up_images = image.subsurface(rect)
        list_images.append(walk_up_images)
    return list_images
#--------------------Ghost Movements Animation-------------------------

#---------------------------------------------------------------------
def update_window(screen, world_map, background_x, background_y, userCharacter, original_screen_width, original_screen_height, Health):
    screen.fill((255, 255, 255))
    world_map.draw_map(screen, background_x - 1500, background_y - 1500)
    userCharacter.draw_main_character(screen, original_screen_width / 2, original_screen_height / 2)
    Health.draw(screen)
    pygame.display.flip()


class map:
    def __init__(self):
        self.map_size = 5
        self.x_pos = 1000
        self.y_pos = 1000
        self.green_layer = differentTiles()[4]
        self.border_layer = differentTiles()[2]
        self.skinny_grass_bordered_layer = differentTiles()[5]
        self.green_layer = pygame.transform.scale(self.green_layer, (self.green_layer.get_width() * self.map_size, self.green_layer.get_height() * self.map_size))
        self.border_layer = pygame.transform.scale(self.border_layer, (self.border_layer.get_width() * self.map_size, self.border_layer.get_height() * self.map_size))
        self.skinny_grass_bordered_layer = pygame.transform.scale(self.skinny_grass_bordered_layer, (self.skinny_grass_bordered_layer.get_width() * self.map_size, self.skinny_grass_bordered_layer.get_height() * self.map_size))
        # Cache the entire map as a single surface
        #Border surface layer----------------------------------------------------------------------------
        self.cached_map = pygame.Surface((20 * self.border_layer.get_width(), 20 * self.border_layer.get_height()))
        for i in range(12):
            for j in range(12):
                self.cached_map.blit(self.border_layer, (self.x_pos + i * self.border_layer.get_width(), self.y_pos + j * self.border_layer.get_height()))

        for i in range(12):
            for j in range(13):
                self.cached_map.blit(self.green_layer, ( self.x_pos + i * self.green_layer.get_width() + 15,self.y_pos + j * self.green_layer.get_height() + 20))
        #Green Surface Layer-----------------------------------------------------------------------------------------------------------------------------

        for i in range(2):
            for j in range(13):
                self.cached_map.blit(self.green_layer, (self.x_pos + i * self.green_layer.get_width() + 4560, self.y_pos + j * self.green_layer.get_height() + 20))

        for i in range(13):
            for j in range(2):
                self.cached_map.blit(self.green_layer, (self.x_pos + i * self.green_layer.get_width() + 20,  self.y_pos + j * self.green_layer.get_height() + 4740))

        #Skinny Grass Bordered layer-------------------------------------------------------------------------
        for i in range(13):
            self.cached_map.blit(self.skinny_grass_bordered_layer, (self.x_pos + i * self.skinny_grass_bordered_layer.get_width() + 15,  self.y_pos + 3))

    def draw_map(self, screen, background_x, background_y):
        # Blit the cached map surface
        screen.blit(self.cached_map, (background_x, background_y))


class heads_up_display:
    def __init__(self):
        self.health_bar_image = pygame.image.load("Heads Up Display/Bar1.png")
        self.stamina_bar_image = pygame.image.load("Heads Up Display/Bar2.png")

        self.health_width = 196
        self.stamina_width = 196
        self.health_bar_red_rect = pygame.Rect(0, 0, self.health_width, 9) #Width: 196, Height: 9
        self.stamina_bar_blue_rect = pygame.Rect(0, 0, self.stamina_width, 9)  # Width: 196, Height: 9

    def draw(self, screen):
        self.health_bar_red_rect.topleft = (26, 26) #RECT WINDOW POSITION
        screen.blit(self.health_bar_image, (20, 20)) #IMAGE WINDOW POSITION
        pygame.draw.rect(screen, (255, 0, 0), self.health_bar_red_rect)

        self.stamina_bar_blue_rect.topleft = (26, 49)  # RECT WINDOW POSITION
        screen.blit(self.stamina_bar_image, (20, 43)) # IMAGE WINDOW POSITION
        pygame.draw.rect(screen, (0, 100, 255), self.stamina_bar_blue_rect)

    def lower_health(self, current_health, maximum_health):
        self.health_width = (current_health / maximum_health) * 196
        self.health_bar_red_rect = pygame.Rect(0, 0, self.health_width, 9)

class Characters:
    def __init__(self, name, age, size, health=20, stamina=20, attack_power=5):
        self.name = name
        self.health = health
        self.age = age
        self.stamina = stamina
        self.attack_power = attack_power
        self.size = size

    def draw(self, screen, x, y):
        centered_x = x - self.image.get_width() // 2
        centered_y = y - self.image.get_height() // 2
        screen.blit(self.image, (centered_x, centered_y))

class main_Character(Characters):
    def __init__(self, name, age, size, image, health=20, stamina=20, attack_power=5):
        super().__init__(name, age, size, health, stamina, attack_power)
        self.image = pygame.transform.scale(image,(image.get_width() * self.size, image.get_height() * self.size)) #initialize initial image
        self.rect = self.image.get_rect()

    def update_image(self, image):
        self.image = pygame.transform.scale(image, (image.get_width() * self.size, image.get_height() * self.size))
        self.rect = self.image.get_rect()

    def draw_main_character(self, screen, x, y):
        centered_x = x - self.image.get_width() // 2
        centered_y = y - self.image.get_height() // 2
        self.rect.topleft = (centered_x, centered_y)
        screen.blit(self.image, (centered_x, centered_y))

    def main_character_rect(self): #for detecting collision with other recs...
        return self.rect

class Enemy(Characters):
    def __init__(self, image, name, age, size, health=20, stamina=20, attack_power=5):
        super().__init__(name, age, size, health, stamina, attack_power)
        self.image = pygame.transform.scale(image, (image.get_width() * self.size, image.get_height() * self.size))  # initialize initial image
        self.rect_enemy = self.image.get_rect()
    def update_image(self, image):
        self.image = pygame.transform.scale(image, (image.get_width() * self.size, image.get_height() * self.size))
        self.rect_enemy = self.image.get_rect()

    def draw_enemy_character(self, screen, x, y):
        centered_x = x - self.image.get_width() // 2
        centered_y = y - self.image.get_height() // 2
        self.rect_enemy.topleft = (centered_x, centered_y)
        screen.blit(self.image, (centered_x, centered_y))

    def main_character_rect(self):  # for detecting collision with other recs...
        return self.rect_enemy


