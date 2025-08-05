indian_dist = {
    "Gujarat": ['Gir Somnath', 'Junagadh', 'Rajkot'],
    "Maharashtra": ['Mumbai', 'Nasik', 'Kolhapur'],
    "Uttar Pradesh": ['Mirzapur', 'Lucknow', 'Kashi']
}

print(indian_dist['Gujarat'][1])

nested_list = ['A', 'B', ['C', 'D', ['E', 'F', 'G']]]

print(nested_list[2][1])

nested_dict = {
    "France": {
        "visited_time": 4,
        "cities": ['Paris', "Lille", "Dijon"]
    },
    "India": {
        "visited_time": 100,
        "cities": ['Somnath', 'Jagannath', 'Mahakaleshvar']
    }
}

print(nested_dict['India']['cities'][0])