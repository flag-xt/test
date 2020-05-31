def second_serch(seq,seach_num):
    begin=0
    end=len(seq)-1
    while begin<=end:
        mid=(begin+end)//2
        if seq[mid]==seach_num:
            return mid
        elif seq[mid]>seach_num:
            end=mid-1
        else:
            begin=mid+1

a=[1,2,3,4,5,6,7,8,9,10]
print(second_serch(a,8))