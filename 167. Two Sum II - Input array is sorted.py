numb = [2,7,11,15]
target = 9
p1 = 0
p2 = len(numb)-1
while p1<p2:
            if numb[p1]+numb[p2] > target:
                p2-=1
            elif numb[p1]+numb[p2]<target:
                p1+=1
            break
print([p1+1, p2+1]) 