# fruits = ["Apple", "Banana", "Cherry", "Orange", "Papaya"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# student_scores = [100, 56, 98, 44, 56, 76, 83]

# total_score = sum(student_scores)
# print(total_score)
# print(total_score / len(student_scores))

# sum_of_score = 0

# for score in student_scores:
    # sum_of_score = sum_of_score + score
    # sum_of_score += score

# print(sum_of_score)



# print(max(student_scores))
# print(min(student_scores))
# print(sum_of_score)



# I have a score list
# I have to loop trohugh it
# I have to make a function or use conditional to find mxa number in list

student_scores = [76, 56, 99, 44, 56, 76, 83]

max_score = student_scores[0]

for score in student_scores[1:]:
    if score > max_score:
        max_score = score
        # print(f"Max score is, {score}")

total = 0
for number in range(1, 101,):
    total += number
# print(total)


