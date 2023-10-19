#Takes a list value as an argument

#Returns string wituh all items seperated by comma and a space, and inserted before the last item

#EXAMPLE spam = ['apples', 'bananas', 'tofu', 'cats'] -> 'apples, bananas, tofu, and cats'.

mylist = ['apples', 'bananas', 'tofu', 'cats', 'Dogs']


def passlist(newlist):
    newlist.insert(-1, "and")
    seperatedlist = ' , '.join(newlist)
    newlistseperated = seperatedlist.replace(", and ,", ", and ")
    print(newlistseperated)

passlist(mylist)