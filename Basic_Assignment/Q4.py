#If there are 20 students who like football ,30 students like badminton and 10 like both.There are 20 who
# are not interested in any of the games .How many total number of students are there?
  
football=int(input("How many students like football:"))
badminton=int(input("How many students like badminton:"))
both=int(input("How many students like both:"))
not_interested=int(input("Students who don't like anything:"))
total=football+badminton+not_interested-both
print("Total number of students :",total)