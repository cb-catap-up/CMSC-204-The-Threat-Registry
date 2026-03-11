from BinarySearchTree import BST 
from AVLTree import AVL
import time

class Application():
    def __init__(self):
        super().__init__

    def clear_console(self):
        print('\033c', end='')

    def start_screen():
        START_SCREEN = """
                ╔════════════════════════════════════════════════════════════╗
                ║                                                            ║
                ║               THE THREAT REGISTRY                          ║
                ║                                                            ║
                ║                    🏥 📋 👥                                ║
                ║                                                            ║
                ║                                                            ║
                ║                                                            ║
                ╚════════════════════════════════════════════════════════════╝
                """
        print(f'{START_SCREEN}\n')

        DESCRIPTION = """
            AVL Tree
            """

        print(f'{DESCRIPTION}\n')

    def application(self):
        print('Press 1 to insert all your 8 keys')
        print('Press 2 to insert one at a time')
        answer = input(': ')

        if answer == '1':
            self.menu_answer_1(answer)

         


        # keys = []
        # answer = [input('Please insert your eight (8) keys: ')]
        # for i in answer:
        #     print(i)

    def menu_answer_1(self, answer, num_key=8):
        self.clear_console()
        while True:
            answer = (input(f"""Please insert all your {num_key} keys and separate them by a comma (You can try 2,5,3,0,1,0,4,6): """))

            if answer == 'y':
                new_answer = [2,5,3,0,1,0,4,6]
                break

            answer = answer.split(',')
            new_answer = []
            for i in answer:
                try:
                    new_answer.append(int(i.strip()))
                except:
                    print('Make sure to input numerical values only (e.g., 90,432,12,4,4)')
            if len(answer) == num_key:
                break
            else:
                print(f'\nPlease make sure to insert {num_key} keys')

        bst_start = BST()
        for key in new_answer:
            bst_start.insert(key)

        while True:
            print('Press 1 if you want to continue and balance the BST to AVL Tree.')
            print('Press 2 if you want to add additional keys.')

            answer = input(': ') 
            if answer == '2':
                try:
                    answer = int(input('Input your new key: '))
                    new_answer.append(answer)
                    bst_start.insert(answer)
                    print(f'{answer} is successfully inserted')
                except:
                    print('Make sure to add numerical values only.')
            
            elif answer == '1':
                self.clear_console()
                break
            else:
                print('Please make sure to enter 1 or 2 only')

        print(new_answer)

        avl_start = AVL()
        for key in new_answer:
            # print(f"\nInserting {key}:")
            avl_start.insert(key)

     


if __name__ == "__main__":
    start = Application()
    start.clear_console()
    Application.start_screen()
    start = Application()
    start.application() 