from lib.stage_worker import StageWorker
from lib.models.command import KindCommand


def main():
    worker = StageWorker()
    worker.init()
    command = None
    while True:
        if command is None:
            command = worker.wait()
        elif command.kind == KindCommand.CreatePipe:
            worker.create_pipe(command)
            command = None
        elif command.kind == KindCommand.GenerateImage:
            worker.generate_image(command)
            command = None


if __name__ == '__main__':
    main()
