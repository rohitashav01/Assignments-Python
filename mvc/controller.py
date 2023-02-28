from model import Person
from model import Blog
import view

#User Data

def showAll():
    user_in_db = Person.getAllUser()
    return view.showAllView(user_in_db)

def start():
    view.startView()
    inp = str(input())
    if inp == 'y':
        return view.enterInput()
    else:
        return view.endView()

def showData():
    view.showView()
    inp_data= str(input())
    if inp_data == 'y':
        return showAll()
    else:
        return view.endView()

#BlogData
def reprBlog():
    blog_in_db = Blog.getAllBlog()
    return view.showAllBlog(blog_in_db)

def enterBlogData():
    inp = input("Do you want to enter the blog data?(y/n)")
    val = True
    if inp == 'y':
        view.inputBlog()
        if val:
            inp_again = input('Do you want to add  another blog: (y/n)')
            if inp_again == 'y':
                return view.inputBlog()
            else:
                return showBlog()        
    else:
        return reprBlog()
        


def showBlog():
    view.seeBlog()
    inp_blog = str(input())
    if inp_blog == 'y':
        return reprBlog()
    else:
        return showAll()

def showUserBlog():
    inp = input("Do you want to see the blogs of a particular user(y/n)")
    if inp == 'y':
        return view.userBlog()
    else:
        return view.endView()

if __name__ == "__main__":
#running controller function
    while True:
        start()
        enterBlogData()
        showBlog()
        showData()
        showUserBlog()

