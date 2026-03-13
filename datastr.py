# To do list dengan menggunakan linked list. Muhammad Bevan Alqarana 25110500020.
# Membuat class node
class Node:
    def __init__(self, id, nama, desc):
        self.id = id
        self.nama = nama
        self.desc = desc
        self.next = None

# Masuk ke linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None

# Buat node baru di depan
    def insert_front(self, id, nama, desc):
        new_node = Node(id, nama, desc)
        new_node.next = self.head
        self.head = new_node

# Buat node baru di belakang
    def insert_end(self, id, nama, desc):
        new_node = Node(id, nama, desc)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

# Menghapus node berdasarkan id
    def delete(self, target):
        if self.head is None:
            return
        if self.head.id == target:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.id != target:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

# Mencari dan mengecek node berdasarkan id 
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.id == target:
                return index
            current = current.next
            index += 1
        return -1 # Invalid / Ga nemu
    
# Menghitung total node 
    def count(self):
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total

# Ngeprint semua node dari head sampai habis
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.id, current.nama, current.desc)   
            current = current.next
        print("Habis")
    
# Buat node template 
nodeA = Node(1, 'Mandi :', 'Mandi pagi hari')
nodeB = Node(2, 'Belajar :', 'Rangkum soal ujian')
nodeC = Node(3, 'Hangout :', 'Janji hangout sama temen')

# Menghubungkan antar node
nodeA.next = nodeB
nodeB.next = nodeC

# Head node pertama, integrasi dengan linked list
head = nodeA
daftar = SinglyLinkedList()
daftar.head = nodeA


# Print linked list sebelum modifikasi
def print_list(head):
    current = head
    while current is not None: #looping
        print(current.id, current.nama, current.desc) #print id nama desc sampai habis
        current = current.next
    print("Habis")

print('To Do List :')
print_list(head)

daftar.insert_front(0, 'Meeting :', 'Rapat jam 8') # masukin node baru di depan
daftar.insert_end(4, 'Tidur :', 'Bobo jam 10 malem') # masukin node baru di belakang
daftar.delete(2) # Hapus node dengna id 2
print('Search ID 3, index ke:', daftar.search(3)) # cari node dengan id 3 lalu ngeprint indexnya
print('Jumlah tugas:', daftar.count()) # ngeprint jumlah node 

print('\n')
print('To Do List setelah modifikasi :') 
daftar.traverse() 