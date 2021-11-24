from unittest import TestCase, mock
from app.controler.patrimonio import PatrimonioControler


class PatrimonioValor(TestCase):



    @mock.patch('app.controler.patrimonio.valor_icms')
    def test_Mockado_impostos_ICMS(self,mokodoValue):
        mokodoValue.return_value = 3
        assert PatrimonioControler.CalculaValorPatrimonio(100,10,None,5) == 118
    
    @mock.patch('app.controler.patrimonio.valor_ipi')
    def test_Mockado_impostos_IPI(self,mokodoValue):
        mokodoValue.return_value = 90
        assert PatrimonioControler.CalculaValorPatrimonio(100,10,10,None) == 210

    @mock.patch('app.controler.patrimonio.valor_frete')
    def test_Mockado_frete(self,mokodoValue):
        mokodoValue.return_value = 100
        assert PatrimonioControler.CalculaValorPatrimonio(100,None,10,5) == 115  

