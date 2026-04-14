cp1 = float(input("Nota CP1 (0-10): "))
cp2 = float(input("Nota CP2 (0-10): "))
cp3 = float(input("Nota CP2 (0-10): "))
sp1 = float(input("Nota Sprint 1 (0-10): "))
sp2 = float(input("Nota Sprint 2 (0-10): "))
gs = float(input("Nota Global Solution (0-10): "))

menor_cp = cp1

if cp1 < cp2 or cp1 < cp3:
    menor_cp = cp1
else:
    if cp2 < cp1 or cp2 < cp3:
        menor_cp = cp2
    else:
        if cp3 < cp2 or cp3 < cp1:
            menor_cp = cp3

media_sempeso = (((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4) + (gs * 0.6)
print(f"A média do semestre sem peso é: {media_sempeso:.1f}")

media_compeso = (media_sempeso * 0.4)
print(f"A média do semestre com peso é: {media_compeso:.1f}")
