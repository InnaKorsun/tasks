import requests
import json

new_book = {
    "title": "Fight club",
    "author": "InnaK"
}
#if it need work with roles: please change base url to "http://pulse-rest-testing.herokuapp.com/roles/
base_url = "http://pulse-rest-testing.herokuapp.com/books/"

update_info= {"title": "Big little lies","author": "InnaKor"}
is_update = False

def add_book(new_book):
    "add new book and return id of new book"
    r = requests.post(base_url,data = new_book)
    print("Add book:"+str(r.status_code))
    id = r.json()["id"]
    return id

def show_all():
    'show all books'
    r = requests.get(base_url)
    books = r.json()
    for i in books:
        print(i)

def show_current_book(id):
    #show book with id
    r = requests.get(base_url+ str(id))
    print("Book get: status code"+str(r.status_code))
    book = r.json()
    print(book)
    if is_update == True:
        assert book['title'] == update_info['title']
        assert book['author'] == update_info['author']


def check_book_in_list(id):
    # check that books with id present in books list
    r = requests.get(base_url)
    list_book = r.json()
    for i in list_book:
        if i["id"]==id:
            print("Book in list {} and status code is {}".format(i,str(r.status_code)))
        if is_update == True:
            assert i["title"]==update_info["title"]
            assert i["author"] == update_info["author"]



def update_book (id, update_info):
    # update book by update_info information
    r = requests.put(base_url + str(id), data = update_info)
    print("Book update: "+str(r.status_code))
    is_update = True


def delete_books(id):
    # delete book with id
    r = requests.delete(base_url+ str(id))
    print("Book deleted and status code is" + str(r.status_code))
    assert (r.status_code == 204)

if __name__ == "__main__":

    id = add_book(new_book)
    #show_current_book(id)
    #check_book_in_list(id)
    #update_book(id,update_info)
    #show_current_book(id)
    #check_book_in_list(id)
    #delete_books(id)

