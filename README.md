
# Pomodoro ToDo List Application

This is a simple Pomodoro ToDo List application built using PyQt6, designed to help users manage their tasks using the Pomodoro Technique. The application provides a login system, task input, a Pomodoro timer, and information about the Pomodoro Technique.


## Features

- Login System: Users can log in to access the ToDo List features.
- Task Management: Users can input tasks and manage their ToDo list.
- Pomodoro Timer: Integrated Pomodoro timer with short breaks and long breaks to enhance productivity.
- Information Dialog: Provides information about the Pomodoro Technique, emoji meanings, and file storage.


## Installation

Clone the repository:

```
git clone https://github.com/henriits/PomoTODOro.git
cd PomoTODOro
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the application:
```
python main.py
```
Change the time for application:
```
Inside "pomidoro_timer.py" change time as desired. 
        self.START_MINUTES = 0
        self.START_SECONDS = 20  
        self.SHORT_MINUTES = 0
        self.SHORT_SECONDS = 30
        self.LONG_MINUTES = 0
        self.LONG_SECONDS = 40
```


### Createing and Running the Executable
```
pyinstaller --name=pomotodoro --onefile --windowed --add-data "C:\*** add here full path ***\icon.ico;." --icon=icon.ico main.py   
```
Add full path to icon, this will make multiple files/folders including dist folder, where you will find pomodoro.exe. 
If using pomotodoro.exe file, you can run the application by double-clicking the executable. The application will work seamlessly and create a CSV file in the same directory as the .exe file.
## Images of application

<div align="center">

![login1](https://github.com/henriits/PomoTODOro/assets/121551949/8a30964e-ae49-48fa-a448-70cbf94b71aa)


![login2](https://github.com/henriits/PomoTODOro/assets/121551949/29900068-d3ae-4010-837c-211acde99ff9)


![register](https://github.com/henriits/PomoTODOro/assets/121551949/4f1f4e29-1685-4d2a-ad8e-9ad90616fe32)


![application](https://github.com/henriits/PomoTODOro/assets/121551949/c6ec0d14-400e-4e73-bc95-a53522794384)

![information](https://github.com/henriits/PomoTODOro/assets/121551949/df351710-ebdd-42ee-a040-1667c30eb5af)
</div>


