from app import Todos
import argparse


def main():
    parser = argparse.ArgumentParser(description= "Todo CLI App")
    parser.add_argument("-add", type=str, help="add new task")
    parser.add_argument("-list", action="store_true", help="list tasks")
    parser.add_argument("-delete", type= int, help="delete task")
    parser.add_argument("-complete", type= int, help="mark task as completed")

    args = parser.parse_args()

    todos = Todos()

    if args.add:
        todos.add(args.add)
    elif args.list:
        todos.list()
    elif args.delete:
        todos.delete(args.delete)
    elif args.complete:
        todos.complete(args.complete)
    else:
        print("invalid arg, please use -h to see options")


if __name__ == "__main__":
    main()