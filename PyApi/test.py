def validBook(bookObject):#sanitizing data
    if ("name" in bookObject and
        "price" in bookObject and
        "isbn" in bookObject):
        return True
    else:
        return False

validObject={
              'name':'Republic',
              'price':3.78,
              'isbn':1234567811
    }

missingName={
            'price':3.78,
            'isbn':1234567811 
 
    }
missingPrice={
           'name':'Republic',
           'isbn':1234567811
    }
missingIsbn={'name':'Republic',
              'price':3.78
           
    }
print(validBook(validObject))
print(validBook(missingName))
print(validBook(missingPrice))
print(validBook(missingIsbn))







