import time
import project

def main():
    start = time.time()
    project.main()
    end = time.time()
    print(f"Runtime: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
