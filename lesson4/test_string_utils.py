import pytest
from string_utils import StringUtils

string_utils=StringUtils()
  

def test_capitilize():
    string_Utils=StringUtils
    res=string_Utils.capitilize("skypro")
    assert res=="Skypro"
    


def test_trim():
    string_Utils=StringUtils
    res=string_Utils.trim("  skypro")
    assert res=="skypro"


def test_to_list():
    string_Utils=StringUtils
    res=string_Utils.to_list("skypro,end")
    assert res=="skypro end"


def test_contains():
    string_Utils=StringUtils
    res=string_Utils.contains("SkyPro", "S")
    print(True)
    res=string_Utils.contains("SkyPro", "U")
    assert res=="SkyPro", "S"

def test_delete_symbol():
    string_Utils=StringUtils
    res=string_Utils.delete_symbol()
    assert res==("\n")
    if(string, "\n"):
        string = string.replace(m, "\n")    
        return string


def test_starts_with():
    string_Utils=StringUtils
    res=string_Utils.starts_with("SkyPro", "S")
    print(True)
    res=string_Utils.starts_with("SkyPro", "P")
    print(False)
    assert res=="SkyPro", "S"

def test_end_with():
    string_Utils=StringUtils
    res=string_Utils.end_with("SkyPro", "y")
    print(False)
    res=string_Utils.end_with("SkyPro", "o")
    print(True)
    assert res=="SkyPro", "o"

def test_is_empty():
    string_Utils=StringUtils
    res=string_Utils.is_empty()
    print(True)
    res=string_Utils.is_empty("string")
    print(False)
    assert res==" "


def list_to_string():
    string_Utils=StringUtils
    res=string_Utils.list_to_string("Sky", "Pro")
    assert res=="Sky, Pro"






























    










        



    
        
