# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.


"""
C1, C2, D3, C4, D5, C6

All in FIFO
<- C1, C2, D3, C4, D5, C6 = QUEUE

KEEP ONLY DOGS AS THE NEXT ELEMEMT, dequeue all the rest

<- D3, C4, D5, C6 = QUEUE
<- C1, C2 = PRIO_QUEUE

If Pop D = Remove D from Queue, and empty all C until next D
If Pop C = Remove Prio Queue if any, else Prio Queue Become Dogs and we empty QUEUE until next D
If Pop Any = Pop Prio Queue if any, else Pop Queue

Reason = Prio queue will always have more ancient animals in order. If people want anything, you give one of it.
But if they want anything specific, you now have a queue for type 1 and prio queue for type 2. Of course,
the type that will have prio might change if prio is empty and someone ask the other type for its special request.
"""
from unittest import TestCase

from Chapter_3_StacksAndQueues.MyQueue import MyQueue


class Animal:
    i = 0

    def __init__(self):
        self.i = Animal.i
        Animal.i += 1

    def __repr__(self):
        return f"{self.i}:{type(self).__name__}"


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:

    def __init__(self):
        self.queue: MyQueue = MyQueue()
        self.prio_queue: MyQueue = MyQueue()
        self.prio_queue_type = None

    def enqueue(self, animal: Animal):
        self.queue.queue(animal)

    def dequeue_any(self):
        if self.prio_queue.is_empty():
            return self.queue.dequeue()
        return self.prio_queue.dequeue()

    def dequeue_wanted_type(self, wanted_type, other_type):
        if self.prio_queue_type == wanted_type and not self.prio_queue.is_empty():
            return self.prio_queue.dequeue()
        # Either we have a prio queue for Dogs, either the prio queue is empty, In both case, just put all dogs at the top in the prio queue and set the prio type to Dog
        self.prio_queue_type = other_type
        while type(self.queue.peek()) == other_type:
            self.prio_queue.queue(self.queue.dequeue())
        return self.queue.dequeue()

    def dequeue_cat(self):
        return self.dequeue_wanted_type(Cat, Dog)

    def dequeue_dog(self):
        return self.dequeue_wanted_type(Dog, Cat)


class TestCase(TestCase):
    def test(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat()) # 0
        shelter.enqueue(Dog()) # 1
        shelter.enqueue(Dog()) # 2
        shelter.enqueue(Cat()) # 3
        shelter.enqueue(Dog()) # 4
        shelter.enqueue(Cat()) # 5

        self.assertEqual(0, shelter.dequeue_any().i)
        self.assertEqual(1, shelter.dequeue_any().i)
        self.assertEqual(3, shelter.dequeue_cat().i)
        self.assertEqual(2, shelter.dequeue_any().i)
        self.assertEqual(4, shelter.dequeue_dog().i)
        self.assertEqual(5, shelter.dequeue_cat().i)
