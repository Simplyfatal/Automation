def wait(message,sec):
    print(message,end=" ")
    import time
    for i in range(sec):
        print(". ",end="")
        time.sleep(1)
    print("Done!")

def dotprint():
    print(". ",end="")

    print("Done!")
    


