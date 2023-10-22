

test_score = {"David": 84, "Brenda": 78}
print(test_score)

test_score["David"] = 65
print(test_score)
test_score["Jane"] = 91
print(test_score)
test_score["David"] = test_score["David"] + 10
print(test_score)
print(test_score.keys())
print(test_score.values())
print(test_score.items())


print(test_score)
if "David" not in test_score:
    test_score["David"] = test_score["David"] + 10
print(test_score.get("David"))
del test_score["David"]
print(test_score)
test_score.clear()
print(test_score)
