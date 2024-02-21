import os

def id_list():
    id = 0
    for i in os.listdir():
        if i.endswith(".cvs"):
            mmax = int(i[0])
            if mmax > id:
                id = mmax
    id += 1 
    return id

def title_note_list(id):
    for i in os.listdir():
        if i.endswith(".cvs"):
            if id == i[0]:
                name_note = i
    return name_note
