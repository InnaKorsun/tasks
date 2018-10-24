import requests
import json

new_role = {
    "name": "Dambldor",
    "type": "Director",
    "level": 1,
    "book": 1
}

base_url = "http://pulse-rest-testing.herokuapp.com/roles/"

update_info= {"name": "Albus Dambldor"}
is_update = False

def add_role(new_role):
    "add new role and return name of new role"
    r = requests.post(base_url,data = new_role)
    print("Add roll:"+str(r.status_code))
    id = r.json()["id"]
    return id

def show_all():
    'show all roles'
    r = requests.get(base_url)
    roles = r.json()
    for i in roles:
        print(i)

def show_current_role(id):
    #show book with name
    r = requests.get(base_url + str(id))
    print("Role get: status code"+str(r.status_code))
    role = r.json()
    print(role)
    if is_update == True:
        assert role['name'] == update_info['name']


def check_role_in_list(id):
    # check that role with id present in books list
    r = requests.get(base_url)
    list_role = r.json()
    for i in list_role:
        if i["id"]==id:
            print("Role in list {} and status code is {}".format(i,str(r.status_code)))
        if is_update == True:
            assert i["name"]==update_info["name"]



def update_role (name, update_info):
    # update role by update_info information
    r = requests.put(base_url + str(id), data = update_info)
    print("Role updates: "+str(r.status_code))
    is_update = True


def delete_role(id):
    # delete book with id
    r = requests.delete(base_url+ str(id))
    print("Role is deleted and status code is " + str(r.status_code))
    assert (r.status_code == 204)

if __name__ == "__main__":

    id= add_role(new_role)
    show_current_role(id)
    check_role_in_list(id)
    update_role(id,update_info)
    show_current_role(id)
    check_role_in_list(id)
    delete_role(id)

