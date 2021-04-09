from vocabulary import words_list
import random
import operator

WORDS = 30

fails = {}


sesion = {}



def report():
    results = sorted(fails.items(), key=operator.itemgetter(1), reverse=True)
    for fail in enumerate(results):
        if fails[fail[1][0]] == 0:
            break
        print(fail[1][0], ' : ', fails[fail[1][0]])


def load_sesion(sesion):
    file = open("sesion.txt", "r")
    for line in file.readlines():
        parts = line.split(";")
        sesion[parts[0]] = {"success": int(parts[1]), "fails": int(parts[2])}
    file.close()


def close_sesion(sesion):
    file = open("sesion.txt", "w")
    for key in sesion.keys():
        file.write("{};{};{}\n".format(key, sesion[key]["success"], sesion[key]["fails"]))
    file.close()


def main(sesion):
    load_sesion(sesion)
    fails_counter = 0
    for word in words_list:
        fails[word[0]] = 0
        if word[0] not in sesion:
            sesion[word[0]] = {"success": 0, "fails": 0}
    #import pdb; pdb.set_trace()
    words_stats = sorted(sesion.items(), key=lambda x: x[1]["fails"] - x[1]["success"], reverse=True)
    training_words = [word[0] for word in words_stats]  # English words in order
    training_list = []
    for target_word in training_words:
        for word in words_list:
            if target_word == word[0]:
                training_list.append(word)
                break
        if len(training_list) == WORDS:
            break

    try:
        while training_list:
            random.shuffle(training_list)
            test = training_list.pop()
            answer = input("\n" + test[1] + "\n")
            if answer.lower() != test[0].lower():
                print("FAIL")
                print("{} -> {}".format(test[1], test[0]))
                training_list.append(test)
                fails_counter += 1
                sesion[test[0]]["fails"] += 1
                fails[test[0]] += 1
            else:
                print("SUCCESS")
                sesion[test[0]]["success"] += 1
    except KeyboardInterrupt:
        pass

    print("\nFINISH\n")
    print("Fails {}:".format(fails_counter))
    report()
    close_sesion(sesion)

main(sesion)