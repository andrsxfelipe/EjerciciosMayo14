
# 1. Library Book Tracker
library=[]
def add_book(title,author,pages):
    library.append(title)
def find_book(title):
    if title in library:
        return title
    else:
        return "Book not found."
def show_books():
    return library

# 2. Student Grade Manager
grades={}
def add_student(name):
    grades[name]=[]
def add_grade(name,grade):
    grades[name].append(grade)
def get_average(name):
    return (sum(grades[name]))/len(grades[name])

# 3. Restaurant Menu Editor
menu={}
def add_dish(name,price,availability):
    menu[name]=[price,availability]
def change_availability(name,availability):
    menu[name][1]=availability
def total_available_price():
    tap=0
    for i in menu.values():
        if i[1]==True:
            tap+=i[0]
    return tap

# 4. Warehouse Box Counter
warehouse={}
def add_box(box,quant1):
    warehouse[box]=quant1
def update_quantity(box,quant2):
    warehouse[box]=quant2
def has_enough(box, quant3):
    if quant3>warehouse[box]:
        return False
    else:
        return True

# 5. Movie Rating System
movies={}
def add_movie(movie):
    movies[movie]=[]
def rate_movie(movie,rating):
    movies[movie].append(rating)
def average_rating(movie):
    return (sum(movies[movie])/len(movies[movie]))
    
# 6. Online Course Tracker
courses={}
def add_course(course,last,enrolls):
    courses[course]=[last,enrolls]
def update_enrollment(course, enrolls):
    courses[course][1]=enrolls
def filter_by_hours(last):
    courses1={}
    for course,info in courses.items():
        if info[0]>=last:
            courses1[course]=info
    return courses1

# 7. To-Do List Organizer
todos={}
def add_task(task,priority): #Añadir tareas
    todos[task]=[priority]
def complete_task(task): #Marcarlas como completadas
    todos[task].append('completed')
def filter_tasks(priority,status): #Filtrar por prioridad o estado
    return [task for task,info in todos.items() if info[0]==priority and info[1]==status]

# 8. Digital Wallet
wallet={}
def add_expense(category,expense):
    if category not in wallet.keys():
        wallet[category]=[expense]
    else:
        wallet[category].append(expense)
def total_spent():
    return sum(map(lambda x: sum(x[1]), wallet.items()))
def expense_percentages():
    return {x:((sum(y)/total_spent())*100) for x,y in wallet.items()}


# 9. Pet Adoption Center
pets=[]
def add_pet(name, kind, age): 
    pets.append({'name':name,'specie':kind,'age':age})
    
def find_by_species(specie):
    return [i for i in pets if i['specie']==specie]
    #return {x:y for x,y in pets.items() if y[0]==specie}
def older_than(age):
    #older = {x:y for x,y in pets.items() if y[1]>age}
    return [i for i in pets if i['age']>age]

# 10. Gym Membership System
members={}
def register_member(name,plan, status):
    members[name]=[plan,status]
def change_plan(member,newplan):
    members[member][1]=newplan
def unpaid_members():
    return [x for x,y in members.items() if y[1]=='late']