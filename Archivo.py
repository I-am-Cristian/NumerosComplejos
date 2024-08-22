import math

def suma(a,b):
    realsuma = (a[0]+b[0])
    imagsuma = (a[1]+b[1])
    return (realsuma , imagsuma)

def resta(a, b):
    realresta = a[0] - b[0]
    imagresta = a[1] - b[1]
    return (realresta, imagresta)

def division(a,b):
    real = (a[0]*b[0]) + (a[1]*b[1]) / (b[0]**2)+(b[1]**2)
    imag =((b[0]*a[1])-(a[0]*b[1])) / (b[0]**2)+(b[1]**2)
    return (real,imag)

def multiplicacion(a,b):
    multres = (a[0]*b[0]) - (a[1]*b[1])
    multsum = (a[0]*b[1]) + (b[0]*a[0])
    return (multres , multsum)

def modulo(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def conjugado(a):
    return (a[0], -a[1])

def cartesian_a_polar(a):
    r = modulo(a)
    theta = math.atan2(a[1], a[0])
    return (r, theta)

def polar_a_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def fase(a):
    return math.atan2(a[1], a[0])


def prettyprint(a):
    print(a[0],"+",a[1],"i")

def main():
    print("División:")
    prettyprint(division((3, 2.8), (1.5, -2)))
    prettyprint(division((5, 7), (3, -2)))

    print("Suma:")
    prettyprint(suma((3, -1), (1, 4)))
    prettyprint(suma((2, 3), (5, -6)))

    print("Resta:")
    prettyprint(resta((3, -1), (1, 4)))
    prettyprint(resta((8, 2), (3, 7)))

    print("Multiplicación:")
    prettyprint(multiplicacion((3, -1), (1, 4)))
    prettyprint(multiplicacion((2, 5), (4, -3)))

    print("Módulo:")
    print(modulo((3, 4)))
    print(modulo((5, 12)))

    print("Conjugado:")
    prettyprint(conjugado((3, 4)))
    prettyprint(conjugado((5, -7)))

    print("Conversión de cartesiano a polar:")
    print(cartesian_a_polar((3, 4)))
    print(cartesian_a_polar((1, 1)))

    print("Conversión de polar a cartesiano:")
    print(polar_a_cartesian(5, math.pi/4))
    print(polar_a_cartesian(10, math.pi/3))

    print("Fase:")
    print(fase((3, 4)))
    print(fase((1, 1)))

main()
