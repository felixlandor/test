def greet(name="world"):
	"""返回一条问候语。"""
	return f"Hello, {name}!"


if __name__ == "__main__":
	print(greet())
	print(greet("Python learner"))
