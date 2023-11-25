def solve_equations(a, b, c, d, e, f):
    determinant = a * e - b * d

    if determinant == 0:
        return "方程组无解或有无穷多解"

    x = (c * e - b * f) / determinant
    y = (a * f - c * d) / determinant

    return x, y

# 用户输入方程组的系数
equation1_coefficients = tuple(map(float, input("输入第一个方程的系数 (a b c，以空格分隔): ").split()))
equation2_coefficients = tuple(map(float, input("输入第二个方程的系数 (d e f，以空格分隔): ").split()))

result = solve_equations(*equation1_coefficients, *equation2_coefficients)
print("方程组的解为:", result)
