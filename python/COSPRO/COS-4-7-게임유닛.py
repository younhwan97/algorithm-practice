class Unit:
    def __init__(self):
        self.HP = 1000
    def under_attack(self, damage):
        pass

class Monster(Unit):
    def __init__(self, attack_point):
        super().__init__()
        self.attack_point = attack_point
    def under_attack(self, damage):
        self.HP -= damage
    def attack(self):
        return self.attack_point

class Warrior(Unit):
    def __init__(self, attack_point):
        super().__init__()
        self.attack_point = attack_point
    def under_attack(self, damage):
        self.HP -= damage
    def attack(self):
        return self.attack_point

class Healer(Unit):
    def __init__(self, healing_point):
        super().__init__()
        self.healing_point = healing_point
    def under_attack(self, damage):
        self.HP -= damage
    def healing(self, unit):
        unit.HP += self.healing_point


def solution(monster_attack_point, warrior_attack_point, healing_point):
    monster = Monster(monster_attack_point)
    warrior = Warrior(warrior_attack_point)
    healer = Healer(healing_point)

    # 전사가 몬스터를 한 번 공격
    monster.under_attack(warrior.attack())
    # 몬스터가 전사를 한 번 공격
    warrior.under_attack(monster.attack())
    # 몬스터가 힐러를 한 번 공격
    healer.under_attack(monster.attack())
    # 힐러가 전사의 체력을 한 번 회복
    healer.healing(warrior)
    # 힐러가 몬스터의 체력을 한 번 회복
    healer.healing(monster)

    answer = [monster.HP, warrior.HP, healer.HP]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
monster_attack_point = 100
warrior_attack_point = 90
healing_point = 30
ret = solution(monster_attack_point, warrior_attack_point, healing_point)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")