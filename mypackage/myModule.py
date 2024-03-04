def top_n (items, n):
    """Return the top n items in an array, in desc order. """

    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-1):

            if items[j] > items[j+1]: #if this item is bigger than next item..
                items[j], items[j+1] = items[j+1], items[j] #swap the two


    # get last two items
    top_n = items[-n:]

    #return in decending order
    return top_n[::-1]