nome = input("Digite o nome do personagem: ");
artista = str(input("Digite o nome do artista: "));
historia = input("Digite a história do personagem: ");
print("");
print("Categorias disponíveis: Animação, Música, Pintura, Escultura, Fotografia");
categoria = input("Digite a categoria da arte: ");

codigo = 0
codigo = codigo + 1

arteTEMPLATE = {
	"id": [codigo],
	"nome": [nome],
	"artista": [artista],
	"historia": [historia],
	"categoria": [categoria],
	};

print("Personagem cadastrado com sucesso!")

#Falta um print para mostrar o dicionário completo.



# CREATE - Criar um personagem
def criar_personagem(nome, artista, historia, categoria):
	personagem = {
		"id": len(personagens) + 1,
		"nome": nome,
		"artista": artista,
		"historia": historia,
		"categoria": categoria,
	}
	personagens.append(personagem)
	print("Personagem cadastrado com sucesso!")


# READ - Visualizar personagens
def visualizar_personagens():
	print("\n=== PERSONAGENS CADASTRADOS ===")
	if not personagens:
		print("Nenhum personagem cadastrado.")
		return

	for personagem in personagens:
		print("----------------------------")
		print("ID:", personagem["id"])
		print("Nome:", personagem["nome"])
		print("Artista:", personagem["artista"])
		print("História:", personagem["historia"])
		print("Categoria:", personagem["categoria"])


# UPDATE - Atualizar um personagem
def atualizar_personagem(id, novo_nome, nova_historia):
	for personagem in personagens:
		if personagem["id"] == id:
			personagem["nome"] = novo_nome
			personagem["historia"] = nova_historia
			print("Personagem atualizado com sucesso!")
			return

	print("Personagem não encontrado.")


# DELETE - Excluir um personagem
def excluir_personagem(id):
	for personagem in personagens:
		if personagem["id"] == id:
			personagens.remove(personagem)
			print("Personagem excluído com sucesso!")
			return

	print("Personagem não encontrado.")


# Demonstração das quatro operações
criar_personagem(
	"Shadow",
	"Artista01",
	"Um guerreiro que protege seu mundo.",
	"Animação",
)

criar_personagem(
	"Luna",
	"Artista02",
	"Uma musicista que controla a luz.",
	"Música",
)

visualizar_personagens()

atualizar_personagem(
	1,
	"Shadow Knight",
	"Um guerreiro que protege diferentes dimensões.",
)

visualizar_personagens()
