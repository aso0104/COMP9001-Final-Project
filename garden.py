'''
This program simulates an interactive garden where users can plant, water, fertilize, and harvest flowers on a 3x3 grid. 
There are three types of flower to choose, rose/sunflower/cherry blossom. 
Each flower grows gradually through watering and fertilizing, and once fully grown, it can be harvested into a basket. 
The program displays a visual map of the garden by representing flowers with vivid emojis. 
It also provides commands like and flower inspection for users to track the growth status of each flower, 
which would help them to manage their own garden easily. 
This program may be suitable for gardening enthusiasts who want to have their own little virtual garden.
'''

class Flower:
    def __init__(self, name):
        self.name = name
        self.growth = 0
        self.watered = False
        self.fertilized = False


    def __str__(self):
        status_flower = (f'Flower name : {self.name}\nGrowth      : {self.growth}%')
        return status_flower



class Garden:
    
    def __init__(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]
        self.basket = []


    # create the garden map
    def display(self):
        print('\nGarden Map')
        print('┌─────┬─────┬─────┐')
        for i in range(3):
            row_display = ''
            for j in range(3):
                cell = self.grid[i][j]
            
                if cell:
                    symbol = {
                        'rose': ' 🌹 ',
                        'sunflower': ' 🌻 ',
                        'sakura': ' 🌸 '
                    }[cell.name].center(5)
                    
                else:
                    symbol = '      '
                row_display += symbol
            print(row_display)
            
            if i < 2:
                print('├─────┼─────┼─────┤')
                
            else:
                print('└─────┴─────┴─────┘')
                


    # choose the flower type:
    def plant_flower(self, x, y):
        
        if self.grid[x][y]:
            print('There is already a flower here!')
            return

        while True:
            flower_type = input('Choose the flower (rose/sunflower/sakura): ').strip().lower()
            
            if flower_type in ['rose', 'sunflower', 'sakura']:
                self.grid[x][y] = Flower(flower_type)
                print(f'{flower_type.capitalize()} planted at ({x}, {y})!')
                break
            
            else:
                print('Currently you can not plant it in your garden, please choose another one!')


    # demonstrate the ststus of certain flower:
    def show_flower(self, x, y):
        flower = self.grid[x][y]
        
        print('\nYour Flowers: ')
        print('-' * 25)
        print(flower)
        print('-' * 25)


    '''
    Watering and fertilizing will increase the growth progress of the flower, 
    each watering/fertilizing will increase the growth progress by 25 points, 
    and the flower will only bloom when the growth progress reaches 100%. 
    In addition, the flower will only reach 100% growth if it has been watered/fertilized at least once each, 
    which means that both fertilizer and watering are both required.
    '''    
        

    # set the function of watering a flower:
    def water(self, x, y):
        flower = self.grid[x][y]
        
        if flower.growth == 100:
            print('The flower has bloomed! Please Pick it!')
            
        elif flower.growth == 75 and not flower.fertilized:
            print('Water is already full! Please fertilize it!')
            
        else:
            flower.watered = True
            flower.growth += 25
            print(f'{flower.name.capitalize()} ({x},{y}) is watered successfully!')


    # set the function of fertilizing a flower:
    def fertilize(self, x, y):
        flower = self.grid[x][y]
        
        if flower.growth == 100:
            print('The flower has bloomed! Pick it!')
            
        elif flower.growth == 75 and not flower.watered:
            print('Fertilizer is already full! Please water it!')
            
        else:
            flower.fertilized = True
            flower.growth += 25
            print(f'{flower.name.capitalize()} ({x},{y}) is fertilized successfully!')


    # set the function of harvesting a flower:
    def harvest(self, x, y):
        flower = self.grid[x][y]
            
        if flower.growth == 100:
            self.basket.append(flower)
            self.grid[x][y] = None
            print(f'{flower.name.capitalize()} ({x},{y}) has been picked!')
                
        else:
            print('The flower has not bloomed yet! Please water/fetilize it!')
                


    # set the function of showing your basket:
    def show_basket(self):
        
        if self.basket:
            print('\nFlower Basket')
            print('-' * 40)
            print(f'\nYou have {len(self.basket)} flower(s) in your basket!')
            
            flower_counts = {}
            
            for f in self.basket:
                if f.name in flower_counts:
                    flower_counts[f.name] += 1
                else:
                    flower_counts[f.name] = 1

            for name, count in flower_counts.items():
                print(f'{name.capitalize()}: {count}\n')
                print('-' * 40)
            
        else:
            print('Your basket is empty!')
        
        
# check if valid input of coordinates   
def enter_coordinates():
        while True:
            coords = input('Enter coordinates (x y) (0<= x or y <= 2, e.g.(2 2))\nor use \'r\' to return: ').strip().split()
            
            # check if user require to return:
            if len(coords) == 1 and coords[0].lower() == 'r':
                return None

            # check if integer:
            if len(coords) != 2 or not all(i.isdigit() for i in coords):
                print('Please enter valid coordinates! e.g.(2 2)')
                continue

            # convert into integer:
            x, y = map(int, coords)

            # check if valid coordinates:
            if (0 <= x <= 2 and 0 <= y <= 2):
                return x,y
            
            else:
                print('Do not plant outside your garden!')
                
                
def main():
    garden = Garden()

    print('Welcome to your own garden!')
    print('\nYou can do:')
    print('plant | show garden | show flower | water | fertilize |')
    print('harvest | show basket | show commands | exit')

    while True:
        command = input('\nEnter command: ').strip().lower()


        if command == 'plant':
            coords = enter_coordinates()
            if coords is None:
                print("Successfully go back, please choose another command.")
                continue
            
            x, y = coords
            garden.plant_flower(x, y)


        elif command == 'show garden':
            garden.display()


        elif command == 'show flower':
            while True:
                coords = enter_coordinates()
                if coords is None:
                    print("Successfully go back, please choose another command.")
                    break
            
                x, y = coords
                flower = garden.grid[x][y]
                
                if flower:
                    garden.show_flower(x, y) 
                    break
                
                else:
                    print('You didn\'t plant any flower!')


        elif command == 'water':
            coords = enter_coordinates()
            if coords is None:
                print("Successfully go back, please choose another command.")
                continue
                
            x, y = coords
            flower = garden.grid[x][y]
                    
            if flower:
                garden.water(x, y)
                    
            else:
                print('There is no flower here. Plant one first!')


        elif command == 'fertilize':
            coords = enter_coordinates()
            if coords is None:
                print("Successfully go back, please choose another command.")
                continue
                
            x, y = coords
            flower = garden.grid[x][y]
                
            if flower:
                garden.fertilize(x, y)
                    
            else:
                print('There is no flower here. Plant one first!')


        elif command == 'harvest':
            coords = enter_coordinates()
            if coords is None:
                print("Successfully go back, please choose another command.")
                continue
                
            x, y = coords
            flower = garden.grid[x][y]
                    
            if flower:
                garden.harvest(x, y)
                    
            else:
                print('There is no flower here. Plant one first!')


        elif command == 'show basket':
            garden.show_basket()

        
        elif command == 'show commands':
            print('\nYou can do:')
            print('plant | show garden | show flower | water | fertilize |')
            print('harvest | show basket | show commands | exit')


        elif command == 'exit':
            print('Remember to care for your flowers! See you next time!')
            break


        else:
            print('Please enter a valid command!')
            print('\nYou can do:')
            print('plant | show garden | show flower | water | fertilize |')
            print('harvest | show basket | show commands | exit')



if __name__ == '__main__':
    main()
