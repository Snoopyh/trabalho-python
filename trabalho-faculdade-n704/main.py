"""
Interface principal do Sistema de Gerenciamento de Biblioteca Pessoal
Demonstra uso de conceitos de programação funcional
"""

from biblioteca import Biblioteca, criar_funcao_desconto, processar_livros_funcional, calcular_estatisticas_livros
from datetime import datetime


def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("    SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("="*50)
    print("1. Cadastrar livro")
    print("2. Buscar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Gerar relatório")
    print("6. Demonstrar conceitos funcionais")
    print("7. Salvar dados")
    print("8. Carregar dados")
    print("0. Sair")
    print("="*50)


def cadastrar_livro_interativo(biblioteca: Biblioteca):
    """Interface para cadastrar livro"""
    print("\n--- CADASTRAR LIVRO ---")
    
    titulo = input("Título do livro: ").strip()
    autor = input("Autor: ").strip()
    
    try:
        ano = int(input("Ano de publicação: "))
    except ValueError:
        print("Ano inválido!")
        return
    
    categoria = input("Categoria: ").strip()
    
    if not all([titulo, autor, categoria]):
        print("Todos os campos são obrigatórios!")
        return
    
    livro = biblioteca.cadastrar_livro(titulo, autor, ano, categoria)
    print(f"\n✅ Livro cadastrado com sucesso!")
    print(f"ID: {livro['id']}")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")


def buscar_livros_interativo(biblioteca: Biblioteca):
    """Interface para buscar livros"""
    print("\n--- BUSCAR LIVROS ---")
    print("1. Por título")
    print("2. Por autor")
    print("3. Por categoria")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        criterio = "titulo"
    elif opcao == "2":
        criterio = "autor"
    elif opcao == "3":
        criterio = "categoria"
    else:
        print("Opção inválida!")
        return
    
    valor = input(f"Digite o {criterio}: ").strip()
    
    if not valor:
        print("Valor não pode estar vazio!")
        return
    
    livros = biblioteca.buscar_livros(criterio, valor)
    
    if not livros:
        print("Nenhum livro encontrado!")
    else:
        print(f"\n📚 {len(livros)} livro(s) encontrado(s):")
        for livro in livros:
            status = "✅ Disponível" if livro['disponivel'] else "❌ Emprestado"
            print(f"  {livro['id']}. {livro['titulo']} - {livro['autor']} ({livro['ano']}) - {status}")


def emprestar_livro_interativo(biblioteca: Biblioteca):
    """Interface para emprestar livro"""
    print("\n--- EMPRESTAR LIVRO ---")
    
    try:
        livro_id = int(input("ID do livro: "))
    except ValueError:
        print("ID inválido!")
        return
    
    pessoa = input("Nome da pessoa: ").strip()
    
    if not pessoa:
        print("Nome é obrigatório!")
        return
    
    try:
        emprestimo = biblioteca.emprestar_livro(livro_id, pessoa)
        print(f"\n✅ Empréstimo realizado com sucesso!")
        print(f"ID do empréstimo: {emprestimo['id']}")
        print(f"Data de vencimento: {emprestimo['data_vencimento']}")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def devolver_livro_interativo(biblioteca: Biblioteca):
    """Interface para devolver livro"""
    print("\n--- DEVOLVER LIVRO ---")
    
    try:
        emprestimo_id = int(input("ID do empréstimo: "))
    except ValueError:
        print("ID inválido!")
        return
    
    try:
        devolucao = biblioteca.devolver_livro(emprestimo_id)
        print(f"\n✅ Devolução realizada com sucesso!")
        if devolucao['multa'] > 0:
            print(f"💰 Multa por atraso: R$ {devolucao['multa']:.2f}")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def gerar_relatorio_interativo(biblioteca: Biblioteca):
    """Interface para gerar relatório"""
    print("\n--- RELATÓRIO DA BIBLIOTECA ---")
    
    relatorio = biblioteca.gerar_relatorio()
    
    print(f"\n📊 ESTATÍSTICAS GERAIS:")
    print(f"  Total de livros: {relatorio['total_livros']}")
    print(f"  Livros disponíveis: {relatorio['livros_disponiveis']}")
    print(f"  Livros emprestados: {relatorio['livros_emprestados']}")
    print(f"  Empréstimos em atraso: {relatorio['emprestimos_em_atraso']}")
    
    print(f"\n📚 LIVROS POR CATEGORIA:")
    for categoria, titulos in relatorio['livros_por_categoria'].items():
        print(f"  {categoria}: {len(titulos)} livro(s)")
        for titulo in titulos:
            print(f"    - {titulo}")


def demonstrar_conceitos_funcionais(biblioteca: Biblioteca):
    """Demonstra os conceitos de programação funcional"""
    print("\n--- DEMONSTRAÇÃO DE CONCEITOS FUNCIONAIS ---")
    
    if not biblioteca.livros:
        print("Cadastre alguns livros primeiro para ver a demonstração!")
        return
    
    # 1. Demonstração de List Comprehension
    print("\n1️⃣ LIST COMPREHENSION:")
    print("Extraindo títulos de todos os livros:")
    titulos = biblioteca.obter_titulos_livros(biblioteca.livros)
    for i, titulo in enumerate(titulos, 1):
        print(f"  {i}. {titulo}")
    
    # 2. Demonstração de Lambda
    print("\n2️⃣ FUNÇÃO LAMBDA:")
    print("Filtrando livros por categoria 'Ficção':")
    livros_ficcao = biblioteca.filtrar_livros_por_categoria('Ficção')
    if livros_ficcao:
        for livro in livros_ficcao:
            print(f"  - {livro['titulo']} ({livro['autor']})")
    else:
        print("  Nenhum livro de ficção encontrado")
    
    # 3. Demonstração de Closure
    print("\n3️⃣ CLOSURE:")
    print("Criando contador de empréstimos:")
    contador = biblioteca.criar_contador_emprestimos()
    print(f"  Empréstimo #{contador()}")
    print(f"  Empréstimo #{contador()}")
    print(f"  Empréstimo #{contador()}")
    
    # 4. Demonstração de Função de Alta Ordem
    print("\n4️⃣ FUNÇÃO DE ALTA ORDEM:")
    print("Aplicando desconto de 20% aos livros:")
    
    # Cria função de desconto usando closure
    funcao_desconto = criar_funcao_desconto(0.2)
    
    # Adiciona preço fictício aos livros para demonstração
    livros_com_preco = []
    for livro in biblioteca.livros[:3]:  # Pega apenas os 3 primeiros
        livro_com_preco = livro.copy()
        livro_com_preco['preco'] = 50.0  # Preço fictício
        livros_com_preco.append(livro_com_preco)
    
    livros_com_desconto = biblioteca.aplicar_desconto_livros(livros_com_preco, funcao_desconto)
    
    for livro in livros_com_desconto:
        print(f"  {livro['titulo']}: R$ {livro['preco']:.2f}")
    
    # 5. Demonstração de processamento funcional
    print("\n5️⃣ PROCESSAMENTO FUNCIONAL:")
    print("Livros publicados após 2000:")
    
    # Filtro para livros após 2000
    filtro_ano = lambda livro: livro['ano'] > 2000
    
    # Transformação para mostrar título e ano
    transformacao = lambda livro: f"{livro['titulo']} ({livro['ano']})"
    
    livros_filtrados = processar_livros_funcional(biblioteca.livros, filtro_ano, transformacao)
    
    if livros_filtrados:
        for livro in livros_filtrados:
            print(f"  - {livro}")
    else:
        print("  Nenhum livro encontrado")
    
    # 6. Demonstração de estatísticas funcionais
    print("\n6️⃣ ESTATÍSTICAS FUNCIONAIS:")
    stats = calcular_estatisticas_livros(biblioteca.livros)
    print(f"  Total de livros: {stats['total']}")
    print(f"  Média de ano de publicação: {stats['media_ano']:.1f}")
    print(f"  Categorias únicas: {stats['categorias_unicas']}")
    print(f"  Livro mais antigo: {stats['ano_mais_antigo']}")
    print(f"  Livro mais recente: {stats['ano_mais_recente']}")


def main():
    """Função principal do programa"""
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca Pessoal!")
    print("Este sistema demonstra conceitos de programação funcional em Python.")
    
    biblioteca = Biblioteca()
    
    # Tenta carregar dados existentes
    biblioteca.carregar_dados()
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "0":
                print("\n👋 Obrigado por usar o sistema!")
                biblioteca.salvar_dados()
                break
            elif opcao == "1":
                cadastrar_livro_interativo(biblioteca)
            elif opcao == "2":
                buscar_livros_interativo(biblioteca)
            elif opcao == "3":
                emprestar_livro_interativo(biblioteca)
            elif opcao == "4":
                devolver_livro_interativo(biblioteca)
            elif opcao == "5":
                gerar_relatorio_interativo(biblioteca)
            elif opcao == "6":
                demonstrar_conceitos_funcionais(biblioteca)
            elif opcao == "7":
                biblioteca.salvar_dados()
                print("✅ Dados salvos com sucesso!")
            elif opcao == "8":
                biblioteca.carregar_dados()
                print("✅ Dados carregados com sucesso!")
            else:
                print("❌ Opção inválida!")
            
            input("\nPressione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            biblioteca.salvar_dados()
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
