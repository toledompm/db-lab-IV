from helpers.helper import interssection, union, support, confidence

# I.2. Considere os seguintes conjuntos:
#   X = {A, B, C, D, E}, -- first_set
#   Ix = {A}, -- first_item
#   Iy = {B},-- second_item
#   Iz = {C}, -- third_item
#   Ƒ = {{A},{A}, {A,B,C}, {A,B}, {B,C}, {B}, {D,E}, {D}, {B} } -- fith_set

first_set = ['A', 'B', 'C', 'D', 'E'] # X
first_item = ['A']  # Ix
second_item = ['B']  # Iy
third_item = ['C']  # Iz
transactions = [
    ['A'],
    ['A'],
    ['A', 'B', 'C'],
    ['A', 'B'],
    ['B', 'C'],
    ['B'],
    ['D', 'E'],
    ['D'],
    ['B']
]  # Ƒ


# 7. Os conjuntos
#   a) Ix ∪ Iy
#   b) Ix ∪ Iz
def question_7():
    a_union_set = union(first_item, second_item)
    b_union_set = union(first_item, third_item)

    print('07.a) Ix ∪ Iy: ', a_union_set)
    print('07.b) Ix ∪ Iz: ', b_union_set)


# 8. Os conjuntos
#   a) (Ix ∩ Iy) ∪  Iz
#   b) (Ix ∩ Iz) ∪  Iy
def question_8():
    a_union_set = union(interssection(first_item, second_item), third_item)
    b_union_set = union(interssection(first_item, third_item), second_item)

    print('08.a) (Ix ∩ Iy) ∪  Iz: ', a_union_set)
    print('08.b) (Ix ∩ Iz) ∪  Iy: ', b_union_set)


# 9. O valor de suporte(Ix, Ix).
def question_9():
    support_value = support(first_item, first_item, transactions)
    print('09. O valor de suporte(Ix, Ix): ', support_value)


# 10. O valor de suporte(Ix, Iy).
def question_10():
    support_value = support(first_item, second_item, transactions)
    print('10. O valor de suporte(Ix, Iy): ', support_value)


# 11. O valor de suporte(Ix,Iz).
def question_11():
    support_value = support(first_item, third_item, transactions)
    print('11. O valor de suporte(Ix, Iz): ', support_value)


# 12. O valor de suporte(Ix, {Iz ∪ Iy}).
def question_12():
    support_value = support(first_item, union(
        third_item, second_item), transactions)
    print('12. O valor de suporte(Ix, {Iz ∪ Iy}): ', support_value)


# 13. O valor de confiança(Ix  Ix). Qual o sentido desse resultado?
def question_13():
    # O resultado é 100% porque os itens são iguais.
    confidence_value = confidence(first_item, first_item, transactions)
    print('13. O valor de confiança(Ix  Ix): ', confidence_value)


# 14. O valor de confiança(Ix  Iy).
def question_14():
    confidence_value = confidence(first_item, second_item, transactions)
    print('14. O valor de confiança(Ix  Iy): ', confidence_value)


# 15. O valor de confiança(Iy  Iy)
def question_15():
    confidence_value = confidence(second_item, second_item, transactions)
    print('15. O valor de confiança(Iy  Iy): ', confidence_value)


# 16. O valor de confiança(Ix  Iz)
def question_16():
    confidence_value = confidence(first_item, third_item, transactions)
    print('16. O valor de confiança(Ix  Iz): ', confidence_value)


# 17. O valor de confiança(Iz  Ix)
def question_17():
    confidence_value = confidence(third_item, first_item, transactions)
    print('17. O valor de confiança(Iz  Ix): ', confidence_value)


# 18. O valor de confiança(Iy  Iz)
def question_18():
    confidence_value = confidence(second_item, third_item, transactions)
    print('18. O valor de confiança(Iy  Iz): ', confidence_value)


# 19. O valor de confiança(Ix  {Iz ∪ Iy})
def question_19():
    confidence_value = confidence(first_item, union(
        third_item, second_item), transactions)
    print('19. O valor de confiança(Ix  {Iz ∪ Iy}): ', confidence_value)


# 20. O valor de confiança({Iz ∪ Iy}  Ix)
def question_20():
    confidence_value = confidence(
        union(third_item, second_item), first_item, transactions)
    print('20. O valor de confiança({Iz ∪ Iy}  Ix): ', confidence_value)


# 21. Considerando os valores calculados anteriormente, escolha valores mínimos
# para suporte e confiança de modo que somente a associação mais “forte” entre 2
# ou mais itens seja selecionada caso um algoritmo do tipo Apriori seja utilizado
# para determinar regras de associação. Justifique esse resultado.
#
# (Obs: Associações entre 2 ou mais itens é feita considerando somente os itens que
# apresentam o suporte superior a um valor mínimo. Esses itens são chamados de itens
# com valores altos [i.e.: “large itemsets”] ).
def question_21():
    print('21. O valor de suporte deve ser >= 0.11\n    O valor da confiança deve ser >= 0.5')


def main():
    question_7()
    question_8()
    question_9()
    question_10()
    question_11()
    question_12()
    question_13()
    question_14()
    question_15()
    question_16()
    question_17()
    question_18()
    question_19()
    question_20()
    question_21()


if __name__ == '__main__':
    main()
