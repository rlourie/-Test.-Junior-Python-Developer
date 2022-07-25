def prepare_pupil(data):
    pupil = data['pupil']
    while check_pupil(data) is not True:
        for i in range(1, len(pupil), 2):
            if i >= len(pupil) - 1:
                break
            if pupil[i + 1] <= pupil[i] <= pupil[i + 2]:
                del pupil[i]
                del pupil[i]
            else:
                for j in range(i + 1, len(pupil) - 1, 2):
                    if j >= len(pupil) - 1:
                        break
                    if pupil[i] >= pupil[j]:
                        del pupil[j]
                        del pupil[j]
                    else:
                        break
        if pupil[0] < data['lesson'][0]:
            pupil[0] = data['lesson'][0]
        if pupil[len(pupil) - 1] > data['lesson'][1]:
            pupil[len(pupil) - 1] = data['lesson'][1]
    return pupil


def prepare_tutor(data):
    tutor = data['tutor']
    while check_tutor(data) is not True:
        for i in range(1, len(tutor), 2):
            if i >= len(tutor) - 1:
                break
            if tutor[i + 1] <= tutor[i] <= tutor[i + 2]:
                del tutor[i]
                del tutor[i]
            else:
                for j in range(i + 1, len(tutor) - 1, 2):
                    if j >= len(tutor) - 1:
                        break
                    if tutor[i] >= tutor[j]:
                        del tutor[j]
                        del tutor[j]
                    else:
                        break
    if tutor[0] < data['lesson'][0]:
        tutor[0] = data['lesson'][0]
    if tutor[len(tutor) - 1] > data['lesson'][1]:
        tutor[len(tutor) - 1] = data['lesson'][1]
    return tutor


def check_pupil(data):
    pupil = data['pupil']
    for i in range(1, len(pupil) - 2, 2):
        if pupil[i] >= pupil[i + 1]:
            return False
    return True


def check_tutor(data):
    tutor = data['tutor']
    for i in range(1, len(tutor) - 2, 2):
        if tutor[i] >= tutor[i + 1]:
            return False
    return True


def appearance(data):
    events = []
    for k in data:
        ev = data[k]
        for i in range(len(ev)):
            events.append((ev[i], 1 - 2 * (i % 2)))  # +-1 для чётного и нечетного индекса
    events.sort()
    count = 0
    start = -1
    result_time = 0
    for event in events:
        count += event[1]
        if count == 3:
            start = event[0]
        if count == 2 and start > 0:
            result_time += event[0] - start
            start = -1
    return result_time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        pupil = prepare_pupil(test['data'])
        tutor = prepare_tutor(test['data'])
        test['data']['pupil'] = pupil
        test['data']['tutor'] = tutor
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
