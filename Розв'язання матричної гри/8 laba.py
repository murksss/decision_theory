from numpy import zeros, delete, reshape
from random import randint
from matplotlib.pyplot import plot, grid, show, title, xlabel, ylabel, tight_layout


def generate_matrix(A, B):
    tmp = zeros([5, 5])
    for i in range(5):
        for j in range(5):
            tmp[i][j] = randint(A, B)
    return tmp


def minmax(mtx):
    alpha_ = max([min(mtx[row]) for row in range(len(mtx))])
    beta_ = min([max(mtx.T[col]) for col in range(len(mtx.T))])

    # print(f'α(maxmin) - {alpha}\nβ(minmax) - {beta}')
    if alpha_ == beta_:
        # print('Saddle point exist')
        isPoint_ = True
    else:
        # print('Saddle point does not exist')
        isPoint_ = False

    return alpha_, beta_, isPoint_


def find_cross(p1, p2, p3, p4):
    if (p1[1] > p3[1] and p2[1] > p4[1]) or (p1[1] < p3[1] and p2[1] < p4[1]):
        return False
    A1 = (p1[1] - p2[1]) / (p1[0] - p2[0])
    A2 = (p3[1] - p4[1]) / (p3[0] - p4[0])
    b1 = p1[1] - A1 * p1[0]
    b2 = p3[1] - A2 * p3[0]

    Xa = (b2 - b1) / (A1 - A2)
    Ya = A1 * Xa + b1
    if 0 < Xa < 1:
        return Xa, Ya


def graph_analytical(data):
    P1, P2 = [], []
    for i in range(len(data[0])):
        plot([0, 1], [data[0][i], data[1][i]], linestyle='-', color='b')
        P1.append([0, data[0][i]])
        P2.append([1, data[1][i]])

    crossed_point = []
    for i in range(len(P1) - 1):
        for j in range(i + 1, len(P1)):
            ans = find_cross(P1[i], P2[i], P1[j], P2[j])
            if ans:
                x, y = ans
                crossed_point.append([x, y, min([P2[j][1], P2[i][1]]), [P1[i], P2[i], P1[j], P2[j]]])

    min_point_y = min([crossed_point[i][2] for i in range(len(crossed_point))])
    i = 0
    while i < len(crossed_point):
        if crossed_point[i][2] != min_point_y:
            crossed_point.pop(i)
        else:
            i += 1

    max_idx = crossed_point.index(max([crossed_point[i] for i in range(len(crossed_point))]))
    plot(crossed_point[max_idx][0], crossed_point[max_idx][1], marker='o', color='r')
    grid()
    title("Графоаналітичний метод розв'язання")
    xlabel('p')
    ylabel('v')
    tight_layout()
    res = crossed_point[max_idx][3]
    plot([res[0][0], res[1][0]], [res[0][1], res[1][1]], color='green')
    plot([res[2][0], res[3][0]], [res[2][1], res[3][1]], color='green')
    return crossed_point[max_idx][3]


def simplification(mtx):
    print('\n\tSimplification\n')
    for z in range(2):
        i = 0
        while i < (len(mtx) - 1):
            j = i + 1
            while j < (len(mtx)):
                isDelete_i = False
                isDelete_j = False
                for k in range(len(mtx[i])):
                    if mtx[i][k] < mtx[j][k]:
                        isDelete_i = True
                    else:
                        isDelete_i = False
                        break
                for k in range(len(mtx[i])):
                    if mtx[i][k] > mtx[j][k]:
                        isDelete_j = True
                    else:
                        isDelete_j = False
                        break
                if isDelete_i:
                    if z == 0:
                        print(f'{mtx[i]} < {mtx[j]}\n{mtx[i]} - deleted\n')
                    else:
                        print(f'{mtx[i]} < {mtx[j]}'
                              f'\n{mtx[i].reshape(len(mtx[i]), 1)} - deleted\n')
                    mtx = delete(mtx, i, axis=0)
                elif isDelete_j:
                    if z == 0:
                        print(f'{mtx[i]} > {mtx[j]}\n{mtx[j]} - deleted\n')
                    else:
                        print(f'{mtx[i]} > {mtx[j]}'
                              f'\n{mtx[j].reshape(len(mtx[i]), 1)} - deleted\n')
                    mtx = delete(mtx, j, axis=0)
                else:
                    j += 1
            i += 1
        mtx = mtx.T
    return mtx


def find_strategy(a):
    minmax(a)
    p1 = (a[1][1] - a[1][0]) / (a[0][0] + a[1][1] - a[0][1] - a[1][0])
    p2 = 1 - p1
    q1 = (a[1][1] - a[0][1]) / (a[0][0] + a[1][1] - a[0][1] - a[1][0])
    q2 = 1 - q1
    v = (a[1][1] * a[0][0] - a[0][1] * a[1][0]) / (a[0][0] + a[1][1] - a[0][1] - a[1][0])
    return p1, p2, q1, q2, v


def menu():
    while True:
        print(f'## ~~~~~~~MENU~~~~~~~\n'
              f'## 1) Generate matrix\n'
              f'## 2) Simplification\n'
              f'## 3) Graphoanalytical method\n'
              f'## 0) Exit\n##')
        var = int(input('## >>> '))

        if var == 0:
            break
        elif var == 1:
            matrix = generate_matrix(-20, 20)
            print(f'##\n## Payoff matrix:\n\n{matrix}\n')
            alpha, beta, isPoint = minmax(matrix)
            print(f'## α(maxmin) - {alpha}\n## β(minmax) - {beta}')
            if isPoint:
                print('## Saddle point exist')
            else:
                print('## Saddle point does not exist')
        elif var == 2:
            try:
                matrix_2 = simplification(matrix)
                print(f'##\n## Matrix after simplification: \n\n{matrix_2}\n')
            except UnboundLocalError:
                print('## First you need to generate a matrix')

        elif var == 3:
            try:
                matrix_3 = matrix[:2]
                print(f'##\n## Payoff matrix[2*5]\n\n{matrix_3}\n')
                alpha, beta, isPoint = minmax(matrix_3)
                print(f'## α(maxmin) - {alpha}\n## β(minmax) - {beta}')
                if isPoint:
                    print('## Saddle point exist')
                else:
                    print('## Saddle point does not exist')
                    res = graph_analytical(matrix_3)
                    result = [res[i][1] for i in range(len(res))]
                    result = reshape(result, [2, 2]).T
                    print(f'##\n## Payoff matrix[2*2]\n\n{result}\n')
                    alpha, beta, isPoint = minmax(result)
                    print(f'## α(maxmin) - {alpha}\n## β(minmax) - {beta}')
                    if isPoint:
                        print('## Saddle point exist')
                    else:
                        print('## Saddle point does not exist')
                        p1, p2, q1, q2, v = find_strategy(result)
                        print(f'## p1 = {round(p1, 3)}\n'
                              f'## p2 = {round(p2, 3)}\n'
                              f'## q1 = {round(q1, 3)}\n'
                              f'## q2 = {round(q2, 3)}\n'
                              f'## v = {round(v, 3)}\n')

                    show()

            except UnboundLocalError:
                print('## First you need to generate a matrix')

        else:
            print('## Choose correct variant')

        _ = input('## Press ENTER to continue\n##\n##\n##')


if __name__ == '__main__':
    menu()
