#   Importing Responsories
import sys

def main():

    #   Prompt the user with a question
    try :
        prompt = str(input('Greetings :').lower())

    except ValueError as e:
        sys.exit(e)

    value = lambda prompt: "$0" if "hello" in prompt else "$20" if prompt.startswith('h') else "$100"
    print(value(prompt))

if __name__ == '__main__':
    main()
