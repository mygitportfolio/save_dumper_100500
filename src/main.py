import datetime
from time import sleep
from publisher.PushSave import PushSaveDispatcher
from Subsribers.WindowsLocalDumper import LocalDumper
from config import settings_map as state


def fun():
    dispatcher = PushSaveDispatcher()
    dispatcher.add_subscriber(LocalDumper)
    dump_dir = state['dump_dir']
    while 1:
        state['dump_dir'] = dump_dir + '\\' + datetime.datetime.now().strftime('%y%m%H%M%S')
        dispatcher.dispatch_save(state)
        print(state)
        sleep(state['frequency'])


fun()
