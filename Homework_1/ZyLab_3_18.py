#Santiago Landaverde
#1856681
import math
paint_colors = {'red':35,'blue':25,'green':23}
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_width * wall_height
paint_needed = wall_area/350
cans_needed = math.ceil(paint_needed)
print('Wall area:', wall_area, 'square feet')
print('Paint needed:','{:.2f}'.format(paint_needed),'gallons')
print('Cans needed:', cans_needed,'can(s)')
print('')
color = input("Choose a color to paint the wall:\n")
cost = cans_needed * paint_colors[color.lower()]
print('Cost of purchasing ' + color + ' paint: $' + str(cost))




