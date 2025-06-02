# Hacker_Rank
hacker rank solution 
if __name__ == '__main__':
    name_list=[]
    score_list=[]
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        name_list.append(name)
        score_list.append(score)
    score_list = list(set(score_list))
    score_list.sort()
    second_low = score_list[1]
    out = [i[0] for i in records if i[1]==second_low]
    out.sort()
    for i in out:
        print(i)    


        # Explanation 

        This Python script is designed to read names and scores from user input, then output the names of students who have the second lowest score, in alphabetical order.

Let me explain it step-by-step:

✅ What the Code Does:
Takes Input:

First, it takes an integer input for the number of students.

Then it takes name and score input pairs for each student.

Stores Records:

records stores each [name, score] as a sublist.

score_list collects all scores, then duplicates are removed using set(), and the list is sorted.

Finds Second Lowest Score:

After sorting unique scores, score_list[1] gives the second lowest score.

Filters Names with the Second Lowest Score:

From the full records, it picks names where the score matches the second lowest.

Sorts Names and Prints Them:

Finally, it prints those names in alphabetical order.

🔁 Example:
Input:

Copy
Edit
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Output:

nginx
Copy
Edit
Berry
Harry
Explanation:

Scores: [37.21, 37.21, 37.2, 41, 39] → unique & sorted: [37.2, 37.21, 39, 41]

Second lowest score = 37.21

Students with that score: Berry, Harry → sorted alphabetically → Berry, Harry

question