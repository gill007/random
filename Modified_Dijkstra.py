import pygame
import time

class Node():
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        
        self.f = float("inf")

    def __eq__(self, other):
        return self.position == other.position

countP=0
countH=0

def dij(grid, start, end):
   
    
    start_node = Node(None, start)
    start_node.f = 0
    end_node = Node(None, end)
 

    
    open_list = []
    closed_list = []

    
    open_list.append(start_node)
    print(start_node.position,"start_node.position\n")

    
    while len(open_list) > 0:

       
        current_node = open_list[0]
        
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
               
                current_index = index
               

       
        open_list.pop(current_index)
        closed_list.append(current_node)
        
     

       
        if current_node == end_node:
            path = []
            current = current_node
            
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 

      
        children = []
        x = end_node.position[0] - start_node.position[0]
        y = end_node.position[1] - start_node.position[1]

        if x>=0 and y>=0:
            for new_position in[(0, 1),(1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                # print(node_position)
           
                if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                    continue

                if grid[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node, node_position)
                onn.append(node_position)
                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.f = current_node.f + 1

                for open_node in open_list:
                    if child == open_node and child.f > open_node.f:
                        continue

                open_list.append(child)

        elif x<0 and y<0:
            for new_position in[(0, -1),(-1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                # print(node_position)
           
                if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                    continue

                if grid[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node, node_position)
                onn.append(node_position)
                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.f = current_node.f + 1

                for open_node in open_list:
                    if child == open_node and child.f > open_node.f:
                        continue

                open_list.append(child)

        elif x<0 and y>0:
            for new_position in[(0, 1),(-1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                # print(node_position)
           
                if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                    continue

                if grid[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node, node_position)
                onn.append(node_position)
                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.f = current_node.f + 1

                for open_node in open_list:
                    if child == open_node and child.f > open_node.f:
                        continue

                open_list.append(child)

        elif x>=0 and y<=0:
            for new_position in[(0, -1),(1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                # print(node_position)
           
                if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                    continue

                if grid[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node, node_position)
                onn.append(node_position)
                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.f = current_node.f + 1

                for open_node in open_list:
                    if child == open_node and child.f > open_node.f:
                        continue

                open_list.append(child)

        
      




    

                
            




# main
  
BLACK  = (0,0,0)
WHITE  = (255,255,255)
GREEN = (0,204,0)
RED     = (255,51,51)
BLUE   = (51,51,255)
GREY = (96,96,96)
PINK = (178,102,255)
HAHA =(255,255,102)

WIDTH=20
HEIGHT=20

MARGIN=5
SET=0
EXP=0
CLICK=0

grid=[]
for row in range(30):
    grid.append([])
    for column in range(30):
        grid[row].append(0)

color1=grid


start = (-1,-1)
end = (-1,-1)
onn = []

pygame.init()


size=[755,755]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Dijkstra Algorithm Simulation")

done=False
clock=pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
           
         
            if SET==0:
                start = (row,column)
                SET=1
            elif CLICK==1:
                end = (row,column)
            elif CLICK>1:
                grid[row][column]=1
            else:
                grid[row][column]=0
            print("Click ", pos, "Grid coordinates: ", row, column)
            print (start , end)
            CLICK+=1
           

        elif pressed[pygame.K_s]:
           
           path=dij(grid,start,end)
         

         

           #print("Path Length",len(path))
           
           for x in range(len(onn)):
               if(grid[onn[x][0]][onn[x][1]]!=1):
                   grid[onn[x][0]][onn[x][1]]=5
               
        
                   
           for n in range(len(path)):
               if(grid[path[n][0]][path[n][1]]!=1):
                   grid[path[n][0]][path[n][1]]=4

        elif pressed[pygame.K_r]:
            for row in range(30):
                for column in range(30):
                    if(grid[row][column]==5):
                        EXP=EXP+1
            print("Explored:",EXP+len(path))
            print("Path Length:",len(path))
                   
           
           
    screen.fill(BLACK)
 
  
    for row in range(30):
        for column in range(30):
            color = WHITE
            if start == (row, column) :
                color = GREEN
            elif end == (row, column):
                color=RED
            elif grid[row][column]==1:
                color=GREY
            elif grid[row][column]==5:
                color=PINK
                
            elif grid[row][column]==4:
                color=HAHA
                
                
            
   
            
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

       
           
 
    
    clock.tick(60)
    
 
  
    pygame.display.flip()

pygame.quit()

