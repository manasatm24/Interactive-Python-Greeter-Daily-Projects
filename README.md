# Interactive Python Greeter & Daily Projects

A collection of **interactive Python mini-projects** built daily to improve programming skills and create real-world applications.

This repository documents my journey of learning Python by building **consistent, hands-on projects**.

---

## About This Repository

* Daily Python project uploads
* Focus on logic building and problem solving
* Hands-on approach to learning
* Continuous improvement and consistency

---

## Projects

### Day 01 – Interactive Python Greeter

A CLI-based Python application that greets users with a personalized message using a typing animation.

**Features:**

* Takes user input (name & hobby)
* Animated typing effect
* Clean terminal interface
* Motivational output

---

### Day 02 – CLI To-Do App

A command-line based To-Do application to manage daily tasks efficiently with persistent storage.

**Features:**

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Save tasks using JSON (data persists after closing app)
* Simple and user-friendly CLI interface

---

### Day 03 – Password Generator

A Python program that generates strong, random passwords based on user-defined length.

**Features:**

* User inputs desired password length
* Generates secure random passwords
* Includes letters, numbers, and special characters
* Fast and simple CLI tool

---

### Day 04 – Quiz Game

A CLI-based Python quiz application that tests user knowledge with multiple-choice questions.

**Features:**

* Multiple-choice questions
* Instant feedback (correct/wrong)
* Score tracking
* Simple and interactive CLI experience

---

### Day 05 – File Organizer

A Python automation tool that organizes files in a selected folder by sorting them into categories based on file types.

**Features:**

* Automatically scans a folder (e.g., Downloads/Desktop)
* Organizes files into categories:

  * Images
  * Documents
  * Videos
  * Music
  * Others
* Creates folders automatically if they don’t exist
* Prevents duplicate file overwrite
* Simple and efficient file management
* Saves time by reducing manual sorting

---

## Demo

### Day 01 Output

```
==================================================
 Welcome to Your Python Journey 
==================================================
 Enter your name: Manasa
Enter your hobby: Coding

Loading your personalized message...

==================================================
Hello, Poorvika!
Welcome to the world of Python programming!
It's awesome that you love Coding.
Today is a perfect day to build something amazing!
Keep learning, keep building, keep winning!
==================================================

 Let's start coding!
```

---

### Day 02 Output (CLI To-Do App)

```
========== TO-DO CLI APP ==========
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit
===================================

 Choose an option: 2
 Enter task: Learn Python
✔ Task added!

 Choose an option: 1

 Your Tasks:

1. Learn Python 

Choose an option: 3
✔ Enter task number to mark complete: 1
 Task completed!

 Choose an option: 1

 Your Tasks:

1. Learn Python 
```

---

### Day 03 Output (Password Generator)

```
Enter password length: 10
Generated Password: A@7k#Pz1Lm
```

---

### Day 04 Output (Quiz Game)

```
 Welcome to the Quiz Game!

1. What is the capital of India?
A. Mumbai
B. Delhi
C. Chennai
D. Kolkata
Enter your answer: B
Correct!

...

Quiz Finished!
Your Score: 3/4
```

---

### Day 05 Output (File Organizer)

```
Scanning folder...
Creating folders if not exist...
Organizing files...

✔ Moved: photo.jpg → Images
✔ Moved: resume.pdf → Documents
✔ Moved: song.mp3 → Music

✅ Files organized successfully!
```

---

## Repository Structure

```
interactive-python-greeter/
│
├── day-01-greeter/
│   ├── main.py  
│
├── day-02-todo-cli/
│   ├── todo.py
│   ├── tasks.json
│
├── day-03-password-generator/
│   ├── password.py
│
├── day-04-quiz-game/
│   ├── quiz_game.py 
│
├── day-05-file-organizer/
│   ├── organizer.py
│
└── README.md
```

---

## How to Run Projects

1. Clone the repository:

```
git clone https://github.com/your-username/interactive-python-greeter.git
```

2. Navigate to a project folder:

```
cd day-01-greeter
# OR
cd day-02-todo-cli
# OR
cd day-03-password-generator
# OR
cd day-04-quiz-game
# OR
cd day-05-file-organizer
```

3. Run the project:

```
python main.py
# OR
python todo.py
# OR
python password.py
# OR
python quiz_game.py
# OR
python organizer.py
```

---

## Technologies Used

* Python 3
* Standard Libraries (`time`, `json`, `os`, `random`, `string`, `shutil`)

---

## Goals

* Build strong Python fundamentals
* Create portfolio-ready projects
* Develop consistency in coding
* Prepare for backend development roles

---

## Upcoming Projects

* GUI-based Applications
* Automation Tools
* Mini AI-based Projects

---

## Contribution

This is a personal learning repository, but suggestions are welcome.

---

## License

Open-source and free to use.

---

## Note

This repository represents a **daily coding journey** focused on learning and  building.

---

## Quote

**The expert at anything was once a beginner.**
