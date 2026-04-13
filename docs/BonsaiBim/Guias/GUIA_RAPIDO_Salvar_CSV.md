# 📋 GUIA RÁPIDO: Como Salvar CSV para o BonsaiBIM

## 🚨 PROBLEMA PRINCIPAL

No Brasil: `10,5` (vírgula)  
No CSV: `10.5` (PONTO) ← O BonsaiBIM precisa disso!

**Se salvar errado, os custos não calculam!**

---

## ✅ MÉTODO RECOMENDADO: Google Sheets

### 1️⃣ Importar
- Google Sheets → **Arquivo → Importar**
- Faça upload do CSV
- Tipo de separador: **Vírgula**

### 2️⃣ Editar
- Digite normalmente: `450,00` ou `450.00` (tanto faz!)

### 3️⃣ Baixar (CRÍTICO!)

🔴 **ANTES DE BAIXAR:**

**Arquivo → Configurações → Localidade → Estados Unidos**

✅ Agora sim: **Arquivo → Fazer download → CSV**

🔄 (Opcional) Volte a localidade para Brasil depois

---

## 📊 Se preferir LibreOffice Calc

### Ao abrir:
- UTF-8
- Separador: vírgula

### Ao salvar:
1. **Salvar Como → CSV**
2. Na janela que abre:
   - UTF-8
   - 🔴 **Procure "Separador decimal" e mude para PONTO (.)**
   
**OU** mude a localidade para Inglês antes de salvar

---

## ❌ Excel: NÃO RECOMENDADO

Muito complicado configurar no Brasil.  
Use Google Sheets!

---

## ✅ SEMPRE VERIFIQUE ANTES DE IMPORTAR

Abra o CSV no **Bloco de Notas** e confira:

```
✅ CORRETO:
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn

❌ ERRADO:
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
         ↑ vírgula aqui = ERRO!
```

Viu `450,00`? Salve de novo seguindo as instruções!

---

## 📞 Dúvidas comuns

**P: Posso digitar vírgula ao editar no Google Sheets?**  
R: Sim! O Google Sheets aceita. Só não esqueça de mudar a localidade ANTES de baixar.

**P: O que acontece se eu salvar com vírgula?**  
R: O BonsaiBIM vai ler errado. Os custos ficarão zerados ou incorretos.

**P: Como sei se salvei certo?**  
R: Abra o CSV no Bloco de Notas. Procure pelos números. Devem ter PONTO, não vírgula.

**P: Posso usar Excel?**  
R: Pode, mas é complicado. Google Sheets é muito mais fácil.

---

## 🎯 Checklist para Alunos

Antes de importar no BonsaiBIM, marque:

- [ ] Abri o CSV no Bloco de Notas
- [ ] Encontrei os valores numéricos (ex: 450.00)
- [ ] Confirmei que têm PONTO, não vírgula
- [ ] O arquivo está em UTF-8 (acentos aparecem corretos)
- [ ] Todas as colunas têm vírgula como separador

Se todos ✅, pode importar no BonsaiBIM!

---

*Última atualização: Abril 2026*
