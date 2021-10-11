import random
import math
from sys import argv


def Check(str, new_str):  # 简易判重
    for i in range(len(str)):
        if new_str != str[i]:
            return 1
        else:
            return 0


def Getdata(argv):  # 获取cmd的命令符
    length = len(argv)
    numb1 = 0
    ran1 = 0
    exercisefile = None
    answerfile = None
    for i in range(length):
        if argv[i] == '-r':
            ran1 = int(argv[i + 1])
        if argv[i] == '-n':
            numb1 = int(argv[i + 1])
        if argv[i] == '-e':
            exercisefile = (argv[i + 1])
        if argv[i] == '-a':
            answerfile = (argv[i + 1])

    return ran1, numb1, exercisefile, answerfile


def Init(num1, ran, str):  # 初始化
    numerator = []  # 存放分子
    denominator = []  # 存放分母
    sym_local = 0
    for i in range(4):
        a = random.randint(1, ran)  # 随机生成分子
        b = random.randint(1, ran)  # 随机生成分子
        if a == 0:
            str[sym_local] = '0'
        elif a % b == 0:
            str[sym_local] = ('%d' % (a / b))
        elif a > b:
            str[sym_local] = ("%d'%d/%d" % (a / b, (a % b) / math.gcd(a, b), b / math.gcd(a, b)))
        else:
            str[sym_local] = ("%d/%d" % (a / math.gcd(a, b), b / math.gcd(a, b)))
        num1.append(a / b)      #浮点数分数
        numerator.append(a)     #分子
        denominator.append(b)   #分母
        sym_local += 2

    sym1 = [None] * 3  # 存放运算符
    sym1[0] = random.randint(0, 4)  # 随机生成运算符，生成数为0代表运算符为空
    sym1[1] = random.randint(1, 4)
    sym1[2] = random.randint(0, 4)
    # print(sym1)
    return num1, sym1, numerator, denominator


def Calculate(num, sym, str, numerator, denominator):  # 计算
    answer_str = [None] * 4
    result = 0
    sym_local = 1
    for i in [0, 2]:
        if sym[i] == 0:  # 运算符为空
            result = num[i + 1]
            str[sym_local] = None
            str[sym_local - 1] = None
            numerator[i] = numerator[i + 1]
            denominator[i] = denominator[i + 1]
        if sym[i] == 1:  # 加
            result = num[i] + num[i + 1]
            str[sym_local] = '+'
            numerator[i] = (numerator[i] * denominator[i + 1] + numerator[i + 1] * denominator[i])
            denominator[i] = denominator[i] * denominator[i + 1]
        if sym[i] == 2:  # 减
            if num[i] >= num[i + 1]:
                result = num[i] - num[i + 1]
                numerator[i] = (numerator[i] * denominator[i + 1] - numerator[i + 1] * denominator[i])
                denominator[i] = denominator[i] * denominator[i + 1]
            else:
                temp = num[i + 1]
                num[i + 1] = num[i]
                num[i] = temp
                result = num[i] - num[i + 1]
                temp1 = str[sym_local - 1]
                str[sym_local - 1] = str[sym_local + 1]
                str[sym_local + 1] = temp1
                numerator[i] = (numerator[i + 1] * denominator[i] - numerator[i] * denominator[i + 1])
                denominator[i] = denominator[i] * denominator[i + 1]
            str[sym_local] = '-'
        if sym[i] == 3:  # 乘
            result = num[i] * num[i + 1]
            str[sym_local] = '×'
            numerator[i] = (numerator[i] * numerator[i + 1])
            denominator[i] = denominator[i] * denominator[i + 1]
        if sym[i] == 4:  # 除
            if num[i + 1] == 0:
                num[i + 1] = None
                str[sym_local] = None
            else:
                result = num[i] / num[i + 1]
                str[sym_local] = '÷'
                numerator[i] = (numerator[i] * denominator[i + 1])
                denominator[i] = denominator[i] * numerator[i + 1]
        sym_local += 4
        sym[i] = result

    if sym[1] == 1:  # 整合运算结果
        sym[1] = sym[0] + sym[2]
        str[3] = '+'
        numerator[1] = (numerator[0] * denominator[2] + numerator[2] * denominator[0])
        denominator[1] = denominator[0] * denominator[2]
    if sym[1] == 2:
        sym[1] = sym[0] - sym[2]
        str[3] = '-'
        numerator[1] = (numerator[0] * denominator[2] - numerator[2] * denominator[0])
        denominator[1] = denominator[0] * denominator[2]
    if sym[1] == 3:
        sym[1] = sym[0] * sym[2]
        str[3] = '×'
        numerator[1] = (numerator[0] * numerator[2])
        denominator[1] = denominator[0] * denominator[2]
    if sym[1] == 4:
        if sym[2] == 0:
            sym[1] = -1
            str[4] = None
            numerator[1] = 1
            denominator[1] = 1
        else:
            sym[1] = sym[0] / sym[2]
            numerator[1] = (numerator[0] * denominator[2])
            denominator[1] = denominator[0] * numerator[2]
        str[3] = '÷'
    if denominator[1] == 0:
        sym[1] = -1
        answer_str.append("-1")
    else:
        if numerator[1] == 0:
            answer_str.append("0")
        elif numerator[1] % denominator[1] == 0:
            answer_str.append("%d" % (numerator[1] / denominator[1]))
        elif numerator[1] > denominator[1]:
            answer_str.append("%d'%d/%d" % (
                numerator[1] / denominator[1],
                (numerator[1] % denominator[1]) / (math.gcd(numerator[1], denominator[1])),
                denominator[1] / (math.gcd(numerator[1], denominator[1]))))
        else:
            answer_str.append("%d/%d" % (numerator[1] / (math.gcd(numerator[1], denominator[1])),
                                         denominator[1] / (math.gcd(numerator[1], denominator[1]))))
        str[7] = '='
    # print(sym)
    return sym[1], str, answer_str[4]


def Kuohao(str):  # 添加括号
    center = 3
    if str[center] == '×' or str[center] == '÷':
        if str[center - 2] == '+' or str[center - 2] == '-':
            str.insert(center - 3, '(')
            str.insert(center + 1, ')')
            center += 2
        if str[center + 2] == '+' or str[center + 2] == '-' or str[center + 2] == '÷':
            str.insert(center + 4, ')')
            str.insert(center + 1, '(')
    if str[center] == '-' or str[center] == '+':
        if str[center + 2] == '+' or str[center + 2] == '-':
            str.insert(center + 4, ')')
            str.insert(center + 1, '(')


def Correcting(a, b):  # 批改答案
    result = open(a, encoding='utf-8')
    correcting = open(b, encoding='utf-8')
    check = open('check_result.txt', 'w', encoding='utf-8')
    wrong = []
    correct = []
    count = len(open('Answers.txt', encoding='utf-8').readlines())
    for i in range(count):
        line1 = result.readline()
        line2 = correcting.readline()
        if line2 == line1:
            correct.append(i + 1)
        else:
            wrong.append(i + 1)
    check.write("%d correct:%s \n" % (len(correct), correct))
    check.write("%d wrong:%s" % (len(wrong), wrong))
    print("批改结果已放到check_result.txt")
    result.close()
    correcting.close()
    check.close()


def main():
    i = 0
    ran, numb, exercisefile, answerfile = Getdata(argv)
    # ran = numb = exercisefile = answerfile= 10
    if ran != 0 and numb != 0:
        string = [None] * numb
        question = open('Exercises.txt', 'a+', encoding='utf-8')
        result = open('Answers.txt', 'a+', encoding='utf-8')
        while i < numb:
            str = [None] * 8
            num = []
            num, sym, fenzi, fenmu = Init(num, ran, str)
            answer, str, ans_str = Calculate(num, sym, str, fenzi, fenmu)
            Kuohao(str)
            # print(str)
            str = list(filter(None, str))
            str1 = ' '.join(str)
            if Check(string, str1) and (answer >= 0):  # 排除掉重复和结果为负数的式子
                string[i] = str1
                print("No.%d: %s" % (i + 1, str1))
                question.write("No.%d: %s\n" % (i + 1, str1))
                result.write("No.%d: %s\n" % (i + 1, ans_str))
                i += 1
            else:
                pass
        print("题目已保存到 Exercises.txt")
        print("答案已保存到 Answers.txt")
        question.close()
        result.close()
        # print(string)
    elif exercisefile != None and answerfile != None:
        Correcting(exercisefile, answerfile)
    else:
        print("参数输入错误，请重新输入")

main()
