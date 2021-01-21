import fire

from data import Join_PDF, Split_PDF


class Main:
    @staticmethod
    def join_pdfs(list_number, location=None, destination=None):
        """
        join diferent pdf secuentially to create a new list with final name 'lista_list#'
        :param list_number: number of list at end of file 'lista_ '
        :param location: optional parameter to specify where to find pdfs to join
        :returns: returns new pdf with name lista_'list_number'.pdf
        """
        try:  # Try to execute code
            if not location:  # if location not specified
                Join_PDF(list_number=list_number).join()  # Join all pdf files found in pre-specified location
            else:
                Join_PDF(list_number=list_number, location=location, destination=destination).join()  # Join all pdf files found in specified location

            print(f"New file 'lista_{list_number}' created successfully!")  # Success mesage
        except:  # Error in execution
            print(f"LIST_{list_number} not found in file.")  # Error message

    @staticmethod
    def split_pdfs(list_number, split_n):
        """
        Split pdf file every n pages into individual files and name new file according to list
        :param list_number: list to split, title of column in csv file
        :param split_n: split every n pages
        :returns individual files with name Endodoso_'data (contract number)'.pdf
        """
        try:  # Try to execute code
            Split_PDF(list_number=list_number, split_n=split_n).split()  # Split into individual files
            print(f"'List_{list_number}' was correctly split into individual files.")  # Success message
        except:  # Error in execution
            print(f"'List_{list_number}' was not able to be split into individual documents.")  # Error message


if __name__ == "__main__":
    fire.Fire(Main)
