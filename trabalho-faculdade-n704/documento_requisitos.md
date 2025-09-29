# Documento de Requisitos - Sistema de Gerenciamento de Biblioteca Pessoal

## Informações da Equipe
- **Integrante 1:** DAYANE DO NASCIMENTO PAULINO - 2326944- **Papel:** Documentador/Arquiteto
- **Integrante 2:** ISMAEL GUSTAVO DA SILVA - 2326204 - **Papel:** Desenvolvedor Backend
- **Integrante 3:** PAULO JONATHAN RIBEIRO LUZ - 2323859 - **Papel:** Tester
- **Integrante 4:** STAYNER RODRIGUES DE LIMA - 2326190 - **Papel:** Tester
- **Integrante 5:** MATHEUS FERREIRA SILVA ROCHA - 2326202 - **Papel:** Desenvolvedor Interface

## Requisitos Funcionais

### RF01 - Cadastro de Livros
- **Descrição:** O sistema deve permitir cadastrar novos livros com informações básicas
- **Implementação:** Função `cadastrar_livro()` no módulo `biblioteca.py`
- **Critérios de Aceitação:** Livro deve ter título, autor, ano de publicação e categoria

### RF02 - Busca de Livros
- **Descrição:** O sistema deve permitir buscar livros por diferentes critérios
- **Implementação:** Função `buscar_livros()` no módulo `biblioteca.py`
- **Critérios de Aceitação:** Busca por título, autor ou categoria

### RF03 - Empréstimo de Livros
- **Descrição:** O sistema deve permitir registrar empréstimos de livros
- **Implementação:** Função `emprestar_livro()` no módulo `biblioteca.py`
- **Critérios de Aceitação:** Deve registrar data de empréstimo e pessoa responsável

### RF04 - Devolução de Livros
- **Descrição:** O sistema deve permitir registrar devoluções de livros
- **Implementação:** Função `devolver_livro()` no módulo `biblioteca.py`
- **Critérios de Aceitação:** Deve registrar data de devolução e calcular multa se houver atraso

### RF05 - Relatórios
- **Descrição:** O sistema deve gerar relatórios sobre o acervo
- **Implementação:** Função `gerar_relatorio()` no módulo `biblioteca.py`
- **Critérios de Aceitação:** Relatório de livros disponíveis, emprestados e por categoria

## Requisitos Não Funcionais

### RNF01 - Performance
- **Descrição:** O sistema deve responder a consultas em menos de 1 segundo
- **Implementação:** Uso de estruturas de dados eficientes e algoritmos otimizados

### RNF02 - Usabilidade
- **Descrição:** Interface deve ser intuitiva e fácil de usar
- **Implementação:** Menu interativo claro e mensagens de erro descritivas

### RNF03 - Manutenibilidade
- **Descrição:** Código deve ser bem documentado e modular
- **Implementação:** Funções pequenas e bem documentadas, separação de responsabilidades

## Conceitos de Programação Funcional Utilizados

### 1. Função Lambda
- **Localização:** Função `filtrar_livros_por_categoria()` em `biblioteca.py`
- **Implementação:** Uso de lambda para filtrar livros por categoria específica
- **Código:** `lambda livro: livro['categoria'] == categoria`

### 2. List Comprehension
- **Localização:** Função `obter_titulos_livros()` em `biblioteca.py`
- **Implementação:** List comprehension para extrair títulos de todos os livros
- **Código:** `[livro['titulo'] for livro in livros]`

### 3. Closure
- **Localização:** Função `criar_contador_emprestimos()` em `biblioteca.py`
- **Implementação:** Closure que mantém estado interno para contar empréstimos
- **Código:** Função interna que acessa variável do escopo externo

### 4. Função de Alta Ordem
- **Localização:** Função `aplicar_desconto_livros()` em `biblioteca.py`
- **Implementação:** Função que recebe outra função como parâmetro
- **Código:** Aplica função de desconto a lista de livros usando `map()`

## Mapeamento de Requisitos para Código

| Requisito | Função | Arquivo |
|-----------|--------|---------|
| RF01 | `cadastrar_livro()` | `biblioteca.py` |
| RF02 | `buscar_livros()` | `biblioteca.py` |
| RF03 | `emprestar_livro()` | `biblioteca.py` |
| RF04 | `devolver_livro()` | `biblioteca.py` |
| RF05 | `gerar_relatorio()` | `biblioteca.py` |
| RNF01 | Estruturas de dados otimizadas | `biblioteca.py` |
| RNF02 | Interface de usuário | `main.py` |
| RNF03 | Documentação e modularização | Todos os arquivos |

## Uso de Chatbot
- **Ferramenta utilizada:** Claude (Anthropic)
- **Finalidade:** Auxílio na estruturação do projeto e implementação dos conceitos de programação funcional
- **Respostas utilizadas:** 
  - Sugestões de arquitetura modular para o sistema
  - Implementação de closures para contadores de estado
  - Criação de funções de alta ordem para processamento de dados
  - Desenvolvimento de casos de teste abrangentes
  - Documentação técnica detalhada dos conceitos funcionais

## Demonstração dos Conceitos Funcionais no Código

### 1. Função Lambda - Filtro por Categoria
**Arquivo:** `biblioteca.py` - linha 67
```python
def filtrar_livros_por_categoria(self, categoria: str) -> List[Dict[str, Any]]:
    # CONCEITO FUNCIONAL: Função Lambda
    return list(filter(lambda livro: livro['categoria'] == categoria, self.livros))
```

### 2. List Comprehension - Extração de Títulos
**Arquivo:** `biblioteca.py` - linha 78
```python
def obter_titulos_livros(self, livros: List[Dict[str, Any]]) -> List[str]:
    # CONCEITO FUNCIONAL: List Comprehension
    return [livro['titulo'] for livro in livros]
```

### 3. Closure - Contador de Empréstimos
**Arquivo:** `biblioteca.py` - linha 87
```python
def criar_contador_emprestimos(self) -> Callable[[], int]:
    # CONCEITO FUNCIONAL: Closure
    contador = 0
    
    def incrementar_contador():
        nonlocal contador
        contador += 1
        return contador
    
    return incrementar_contador
```

### 4. Função de Alta Ordem - Aplicação de Desconto
**Arquivo:** `biblioteca.py` - linha 99
```python
def aplicar_desconto_livros(self, livros: List[Dict[str, Any]], 
                           funcao_desconto: Callable[[Dict[str, Any]], Dict[str, Any]]) -> List[Dict[str, Any]]:
    # CONCEITO FUNCIONAL: Função de Alta Ordem
    return list(map(funcao_desconto, livros))
```

## Casos de Teste Implementados

### Testes de Funcionalidade
1. **test_cadastrar_livro()** - Verifica cadastro correto de livros
2. **test_buscar_livros_por_titulo()** - Testa busca por título
3. **test_buscar_livros_por_autor()** - Testa busca por autor
4. **test_buscar_livros_por_categoria()** - Testa busca por categoria
5. **test_emprestar_livro()** - Verifica sistema de empréstimo
6. **test_devolver_livro()** - Verifica sistema de devolução
7. **test_gerar_relatorio()** - Testa geração de relatórios

### Testes de Conceitos Funcionais
8. **test_funcao_lambda()** - Verifica uso correto de lambda
9. **test_list_comprehension()** - Verifica list comprehension
10. **test_closure()** - Verifica funcionamento de closure
11. **test_funcao_alta_ordem()** - Verifica função de alta ordem
12. **test_processamento_funcional()** - Testa processamento funcional
13. **test_estatisticas_funcionais()** - Verifica cálculos funcionais
14. **test_casos_limite()** - Testa tratamento de erros

**Total de Testes:** 14 casos de teste abrangentes
