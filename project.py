from time import sleep
import abb
import sys

if __name__ == '__main__':
    R = abb.Robot(ip='192.168.125.1')
    for timeout_count in range(10):
        if R == None :
            sleep(5)
            print('Reconnecting...', timeout_count + 1, ' try!')
            R = abb.Robot(ip='192.168.125.1')
        else :
            print('Robot Connected!')
            break
    if R == None:
        print('Failed To Connect!')
        sys.exit()
    pose = R.get_cartesian()[0]
    print(pose)
    pose[2] += 30
    # index 0 正數: 往自己移動
    # index 1 正數: 往右移動
    # index 2 正數: 往上移動
    R.set_joints([pose, [0,0,1,0]])
    sleep(3)
    pose = R.get_cartesian()[0]
    print(pose)