
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    def __init__(self, file_path="state.json"):
        self.quizzes = []
        self.high_score = 0
        self.file_path = file_path

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)


game1 = QuizGame()

quiz1 = Quiz(
    "Python 파일의 확장자는?",
    [".txt", ".py", ".java", ".html"],
    2
)
game1.add_quiz(quiz1)
quiz2 = Quiz(
    "Python에서 화면에 글자를 출력하는 함수는?",
    ["input", "print", "len", "type"],
    2
)
game1.add_quiz(quiz2)
quiz3 = Quiz(
    "Python에서 반복문을 만드는 키워드는?",
    ["if", "for", "def", "class"],
    2
)
game1.add_quiz(quiz3)
quiz4 = Quiz(
    "Python에서 함수를 정의하는 키워드는?",
    ["for", "return", "def", "while"],
    3
)
game1.add_quiz(quiz4)
quiz5 = Quiz(
    "Python에서 리스트를 나타내는 기호는?",
    ["()", "{}", "[]", "<>"],
    3
)
game1.add_quiz(quiz5)


def play_quiz():
    score = 0

    for quiz in game1.quizzes:
        print(quiz.question)

        for number, option in enumerate(quiz.options, start=1):
            print(f"{number}. {option}")

        user_answer = input("정답 번호를 입력하세요 (1~4): ")

        if user_answer == str(quiz.answer):
            print("정답입니다!")
            score += 1
        else:
            print("오답입니다!")

    print(f"최종점수: {score}점")



def add_new_quiz():
    print("\n=== 새로운 퀴즈 추가 ===")

    question = input("문제를 입력하세요: ")

    options = []

    for number in range(1, 5):
        option = input(f"{number}번 선택지: ")
        options.append(option)

    answer = int(input("정답 번호를 입력하세요 (1~4): "))

    new_quiz = Quiz(question, options, answer)
    game1.add_quiz(new_quiz)

    print("새로운 퀴즈가 등록되었습니다!")


while True:
    print("\n===== Python 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 문제 추가")
    print("3. 문제 목록 확인")
    print("4. 최고 점수 확인")
    print("5. 종료")

    menu = input("메뉴 번호를 선택하세요: ")

    
    if menu == "1":
        play_quiz()


    elif menu == "2":
        add_new_quiz()


    elif menu == "3":
        print("\n=== 등록된 퀴즈 목록 ===")

        for number, quiz in enumerate(game1.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    elif menu == "5":
        print("게임을 종료합니다.")
        break

    else:
        print("선택한 메뉴:", menu)