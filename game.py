class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = {}

    def connect(self, direction, room):
        self.connected_rooms[direction] = room

class DarkRotationGame:
    def __init__(self):
        self.start_room = None
        self.current_room = None
        self.create_map()

    def create_map(self):
        # Initialize rooms
        start_room = Room("기상실", "이곳은 게임이 시작되는 곳이다. 차가운 금속 침대가 있다.")
        hallway = Room("복도", "중앙 복도. 여러 방으로 갈 수 있을 것 같다.")
        lab = Room("실험실", "실험실이다. 다양한 퍼즐과 단서가 숨겨져 있다.")
        security = Room("보안실", "보안실이다. 보안 시스템을 무력화할 수 있을지 모른다.")
        meeting = Room("비밀 회의실", "중요한 정보가 있을지 모른다.")
        exit_room = Room("탈출 구역", "탈출구로 갈 수 있는 마지막 통로.")

        # Connect rooms
        start_room.connect("south", hallway)
        hallway.connect("west", security)
        hallway.connect("east", lab)
        security.connect("south", meeting)
        lab.connect("south", exit_room)

        self.start_room = start_room
        self.current_room = start_room

    def play(self):
        print("Dark Rotation: 무한 감옥에 오신 것을 환영합니다.")
        while True:
            print(f"\n현재 위치: {self.current_room.name}")
            print(self.current_room.description)

            action = input("방향 선택 (south, east, west, exit): ").strip().lower()
            if action == "exit":
                print("게임을 종료합니다. 안녕히 가세요!")
                break

            if action in self.current_room.connected_rooms:
                self.current_room = self.current_room.connected_rooms[action]
            else:
                print("그 방향으로는 갈 수 없습니다.")

if __name__ == "__main__":
    game = DarkRotationGame()
    game.play()