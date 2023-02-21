import pytest
from string_utils import StringUtils



string_utils=StringUtils()

  
@pytest.mark.parametrize("text, answer", [("skypro","Skypro")])
def test_capitilize(text, answer):
    string_Utils=StringUtils()
    res=string_Utils.capitilize(text)
    assert res==answer


































    










        



    
        
