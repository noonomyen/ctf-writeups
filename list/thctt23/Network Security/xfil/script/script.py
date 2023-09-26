with open('data.jpeg', 'ab') as f:
    try:
        while True:
            f.write(bytes.fromhex(input().replace('.totallynotmalicious.xyz', '')))
    except EOFError:
        f.close()
