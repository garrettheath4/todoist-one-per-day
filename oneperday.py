import configparser
import random
import todoist

def get_opd_label(api):
    l = list(filter(lambda l: l['name'] == 'one-per-day', api.state['labels']))
    if len(l) == 0:
        return None
    else:
        return l[0]

def get_opd_tasks(api):
    opd = get_opd_label(api)
    if opd == None:
        return None
    return list(filter(lambda i: opd['id'] in i['labels'], api.state['items']))

def schedule_one(api):
    opd_tasks = get_opd_tasks(api)
    if opd_tasks == None or len(opd_tasks) == 0:
        return None
    random.shuffle(opd_tasks)
    api.items.update(opd_tasks[0]['id'], due={'string': 'today'})
    for unschedule_me in [task for task in opd_tasks[1:] if task['due']]:
        api.items.update(unschedule_me['id'], due=None)
    api.commit()

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config['Todoist']['token']

    api = todoist.TodoistAPI(token)
    api.sync()
    schedule_one(api)

if __name__ == '__main__':
    main()
