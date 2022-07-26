from app.models import Categoria, Produto

cadeira = Produto("Cadeira", categoria=Categoria("Moveis"))
mouse = Produto("Mouse - Redragon COBRA", categoria=Categoria("Eletrônicos"))
