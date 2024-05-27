import sys
while True:
    msg = input("")
    match msg:
        case "CU":
            print("see you")
        case ":-)":
            print("I'm happy")
        case ":-(":
            print("I'm unhappy")
        case ";-)":
            print("wink")
        case ":-P":
            print("stick out my tongue")
        case "(~.~)":
            print("sleepy")
        case "TA":
            print("totally awesome")
        case "CCC":
            print("Canadian Computing Competition")
        case "CUZ":
            print("because")
        case "TY":
            print("thank-you")
        case "YW":
            print("you're welcome")
        case "TTYL":
            print("talk to you later")
            sys.exit(0)
        case _:
            print(msg)
