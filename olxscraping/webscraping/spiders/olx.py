import scrapy

class OlxSpider(scrapy.Spider):
    name = 'olx'
    
    #PÁGINA PRINCIPAL DOS TERRENOS
    def start_requests(self):
        yield scrapy.Request(("https://sc.olx.com.br/florianopolis-e-regiao/imoveis/terrenos/"), callback=self.parse_category)
        #yield scrapy.Request(("https://sc.olx.com.br/florianopolis-e-regiao/imoveis/terrenos/"), callback=self.parse_category, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
	#CAPTURAR TODOS OS LINKS DE ANÚNCIOS DA 1ª PÁGINA
    def parse_category(self, response):
        news = response.xpath('//div//ul[@class="sc-1fcmfeb-1 kntIvV"]//@href').getall()
        for new_url in news:
            yield scrapy.Request(response.urljoin(new_url), callback=self.parse)
            
	#PASSAR PARA PRÓXIMA PÁGINA
        page = response.xpath('//div[@class="sc-hmzhuo kJjuHR sc-jTzLTM iwtnNi"]//@href').get()
        yield scrapy.Request((page),callback=self.parse_category)
        
	#OBTER DADOS DE CADA ANÚNCIO
    def parse(self, response):
        
        if (response.xpath('//div[@class="h3us20-6 jUPCvE"]//h2[@class="sc-ifAKCX eQLrcK"]//text()').get()) != 0:
           price = response.xpath('//div[@class="h3us20-6 jUPCvE"]//h2[@class="sc-ifAKCX eQLrcK"]//text()').get()
        else: price = None
        texto = ' '.join(response.xpath('//div[@class="h3us20-6 jtENip"]//text()').getall())
        categoria = response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Categoria")]//following::text()').get()
        tipo = response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Tipo")]//following::text()').get()
        if((response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Condomínio")]//following::text()').get()) != None):
            condominio = (response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Condomínio")]//following::text()').get()).replace('R$ ','')
        else: condominio = response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Condomínio")]//following::text()').get()
        if((response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "IPTU")]//following::text()').get())!= None):
            iptu = (response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "IPTU")]//following::text()').get()).replace('R$ ','')
        else: iptu = response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "IPTU")]//following::text()').get()
        if ((response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Tamanho")]//following::text()').get()) != None) :
	        tamanho = (response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Tamanho")]//following::text()').get()).replace('m²','')
        else: tamanho = response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Tamanho")]//following::text()').get()
        if ((response.xpath('//div[@class="h3us20-6 bcHOOp"]//div//dt[contains(string(), "Tamanho")]//following::text()').get()) == 0 ):
            tamanho = None
        cep = response.xpath('//div[@class="h3us20-6 fiikIi"]//div//dt[contains(string(), "CEP")]//following::text()').get()
        municipio = response.xpath('//div[@class="h3us20-6 fiikIi"]//div//dt[contains(string(), "Município")]//following::text()').get()
        bairro = response.xpath('//div[@class="h3us20-6 fiikIi"]//div//dt[contains(string(), "Bairro")]//following::text()').get()
        logradouro = response.xpath('//div[@class="h3us20-6 fiikIi"]//div//dt[contains(string(), "Logradouro")]//following::text()').get()
        
        titulo = response.xpath('//div//h1[@class="sc-45jt43-0 eCghYu sc-ifAKCX cmFKIN"]//text()').get()
        #anunciante = (response.xpath('//script[contains(string(), "sellerName")]//text()').getall()).split('"')

        
        
        #TRANSFORMAR DADOS EM DICIONÁRIO 
        yield {
            
            'preco': price,
            'descrição': texto,
            'url': response.url,
            
            'categoria': categoria,
            'tipo': tipo,
            'condomínio': condominio,
            'iptu': iptu,
            'tamanho': tamanho,
            
            'cep': cep,
            'município': municipio,
            'bairro': bairro,
            'logradouro': logradouro,
            'título': titulo,
            #'anunciante': anunciante,
            
			}
			
        
