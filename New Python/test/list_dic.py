def list_dic():
    Key = [1,2,3]
    values = ["one","two","three"]
    result=dict(zip(Key,values))
    print(result)
list_dic()

def dic_to_tuple():
    x={1:'one', 2:'two', 3:'three'} 
    for i in x.items():
        print(i)
dic_to_tuple()
    