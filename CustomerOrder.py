product_File=open(r"C:\Users\HP\Desktop\AIML\PythonLearning\InventoryManagement.txt","r")
products=product_File.read().split("\n")
name=input("enter product name")
phone=input("enter phone number")
email=input("enter email")
quantity=input("enter Quantity")
productName=input("enter Product Name")

# product_File.writelines([id,",",name,",",price,",",quantity,",",category,"\n"])
bill=[]
for product in products:
    p=product.split(",")
    if p[1]==productName and p[3]>=quantity:
        print("-----------------------------")
        print("Product Name     : ", p[1])
        print("Price            : ", p[2]) 
        print("Quantity         : ", quantity) 
        print("-----------------------------")
        print("Billing Amount   : ", int(quantity) * int(p[2]))
        p.replace(p[3],str(int(p[2])-int(quantity)))
        print("-----------------------------")
        billing=name+",",phone+","+email+",",quantity+","+str(int(quantity) * int(p[2]))+"\n"
        
    elif p[1]==name and p[3]<=quantity:
        ch=input("y/n")
        if(ch=='y'):
            print("-----------------------------")
            print("-----------------------------")
            print("Product Name     : ", p[1])
            print("Price            : ", p[2]) 
            print("Quantity         : ", quantity) 
            print("-----------------------------")
            print("Billing Amount   : ", int(quantity) * int(p[2]))
            print("-----------------------------")
            p.replace(p[3],"0")
            billing=name+",",phone+","+email+",",quantity+","+str(int(quantity) * int(p[2]))+"\n"
    else :
        print("not found")   
st=open(r"C:\Users\HP\Desktop\AIML\PythonLearning\Salses.txt","a+")
st.writelines(billing)
st.writelines(bill)
