#Тренажер 2
def vote(votes):
    s_votes = set(votes)

    most_common = None
    qty_most_common = 0

    for item in s_votes:
        qty = votes.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    return most_common
    
if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))