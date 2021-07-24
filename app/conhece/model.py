
import json
from os import write
from typing import final

FILES_RELATIVE_PATH = "app/conhece/files/"

#### CRUD ######
def create_file(name):
    with open(FILES_RELATIVE_PATH+name, "w") as file:
        json.dump({},file)
        file.close()


def get_file(name):
    try:
        with open(FILES_RELATIVE_PATH+name,"r+") as read_file:
            file_json = json.load(read_file)
            read_file.close()
            return file_json
    except:
        create_file(name)
        with open(FILES_RELATIVE_PATH+name,"r+") as read_file:
            file_json = json.load(read_file)
            read_file.close()
            return file_json
    
def write_to_file(json_info,filename):
    with open(FILES_RELATIVE_PATH+filename,"w") as file:
        json.dump(json_info,file)
        file.close()

### END CRUD ###

def create_index():
    base_index = {
        "a":"a.json",
        "b":"b.json",
        "c":"c.json",
        "d":"d.json",
        "e":"e.json",
        "f":"f.json",
        "g":"g.json",
        "h":"h.json",
        "i":"i.json",
        "j":"j.json",
        "k":"k.json",
        "l":"l.json",
        "m":"m.json",
        "n":"n.json",
        "o":"o.json",
        "p":"p.json",
        "q":"q.json",
        "r":"r.json",
        "s":"s.json",
        "t":"t.json",
        "u":"u.json",
        "v":"v.json",
        "w":"w.json",
        "x":"x.json",
        "y":"y.json",
        "z":"z.json",
    }

    write_to_file(base_index, "index.json")

def get_index():
    return get_file("index.json")

def get_persons_with_letter_file(name):
    index = get_index()
    name_initial_letter = name[0]
    file_name = index[name_initial_letter]
    person_with_letter_info = get_file(file_name)
    return person_with_letter_info,file_name

def get_persons_friend(name):
    person_with_letter_info,file_name = get_persons_with_letter_file(name)
    return person_with_letter_info[name]


def insert_person(name,friends):
    respective_file,file_name = get_persons_with_letter_file(name)
    if(respective_file == {} or name not in respective_file.keys()):
        respective_file[name] = friends
        write_to_file(respective_file,file_name)
        return name
    else:
        return "error: person already exists"

def get_friends(name):
    respective_file,file_name = get_persons_with_letter_file(name)
    return respective_file[name]

def initial_setup():
    create_index()
    initial_graph = {
        "ana":["carlos","maria","vinicius","joao"],
        "carlos":["ana"],
        "maria":["ana","vinicius",],
        "vinicius":["ana","maria"],
        "joao":["ana","luiza"],
        "luiza":["joao"]
    }
    for person_name in initial_graph:
        print("inserindo: "+person_name)
        print(initial_graph[person_name])
        result = insert_person(person_name,initial_graph[person_name])
        if "error" in result:
            print(result)
        else:
            print(result+" succesfully created")


def get_all_people_from_file(filename):
    names = []
    file = get_file(filename)
    for name in file:
        names.append(name)
    return names

def get_all_nodes():
    names = []
    index = get_index()
    for letter in index:
        letter_names = get_all_people_from_file(index[letter])
        if(len(letter_names)>0):
            names = names + list(letter_names)
    return names

def on_list1_but_not_on_list2(list1,list2):
    return list(set(list1) - set(list2))

def compress_list(name,result_friends):
    final_result = []
    for item in result_friends:
        if(item not in final_result and item != name):
            final_result.append(item)
    
    return final_result


def get_not_friends(name):
    friends = get_persons_friend(name)
    result_friends = []
    for friend in friends:
        friends_of_friend = get_persons_friend(friend)
        friends_that_match = on_list1_but_not_on_list2(friends_of_friend,friends)
        result_friends = result_friends + friends_that_match
    return compress_list(name,result_friends)

