print("\n======= You Excel Attendance System =======\n")
webST_count=1
while webST_count <= 5:
    print(f"\n---- Web Development with Python Students ({webST_count}) ----\n")

    name = input("Student Full Name: ")
    att = eval(input("Attendance Percentage: "))
    performance = input("Performance According to management: ")

    if att >= 90:
        remark = "Excellent Attendance"
        certificate = "Got the certificate"
    elif att >=80:
        remark = "Good Attendance"
        certificate = "Got the certificate"
    elif att >=70:
        remark = "Aur achi hosakti thi"
        certificate = "Got the certificate"
    elif att >= 60:
        remark = "Average Attendance"
        certificate = "Give reason about the low attendance to get the certificate"
    else:
        remark = "Bad Attendance!"
        certificate = "Not eligible for the certificate"
        

    print(f"\nResult for {name} \nAttendance Percentage: {att}% \nRemark: {remark} \nCertificate Status: {certificate} \nPerformance: {performance}")

    print(f"\nDear {name}, there are some offers according to your skills:")
    
    skills = ["Python", "Django", "Flask", "Backend Development", "Frontend Development"]

    for skill in skills:
        if skill == "Python":
            offer = "Python Developer Internship"
        elif skill == "Django":
            offer = "Backend Internship (Django)"
        elif skill == "Flask":
            offer = "Backend Internship (Flask)"
        elif skill == "Backend Development":
            offer = "Backend Developer Internship (Node / Django)"
        elif skill == "Frontend Development":
            offer = "Frontend Developer Internship (React / Tailwind)"
        else:
            offer = "General IT Training Program"
    
        print(f"{skill} : {offer}")

        
    webST_count += 1 
    
    
        
    
