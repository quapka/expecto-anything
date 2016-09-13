import argparse
import json

class CommandLineApplication(object):
    """docstring for CommandLineApplication"""
    def __init__(self, *args, **kwargs):
        
        self.process_arguments(**kwargs)
        # print(self.__class__.__module__)

    def process_arguments(self, **kwargs):    

        
        with open(self.__class__.__name__.lower() + "_args.json", "r") as f:
            args = json.load(f)

        parser = argparse.ArgumentParser(description=self.__doc__)
        # for arg, options in args.items():
        #     arg_name = arg.strip("-")
        #     if not self.__class__.__module__ == "__main__":
        #         if arg_name not in kwargs.keys():
        #             try:
        #                 value = input(options["help"] + ": ")
        #             except KeyError:
        #                 print("Missing help for argument: {}".format(arg_name))
        #                 value = input("Give me {}: ".format(arg_name))
        #         else:
        #             value = kwargs[arg_name]
        #         setattr(self, arg_name, value)
        #     else:
        #         parser.add_argument(arg, **options)

        self.args = parser.parse_args()
        if self.args:
            print(self.args)
            for arg, value in vars(self.args).items():
                setattr(self, arg, value)

if __name__ == "__main__":

    pass