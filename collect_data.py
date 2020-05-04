import numpy as np
import cv2
from Autonomous_Driving.get_screen import grab_screen


def get_data():
    training_data = []
    number = 1
    # paused = True
    while True:
        screen = grab_screen(region=(0, 30, 800, 630))
        screen = cv2.resize(screen, (299, 299))
        training_data.append(screen)
        if len(training_data) == 5:
            file = 'D:/PycharmProjects/Self_Driving/Autonomous_Driving/data/training_data-{}.npy'.format(number)
            np.save(file, training_data)
            training_data = []
            print('Appended 5')
            number += 1
        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
