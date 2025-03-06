import time
import pyautogui
import os, ctypes


try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if(is_admin == False):
    print('Please Run Script as Administrator')
    exit()

screen_width, screen_height = pyautogui.size()
lock_in_x, lock_in_y = 0, 0
if screen_width == 2560:
    lock_in_x = 1265
    lock_in_y = 1000
if screen_width == 1920:
    lock_in_x = 950
    lock_in_y = 750
if screen_width == 1280:
    lock_in_x = 635
    lock_in_y = 500

def wait():
    os.system('cls')
    print('1. Astra')
    print('2. Breach')
    print('3. Brimstone')
    print('4. Chamber')
    print('5. Clove')
    print('6. Cypher')
    print('7. Deadlock')
    print('8. Fade')
    print('9. Gekko')
    print('10. Harbor')
    print('11. Iso')
    print('12. Jett')
    print('13. Kayo')
    print('14. Killjoy')
    print('15. Neon')
    print('16. Omen')
    print('17. Phoenix')
    print('18. Raze')
    print('19. Reyna')
    print('20. Sage')
    print('21. Skye')
    print('22. Sova')
    print('23. Tejo')
    print('24. Viper')
    print('25. Vyse')
    print('26. Waylay')
    print('27. Yoru')
    print()
    agent = input('Select The Agent You Want To Instalock: ')
    agent = int(agent)
    if agent == 1 or str(agent).lower() == 'astra':
        choose_agent('astra', 'controller')
    if agent == 2 or str(agent).lower() == 'breach':
        choose_agent('breach', 'initiator')
    if agent == 3 or str(agent).lower() == 'brimstone':
        choose_agent('brimstone', 'controller')
    if agent == 4 or str(agent).lower() == 'chamber':
        choose_agent('chamber', 'sentinel')
    if agent == 5 or str(agent).lower() == 'clove':
        choose_agent('clove', 'controller')
    if agent == 6 or str(agent).lower() == 'cypher':
        choose_agent('cypher', 'sentinel')
    if agent == 7 or str(agent).lower() == 'deadlock':
        choose_agent('deadlock', 'sentinel')
    if agent == 8 or str(agent).lower() == 'fade':
        choose_agent('fade', 'initiator')
    if agent == 9 or str(agent).lower() == 'gecko':
        choose_agent('gecko', 'initiator')
    if agent == 10 or str(agent).lower() == 'harbor':
        choose_agent('harbor', 'controller')
    if agent == 11 or str(agent).lower() == 'iso':
        choose_agent('iso', 'duelist')
    if agent == 12 or str(agent).lower() == 'jett':
        choose_agent('jett', 'duelist')
    if agent == 13 or str(agent).lower() == 'kayo':
        choose_agent('kayo', 'initiator')
    if agent == 14 or str(agent).lower() == 'killjoy':
        choose_agent('killjoy', 'sentinel')
    if agent == 15 or str(agent).lower() == 'neon':
        choose_agent('neon', 'duelist')
    if agent == 16 or str(agent).lower() == 'omen':
        choose_agent('omen', 'controller')
    if agent == 17 or str(agent).lower() == 'phoenix':
        choose_agent('phoenix', 'duelist')
    if agent == 18 or str(agent).lower() == 'raze':
        choose_agent('raze', 'duelist')
    if agent == 19 or str(agent).lower() == 'reyna':
        choose_agent('reyna', 'duelist')
    if agent == 20 or str(agent).lower() == 'sage':
        choose_agent('sage', 'sentinel')
    if agent == 21 or str(agent).lower() == 'skye':
        choose_agent('skye', 'initiator')
    if agent == 22 or str(agent).lower() == 'sova':
        choose_agent('sova', 'initiator')
    if agent == 23 or str(agent).lower() == 'tejo':
        choose_agent('tejo', 'initiator')
    if agent == 24 or str(agent).lower() == 'viper':
        choose_agent('viper', 'controller')
    if agent == 25 or str(agent).lower() == 'vyse':
        choose_agent('vyse', 'sentinel')
    if agent == 26 or str(agent).lower() == 'waylay':
        choose_agent('waylay', 'duelist')
    if agent == 27 or str(agent).lower() == 'yoru':
        choose_agent('yoru', 'duelist')

def lock_in_agent():
    time.sleep(0.1)
    pyautogui.moveTo(x=lock_in_x, y=lock_in_y, duration=0.1)
    time.sleep(0.1)
    pyautogui.tripleClick(interval=0.1)
    time.sleep(85)

def filter_agent_class(agent_class):
    agent_class = pyautogui.locateOnScreen('./images/' + agent_class + '.png', confidence = 0.8)
    if (agent_class != None):
        pyautogui.moveTo(960, 865, duration=0.2)
        time.sleep(0.1)
        pyautogui.doubleClick(agent_class)
        time.sleep(0.1)

def choose_agent(agent_name, role):
    waiting_agent(agent_name)
    while True:
        try:
            filter_agent_class(role)
        except:
            pass

        try:
            agent = pyautogui.locateOnScreen(f'./images/{agent_name}.png', confidence=0.8)
        except:
            agent = None

        if agent is not None:
            time.sleep(0.1)
            pyautogui.moveTo(960, 865)
            pyautogui.tripleClick(agent, duration=0.2, tween=pyautogui.easeOutQuad)

            lock_in_agent()

def waiting_agent(agent_name):
    print(f'Waiting On Agent Select for {agent_name}...')
    print()
    return

wait()