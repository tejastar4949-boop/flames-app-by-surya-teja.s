import js

def run_game():
    # We use js.prompt instead of sync.input
    name1 = js.prompt("Enter the first name:")
    name2 = js.prompt("Enter the second name:")

    if name1 and name2:
        n1 = name1.lower().replace(" ", "")
        n2 = name2.lower().replace(" ", "")
        
        list1, list2 = list(n1), list(n2)
        for char in list1[:]:
            if char in list2:
                list1.remove(char)
                list2.remove(char)

        count = len(list1) + len(list2)
        flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

        if count > 0:
            while len(flames) > 1:
                idx = (count % len(flames)) - 1
                if idx >= 0:
                    flames = flames[idx + 1:] + flames[:idx]
                else:
                    flames.pop()
            
            # Show the result in a pop-up box
            js.alert(f"🔥 FLAMES Result: {flames[0]} 🔥")
        else:
            js.alert("The names are too similar!")
    else:
        js.alert("Names are missing!")

run_game()
