comments=['hey what a wrong','hey how are you','what the bullshit']
redicularswords=['wrong','bullshit']
wrongcomments=[]
for i in comments:
    temp1=i.split(' ')
    for j in temp1:
        if(j in redicularswords):
            wrongcomments.append(i)
            break
print(wrongcomments)
# output:-
# ['hey what a wrong', 'what the bullshit']