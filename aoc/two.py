from util import load_data_file

one_actions = {
    'down': lambda u, x, y: [x, y + u],
    'up': lambda u, x, y: [x, y - u],
    'forward': lambda u, x, y: [x + u, y]
}


def down(u, x, y, a):
    return x, y, a + u


def up(u, x, y, a):
    return x, y, a - u


def forward(u, x, y, a):
    nx = x + u
    ny = y + a * u
    return nx, ny, a


aim_actions = {
    'down': down,
    'up': up,
    'forward': forward
}


def parse_command(com):
    d, u = com.split(' ')
    return d, int(u)


def compute_current_pos(data):
    x = 0
    y = 0
    for com in data:
        d, u = parse_command(com)
        x, y = one_actions[d](u, x, y)

    return x * y


def compute_current_aim(data):
    x = 0
    y = 0
    a = 0
    for com in data:
        d, u = parse_command(com)
        x, y, a = aim_actions[d](u, x, y, a)

    return x * y


data = load_data_file(2, 1)
print(compute_current_pos(data))

test = load_data_file(2, 't')
print(compute_current_aim(test))

print(compute_current_aim(data))
