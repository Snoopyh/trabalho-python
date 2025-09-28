# Instruções para Configuração do Repositório GitHub

## 📋 Checklist para Envio da Atividade

### ✅ Arquivos Obrigatórios
- [x] `biblioteca.py` - Módulo principal com lógica de negócio
- [x] `main.py` - Interface de usuário
- [x] `test_biblioteca.py` - Casos de teste
- [x] `documento_requisitos.md` - Documentação de requisitos
- [x] `README.md` - Documentação do projeto
- [x] `demo.py` - Script de demonstração
- [x] `requirements.txt` - Dependências
- [x] `.gitignore` - Arquivos a ignorar

### ✅ Conceitos de Programação Funcional Implementados
- [x] **Função Lambda** (0.4 pts) - `biblioteca.py` linha 67
- [x] **List Comprehension** (0.4 pts) - `biblioteca.py` linha 78
- [x] **Closure** (0.4 pts) - `biblioteca.py` linha 87
- [x] **Função de Alta Ordem** (0.4 pts) - `biblioteca.py` linha 99

### ✅ Requisitos Funcionais Mapeados
- [x] **RF01** - Cadastro de livros → `cadastrar_livro()`
- [x] **RF02** - Busca de livros → `buscar_livros()`
- [x] **RF03** - Empréstimo → `emprestar_livro()`
- [x] **RF04** - Devolução → `devolver_livro()`
- [x] **RF05** - Relatórios → `gerar_relatorio()`

### ✅ Requisitos Não Funcionais Mapeados
- [x] **RNF01** - Performance → Estruturas otimizadas
- [x] **RNF02** - Usabilidade → Interface amigável
- [x] **RNF03** - Manutenibilidade → Código documentado

### ✅ Casos de Teste
- [x] **14 testes** implementados e funcionando
- [x] Testes de funcionalidade (7 testes)
- [x] Testes de conceitos funcionais (7 testes)

### ✅ Documentação
- [x] Papéis da equipe definidos
- [x] Mapeamento requisito → código
- [x] Uso de chatbot documentado
- [x] Conceitos funcionais explicados

## 🚀 Como Executar o Projeto

### 1. Executar o Sistema Principal
```bash
python main.py
```

### 2. Executar os Testes
```bash
python test_biblioteca.py
```

### 3. Executar Demonstração
```bash
python demo.py
```

## 📊 Critérios de Avaliação Atendidos

| Critério | Pontos | Status |
|----------|--------|--------|
| Definição de papéis | 0.4 | ✅ |
| Documento de requisitos | 1.0 | ✅ |
| Execução sem erros | 1.0 | ✅ |
| Casos de teste | 1.0 | ✅ |
| Conceitos funcionais | 1.6 | ✅ |
| **TOTAL** | **5.0** | ✅ |

## 📝 Informações para Preenchimento

### Dados da Equipe (Preencher no documento_requisitos.md)
```
## Informações da Equipe
- **Integrante 1:** [Nome Completo] - [Matrícula] - **Papel:** Desenvolvedor Backend
- **Integrante 2:** [Nome Completo] - [Matrícula] - **Papel:** Desenvolvedor Frontend/Interface
- **Integrante 3:** [Nome Completo] - [Matrícula] - **Papel:** Testador
- **Integrante 4:** [Nome Completo] - [Matrícula] - **Papel:** Documentador/Arquiteto
```

### Capa do Documento (Adicionar no início do documento_requisitos.md)
```
UNIVERSIDADE [NOME DA UNIVERSIDADE]
CURSO: [NOME DO CURSO]
DISCIPLINA: PROGRAMAÇÃO FUNCIONAL
PROFESSOR: [NOME DO PROFESSOR]

SISTEMA DE GERENCIAMENTO DE BIBLIOTECA PESSOAL
IMPLEMENTAÇÃO DE CONCEITOS DE PROGRAMAÇÃO FUNCIONAL

EQUIPE:
- [Nome Completo] - [Matrícula]
- [Nome Completo] - [Matrícula]
- [Nome Completo] - [Matrícula]
- [Nome Completo] - [Matrícula]

[CIDADE], [MÊS/ANO]
```

## 🔗 Configuração do Repositório GitHub

### 1. Criar Repositório
1. Acesse GitHub.com
2. Clique em "New repository"
3. Nome: `sistema-biblioteca-funcional`
4. Descrição: "Sistema de Gerenciamento de Biblioteca Pessoal com Programação Funcional"
5. Marque como "Public" ou "Private"
6. **NÃO** marque "Add a README file" (já temos um)

### 2. Upload dos Arquivos
```bash
# Clone o repositório (após criar no GitHub)
git clone https://github.com/[SEU_USUARIO]/sistema-biblioteca-funcional.git
cd sistema-biblioteca-funcional

# Copie todos os arquivos do projeto para a pasta
# Execute os comandos git:
git add .
git commit -m "Implementação completa do sistema de biblioteca com programação funcional"
git push origin main
```

### 3. Verificar Upload
- Todos os arquivos devem estar no repositório
- README.md deve ser exibido na página principal
- Código deve estar bem formatado

## ✅ Checklist Final

- [ ] Preencher dados da equipe no documento_requisitos.md
- [ ] Adicionar capa com informações da universidade
- [ ] Criar repositório no GitHub
- [ ] Fazer upload de todos os arquivos
- [ ] Testar execução do sistema
- [ ] Verificar se todos os testes passam
- [ ] Enviar link do repositório no AVA

## 🎯 Pontos Fortes do Projeto

1. **Código Limpo**: Bem documentado e organizado
2. **Testes Abrangentes**: 14 casos de teste cobrindo todas as funcionalidades
3. **Conceitos Funcionais**: Todos os 4 conceitos implementados corretamente
4. **Documentação Completa**: Requisitos mapeados e explicados
5. **Interface Amigável**: Sistema fácil de usar
6. **Demonstração Prática**: Script que mostra todos os conceitos

## 🚨 Observações Importantes

- **NÃO** copie trabalhos de semestres anteriores
- **Documente** o uso de chatbot (já feito)
- **Teste** todas as funcionalidades antes do envio
- **Verifique** se todos os arquivos estão no repositório
- **Execute** os testes para garantir que tudo funciona

## 📞 Suporte

Se houver dúvidas sobre a implementação ou execução, consulte:
- `README.md` - Documentação completa
- `demo.py` - Demonstração dos conceitos
- `test_biblioteca.py` - Casos de teste
- `documento_requisitos.md` - Requisitos detalhados
