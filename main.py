import requests
import threading
from time import sleep


def bring_quote():
    res = requests.get("https://zenquotes.io/api/random")
    res = res.json()
    print(f"'{res[0]['q']}' --{res[0]['a']}")


def run_in_thread(func, args=(), n_o_t=1, w_f=True, interval=1):
    t_l = []
    for _ in range(n_o_t):
        td = threading.Thread(target=func, args=args)
        td.start()
        if interval:
            sleep(interval)
        t_l.append(td)
        if w_f:
            [t.join() for t in t_l]


print(run_in_thread(func=bring_quote))
