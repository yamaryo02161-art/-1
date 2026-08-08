import random


def main():
    print("=== 数字当てゲーム ===")
    print("コンピューターが1〜100の間で数字を1つ選びました。")
    print("その数字を当ててみてください！\n")

    answer = random.randint(1, 100)
    attempts = 0

    while True:
        guess_input = input("数字を入力してください: ")

        if not guess_input.isdigit():
            print("1〜100の整数を入力してください。\n")
            continue

        guess = int(guess_input)

        if guess < 1 or guess > 100:
            print("1〜100の範囲で入力してください。\n")
            continue

        attempts += 1

        if guess < answer:
            print("もっと大きい数字です。\n")
        elif guess > answer:
            print("もっと小さい数字です。\n")
        else:
            print(f"正解！ {attempts}回目で当てました。おめでとうございます！")
            break


if __name__ == "__main__":
    main()
