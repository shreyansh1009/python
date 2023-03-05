def countCurrency(amount):
    notes=[2000,500,100]
    notesCount={}

    for note in notes:
        if amount >= note:
           notesCount[note]=amount//note
           amount = amount % note

    print("Currency count ->")
    for key, val in notesCount.items():
        print(f"{key} : {val}")
amount=int(input("enter the amount"))
countCurrency(amount)