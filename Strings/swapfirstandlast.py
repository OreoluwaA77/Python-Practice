def name_shuffle (name):
    space=name.index(" ")
    first_name=name[0:space:1]
    last_name=name[space::]
    print(last_name+" "+ first_name)

name_shuffle("Zendaya Coleman")