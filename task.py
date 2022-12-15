#Задача 1
text=" hbvj, впиишр, укп, купипк, абв, аваыц"
text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, text.split()))
print(text_list)

# Задача 2.
n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

# Задача 3.
some_list=[2,3,5,6]
n=len(some_list)
new_List= list(some_list[i]*some_list[-1*(1+i)] for i in range(n//2+1*(n%2)))
print(new_List)


#Задача 4
some_list=list(map(int,input().split()))
new_list=[]
new_list=[i for i in range(len(some_list)) if some_list.count(i)==1]
print(new_list)