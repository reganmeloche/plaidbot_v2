class IPrintMessages:
    def mprint(self, msg:str):
        raise NotImplementedError()

class ConsolePrinter(IPrintMessages):
    def mprint(self, msg:str):
        print(msg)