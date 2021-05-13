"""
Find all the students of the Class if following are given:

dance_list: People who love dance.

music_list: People who love music.

both: People who love both these things

nothing: People who love none of the above.....Maybe they love travelling, book reading or PUBG.

Note: Please Print sorted only. I actually have to mark attendance.:)

Input Format:

No need to take input, you will get all the list already.

Output Format:

Print the sorted list of all the students.

Sample Input 0:

[1,6],[3,4],[2,3,4],[3,4,5]
Sample Output 0:

[1, 2, 3, 4, 5, 6]
"""

nothing_list,both_list,dance_list,music_list = eval(input())
# Write your code here
list_join = nothing_list + both_list + dance_list + music_list
sort = sorted(list(set(list_join)))
print(sort)