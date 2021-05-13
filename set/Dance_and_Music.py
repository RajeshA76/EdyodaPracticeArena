"""
3 list will be given:

all_student_list: Containing all the students roll no.

dance_list: Containing roll no of only those who love dance.

music_list: Containing roll no of only those who love music.

Print the sorted list of those who love both in first line and None of them in Second line.

Input Format:

No need to take input. 3 list will be given with above name.

Output Format:

Print two list in two lines as explained above.

Sample Input 0:

[1,2,3,4,5,6],[2,3,4],[3,4,5]
Sample Output 0:

[3, 4]
[1, 6]
"""

all_student_list,dance_list,music_list = eval(input())
# Write your code here
res1 = list(sorted((set(all_student_list).intersection(set(dance_list))).intersection(set(music_list))))
print(res1)
res2 = list(sorted(set(all_student_list).symmetric_difference(set(dance_list)).intersection(set(all_student_list).symmetric_difference(set(music_list)))))
print(res2)