TASKS_LIST = [
    {
        "name": "Write Task class",
        "priority": "high",
        "is_completed": True
    },
    {
        "name": "Implement list printing",
        "priority": "high",
        "is_completed": False
    },
    {
        "name": "Logic for open tasks",
        "priority": "medium",
        "is_completed": False
    },
    {
        "name": "Document Clean Code",
        "priority": "low",
        "is_completed": True
    },
    {
        "name": "Daily summary validation",
        "priority": "medium",
        "is_completed": False
    }
]
MENU = '''
press 1 to show all tasks
press 2 to see how many tasks are open
press 3 to see how many tasks completed
press 4 to see how many tasks are high priority
press 5 to see daily summery
press 6 to exit
'''

def show_mission(task: dict) -> str:
    return f'''
    the mission name: {task['name']} 
    the priority: {task['priority']}
    is completed: {'yes' if task['is_completed'] else 'no'}
    
    '''

def show_all_missions(_tasks_list: list[dict]) -> str:
    all_tasks = ''
    for task in _tasks_list:
        all_tasks += show_mission(task)
    return all_tasks

def calculate_missions_completed(_tasks_list: list[dict]) -> int:
    completed_counter = 0
    for task in _tasks_list:
        if task['is_completed']:
            completed_counter += 1
    return completed_counter

def calculate_missions_not_completed(_tasks_list: list[dict]) -> int:
    not_completed_counter = 0
    for task in _tasks_list:
        if not task['is_completed']:
            not_completed_counter += 1
    return not_completed_counter

def high_priority_missions(_tasks_list: list[dict]) -> int:
    high_priority = 0
    for task in _tasks_list:
        if task['priority'] == 'high':
            high_priority += 1
    return high_priority

def daily_summery(_tasks_list: list[dict]) -> str:
    summery = f'''
    the number if tasks is: {len(_tasks_list)}
    the number of open tasks is: {calculate_missions_not_completed(_tasks_list)}
    the number of completed tasks: {calculate_missions_completed(_tasks_list)}
    the number of high priority tasks is: {high_priority_missions(_tasks_list)}
    '''
    return summery

def get_valid_input() -> str:
    while True:
        _choice = input('Enter your choice: ')
        if _choice in '123456' and len(_choice) == 1:
            final_choice = _choice
            break
        else:
            print('you have to choose from the menu')
    return final_choice



dict_of_function = {
    '1': show_all_missions,
    '2': calculate_missions_not_completed,
    '3': calculate_missions_completed,
    '4': high_priority_missions,
    '5': daily_summery,
}


def main(_tasks_list: list[dict]) -> None:
    while True:
        print(MENU)
        _choice = get_valid_input()
        if _choice == '6':
            print('bay bay')
            break
        print(dict_of_function[_choice](_tasks_list))


if __name__ == '__main__':
    main(TASKS_LIST)

