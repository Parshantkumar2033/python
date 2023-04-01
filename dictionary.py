a = {
    "name" : "parshant kumar",
    "roll no" : "2101140",
    "branch" : "CSE",
    1 : 50 ,

    "newdict" : {
        "abc" : "sdifhre",
        "as" : "hello",
        "we" : "world"
    }
}
print(type(a))
print(a["name"])
print("\n")
print(a.keys())
print("\n")
print(a.values())
print("\n") 
print(a.items())
print("\n")
print(a.get("newdict"))
print("\n")
print(a["newdict"]["we"])
print("\n")
print(a.get("branch"))
