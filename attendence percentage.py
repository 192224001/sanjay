no_of_class_attended=int(input("enter no of classes attended"))
total_no_of_classes=int(input("enter the number of classes attend:"))
attendence=no_of_class_attended/total_no_of_classes*100
if 75>=attendence:
    print("less attendence percentage")
    medical_issue=input("did you have any medical issues,yes or no ?")
    if medical_issue=="yes":
        print("having medical issue, eligible for write exam")
    else:
        print("not having medical issue ,not eligible for write exam")
else:
    print("having attendence percentage,s eligible for exam")
