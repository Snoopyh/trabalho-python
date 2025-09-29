
from biblioteca import Biblioteca, criar_funcao_desconto, processar_livros_funcional, calcular_estatisticas_livros


def demonstrar_conceitos_funcionais():
    print("🚀 DEMONSTRAÇÃO DOS CONCEITOS DE PROGRAMAÇÃO FUNCIONAL")
    print("="*60)
    
  
    biblioteca = Biblioteca()
    
    print("\n📚 Cadastrando livros de exemplo...")
    biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")
    biblioteca.cadastrar_livro("1984", "George Orwell", 1949, "Ficção Científica")
    biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899, "Literatura Brasileira")
    biblioteca.cadastrar_livro("Duna", "Frank Herbert", 1965, "Ficção Científica")
    biblioteca.cadastrar_livro("Harry Potter", "J.K. Rowling", 1997, "Fantasia")
    
    print("✅ 5 livros cadastrados com sucesso!")
    
    
    print("\n" + "="*60)
    print("1️⃣ LIST COMPREHENSION - Extraindo títulos")
    print("="*60)
    
    titulos = biblioteca.obter_titulos_livros(biblioteca.livros)
    print("Títulos dos livros:")
    for i, titulo in enumerate(titulos, 1):
        print(f"  {i}. {titulo}")
    
   
    print("\n" + "="*60)
    print("2️⃣ FUNÇÃO LAMBDA - Filtrando por categoria")
    print("="*60)
    
    print("Livros de Fantasia:")
    livros_fantasia = biblioteca.filtrar_livros_por_categoria("Fantasia")
    for livro in livros_fantasia:
        print(f"  - {livro['titulo']} ({livro['autor']})")
    
    print("\nLivros de Ficção Científica:")
    livros_ficcao = biblioteca.filtrar_livros_por_categoria("Ficção Científica")
    for livro in livros_ficcao:
        print(f"  - {livro['titulo']} ({livro['autor']})")
    
    
    print("\n" + "="*60)
    print("3️⃣ CLOSURE - Contador de empréstimos")
    print("="*60)
    
    contador = biblioteca.criar_contador_emprestimos()
    print("Simulando empréstimos:")
    for i in range(3):
        print(f"  Empréstimo #{contador()}")
    
    
    contador2 = biblioteca.criar_contador_emprestimos()
    print(f"\nNovo contador independente: #{contador2()}")
    
   
    print("\n" + "="*60)
    print("4️⃣ FUNÇÃO DE ALTA ORDEM - Aplicando desconto")
    print("="*60)
    

    livros_com_preco = []
    for livro in biblioteca.livros[:3]:
        livro_com_preco = livro.copy()
        livro_com_preco['preco'] = 50.0
        livros_com_preco.append(livro_com_preco)
    
    print("Preços originais:")
    for livro in livros_com_preco:
        print(f"  {livro['titulo']}: R$ {livro['preco']:.2f}")
    
    
    funcao_desconto = criar_funcao_desconto(0.2)
    
    
    livros_com_desconto = biblioteca.aplicar_desconto_livros(livros_com_preco, funcao_desconto)
    
    print("\nPreços com desconto de 20%:")
    for livro in livros_com_desconto:
        print(f"  {livro['titulo']}: R$ {livro['preco']:.2f}")
    
  
    print("\n" + "="*60)
    print("5️⃣ PROCESSAMENTO FUNCIONAL - Filtrando e transformando")
    print("="*60)
    
   
    filtro_ano = lambda livro: livro['ano'] > 1950
    
   
    transformacao = lambda livro: f"{livro['titulo']} ({livro['ano']})"
    
    print("Livros publicados após 1950:")
    livros_filtrados = processar_livros_funcional(biblioteca.livros, filtro_ano, transformacao)
    for livro in livros_filtrados:
        print(f"  - {livro}")
    
    
    print("\n" + "="*60)
    print("6️⃣ ESTATÍSTICAS FUNCIONAIS - Cálculos usando programação funcional")
    print("="*60)
    
    stats = calcular_estatisticas_livros(biblioteca.livros)
    print("Estatísticas da biblioteca:")
    print(f"  📊 Total de livros: {stats['total']}")
    print(f"  📅 Média de ano de publicação: {stats['media_ano']:.1f}")
    print(f"  📚 Categorias únicas: {stats['categorias_unicas']}")
    print(f"  📖 Livro mais antigo: {stats['ano_mais_antigo']}")
    print(f"  📖 Livro mais recente: {stats['ano_mais_recente']}")
    
   
    print("\n" + "="*60)
    print("7️⃣ SISTEMA DE EMPRÉSTIMO - Funcionalidade completa")
    print("="*60)
    
   
    emprestimo1 = biblioteca.emprestar_livro(1, "João Silva")
    emprestimo2 = biblioteca.emprestar_livro(2, "Maria Santos")
    
    print("Empréstimos realizados:")
    print(f"  - {emprestimo1['pessoa']} pegou emprestado o livro ID {emprestimo1['livro_id']}")
    print(f"  - {emprestimo2['pessoa']} pegou emprestado o livro ID {emprestimo2['livro_id']}")
    
  
    relatorio = biblioteca.gerar_relatorio()
    print(f"\n📊 Relatório da biblioteca:")
    print(f"  Total de livros: {relatorio['total_livros']}")
    print(f"  Livros disponíveis: {relatorio['livros_disponiveis']}")
    print(f"  Livros emprestados: {relatorio['livros_emprestados']}")
    
    print("\n🎉 DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("Todos os conceitos de programação funcional foram demonstrados:")
    print("✅ List Comprehension")
    print("✅ Função Lambda")
    print("✅ Closure")
    print("✅ Função de Alta Ordem")
    print("✅ Processamento Funcional")
    print("✅ Estatísticas Funcionais")


if __name__ == "__main__":
    demonstrar_conceitos_funcionais()
