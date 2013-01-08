def triangle(first_edge, second_edge, third_edge):
    min_edge = min(first_edge, second_edge, third_edge)
    a, b, c = sorted([first_edge, second_edge, third_edge])
    if min_edge <= 0 or a + b <= c:
        raise TriangleError
    if first_edge == second_edge == third_edge:
        return 'equilateral'
    elif first_edge == second_edge or first_edge == third_edge or second_edge == third_edge:
        return 'isosceles'
    else:
        return 'scalene'

class TriangleError(RuntimeError):
    pass
