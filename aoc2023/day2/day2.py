import re
import utils


def part1(data):
    RED = 12
    GREEN = 13
    BLUE = 14
    gameSum = 0
    count = 0

    for i, line in enumerate(data):
        if line == '':
            break
        gameNumber = re.findall(r'Game (\d+)', line)[0]
        games = line.split(';')
        fits = 1

        for g in games:
            dices = re.findall(r'(\d+) (red|green|blue)', g)
            red, green, blue = 0, 0, 0
            for d in dices:
                color = d[1]
                if color == 'red':
                    red += int(d[0])
                elif color == 'green':
                    green += int(d[0])
                elif color == 'blue':
                    blue += int(d[0])
                else:
                    print('SOMETHING GONE WRONG')
            if red > RED or green > GREEN or blue > BLUE:
                fits = 0
                break

        if fits == 1:
            gameSum += int(gameNumber)

    return str(gameSum)


def part2(data):
    RED = 12
    GREEN = 13
    BLUE = 14
    gameSum = 0

    for i, line in enumerate(data):
        if line == '':
            break
        gameNumber = re.findall(r'Game (\d+)', line)[0]
        games = line.split(';')

        red, green, blue = 0, 0, 0
        for g in games:
            dices = re.findall(r'(\d+) (red|green|blue)', g)

            for d in dices:
                color = d[1]
                number = int(d[0])
                if color == 'red' and number > red:
                    red = number
                elif color == 'green' and number > green:
                    green = number
                elif color == 'blue' and number > blue:
                    blue = number

        gameSum += (red * green * blue)

    return str(gameSum)


print('Part 1: ' + part1(utils.parse_single_string('input.txt')))
print('Part 2: ' + part2(utils.parse_single_string('input.txt')))
