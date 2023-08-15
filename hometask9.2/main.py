
def generate_me_smth(n):
    for i in range(n):
        yield "#" * n


res = generate_me_smth(n=3)

for line in res:
    print(line)
