import json

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

    if score > game1.high_score:
        game1.high_score = score
        print("새로운 최고 점수입니다!")
        save_quizzes()


def add_new_quiz():
    print("\n=== 새로운 퀴즈 추가 ===")

    question = input("문제를 입력하세요: ")

    options = []

    for number in range(1, 5):
        option = input(f"{number}번 선택지: ")
        options.append(option)

    while True:
        try:
            answer =  int(input("정답 번호를 입력하세요. (1~4): "))

            if 1 <= answer <= 4:
                break
            else:
                print("1~4 사이의 숫자를 입력해주세요.")
        
        except ValueError:
            print("숫자만 입력해주세요.")
 
    new_quiz = Quiz(question, options, answer)
    game1.add_quiz(new_quiz)

    print("새로운 퀴즈가 등록되었습니다!")

def save_quizzes():
    quiz_data = []

    for quiz in game1. quizzes:
        quiz_data.append({
            "question": quiz.question,
            "options": quiz.options,
            "answer": quiz.answer
        })

    data = {
        "high_score": game1.high_score,
        "quizzes": quiz_data
    }

    with open("state.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


    print("퀴즈와 최고 점수가 저장되었습니다!")

def load_quizzes():
    try:
        with open("state.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            quiz_data = data
            game1.high_score = 0
        else:
            quiz_data =data["quizzes"]
            game1.high_score = data.get("high_score", 0)
        
        game1.quizzes = [] 

        for item in quiz_data:
            quiz = Quiz(
                item["question"],
                item["options"],
                item["answer"],
            )
            game1.add_quiz(quiz)

        print("퀴즈와 최고 점수를 불러왔습니다!")

    except FileNotFoundError:
        print("저장된 파일이 없어 기본 퀴즈를 사용합니다.")

load_quizzes()

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
        save_quizzes()

    elif menu == "3":
        print("\n=== 등록된 퀴즈 목록 ===")

        for number, quiz in enumerate(game1.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    elif menu == "4":
        print(f"현재 최고 점수: {game1.high_score}점")

    elif menu == "5":
        save_quizzes()
        print("게임을 종료합니다.")
        break

    else:
        print("선택한 메뉴:", menu)