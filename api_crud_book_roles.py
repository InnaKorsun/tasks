import requests
import json

#is_item == 0 works with books
#is_item == 1 works with roles
is_item = 1

if is_item==0:
    new_item = {
    "title": "Fight club",
    "author": "InnaK"
}
    base_url = "http://pulse-rest-testing.herokuapp.com/books/"
    update_info= {"title": "Big little lies","author": "InnaKor"}
else:
    new_item = {
    "name": "Dambldor",
    "type": "Director",
    "level": 1,
    "book": 1
}
    base_url = "http://pulse-rest-testing.herokuapp.com/roles/"
    update_info= {"name": "Albus Dambldor"}

is_update = False

def add_item(new_item):

    "add new item and return id/name of new item"
    r = requests.post(base_url,data = new_item)
    print("Add item:"+str(r.status_code))
    id = r.json()["id"]
    return id

def show_all():
    'show all item'
    r = requests.get(base_url)
    items= r.json()
    for i in items:
        print(i)

def show_current_item(id):
    #show book with id or role with name
    r = requests.get(base_url+ str(id))
    print("Item get: status code"+str(r.status_code))
    item = r.json()
    print(item)
    if is_update == True:
        if is_item==0:
            assert item['title'] == update_info['title']
            assert item['author'] == update_info['author']
        else:
            assert item['name'] == update_info['name']


def check_item_in_list(id):
    # check that books/roles with id/name present in books list
    r = requests.get(base_url)
    list_item = r.json()
    for i in list_item:
        if i["id"]==id:
            print("Item in list {} and status code is {}".format(i,str(r.status_code)))
        if is_update == True:
            if is_item==0:
                assert i["title"]==update_info["title"]
                assert i["author"] == update_info["author"]
            else:
                assert i["name"]==update_info["name"]


def update_item (id, update_info):
    # update book by update_info information
    r = requests.put(base_url + str(id), data = update_info)
    print("Item update: "+str(r.status_code))
    is_update = True


def delete_item(id):
    # delete book with id
    r = requests.delete(base_url+ str(id))
    print("Item deleted and status code is" + str(r.status_code))
    assert (r.status_code == 204)

if __name__ == "__main__":

    id = add_item(new_item)
    show_current_item(id)
    check_item_in_list(id)
    update_item(id,update_info)
    show_current_item(id)
    check_item_in_list(id)
    delete_item(id)
