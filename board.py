import pygame


pygame.init()


row_1 = []
array = []
row_2 = []
row_3 = []
row_4 = []
row_5 = []
row_6 = []
row_7 = []
row_8 = []
row_9 = []


for i in range(9):
   row_1.append("")
   row_2.append("")
   row_3.append("")
   row_4.append("")
   row_5.append("")
   row_6.append("")
   row_7.append("")
   row_8.append("")
   row_9.append("")


array.append(row_1)
array.append(row_2)
array.append(row_3)
array.append(row_4)
array.append(row_5)
array.append(row_6)
array.append(row_7)
array.append(row_8)
array.append(row_9)




class Board:
   def __init__(self, width, height, window):
       self.width = width
       self.height = height
       self.window = window
   def select(self):
       x, y = pygame.mouse.get_pos()
       self.x = x
       self.y = y
       return self.x, self.y


   def window_select(self, x, y):
       #difficulty select
       if self.window == 1 and 10 <= x <= 196 and 610 <= y <= 700:
           pygame.display.quit()
           game_board = Board(603, 810, 21)
           game_board.screen()
       elif self.window == 1 and 206 <= x <= 397 and 610 <= y <= 700:
           pygame.display.quit()
           game_board = Board(603, 810, 22)
           game_board.screen()
       elif self.window == 1 and 407 <= x <= 593 and 610 <= y <= 700:
           pygame.display.quit()
           game_board = Board(603, 810, 23)
           game_board.screen()




       # reset button
       elif self.window == 21 and self.x >= 10 and self.x <= 196 and self.y >= 680 and self.y <= 740:
           for r in range(9):
               for c in range(9):
                   array[r][c] = ""
           pygame.display.quit()
           game_board = Board(603, 810, 21)
           game_board.screen()
       elif self.window == 22 and self.x >= 10 and self.x <= 196 and self.y >= 680 and self.y <= 740:
           for r in range(9):
               for c in range(9):
                   array[r][c] = ""
           pygame.display.quit()
           game_board = Board(603, 810, 22)
           game_board.screen()
       elif self.window == 23 and self.x >= 10 and self.x <= 196 and self.y >= 680 and self.y <= 740:
           for r in range(9):
               for c in range(9):
                   array[r][c] = ""
           pygame.display.quit()
           game_board = Board(603, 810, 23)
           game_board.screen()


       #exit button
       elif self.window == 21 and self.x >= 407 and self.x <= 593 and self.y >= 680 and self.y <= 740:
           pygame.quit()
       elif self.window == 22 and self.x >= 407 and self.x <= 593 and self.y >= 680 and self.y <= 740:
           pygame.quit()
       elif self.window == 23 and self.x >= 407 and self.x <= 593 and self.y >= 680 and self.y <= 740:
           pygame.quit()


       #restart/ return to main menu
       elif self.window == 21 and self.x >= 206 and self.x <= 397 and self.y >= 680 and self.y <= 740:
           pygame.display.quit()
           game_board = Board(603, 810, 1)
           game_board.screen()
       elif self.window == 22 and self.x >= 206 and self.x <= 397 and self.y >= 680 and self.y <= 740:
           pygame.display.quit()
           game_board = Board(603, 810, 1)
           game_board.screen()
       elif self.window == 23 and self.x >= 206 and self.x <= 397 and self.y >= 680 and self.y <= 740:
           pygame.display.quit()
           game_board = Board(603, 810, 1)
           game_board.screen()


   def click(self, x, y):
       self.col = (x // 67) + 1
       self.row = (y//67)+1
       return self.col, self.row


   def empty(self):
       runns = True
       for i in range(9):
           for j in range(9):
               if array[i][j] == "":
                   print(f"row: {i + 1}, col: {j + 1}")
                   runns = False
                   break
           if runns == False:
               break
   def check_full(self):
       count = 0
       for i in range(9):
           for j in range(9):
               if array[i][j] != "":
                   count += 1
       if count == 81:
           print("board is filled")


   def clear(self):
       want_to_delete = input("do you want to delete, y/n: ")
       if want_to_delete == "y":
           delete_val = True
           return delete_val
       elif want_to_delete == "n":
           delete_val = False
           return delete_val




       #will clear a cell but only if the player filled in that square
   def sketch(self, value):
       self. value = value
       return self.value






   def place_number(self, value, x, y):
       array[y-1][x-1] = value
       print(array)
       for i in range(1, 10):
           if i == x:
               x = (x * 67) - 33
       for j in range(1, 10):
           if j == y:
               y = (y * 67) - 33
       pygame.display.set_caption("Pygame Text Example")
       pygame.font.init()
       font2 = pygame.font.SysFont("Arial", 25)
       text_surface_number = font2.render(f"{value}", True, ("dark gray"))
       text_rect_number = text_surface_number.get_rect()
       text_rect_number.center = (x, y)
       return self.screen.blit(text_surface_number, text_rect_number)


       #takes the value from sketch to add the value where the user has clicked


   def screen(self):
       #welcome screen
       if self.window == 1:
           screen_width = 603
           screen_height = 810


           screen = pygame.display.set_mode((603, 810))
           my_rectangle = pygame.Rect(603 - 196, 610, 186, 90)
           my_rectangle2 = pygame.Rect(603- 397, 610, 191, 90)
           my_rectangle3 = pygame.Rect(10, 610, 186, 90)


           clock = pygame.time.Clock()
           pygame.display.set_caption("Pygame Text Example")


           pygame.font.init()


           font = pygame.font.SysFont("Arial", 48)
           font2 = pygame.font.SysFont("Arial", 25)




           text_surface = font.render("Welcome to Sudoku!", True, ("Black"))
           text_rect = text_surface.get_rect()
           text_rect.center = (screen_width // 2, screen_height - 600)


           text_surface_mod = font2.render("Select Game Mode:", True, ("Black"))
           text_rect_mod = text_surface_mod.get_rect()
           text_rect_mod.center = ((603 // 2, 810 // 2))


           text_surface_1 = font2.render("Easy", True, ("White"))
           text_rect_1 = text_surface_1.get_rect()
           text_rect_1.center = ((196 - 10) // 2, 655)


           text_surface_m = font2.render("Medium", True, ("White"))
           text_rect_m = text_surface_m.get_rect()
           text_rect_m.center = (603// 2, 655)


           text_surface_h = font2.render("Hard", True, ("White"))
           text_rect_h = text_surface_h.get_rect()
           text_rect_h.center = (603 - 98, 655)


           running = True
           screen.fill("Light blue")
           pygame.draw.rect(screen, "orange", my_rectangle)
           pygame.draw.rect(screen, "orange", my_rectangle2)
           pygame.draw.rect(screen, "orange", my_rectangle3)
           screen.blit(text_surface, text_rect)
           screen.blit(text_surface_1, text_rect_1)
           screen.blit(text_surface_m, text_rect_m)
           screen.blit(text_surface_h, text_rect_h)
           screen.blit(text_surface_mod, text_rect_mod)
           pygame.display.update()
           while running:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       running = False
                   elif event.type == pygame.MOUSEBUTTONDOWN:
                       self.select()
                       self.window_select(self.x,self.y)


           clock.tick(60)


       elif self.window == 21:
           # game board easy


           self.screen = pygame.display.set_mode((603, self.height))
           screen = self.screen
           font2 = pygame.font.SysFont("Arial", 25)
           my_rectangle = pygame.Rect(603 - 196, 680, 186, 60)
           my_rectangle2 = pygame.Rect(603 - 397, 680, 191, 60)
           my_rectangle3 = pygame.Rect(10, 680, 186, 60)
           text_surface_reset = font2.render("Reset", True, ("White"))
           text_rect_reset = text_surface_reset.get_rect()
           text_rect_reset.center = ((196 - 10) // 2, 700)


           text_surface_restart = font2.render("Restart", True, ("White"))
           text_rect_restart = text_surface_restart.get_rect()
           text_rect_restart.center = (603 // 2, 700)


           text_surface_exit_2 = font2.render("Exit", True, ("White"))
           text_rect_exit_2 = text_surface_exit_2.get_rect()
           text_rect_exit_2.center = (603 - 98, 700)




           clock = pygame.time.Clock()
           running = True
           screen.fill("light blue")
           for x in range(0, 603, 67):
               pygame.draw.line(screen, "black", (x, 0), (x, 603), )
           for y in range(0, 603, 67):
               pygame.draw.line(screen, "black", (0, y), (603, y))
           for y in range(0, 603, 201):
               pygame.draw.line(screen, "black", (0, y), (603, y), 5)
           for x in range(0, 603, 201):
               pygame.draw.line(screen, "black", (x, 0), (x, 603), 5)
           pygame.draw.rect(screen, "orange", my_rectangle)
           pygame.draw.rect(screen, "orange", my_rectangle2)
           pygame.draw.rect(screen, "orange", my_rectangle3)
           screen.blit(text_surface_reset, text_rect_reset)
           screen.blit(text_surface_restart, text_rect_restart)
           screen.blit(text_surface_exit_2, text_rect_exit_2)
           while running:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       running = False
                   elif event.type == pygame.MOUSEBUTTONDOWN:
                       self.select()
                       if self.x >= 0 and self.x <= 603 and self.y >= 0 and self.y <= 603:
                           self.click(self.x, self.y)


                           if array[(self.row) - 1][(self.col) - 1] != '':
                               my_rectangle_clear = pygame.Rect(self.x - 20, self.y - 20, 50, 50)
                               pygame.draw.rect(screen, "Light blue", my_rectangle_clear)
                               array[(self.row) - 1][(self.col) - 1] = ''
                           elif array[(self.row)][self.col] == '':
                               value = int(input("value: "))
                               self.place_number(value, self.col, self.row)


                       elif self.x >= 10 and self.x <= 196 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       elif self.x >= 407 and self.x <= 593 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       elif self.x >= 206 and self.x <= 397 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       pygame.display.update()




               pygame.display.update()
           clock.tick(60)


       elif self.window == 22:
           # game board medium


           self.screen = pygame.display.set_mode((603, self.height))
           screen = self.screen
           font2 = pygame.font.SysFont("Arial", 25)
           my_rectangle = pygame.Rect(603 - 196, 680, 186, 60)
           my_rectangle2 = pygame.Rect(603 - 397, 680, 191, 60)
           my_rectangle3 = pygame.Rect(10, 680, 186, 60)
           text_surface_reset = font2.render("Reset", True, ("White"))
           text_rect_reset = text_surface_reset.get_rect()
           text_rect_reset.center = ((196 - 10) // 2, 700)


           text_surface_restart = font2.render("Restart", True, ("White"))
           text_rect_restart = text_surface_restart.get_rect()
           text_rect_restart.center = (603 // 2, 700)


           text_surface_exit_2 = font2.render("Exit", True, ("White"))
           text_rect_exit_2 = text_surface_exit_2.get_rect()
           text_rect_exit_2.center = (603 - 98, 700)


           clock = pygame.time.Clock()
           screen.fill("light blue")
           for x in range(0, 603, 67):
               pygame.draw.line(screen, "black", (x, 0), (x, 603), )
           for y in range(0, 603, 67):
               pygame.draw.line(screen, "black", (0, y), (603, y))
           for y in range(0, 603, 201):
               pygame.draw.line(screen, "black", (0, y), (603, y), 5)
           for x in range(0, 603, 201):
               pygame.draw.line(screen, "black", (x, 0), (x, 603), 5)
           pygame.draw.rect(screen, "orange", my_rectangle)
           pygame.draw.rect(screen, "orange", my_rectangle2)
           pygame.draw.rect(screen, "orange", my_rectangle3)
           screen.blit(text_surface_reset, text_rect_reset)
           screen.blit(text_surface_restart, text_rect_restart)
           screen.blit(text_surface_exit_2, text_rect_exit_2)
           running = True
           while running:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       running = False
                   elif event.type == pygame.MOUSEBUTTONDOWN:
                       self.select()
                       if self.x >= 0 and self.x <= 603 and self.y >= 0 and self.y <= 603:
                           self.click(self.x, self.y)
                           if array[(self.row) - 1][(self.col) - 1] != '':
                               my_rectangle_clear = pygame.Rect(self.x - 20, self.y - 20, 50, 50)
                               pygame.draw.rect(screen, "Light blue", my_rectangle_clear)
                               array[(self.row) - 1][(self.col) - 1] = ''
                           elif array[(self.row)][self.col] == '':
                               value = int(input("value: "))
                               self.place_number(value, self.col, self.row)
                       elif self.x >= 10 and self.x <= 196 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       elif self.x >= 407 and self.x <= 593 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       elif self.x >= 206 and self.x <= 397 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       pygame.display.update()


               pygame.display.update()
           clock.tick(60)


       elif self.window == 23:
           #game board hard


           self.screen = pygame.display.set_mode((603, self.height))
           screen = self.screen
           font2 = pygame.font.SysFont("Arial", 25)
           my_rectangle = pygame.Rect(603 - 196, 680, 186, 60)
           my_rectangle2 = pygame.Rect(603 - 397, 680, 191, 60)
           my_rectangle3 = pygame.Rect(10, 680, 186, 60)
           text_surface_reset = font2.render("Reset", True, ("White"))
           text_rect_reset = text_surface_reset.get_rect()
           text_rect_reset.center = ((196 - 10) // 2, 700)


           text_surface_restart = font2.render("Restart", True, ("White"))
           text_rect_restart = text_surface_restart.get_rect()
           text_rect_restart.center = (603 // 2, 700)


           text_surface_exit_2 = font2.render("Exit", True, ("White"))
           text_rect_exit_2 = text_surface_exit_2.get_rect()
           text_rect_exit_2.center = (603 - 98, 700)


           clock = pygame.time.Clock()
           screen.fill("light blue")
           for x in range(0, 603, 67):
               pygame.draw.line(screen, "black", (x, 0), (x, 603), )
           for y in range(0, 603, 67):
               pygame.draw.line(screen, "black", (0, y), (603, y))
           for y in range(0, 603, 201):
               pygame.draw.line(screen, "black", (0, y), (603, y), 5)
           for x in range(0, 603, 201):
               pygame.draw.line(screen, "black", (x, 0), (x, 603), 5)
           pygame.draw.rect(screen, "orange", my_rectangle)
           pygame.draw.rect(screen, "orange", my_rectangle2)
           pygame.draw.rect(screen, "orange", my_rectangle3)
           screen.blit(text_surface_reset, text_rect_reset)
           screen.blit(text_surface_restart, text_rect_restart)
           screen.blit(text_surface_exit_2, text_rect_exit_2)
           running = True
           while running:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       running = False
                   elif event.type == pygame.MOUSEBUTTONDOWN:
                       self.select()
                       if self.x >= 0 and self.x <= 603 and self.y >= 0 and self.y <= 603:
                           self.click(self.x, self.y)
                           if array[(self.row) - 1][(self.col) - 1] != '':
                               my_rectangle_clear = pygame.Rect(self.x - 20, self.y - 20, 50, 50)
                               pygame.draw.rect(screen, "Light blue", my_rectangle_clear)
                               array[(self.row) - 1][(self.col) - 1] = ''
                           elif array[(self.row)][self.col] == '':
                               value = int(input("value: "))
                               self.place_number(value, self.col, self.row)
                       elif self.x >= 10 and self.x <= 196 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       elif self.x >= 407 and self.x <= 593 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       elif self.x >= 206 and self.x <= 397 and self.y >= 680 and self.y <= 740:
                           self.window_select(self.x, self.y)
                       pygame.display.update()


               pygame.display.update()
           clock.tick(60)




       elif self.window == 3:
           #game won
           screen_width = 810
           screen_height = 810


           screen = pygame.display.set_mode((810, 810))
           my_rectangle_exit_red = pygame.Rect((810 // 2) - 120, 810 - 200, 240, 90)
           my_rectangle_exit_white = pygame.Rect((810 // 2) - 115, 810 - 195, 230, 80)
           my_rectangle_exit_orange = pygame.Rect((810 // 2) - 110, 810 - 190, 220, 70)


           clock = pygame.time.Clock()
           pygame.display.set_caption("Pygame Text Example")


           pygame.font.init()


           font = pygame.font.SysFont("Arial", 70, "bold")
           font2 = pygame.font.SysFont("Arial", 30, )


           text_surface = font.render("Game Won!", True, ("Black"))
           text_rect = text_surface.get_rect()
           text_rect.center = (screen_width // 2, screen_height - 600)
           text_surface_2 = font2.render("Exit", True, ("White"))
           text_rect_2 = text_surface_2.get_rect()
           text_rect_2.center = (screen_width // 2, 655)


           running = True
           while running:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       running = False
                   elif event.type == pygame.MOUSEBUTTONDOWN:
                       self.select()
               screen.fill("Light blue")
               pygame.draw.rect(screen, (255, 69, 0), my_rectangle_exit_red)
               pygame.draw.rect(screen, (255, 255, 255), my_rectangle_exit_white)
               pygame.draw.rect(screen, "orange", my_rectangle_exit_orange)
               screen.blit(text_surface, text_rect)
               screen.blit(text_surface_2, text_rect_2)


               pygame.display.update()


           clock.tick(60)
       elif self.window == 4:
           # game lost
           screen_width = 810
           screen_height = 810


           screen = pygame.display.set_mode((810, 810))
           my_rectangle_exit_red = pygame.Rect((810 // 2) - 120, 810 - 200, 240, 90)
           my_rectangle_exit_white = pygame.Rect((810 // 2) - 115, 810 - 195, 230, 80)
           my_rectangle_exit_orange = pygame.Rect((810 // 2) - 110, 810 - 190, 220, 70)


           clock = pygame.time.Clock()
           pygame.display.set_caption("Pygame Text Example")


           pygame.font.init()


           font = pygame.font.SysFont("Arial", 70, "bold")
           font2 = pygame.font.SysFont("Arial", 30, )


           text_surface = font.render("Game Over :(", True, ("Black"))
           text_rect = text_surface.get_rect()
           text_rect.center = (screen_width // 2, screen_height - 600)
           text_surface_2 = font2.render("Restart", True, ("White"))
           text_rect_2 = text_surface_2.get_rect()
           text_rect_2.center = (screen_width // 2, 655)




           running = True
           while running:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       running = False
                   elif event.type == pygame.MOUSEBUTTONDOWN:
                       self.select()
               screen.fill("Light blue")
               pygame.draw.rect(screen, (255, 69, 0), my_rectangle_exit_red)
               pygame.draw.rect(screen, (255, 255, 255), my_rectangle_exit_white)
               pygame.draw.rect(screen, "orange", my_rectangle_exit_orange)
               screen.blit(text_surface, text_rect)
               screen.blit(text_surface_2, text_rect_2)


               pygame.display.update()


           clock.tick(60)












board = Board(603, 810, 1)
board.screen()
