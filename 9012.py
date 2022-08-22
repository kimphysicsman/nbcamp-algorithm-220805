# 문제
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
#
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
#
# 입력
# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
#
# 출력
# 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.


def check_unit_vps(sub_ps):
    if sub_ps == "()":
        return True
    elif sub_ps[0] == "(" and sub_ps[-1] == ")":
        return check_vps(sub_ps[1:-1])
    else:
        return False


def check_vps(ps):
    # 문자하나씩 괄호 상태 확인후 괄호가 모두 닫히면 check_vps(sub_ps)
    check_num = 0
    check_list = []

    sub_ps = ""
    for char in ps:
        sub_ps += char
        if char == "(":
            check_num += 1
        else:
            check_num -= 1

        if check_num < 0:
            return False
        if check_num == 0:
            if ps == sub_ps:
                check_list.append(check_unit_vps(sub_ps))
            else:
                check_vps(sub_ps)
            sub_ps = ""

    if check_num > 0:
        return False

    result = True
    for check in check_list:
        result = result and check

    return result


def main():
    n = int(input("input N : "))
    ps_list = []

    for _ in range(n):
        ps = input("input PS : ")
        ps_list.append(ps)

    for ps in ps_list:
        if check_vps(ps):
            print("YES")
        else:
            print("NO")

main()
