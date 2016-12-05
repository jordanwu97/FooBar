def answer(dimensions, captain_position, badguy_position, distance):
    d1, d2 = dimensions
    c1, c2 = captain_position
    b1, b2 = badguy_position

    # x,y position of bad guy
    y = b2 - c2
    x = b1 - c1

    # creating lines of reflection
    ry = sorted(reflectionsy(dimensions, captain_position, distance))
    rx = sorted(reflectionsx(dimensions, captain_position, distance))

    # creating sets of points in the format of (position, length to origin): ((x,y),l)
    goods = set()
    bads = set()

    goods.add(((-c1, -c2), dist((-c1, -c2))))
    goods.add(((-c1, d2 - c2), dist((-c1, d2 - c2))))
    goods.add(((d1 - c1, -c2), dist((d1 - c1, -c2))))
    goods.add(((d1 - c1, d2 - c2), dist((d1 - c1, d2 - c2))))


    if inRange((x, y), distance):
        bads.add(((x, y), dist((x, y))))

    # good guy position
    g1 = 0
    g2 = 0

    # reflects bad guy across.
    for ny in ry:
        if ny >= 0:
            # bad guys
            point = (x, 2 * ny - y)
            x, y = point

            if inRange(point, distance):
                bads.add((point, dist(point)))
    # reset badguy
    y = b2 - c2
    x = b1 - c1

    for ny in reversed(ry):
        if ny < 0:
            # bad guys
            point = (x, 2 * ny - y)
            x, y = point
            if inRange(point, distance):
                bads.add((point, dist(point)))

    noshot = set(goods)
    goods.add(((0, 0), 0))
    for ny in goods:
        p1, l = ny
        x, y = p1
        for nx in ry:
            if nx >= 0:
                point = (x, 2 * nx - y)
                x, y = point
                if inRange(point, distance):
                    noshot.add((point, dist(point)))
        x, y = p1
        for nx in reversed(ry):
            if nx < 0:
                point = (x, 2 * nx - y)
                x, y = point
                if inRange(point, distance):
                    noshot.add((point, dist(point)))



    shots = set(bads)
    for ny in bads:
        p1, l = ny
        x, y = p1

        for nx in rx:
            if nx > 0:
                point = (2 * nx - x, y)
                x, y = point
                if inRange(point, distance):
                    shots.add((point, dist(point)))
        x, y = p1

        for nx in reversed(rx):
            if nx < 0:
                point = (2 * nx - x, y)
                x, y = point
                if inRange(point, distance):
                    shots.add((point, dist(point)))


    for ny in goods:
        p1, l = ny
        x, y = p1
        for nx in rx:
            if nx >= 0:
                point = (2 * nx - x, y)
                x, y = point
                if inRange(point, distance):
                    noshot.add((point, dist(point)))
        x, y = p1
        for nx in reversed(rx):
            if nx < 0:
                point = (2 * nx - x, y)
                x, y = point
                if inRange(point, distance):
                    noshot.add((point, dist(point)))

    result = dict()
    for i in shots:
        p1, l = i
        a, b = p1
        hyp = float((a ** 2 + b ** 2))
        hyp = float((distance ** 2) / hyp) ** (1 / 2.0)
        if hyp != 0:
            point = (hyp*a,hyp*b)
            if point not in result:
                result[point] = l
            else:
                temp = result[point]
                result[point] = min(temp, l)
    if ((0,0),0) in noshot:
        noshot.remove(((0,0),0.0))
    for i in noshot:
        p1, l = i
        a, b = p1
        hyp = float((a ** 2 + b ** 2))
        hyp = float(distance**2/hyp)**(1/2.0)
        if hyp != 0:
            # point = ((a/gcd(a,b), b/gcd(a,b)))
            point = (hyp*a,hyp*b)
            if point in result:
                if result[point] > l:
                    del result[point]



    # # print ry
    # # print rx
    print noshot
    # print
    # print shots
    print result
    return len(result)

def gcd(a,b):
    if a%b != 0:
        return gcd(a, a%b)
    return b

def dist(point):
    x, y = point
    return x ** 2 + y ** 2


def reflectionsy(dimensions, captain_position, distance):
    d1, d2 = dimensions
    c1, c2 = captain_position
    y = d2 - c2
    ry = set()

    ry.add(y)
    while y <= distance:
        y += d2
        ry.add(y)

    y = - c2

    ry.add(y)
    while -y <= distance:
        y -= d2
        ry.add(y)
    return ry


def reflectionsx(dimensions, captain_position, distance):
    d1, d2 = dimensions
    c1, c2 = captain_position
    x = d1 - c1
    rx = set()
    rx.add(x)
    while x <= distance:
        x += d1
        rx.add(x)
    x = - c1

    rx.add(x)
    while -x <= distance:
        x -= d1
        rx.add(x)
    return rx


def inRange(point, distance):
    x, y = point
    if x ** 2 + y ** 2 > distance ** 2:
        return False
    return x ** 2 + y ** 2 <= distance ** 2

# def answer(dim, shooter, target, distance):
#     a = answer1(dim, shooter, target, distance)
#     b = answer2(dim, shooter, target, distance)
#     if a > b:
#         return a
#     else:
#         return b


print answer([10, 5], [1, 1], [9, 1], 14)


