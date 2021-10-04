def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

printArea() # Default  arguments
printArea(4, 2.5)
printArea(width = 1.2)
printArea(height = 6.2)