import qiskit
import module1.utils as util
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':
    util.important_func()
    plt.plot(range(10), range(10))
    plt.show()
    if not os.path.exists("test"):
        os.makedirs("test", exist_ok=True)
    print("2")

    util.save_as_json({"data": "2", "name": "test"}, "test", "test")

