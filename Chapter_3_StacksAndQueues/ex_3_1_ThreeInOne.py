import unittest


class NStack:

    def __init__(self, bucket_nbr, bucket_size):
        self.bucket_nbr = bucket_nbr  # eg : 3
        self.bucket_size = bucket_size  # eg : 10
        self.tab = [None] * bucket_size * bucket_nbr  # eg : 30
        self.heads = [i*self.bucket_size for i in range(self.bucket_nbr)]  # [0, 10, 20]


    def next_head(self, bucket_i):
        new_head = bucket_i * self.bucket_size + (self.heads[bucket_i] + 1) % self.bucket_size
        self.heads[bucket_i] = new_head
        return new_head

    def previous_head(self, bucket_i):
        new_head = bucket_i * self.bucket_size + (self.heads[bucket_i] - 1) % self.bucket_size
        self.heads[bucket_i] = new_head
        return new_head

    def push(self, bucket, value):
        if self.tab[self.heads[bucket]]:
            new_head = self.next_head(bucket)
        else:
            new_head = self.heads[bucket]
        if self.tab[new_head]:
            self.previous_head(bucket)
            raise ValueError(f"Bucket {bucket} max size met")
        else:
            self.tab[new_head] = value

    def peek(self, bucket):
        return self.tab[self.heads[bucket]]

    def pop(self, bucket):
        value = self.tab[self.heads[bucket]]
        if value is None:
            raise ValueError(f"No more element to pop in bucket {bucket}")
        self.tab[self.heads[bucket]] = None
        self.previous_head(bucket)
        return value

    def isEmpty(self, bucket):
        return self.peek(bucket) is None


class TestStringMethods(unittest.TestCase):
    def test_threeinone(self):
        nstack = NStack(3,5)
        for i in range(3):
            nstack.push(i,1+10*i)
            nstack.push(i,2+10*i)
            nstack.push(i,3+10*i)
            nstack.push(i,4+10*i)
            nstack.push(i,5+10*i)
        self.assertEqual([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25], nstack.tab)
        self.assertRaises(ValueError, lambda: nstack.push(0, 6))
        self.assertEqual(5, nstack.peek(0))
        self.assertEqual(15, nstack.peek(1))
        self.assertEqual(25, nstack.peek(2))
        for i in range(3):
            self.assertEqual(5+10*i, nstack.pop(i))
            self.assertEqual(4+10*i, nstack.pop(i))
            self.assertEqual(3+10*i, nstack.pop(i))
            self.assertEqual(2+10*i, nstack.pop(i))
            self.assertEqual(1+10*i, nstack.pop(i))
        self.assertEqual([None] * 15, nstack.tab)
        self.assertRaises(ValueError, lambda: nstack.pop(0))
        self.assertRaises(ValueError, lambda: nstack.pop(1))
        self.assertRaises(ValueError, lambda: nstack.pop(2))


if __name__ == '__main__':
    unittest.main()
