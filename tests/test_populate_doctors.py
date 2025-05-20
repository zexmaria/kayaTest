










for _ in range(total):
    todos_nomes = random.choice([nomes_mulheres, nomes_homens])
    nome = random.choice(todos_nomes)
    nome_count += 1
    if nome in nomes_mulheres and nome_count < 12:
        foto_nome = random.choice(add_fotos_mulheres)
    else:
        foto_nome = random.choice(add_fotos_homens)
    if nome in nomes_homens and nome_count > 12:
        foto_nome = random.choice(add_fotos_homens)
    else:
        foto_nome = random.choice(add_fotos_homens)

    especialidade = random.choice(especialidades)
    crm = ''.join(random.choices('0123456789', k=5))
    visualizacoes = random.randint(1, 75)

    foto_caminho = os.path.join(img_folder, foto_nome)