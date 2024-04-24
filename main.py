from secondary import secondary_call

def main():
  print("Variável __name__ for main file: ", __name__)
  secondary_call()

if __name__ == "__main__":
  main()