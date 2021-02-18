def ch1(a,b,start,end):
    a_total=0;
    b_total=0;
    a_b_total=0;
    non = 0;
    for i in range(start,end+1):
        if i%a==0 and i%b!=0:
            a_total+=1;
        elif i%a==0 and i%b==0:
            a_b_total+=1;
        elif i%a!=0 and i%b==0:
            b_total+=1;
        else :
            non+=1;
    return [a_total,b_total,a_b_total,non];


f = open("./input.txt", "r")
f1=f.readline()
f2=f.readline()
x1=f1.split(" ")
x2=f2.split(" ")
a = int(x1[0]);
b= int(x1[1]);
start = int(x2[0]);
end = int(x2[1]);

lst = ch1(a,b,start,end);
for i in lst:
    print(i)