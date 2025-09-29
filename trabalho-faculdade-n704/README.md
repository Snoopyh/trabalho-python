# Sistema de Gerenciamento de Biblioteca Pessoal

## Informações da Equipe
- **Integrante 1:** DAYANE DO NASCIMENTO PAULINO - 2326944- **Papel:** Documentador/Arquiteto
- **Integrante 2:** ISMAEL GUSTAVO DA SILVA - 2326204 - **Papel:** Desenvolvedor Backend
- **Integrante 3:** PAULO JONATHAN RIBEIRO LUZ - 2323859 - **Papel:** Tester
- **Integrante 4:** STAYNER RODRIGUES DE LIMA - 2326190 - **Papel:** Tester
- **Integrante 5:** MATHEUS FERREIRA SILVA ROCHA - 2326202 - **Papel:** Desenvolvedor Interface

### Capa do Documento 
```
Fundação Edson Queiroz - Universidade de Fortaleza
CURSO: ANALISE E DESENVOLVIMENTO DE SISTEMAS
DISCIPLINA: N704-Programação funcional
PROFESSOR: Bruno Lopes Alcantara

SISTEMA DE GERENCIAMENTO DE BIBLIOTECA PESSOAL
IMPLEMENTAÇÃO DE CONCEITOS DE PROGRAMAÇÃO FUNCIONAL


## 📚 Sobre o Projeto

Este projeto implementa um sistema de gerenciamento de biblioteca pessoal utilizando **conceitos de programação funcional** em Python. O sistema demonstra o uso de:

- **Funções Lambda**
- **List Comprehensions** 
- **Closures**
- **Funções de Alta Ordem**

## 🚀 Funcionalidades

### Requisitos Funcionais
- ✅ **RF01**: Cadastro de livros com informações completas
- ✅ **RF02**: Busca de livros por título, autor ou categoria
- ✅ **RF03**: Sistema de empréstimo de livros
- ✅ **RF04**: Sistema de devolução com cálculo de multa
- ✅ **RF05**: Geração de relatórios estatísticos

### Requisitos Não Funcionais
- ✅ **RNF01**: Performance otimizada com estruturas de dados eficientes
- ✅ **RNF02**: Interface intuitiva e amigável
- ✅ **RNF03**: Código bem documentado e modular

## 🛠️ Conceitos de Programação Funcional Implementados

### 1. Função Lambda 
**Localização**: `biblioteca.py` - método `filtrar_livros_por_categoria()`
```python
# Filtra livros por categoria usando lambda
return list(filter(lambda livro: livro['categoria'] == categoria, self.livros))
```

### 2. List Comprehension
**Localização**: `biblioteca.py` - método `obter_titulos_livros()`
```python

return [livro['titulo'] for livro in livros]
```

### 3. Closure 
**Localização**: `biblioteca.py` - método `criar_contador_emprestimos()`
```python
def criar_contador_emprestimos(self) -> Callable[[], int]:
    contador = 0  
    
    def incrementar_contador():  
        nonlocal contador
        contador += 1
        return contador
    
    return incrementar_contador  
```

### 4. Função de Alta Ordem 
**Localização**: `biblioteca.py` - método `aplicar_desconto_livros()`
```python
def aplicar_desconto_livros(self, livros: List[Dict[str, Any]], 
                           funcao_desconto: Callable[[Dict[str, Any]], Dict[str, Any]]) -> List[Dict[str, Any]]:
   
    return list(map(funcao_desconto, livros))
```

## 📁 Estrutura do Projeto

```
sbobis/
├── biblioteca.py          # Módulo principal com lógica de negócio
├── main.py               # Interface de usuário
├── test_biblioteca.py    # Casos de teste abrangentes
├── documento_requisitos.md  # Documentação de requisitos
└── README.md             # Este arquivo
```

## 🧪 Casos de Teste

O sistema inclui **12 casos de teste** abrangentes que verificam:

- ✅ Cadastro e busca de livros
- ✅ Sistema de empréstimo e devolução
- ✅ Geração de relatórios
- ✅ Todos os conceitos de programação funcional
- ✅ Tratamento de erros e casos limite

**Executar testes:**
```bash
python test_biblioteca.py
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior

### Execução
```bash
# Executar o sistema principal
python main.py

# Executar apenas os testes
python test_biblioteca.py
```

## 📋 Menu do Sistema

```
==================================================
    SISTEMA DE GERENCIAMENTO DE BIBLIOTECA
==================================================
1. Cadastrar livro
2. Buscar livros
3. Emprestar livro
4. Devolver livro
5. Gerar relatório
6. Demonstrar conceitos funcionais
7. Salvar dados
8. Carregar dados
0. Sair
```

## 🔍 Demonstração dos Conceitos Funcionais

O sistema inclui uma opção especial (menu item 6) que demonstra todos os conceitos de programação funcional:

1. **List Comprehension**: Extrai títulos de todos os livros
2. **Função Lambda**: Filtra livros por categoria específica
3. **Closure**: Cria contador independente de empréstimos
4. **Função de Alta Ordem**: Aplica desconto usando função como parâmetro
5. **Processamento Funcional**: Filtra e transforma dados
6. **Estatísticas Funcionais**: Calcula métricas usando programação funcional

## 📊 Mapeamento de Requisitos

| Requisito | Função | Arquivo | Status |
|-----------|--------|---------|--------|
| RF01 | `cadastrar_livro()` | `biblioteca.py` | ✅ |
| RF02 | `buscar_livros()` | `biblioteca.py` | ✅ |
| RF03 | `emprestar_livro()` | `biblioteca.py` | ✅ |
| RF04 | `devolver_livro()` | `biblioteca.py` | ✅ |
| RF05 | `gerar_relatorio()` | `biblioteca.py` | ✅ |
| RNF01 | Estruturas otimizadas | `biblioteca.py` | ✅ |
| RNF02 | Interface amigável | `main.py` | ✅ |
| RNF03 | Código documentado | Todos | ✅ |

## 👥 Papéis da Equipe

- **Desenvolvedor Backend**: Implementação da lógica de negócio
- **Desenvolvedor Frontend**: Interface de usuário e experiência
- **Testador**: Criação e execução de casos de teste
- **Documentador/Arquiteto**: Documentação e arquitetura do sistema


## 🔧 Tecnologias Utilizadas

- **Python 3.7+**
- **Programação Funcional**
- **Testes Unitários (unittest)**
- **JSON para persistência**
- **Type Hints para documentação**

## USO DE IA 
CLOUND para auxilio e formatação de documentação.

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte de uma atividade de programação funcional.
