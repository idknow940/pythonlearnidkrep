a = 'hello'

def text_func(txt: str, step: int) -> str:
	txt = txt[::step]


print(text_func(a, 1))