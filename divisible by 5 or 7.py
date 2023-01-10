start_num=int(35)
end_num=int(35)
cnt=start_num
while cnt <=end_num:
    if cnt %5==0 and cnt %7==0:
        print(cnt,"is divisible by 7 and 5")
        cnt+=1
    else:
        print("the number is not divisible by 7 and 5")
