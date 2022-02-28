import pandas as pd
#LER CSV
olx_bd = pd.read_csv("olx.csv")

#EXTRAINDO INFOMAÇÕES
total_regioes = olx_bd['município'].value_counts()

price_med = olx_bd[['município','preco']].groupby('município').mean()
price_max = olx_bd[['município','preco']].groupby('município').max()
price_min = olx_bd[['município','preco']].groupby('município').min()

tam_med = olx_bd[['município','tamanho']].groupby('município').mean()
tam_max = olx_bd[['município','tamanho']].groupby('município').max()
tam_min = olx_bd[['município','tamanho']].groupby('município').min()

num = int(input("Deseja exportar csv?(0). Deseja mostrar na tela?(1): "))

if (num==0):
	#EXPORTAR 7 CSV
	print("\nForam criados 7 arquivos na pasta")
	total_regioes.to_csv('analise_regioes.csv')

	price_med.to_csv('analise_price_med.csv')
	price_max.to_csv('analise_price_max.csv')
	price_min.to_csv('analise_price_min.csv')

	tam_med.to_csv('analise_tam_med.csv')
	tam_max.to_csv('analise_tam_max.csv')
	tam_min.to_csv('analise_tam_min.csv')
if(num==1):
	#MOSTRAR NA TELA
	print("Quantos anúncios por região:\n",total_regioes)

	print("\n\n================================\n\nPreço médio por região:", price_med)
	print("\n\n================================\n\nPreço máximo por região:", price_max)
	print("\n\n================================\n\nPreço mínimo por região:",price_min)

	print("\n\n================================\n\nTamanho médio por região:\n",tam_med)
	print("\n\n================================\n\nTamanho máximo por região:\n",tam_max)
	print("\n\n================================\n\nTamanho mínimo por região:\n",tam_min)

