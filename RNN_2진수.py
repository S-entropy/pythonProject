import numpy as np
import matplotlib.pyplot as plt

n_time = 8
n_in = 2
n_mid = 32
n_out = 1

eta = 0.01
n_learn = 5001
interval = 500

max_num = 2 ** n_time

binaries = np.zeros((max_num, n_time), dtype=int)
for i in range(max_num):
    num10 = i
    for j in range(n_time):
        pow2 = 2 ** (n_time - 1 - j)
        binaries[i, j] = num10 // pow2
        num10 %= pow2


class SimpleRNNLayer:
    def __init__(self, n_upper, n):
        self.w = np.random.randn(n_upper, n) / np.sqrt(n_upper)
        self.v = np.random.randn(n, n) / np.sqrt(n)
        self.b = np.zeros(n)

    def forward(self, x, y_prev):
        u = np.dot(x, self.w) + np.dot(y_prev, self.v) + self.b
        self.y = np.tanh(u)

    def backward(self, x, y, y_prev, grad_y):
        delta = grad_y * (1 - y ** 2)

        self.grad_w += np.dot(x.T, delta)
        self.grad_v += np.dot(y_prev.T, delta)
        self.grad_b += np.sum(delta, axis=0)

        self.grad_x = np.dot(delta, self.w.T)
        self.grad_y_prev = np.dot(delta, self.v.T)

    def reset_sum_grad(self):
        self.grad_w = np.zeros_like(self.w)
        self.grad_v = np.zeros_like(self.v)
        self.grad_b = np.zeros_like(self.b)

    def update(self, eta):
        self.w -= eta * self.grad_w
        self.v -= eta * self.grad_v
        self.b -= eta * self.grad_b


# 전결합 출력층
class RNNOutputLayer:
    def __init__(self, n_upper, n):
        self.w = np.random.randn(n_upper, n) / np.sqrt(n_upper)
        self.b = np.zeros(n)

    def forward(self, x):
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = 1 / (1 + np.exp(-u))

    def backward(self, x, y, t):
        delta = (y - t) * y * (1 - y)
        self.grad_w += np.dot(x.T, delta)
        self.grad_b += np.sum(delta, axis=0)
        self.grad_x = np.dot(delta, self.w.T)

    def reset_sum_grad(self):
        self.grad_w = np.zeros_like(self.w)
        self.grad_b = np.zeros_like(self.b)

    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b


rnn_layer = SimpleRNNLayer(n_in, n_mid)
output_layer = RNNOutputLayer(n_mid, n_out)


def train(x_mb, t_mb):
    y_rnn = np.zeros((len(x_mb), n_time + 1, n_mid))
    y_out = np.zeros((len(x_mb), n_time, n_out))

    # 순전파
    y_prev = y_rnn[:, 0, :]
    for i in range(n_time):
        # RNN층
        x = x_mb[:, i, :]
        rnn_layer.forward(x, y_prev)
        y = rnn_layer.y
        y_rnn[:, i + 1, :] = y
        y_prev = y

        # 출력층
        output_layer.forward(y)
        y_out[:, i, :] = output_layer.y

    # 역전파
    output_layer.reset_sum_grad()
    rnn_layer.reset_sum_grad()
    grad_y = 0
    for i in reversed(range(n_time)):
        # 출력층
        x = y_rnn[:, i + 1, :]
        y = y_out[:, i, :]
        t = t_mb[:, i, :]
        output_layer.backward(x, y, t)
        grad_x_out = output_layer.grad_x

        #RNN층
        x = x_mb[:, i, :]
        y = y_rnn[:, i+1, :]
        y_prev = y_rnn[:, i, :]
        rnn_layer.backward(x, y, y_prev, grad_y+grad_x_out)
        grad_y = rnn_layer.grad_y_prev

    #파라미터 갱신
    rnn_layer.update(eta)
    output_layer.update(eta)
    return y_out

def get_error(y, t):
    return 1.0 / 2.0 * np.sum(np.square(y - t))

for i in range(n_learn):
    num1 = np.random.randint(max_num//2)
    num2 = np.random.randint(max_num//2)

    # 입력 데이터 생성
    x1 = binaries[num1]
    x2 = binaries[num2]
    x_in = np.zeros((1, n_time, n_in))
    x_in[0, :, 0] = x1
    x_in[0, :, 1] = x2
    x_in = np.flip(x_in, axis=1)

    # 정답 데이터 준비
    t = binaries[num1+num2]
    t_in = t.reshape(1, n_time, n_out)
    t_in = np.flip(t_in, axis=1)

    # 훈련
    y_out = train(x_in, t_in)
    y = np.flip(y_out, axis=1).reshape(-1)

    # 오차 구하기
    error = get_error(y_out, t_in)

    # 경과 표시
    if i%interval == 0:
        y2 = np.where(y<0.5, 0, 1)
        y10 = 0
        for j in range(len(y)):
            pow2 = 2 ** (n_time-1-j)
            y10 += y2[j]*pow2

        print("n_learn : ", i)
        print("error : ", error)
        print("output : ", y2)
        print("correct : ", t)

        c = "Good" if (y2 == t).all() else "Bad"
        print(c+str(num1)+"+"+str(num2)+"="+str(y10))
        print("---------------------")