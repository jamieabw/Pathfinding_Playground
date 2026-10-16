from screen_manager import Screen_Manager
from map import Map

def main():
    screen_manager = Screen_Manager(Map)
    screen_manager.run()

if __name__ == "__main__":
    main()