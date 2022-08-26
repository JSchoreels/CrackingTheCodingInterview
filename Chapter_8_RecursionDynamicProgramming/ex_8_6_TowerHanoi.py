# Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
# constraints


def towers_hanoi(tower_1, tower_2, tower_3):
    def move(n, src, dest, buffer):
        if n == 1:
            elt = src.pop()
            dest.append(elt)
        else:
            move(n-1, src, buffer, dest)
            move(1, src, dest, buffer)
            move(n-1, buffer, dest, src)
    move(len(tower_1), tower_1, tower_2, tower_3)

tower_1 = [5,3,2,1,0]
tower_2 = []
tower_3 = []
towers_hanoi(tower_1, tower_2, tower_3)
print(tower_1)
print(tower_2)
print(tower_3)