import sys, time

def loading(text="Loading"):
    for i in range(5):
        for j in ["|","/","-","\\"]:
            sys.stdout.write(f"\r{text} {j}")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\nDone!")
