
from PIL import Image, ImageTk


while True:
     print("SUBJECTS")
     print("1.MATHEMATICS")
     print("2.PHYSICS")
     print("3.CHEMISTRY")
     print("4.EXIT")
     subject_choice=int(input("\nENTER YOUR CHOICE OF SUBJECT FOR FORMULAS:"))

     if subject_choice==1:
         while True:
             print("CHAPTERS")
             print("1.SETS")
             print("2.TRIGONOMETRIC FUNCTIONS(TG)")
             print("3.COMPLEX NUMBERS")
             print("4.PERMUTATIONS AND COMBINATIONS(PC)")
             print("5.STRAIGHT LINES")
             print("6.EXIT")
             choice=int(input("\nENTER CHOICE FOR CHAPTERS:"))

          
          
             if choice==1:
                    
               im = Image.open(r"D:\Nishanth dell\Nishanth\setsformula.png") 
               im.show()

             elif choice==2:
               im = Image.open(r"D:\Nishanth dell\Nishanth\tgformula.png") 
               im.show()

             elif choice==3:
               im = Image.open(r"D:\Nishanth dell\Nishanth\cnformulas.png") 
               im.show()

             elif choice==4:
               im = Image.open(r"D:\Nishanth dell\Nishanth\pcformulas.png") 
               im.show()

             elif choice==5:
               im = Image.open(r"D:\Nishanth dell\Nishanth\stformulas.png") 
               im.show()

             elif choice==6:
                 break

             else:
                 print("Incorrect choice!")
                 
     elif subject_choice==2 :
         while True:
             print("CONCEPTS")
             print("1.GRAVITATION")
             print("2.WORK,POWER AND ENERGY(WPE)")
             print("3.KINEMATICS")
             print("4.PROJECTILE MOTION(PM)")
             print("5.EXIT")
             choice=int(input("\nENTER CHOICE FOR CONCEPTS:"))

             if choice==1:
                 im = Image.open(r"D:\Nishanth dell\Nishanth\gtformulas.png") 
                 im.show()

             elif choice==2:
                im = Image.open(r"D:\Nishanth dell\Nishanth\wpeformulas.png") 
                im.show()

             elif choice==3:
                im = Image.open(r"D:\Nishanth dell\Nishanth\kmformulas.png") 
                im.show()

             elif choice==4:
                im = Image.open(r"D:\Nishanth dell\Nishanth\pmformulas.png") 
                im.show()

             elif choice==5:
                 break

             else:
                 print("Incorrect choice!")
                 
                 

     elif subject_choice==3 :
         while True:
             print("CONCEPTS")
             print("1.CONCENTRATION OF SOLUTIONS(CS)")
             print("2.CHEMICAL BONDING(CM)")
             print("3.THERMODYNAMICS")
             print("4.EQUILIBRIUM")
             print("5.EXIT")
             choice=int(input("\nENTER CHOICE FOR LESSONS:"))

             if choice==1:
                im = Image.open(r"D:\Nishanth dell\Nishanth\csformulas.png") 
                im.show()

             elif choice==2:
                im = Image.open(r"D:\Nishanth dell\Nishanth\cmformulas.png") 
                im.show()

             elif choice==3:
                im = Image.open(r"D:\Nishanth dell\Nishanth\tmformulas.png") 
                im.show()

             elif choice==4:
                im = Image.open(r"D:\Nishanth dell\Nishanth\eqformulas.png") 
                im.show()

             elif choice==5:
                 break

             else:
                 print("Incorrect choice!")
             
                
     elif subject_choice == 4:
        print("THANK YOU FOR USING MY PROGRAM:)")
        break
    
     else:
        print("INCORRECT CHOICE :( PLEASE TRY AGAIN!")
        
