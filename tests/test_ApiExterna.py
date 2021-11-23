from unittest import TestCase, mock
from app.controler.APIexternas import IBGE,MercadoLivre,API_IBGE_is_on,API_ML_is_on


class TestApiData(TestCase):
    def test_se_nao_volta_nada_de_estado(self):
        assert IBGE.estadoBrasil() is not None
    
    def test_se_nao_volta_nada_de_pais(self):
        assert IBGE.pais() is not None
    
    def test_se_nao_volta_nada_de_categoria(self):
        assert MercadoLivre.cotegorias() is not None
    
    def test_se_nao_volta_Bahia_dentro_array(self):
        self.assertIn("Bahia",IBGE.estadoBrasil())

    def test_se_nao_volta_Brasil_dentro_array(self):
        self.assertIn("Brasil",IBGE.pais())

    def test_se_nao_volta_Ingressos_dentro_array(self):
        self.assertIn("Ingressos",MercadoLivre.cotegorias())




class TestApis_on(TestCase):

    @mock.patch('app.controler.APIexternas.head')
    def test_Mockado_IBGE_on(self,metado_mokado):
        metado_mokado.return_value.status_code = 200
        self.assertTrue(API_IBGE_is_on())

    @mock.patch('app.controler.APIexternas.head')
    def test_Mockado_IBGE_off(self,metado_mokado):
        metado_mokado.return_value.status_code = 500
        self.assertFalse(API_IBGE_is_on())

    @mock.patch('app.controler.APIexternas.head')
    def test_Mockado_ML_on(self,metado_mokado):
        metado_mokado.return_value.status_code = 200
        self.assertTrue(API_ML_is_on())
    
    @mock.patch('app.controler.APIexternas.head')
    def test_Mockado_ML_off(self,metado_mokado):
        metado_mokado.return_value.status_code = 500
        self.assertFalse(API_ML_is_on())