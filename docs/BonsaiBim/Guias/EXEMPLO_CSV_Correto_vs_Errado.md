# Exemplo Visual: CSV Correto vs Errado

## ❌ CSV SALVO ERRADO (com vírgula decimal)

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
              ↑↑↑↑↑↑ ERRO! Vírgula no decimal
3,,Vigas,,m³,420,50,,GrossVolume,IfcBeam
            ↑↑↑↑↑↑ ERRO! Vírgula no decimal
3,,Lajes,,m³,380,00,,GrossVolume,IfcSlab
            ↑↑↑↑↑↑ ERRO! Vírgula no decimal
```

**Resultado no BonsaiBIM:**
- ❌ Custos aparecem como 0.00 ou valores incorretos
- ❌ Total Cost não calcula
- ❌ BonsaiBIM não consegue interpretar o valor unitário

---

## ✅ CSV SALVO CORRETO (com ponto decimal)

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn
              ↑↑↑↑↑↑ CORRETO! Ponto no decimal
3,,Vigas,,m³,420.50,,GrossVolume,IfcBeam
            ↑↑↑↑↑↑ CORRETO! Ponto no decimal
3,,Lajes,,m³,380.00,,GrossVolume,IfcSlab
            ↑↑↑↑↑↑ CORRETO! Ponto no decimal
```

**Resultado no BonsaiBIM:**
- ✅ Valores unitários aparecem corretamente: 450.00, 420.50, 380.00
- ✅ Volumes são calculados: 0.40 m³, 0.12 m³, 563.62 m³
- ✅ Total Cost calcula automaticamente:
  - Pilares: 0.40 × 450.00 = 180.00
  - Vigas: 0.12 × 420.50 = 50.46
  - Lajes: 563.62 × 380.00 = 214,175.60

---

## 🔍 Como Identificar o Erro

### Abra o CSV no Bloco de Notas e procure:

**Sinais de arquivo ERRADO:**
```
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
                   ↑ duas vírgulas seguidas = campo vazio?
```
O computador vê: "Unit=m³" e depois "Value=vazio" e depois "TotalPrice=0"

**Sinais de arquivo CORRETO:**
```
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn
                   ↑ ponto, depois vírgula = OK!
```
O computador vê: "Unit=m³" e depois "Value=450.00" e depois "TotalPrice=vazio"

---

## 💡 Dica Visual Rápida

Conte as vírgulas na linha:

```
❌ ERRADO - 9 vírgulas:
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
 1 2       3 4  5   6 7 8           9

✅ CORRETO - 8 vírgulas:
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn
 1 2       3 4  5     6 7           8
```

Se você tem MAIS vírgulas do que deveria = problema com decimais!

---

## 📱 Teste Rápido

Cole estas linhas no Bloco de Notas e salve como `teste.csv`:

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
3,,Teste,,un,10.50,,Count,IfcDoor
```

Importe no BonsaiBIM. Se aparecer Value = 10.50, está CORRETO! ✅

Se aparecer Value = vazio ou 0, está ERRADO! ❌

---

*Este exemplo mostra a diferença entre salvar o CSV corretamente vs incorretamente*
