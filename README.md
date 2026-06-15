# Projeto de capacitação interna Lasi
## Atividade 1: Calculadora multifuncional

**Autor:** Rafael Santos

---

## Funcionalidades do Código

O programa oferece um menu iterativo de terminal com 7 opções de controle. Suas principais características técnicas e operacionais incluem:

### 1. Operações Aritméticas Básicas
* **Soma (`+`)**, **Subtração (`-`)**, **Multiplicação (`*`)** e **Divisão (`/`)**.

### 2. Módulo de Física
* **Cálculo do Alcance de um Projétil:** Determina a distância horizontal máxima percorrida por um projétil lançado obliquamente. O código utiliza a fórmula matemática da distancia horizontal percorrida por um projétil em função da velocidade inicial e do ângulo:
    $$R = \frac{V^2 \cdot \sin(2\theta)}{g}$$
    * Faz a conversão automática do ângulo de graus para radianos utilizando a biblioteca nativa `math`.
    * Adota o valor padrão de gravidade como $9.8 m/s^2$.

### 3. Módulo de Álgebra Linear
* **Cálculo de Determinante de Matrizes:** Capaz de calcular o determinante de uma matriz quadrada de qualquer ordem informada pelo usuário (2x2, 3x3, 4x4, etc.).
    * A solução foi implementada utilizando o conceito de **Teorema de Laplace**, de forma recursiva, utilizando funções auxiliares para fatiamento de submatrizes.

### 4. Tratamento de Erros e Validação (Robustez)
* **Função de Verificação (`verificar`):** Bloco estruturado com `try/except` que impede o encerramento do programa caso o usuário digite um caractere inválido (letras ou símbolos), forçando a entrada correta e garantindo que o programa continue rodando sem quebras repentinas.

---

## 🛠️ Detalhes Importantes do Código

* **Linguagem:** Python
* **Biblioteca Utilizada:** `math`.
* **Interface:** Menu em loop (`while True`) acionado via entrada de texto (`input`).

---

## 🎯 Possíveis Aplicações

Esta ferramenta pode ser aplicada em diversos cenários práticos e acadêmicos, tais como:

1.  **Ambiente Educacional:** Auxílio a estudantes de física e matemática na verificação rápida de exercícios de lançamento oblíquo e propriedades matriciais.
2.  **Laboratórios de Geometria Analítica:** Agilização de cálculos de determinantes para encontrar volumes de paralelepípedos ou dependência linear de vetores.

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python calculadora_lasi.py
