while True:
    h = int(input("fale uma altura: "))
    se = input("fale sua sexualidade: [H/M]")[0].upper().strip()
    if se == "H":
        p = (72.7 * h) - 58
        print(f"seu peso ideal e: {p}")
        break
    elif se == "M":
        p = (62.1 * h) - 44.7
        print(f"seu peso ideal e: {p}")
        break
    else:
        print("sexo nao adequado!")
        print("tente novemente")