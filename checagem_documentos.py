#O programa deve checar se os documentos apresentados por uma pessoa estão completos ou não

l1 = str(input())


if l1 == "F":
    l2 = str(input())
    l3 = str(input())

    if l2 == "S" and l3 == "S":
        print("Completa")
    else:
        print("Incompleta")


if l1 =="M":
    l2 = str(input())
    l3 = str(input())
    l4 = str(input())

    if l2 == "S" and l3 == "S" and l4 == "S":
        print("Completa")
    else:
        print("Incompleta")