from django.test import TestCase
from numpy import product
from .models import Product, Category, Marca, Size

# Create your tests here.


class TestAccounts(TestCase):
    def setUp(self):
        self.categories = [Category.objects.create(name=f'Category {i}') for i in range(1, 4)]
        self.marcas = [Marca.objects.create(name=f'Marca {i}') for i in range(1, 4)]
        self.sizes = [Size.objects.create(name=f'Size {i}') for i in range(1, 4)]
        self.products = [Product.objects.create(name=f'Product {i}', category=self.categories[i % 3], marca=self.marcas[i % 3], size=self.sizes[i % 3]) for i in range(1, 4)]

    def test_product_list(self):
        response = self.client.get('/product-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertEqual(len(response.context['products']), 3)

    def test_product_detail(self):
        response = self.client.get('/product/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertEqual(response.context['product'], self.products[0])

    def test_category_list(self):
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertEqual(len(response.context['categories']), 3)

    def test_category_detail(self):
        response = self.client.get('/category/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(response.context['category'], self.categories[0])


class TestLoja(TestCase):
    def setUp(self):
        self.categories = [Category.objects.create(name=f'Category {i}') for i in range(1, 4)]
        self.marcas = [Marca.objects.create(name=f'Marca {i}') for i in range(1, 4)]
        self.sizes = [Size.objects.create(name=f'Size {i}') for i in range(1, 4)]
        self.products = [Product.objects.create(name=f'Product {i}', category=self.categories[i % 3], marca=self.marcas[i % 3], size=self.sizes[i % 3]) for i in range(1, 4)]

    def test_product_list(self):
        response = self.client.get('/product-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertEqual(len(response.context['products']), 3)

    def test_product_detail(self):
        response = self.client.get('/product/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertEqual(response.context['product'], self.products[0])

    def test_category_list(self):
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertEqual(len(response.context['categories']), 3)

    def test_category_detail(self):
        response = self.client.get('/category/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(response.context['category'], self.categories[0])


class TestRegister(TestCase):
    def setUp(self):
        self.categories = [Category.objects.create(name=f'Category {i}') for i in range(1, 4)]
        self.marcas = [Marca.objects.create(name=f'Marca {i}') for i in range(1, 4)]
        self.sizes = [Size.objects.create(name=f'Size {i}') for i in range(1, 4)]
        self.products = [Product.objects.create(name=f'Product {i}', category=self.categories[i % 3], marca=self.marcas[i % 3], size=self.sizes[i % 3]) for i in range(1, 4)]

    def test_product_list(self):
        response = self.client.get('/product-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertEqual(len(response.context['products']), 3)

    def test_product_detail(self):
        response = self.client.get('/product/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertEqual(response.context['product'], self.products[0])

    def test_category_list(self):
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertEqual(len(response.context['categories']), 3)

    def test_category_detail(self):
        response = self.client.get('/category/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(response.context['category'], self.categories[0])



class TestProduct(TestCase):
    def test_product_list(self):
        response = self.client.get('/product-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product-list.html')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
    @classmethod
    def setUpTestData(cls):
        product_list = []



class MarcaTest(TestCase):
    def test_marca_list(self):
        response = self.client.get('/marca-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marca-list.html')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')



class SizeTest(TestCase):
    def test_size_list(self):
        response = self.client.get('/size-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'size-list.html')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Produtos')
        self.assertContains(response, 'Categorias')
        self.assertContains(response, 'Marcas')
        self.assertContains(response, 'Tamanhos')
        self.assertContains(response, 'Carrinho')
        self.assertContains(response, 'Checkout')
        self.assertContains(response, 'Minha Conta')
        self.assertContains(response, 'Sair')
        self.assertContains(response, 'Cadastrar')