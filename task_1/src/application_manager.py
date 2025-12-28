from cmd import Cmd
from queue import Queue

from task_1.src.models.application import Application


def process_request(queue: Queue):
    if queue.empty():
        print("No requests to process.")
        return
    application = queue.get()
    print("Request processed:", application)


def generate_request(queue: Queue, params):
    application = Application(params)
    queue.put(application)
    print("Request generated:", application)


def all_requests(queue: Queue):
    applications = list(queue.queue)
    for application in applications:
        print(application)


class ApplicationManager(Cmd):
    prompt = ">>> "

    queue = Queue()

    def do_generate_request(self, arg):
        generate_request(self.queue, arg)

    def do_process_request(self, arg):
        process_request(self.queue)

    def do_all_requests(self, arg):
        all_requests(self.queue)

    def do_quit(self, arg):
        print("Good bye!")
        return True


def main():
    print("Greetings! ApplicationManager is running. How can I assist you today?")

    ApplicationManager().cmdloop()


def run():
    main()


if __name__ == "__main__":
    main()
