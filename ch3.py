# ch#3 practice set p#1 python
name=input("ENTER THE NAME: ")
print(f"GOOD AFTER NOON:{name}")
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace(" <|Name|>","UMAIR").replace("<|Date|>","11/1/2025"))
name="umair  is here"
print(name.capitalize())
print(name.find("  "))
print(name.replace("  "," "))
name="DEAR UMAIR\n THIS\t PYTHON\a COURSE \'IS\' \"VERY HELPFUL "
print(name)
