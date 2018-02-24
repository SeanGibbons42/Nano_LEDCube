from CoordinateSystem import CoordinateSystem
from tkinter import *


def layerDisplay(cube, root, r=5):
    n = cube.getDimensions()
    nx = n[2]; ny = n[1]; nz = n[0];
    grid = cube.exportGrid()[1]
    canvas = Canvas(root, width=(4*nx+8)*nz*r, height=5*ny*r)
    canvas.grid(row=0, column=0)
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                if grid[z, y, x] == 1:
                    canvas.create_oval((4*nx+8)*r*z + 5*r + 4*r*x, 5*r + 4*r*y,
                                       (4*nx+8)*r*z + 7*r + 4*r*x, 7*r + 4*r*y, fill='blue')
                else:
                    canvas.create_oval((4*nx+8)*r*z + 5*r + 4*r*x, 5*r + 4*r*y,
                                       (4*nx+8)*r*z + 7*r + 4*r*x, 7*r + 4*r*y)
    print(grid)


def crystal(cube, structure):
    n = cube.getDimensions()
    if structure == 'fcc':
        for z in range(n[2]):
            for y in range(n[1]):
                for x in range(n[0]):
                    if (x + y + z) % 2 == 0:
                        cube.setPixel([z, y, x], 1)

root = Tk()

nx, ny, nz = 7, 7, 7

cube = CoordinateSystem([0, 0, 0], [nz, ny, nx])

crystal(cube, 'fcc')

layerDisplay(cube, root)

root.mainloop()