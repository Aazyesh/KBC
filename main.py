import random
import time

questions = [
    ["Current Railway Minister of India is", "Mamta Banarjee", "Ram Vilash", "Ashwini Vaishnaw", "Piyush Goyal", 3],
    ["Which god is also known as â€˜Gauri Nandanâ€™?", "Agni", "Indra", "Hanuman", "Ganesha", 4],
    ["What does not grow on tree according to a popular Hindi saying?", "Money", "Flowers", "Leaves", "Fruits", 1],
    ["Which city is known as the Pink City of India?", "Banglore", "Mysore", "Jaipur", "Kochi", 3],
    ["Who wrote India's National Anthem?", "Rabindranath Tagore", "Lal Bahadur Shastri", "Chetan Bhagat", "RK Narayan",
     1],
    ["How many major religions are there in India?", "6", "7", "8", "9", 1],
    ["When is the National Hindi Diwas celebrated?", "13 September", "14 September", "14 July", "15 August", 2],
    ["How many states are there in India?", "28", "29", "30", "31", 1],
    ["Where is India Gate located?", "Agra", "Punjab", "Mumbai", "New Delhi", 4],
    ["Who wrote Vande Mataram?", "Sarat Chandra Chattopadhyay", "Rabindranath Tagore", "Bankim Chandra Chatterjee",
     "Ishwar Chandra Vidyasagar", 3],
    ["Which one of the following places is famous for the Great Vishnu Temple?", "Bordubar, Indonesia",
     "Bamiyan, Afghanisthan", "Panja Sahib, Pakistan", "Ankorvat, Cambodia", 4],
    ["Where is the largest Buddhist Monastery in India located?", "Sarnath, Uttar Pradesh", "Tawang, Arunachal Pradesh",
     "Dharmashala, Himachal Pradesh", "Gangtok, Sikkim", 2],
    ["Who among the following was killed during 'Operation Bluestar' of 1984?", "Baba Santa Singh", "Haji Mastan",
     "Jarnail Singh Bhindrawale", "Homi Jehangir Bhabha", 3],
    ["Which former Indian President died as a result of a road accident?", "Rajendra Prasad", "Faqruddin Ali Ahmed",
     "Giani Zail Singh", "R. Venkatraman", 3],
    ["Who was the first Indian woman to win a medal in the Olympics?", "P.T. Usha", "Kunjarani Devi", "Bachendri Pal",
     "Karnam Maleshwari", 4],
    ["Which Mughal Emperor was deported to Rangoon by the British?", "Shah Jahan", "Bahadur Shah II", "Akbar Shah I",
     "Bahadur Shah I", 2],
    ["Which of the following is not a state of India?", "Vrindachal", "Goa", "Jharkhand", "Chattisgarh", 1]
]

level = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000,
         10000000, 75000000]
money = 0

nums = list(range(17))
random.shuffle(nums)

if __name__ == "__main__":
    for i in range(len(questions)):
        question = questions[nums[i]]
        print(f'Question for Rs.{level[i]} is:')
        time.sleep(1)
        print(question[0])
        print(f'1. {question[1]}')
        print(f'2. {question[2]}')
        print(f'3. {question[3]}')
        print(f'4. {question[4]}')
        inpt = input("Enter your answer: ")
        while True:
            try:
                if int(inpt) == 1 or int(inpt) == 2 or int(inpt) == 3 or int(inpt) == 4:
                    break
                else:
                    print("Please enter a valid input")
                    inpt = input("Enter your answer: ")
            except ValueError:
                print("Please enter a valid input")
                inpt = input("Enter your answer: ")

        if int(inpt) == question[-1]:
            print(f'Correct Answer :)\n\n')
            time.sleep(2)
            if i == 4:
                money = 10000
            elif i == 9:
                money = 320000
            elif i == 14:
                money = 7500000
            elif i == 16:
                money = 75000000
        else:
            print(f'Wrong answer :(\n\n')
            time.sleep(2)
            break
    else:
        print("Congrats you actually win KBC (99% tax deduction)")
    print(f'You win Rs. {money}')
