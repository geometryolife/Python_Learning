#  编写一个名为favorite_book()的函数，其中包含一个名为title的形参，
#  这个函数打印一条消息，调用函数，并传递实参。
def favorite_book(title):
    """显示喜欢的图书消息"""
    print("One of my favorite books is " + title.title())


#  book = "Alice in Wonderland"
book = input("What's the name of your favorite book? ")
favorite_book(book)
