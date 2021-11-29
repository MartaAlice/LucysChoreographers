import math
import subprocess
import time

def main():
    robot_ip = "127.0.0.1"
    robot_port = 37573
    move = "AirGuitar"
    print("Executing: " + move + "... ")
    python2_command = "python2 ./" + move + ".py  " + robot_ip + " " + str(robot_port)
    start_move = time.time()
    process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
    end_move = time.time()
    print(end_move-start_move)
    move = "Crouch"
    print("Executing: " + move + "... ")
    python2_command = "python2 ./" + move + ".py  " + robot_ip + " " + str(robot_port)
    start_move = time.time()
    process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
    end_move = time.time()
    print(end_move-start_move)

if __name__ == "__main__":
	main()
