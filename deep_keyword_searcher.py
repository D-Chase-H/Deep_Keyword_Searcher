
# This module is part of Deep_Keyword_Searcher and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

#   Author: D-Chase-H



################################################################################
# Stuff To look at to possibly clean up and increase readability.

# imports... Refer to the Google Python Style Guide again on this one.
# comments... DONE. Maybe could add soe more though. Do a second pass.
# docstrings... DONE
# property/setter getter stuff.. This code doesn't really benifit from it.
# annotations... Maybe.... I don't know though.
################################################################################

import ntpath
import os
import shutil
import sys
import zipfile


"""
Summary:
    Prints all file name matches only.

Arguments:
    None

Returns:
    None

Raises:
    None
"""


class InternalFileTextMatch(object):
    """
    An object for storing the line number and line text for any keyword
    matches that occur when searching a file's text.

    Attributes:
        line_num: A integer indicating the line number the text occurs.
        line_text: A string containing the text of the line on which a keyword
            match was detected.
    """

    def __init__(self):
        """Inits InternalFileTextMatch."""
        self.line_num = None
        self.line_text = None


    def get_line_numbered_string(self):
        """
        Formats a string to contain both the line number and the line text.
            The string comes indented with 4 spaces.
        example: '   LINE #: Line Text Goes Here'

        Returns:
            line_text: A string containing the line number and line text.
        """

        line_num = str(int_text_match.line_num)
        line_txt = int_text_match.line_text
        line_text = "   LINE {}:  {}".format(line_num, line_txt)

        return line_text



class MatchDirectory(object):
    """
    An object for storing the line number and line text for any keyword
    matches that occur when searching a file's text.

    Attributes:
        current_dir: A string containing the full path to the directory(Folder).
        folder_name: A string containing the folder name.
        sub_folders: A list of MatchDirectory objects for all sub-folders in
            which a keyword match was found.
             Keep in mind that if there were no keyword matches found in a
             sub-folder, but there were keyword matches found in a sub-folder of
             a directory's sub-folders, then the root sub-folder will still be
             found in this list, but all it's attributes will be empty, except
             for it's list of sub-folders. Whether a keyword match is found is
             dependent upon which rules were selected...
             (i.e. in folder names, in file names, in text within a file,
             in text within a file within a zipped file)

        file_name_match: A Set of strings that contains strings of file names
            where a keyword match was found.
        zip_file_name_match: A Set of strings that contains strings of zip file
            names where a keyword match was found.

        file_text_match: A dictionary(Hash Table) with Key:Value pairs as........
            Keys: A string of a full file path, to a file that conatains text in
                which a keyword match was found.
            Value: An InternalFileTextMatch object that contains the line number
                and the text of the line on which the keyword match was found.
        zip_file_text_match: A dictionary(Hash Table) with Key:Value pairs as...
            Keys: A string of a full file path, to a zip file that conatains
                text in which a keyword match was found.
            Value: An InternalFileTextMatch object that contains the line number
                and the text of the line on which the keyword match was found.
    """

    def __init__(self):
        """Inits MatchDirectory."""

        # Path to folder
        self.current_dir = None
        # Folder name
        self.folder_name = None
        # Positive matches for the keyword search
        self.sub_folders = list()

        # Name of file matches
        self.file_name_match = set([])
        self.zip_file_name_match = set([])

        # Text within file matches
        self.file_text_match = dict()
        self.zip_file_text_match = dict()


    def print_all_file_name_matches(self):
        """
        Prints all keyword matches found within a file's name.
        """

        for file_name in self.file_name_match:
            print(file_name)
        return


    def print_all_zip_file_name_matches(self):
        """
        Prints all keyword matches found within a zipped file's name.
        """

        for file_name in self.zip_file_name_match:
            print(file_name)
        return


    def print_all_file_text_matches(self):
        """
        Prints all keyword matches found within a file's text.
        """

        for file_name, text_matches in self.file_text_match.items():
            print_name = "  FILE: {}".format(file_name)
            print(print_name)

            for internal_text_match in text_matches:
                line_text = internal_text_match.get_line_numbered_string()
                print(line_text)
        return


    def print_all_internal_zip_file_text_matches(self):
        """
        Prints all keyword matches found within an internal zipped file's text.
        """

        for file_name, text_matches in self.zip_file_text_match.items():
            print_name = "  FILE: {}".format(file_name)
            print(print_name)

            for internal_text_match in text_matches:
                line_text = internal_text_match.get_line_numbered_string()
                print(line_text)
        return


    def print_contents(self):
        """
        Runs all of the above print functions.
        """

        self.print_all_file_name_matches()
        self.print_all_file_text_matches()
        self.print_all_zip_file_name_matches()
        self.print_all_internal_zip_file_text_matches()
        return



class KeywordFileSearch(object):
    """
    This is the main class in which all the magic happens and the main class
        that the user will work with.

    Attributes:
        root_directory: A string containing the full file path to the root
            directory in which the root keyword search will occur.
        base_search_dir: A MatchDirectory object for the root_directory.
        zip_formats: A list of strings of commonly used zip formats.
        ignored_file_types: A list of strings of file extension types to ignore
            when doing a keyword search, in order to increase performance.
    """

    def __init__(self, root_dir):
        """Inits KeywordFileSearch."""

        self.root_directory = root_dir
        self.base_search_dir = MatchDirectory()
        self.base_search_dir.current_dir = root_dir

        self.zip_formats = set([".zip", ".7z", ".rar", ".tar", ".tar.gz"])

        ignored_image_types = [".dds", ".jpg", ".png", ".tiff", ".gif "]

        ignored_video_types = [".wav", ".mp4", ".avi", ".mov", ".qt", ".amv",
        ".mpg", ".mpeg", ".m2v", ".mpv", ".mpe", ".m2p", ".m4v", ".svi", "3gp",
        "3g2", ".mxf", ".gifv", ".mkv", ".flv"]

        ignored_audio_typed = [".mp3", ".wav", ".wma", ".webm", ".aiff", ".aa",
        ".aax", ".flac", ".dvf", ".m4b", ".m4a", ".m4p", ".mpc", ".ogg", ".oga",
        ".mogg", ".ra", ".rm"]

        ignored_other_file_types = [".exe", ".dll"]


        self.ignored_file_types = list()
        self.ignored_file_types += ignored_image_types
        self.ignored_file_types += ignored_video_types
        self.ignored_file_types += ignored_audio_typed
        self.ignored_file_types += ignored_other_file_types
        # Make it into a set for faster lookups.
        self.ignored_file_types = set(self.ignored_file_types)


    def add_zip_text_match(self, curr_dir_obj_zip_text_match, sub_path, match):
        """
        Adds an entry(Key:Value) into a MatchDirectory objects's
        zip_file_text_match attribute dictionary.

        Args:
            curr_dir_obj_zip_text_match: A dictionary which is a MatchDirectory
                objects's zip_file_text_match attribute.
            sub_path: A string with the file path (within a zipped file) to the
                internal file within a zipped file in which a keyword match was
                detected.
            match: A InternalFileTextMatch object that contains the keyword
                match data.

        Returns:
            None
        """

        try:
            curr_dir_obj_zip_text_match[sub_path].append(match)
        except KeyError:
            curr_dir_obj_zip_text_match[sub_path] = [match]
        return


    def search_thru_zip_for_keyword(self, curr_match_dir_obj, full_file_path,
                                    keyword, search_file_names, case_sensitive):
        """
        Searches through the files within a zipped file to find if there are any
        occurances of the keyword is found within any strings on an any lines of
        the file.

        Args:
            curr_match_dir_obj: A MatchDirectory object, the current
                MatchDirectory for the directory in which the zipped file
                exists.
            full_file_path: A string, the full file path for the zipped file in
                which the keyword search will take place.
            keyword: A string, the keyword that is to be searched for.

            search_file_names: A Bool, a rule for whether to search for the
                keyword within the file name.
            case_sensitive: A Bool, a rule for whether the keyword should be
                search for as case sensitive or case insensitive.

        Returns:
            A list containing: [keyword_is_in_text, curr_match_dir_obj]
            keyword_is_in_text: A Bool if keyword was found in the text of a
                file.
            curr_match_dir_obj: A MatchDirectory object, the current
                MatchDirectory for the directory in which the zipped file
                exists.
        """

        keyword_is_in_text = False
        keyword_is_in_text_file = False
        dir_objs_zip_text_matches = curr_match_dir_obj.zip_file_text_match
        dir_objs_filename_matches = curr_match_dir_obj.zip_file_name_match

        try:
            with zipfile.ZipFile(full_file_path, "r") as myzip:

                root_zip_files_name = ntpath.basename(full_file_path)

                file_list = myzip.namelist()

                for zip_subfile_name in file_list:

                    file_name, file_ext = os.path.splitext(zip_subfile_name)

                    with myzip.open(zip_subfile_name, "r") as zipped_text_file:

                        for index, line in enumerate(zipped_text_file):
                            try:
                                line = line.decode("utf-8")

                                if case_sensitive is False:
                                    line = line.lower()

                                if keyword in line:
                                    keyword_is_in_text = True
                                    keyword_is_in_text_file = True

                                    match = InternalFileTextMatch()
                                    match.line_num = index
                                    match.line_text = line

                                    sub_path = "{}/{}".format(
                                                root_zip_files_name,
                                                zip_subfile_name)

                                    self.add_zip_text_match(
                                                      dir_objs_zip_text_matches,
                                                      sub_path,
                                                      match)

                            except UnicodeDecodeError:
                                break

                        zipped_text_file.close()

                    # Check if the keyword is in the name of any of the files
                    # within the zipped file. But only if there is NOT already
                    # an internal file with text that matches the keyword.
                    if keyword in zip_subfile_name:
                        if search_file_names is True:
                            if keyword_is_in_text_file is False:
                                keyword_is_in_text = True
                                dir_objs_filename_matches.add(
                                                            root_zip_files_name)

            myzip.close()
        except:
            pass

        return [keyword_is_in_text, curr_match_dir_obj]


    def add_file_text_match(self, dir_objs_file_text_matches, file_path, match):
        """
        Adds an entry(Key:Value) into a MatchDirectory objects's
        zip_file_text_match attribute dictionary.

        Args:
            curr_dir_obj_zip_text_match: A dictionary which is a MatchDirectory
                objects's zip_file_text_match attribute.
            sub_path: A string with the file path (within a file) to the
                internal file within a file in which a keyword match was
                detected.
            match: A InternalFileTextMatch object that contains the keyword
                match data.

        Returns:
            None
        """

        try:
            dir_objs_file_text_matches[file_path].append(match)
        except KeyError:
            dir_objs_file_text_matches[file_path] = [match]
        return



    def search_file_text(self, curr_match_dir_obj,
                        full_file_path, keyword,
                        search_file_names, case_sensitive):
        """
        If a file contains text that can be read, then this function will
        search through the text for the keyword. If found, an
        InternalFileTextMatch object will be put in the curr_match_dir_obj's
        file_text_search(dict) attribute. This will store the line number and
        the text of the line where a keyword match occured.

        Handles the edge cases where the file contains binary, and is
        unreadable text.

        Args:
            curr_match_dir_obj: A MatchDirectory object, the current
                MatchDirectory for the directory in which the file
                exists.
            full_file_path: A string, the full file path for the file in
                which the keyword search will take place.
            keyword: A string, the keyword that is to be searched for.

            search_file_names: A Bool, a rule for whether to search for the
                keyword within the file name.
            case_sensitive: A Bool, a rule for whether the keyword should be
                search for as case sensitive or case insensitive.

        Returns:
            A list containing: [keyword_is_in_text, curr_match_dir_obj]
            keyword_is_in_text: A Bool if keyword was found in the text of a
                file.
            curr_match_dir_obj: A MatchDirectory object, the current
                MatchDirectory for the directory in which the file
                exists.
        """

        keyword_is_in_text = False
        dir_objs_file_text_matches = curr_match_dir_obj.file_text_match
        dir_objs_filename_matches = curr_match_dir_obj.zip_file_name_match


        # full_file_name == FileName.FileExtensoin
        full_file_name = os.path.basename(full_file_path)

        with open(full_file_path, "r") as file_text:

            try:

                for index, line in enumerate(file_text):

                    if case_sensitive is False:
                        line = line.lower()

                    if keyword in line:
                        keyword_is_in_text = True
                        match = InternalFileTextMatch()
                        match.line_num = index
                        match.line_text = line

                        self.add_file_text_match(
                                                dir_objs_file_text_matches,
                                                full_file_name,
                                                match)

            except UnicodeDecodeError:
                pass

        file_text.close()

        # If the file's name contains the keyword, then put it in the
        # curr_match_dir_obj objects's file_names attribute's list.
        if keyword_is_in_text is False:
            root_files_name = ntpath.basename(full_file_path)

            if keyword in root_files_name and search_file_names is True:
                curr_match_dir_obj.file_name_match.add(root_files_name)
                keyword_is_in_text = True

        return [keyword_is_in_text, curr_match_dir_obj]


    def search_for_keyword_in_folder(
        self, keyword, root=None, curr_match_dir_obj=None,
        search_sub_folders=False, search_in_file_text=False,
        search_file_names=False, search_zip_files=False, case_sensitive=False):

        """
        This is the main function that does the heavy lifting. It recursivley
        iterates through the directory structure of only sub directories, and
        does not search through directories above the directory the user chooses
        as the self.root_directory when they create a KeywordFileSearch object.


        Args:
            keyword: A string, the keyword that is to be searched for.
            root: a string for the full file path for the current directory
                being searched through. If it is empty or set to None, then it
                will be set to self.root_directory.
            curr_match_dir_obj: A MatchDirectory object, the current
                MatchDirectory for the directory in which the search is taking
                palce. If it is empty or set to None, then it will be
                set to self.base_search_dir.

            search_sub_folders:A Bool, a rule for whether to search for the
                keyword within the sub-folders of the root directory.
            search_in_file_text: A Bool, a rule for whether to search for the
                keyword within the text of a file.
            search_file_names: A Bool, a rule for whether to search for the
                keyword within the file name.
            search_zip_files: A Bool, a rule for whether to search for the
                keyword within the files within a zipped file.
            case_sensitive: A Bool, a rule for whether the keyword should be
                search for as case sensitive or case insensitive.

        Returns:
                A list containg: [True, curr_match_dir_obj]
                    The first item: A Bool, stating whether a keyword match was
                        found in the directory. This will also be True if there
                        was a keyword match found in any of the sub-directories.
                    The second item: A MatchDirectory object, the MatchDirectory
                    for the directory in which the search took palce.
        """

        if curr_match_dir_obj is None:
            curr_match_dir_obj = self.base_search_dir
        if root == None:
            root = self.root_directory
        if case_sensitive is False:
            keyword = keyword.lower()

        at_least_one_match = False
        in_sub_dirs = False

        # item can be either a file or a folder.
        for item in list(os.scandir(root)):

            # If the item is a sortcut or symbolic link, then skip it.
            if os.path.islink(item) is True:
                continue

            if item.is_file() is True:

                file_name, file_ext = os.path.splitext(item.name)

                # Skip the file if it isn't a file type known to contain text.
                if file_ext in self.ignored_file_types:
                    continue

                full_file_path = item.path

                # If file is a zipped file do this.
                if file_ext in self.zip_formats and search_zip_files is True:
                    # kw_match_obj_temp exists to help shorten the line length
                    # to 80 for line 313.
                    kw_match_obj_temp = self.search_thru_zip_for_keyword(
                        curr_match_dir_obj, full_file_path,
                        keyword, search_file_names, case_sensitive)

                    keyword_found, curr_match_dir_obj = kw_match_obj_temp

                    if keyword_found is True:
                        at_least_one_match = True
                    continue


                # If the search_in_file_text is True, then do this.
                if search_in_file_text is True:
                    keyword_found, curr_match_dir_obj = self.search_file_text(
                        curr_match_dir_obj,
                        full_file_path, keyword,
                        search_file_names, case_sensitive)

                    if keyword_found is True:
                        at_least_one_match = True
                    continue


            if item.is_dir() is True and search_sub_folders is True:

                next_dir = MatchDirectory()
                sub_root = item.path
                next_dir.current_dir = sub_root
                next_dir.folder_name = item.name

                in_sub_dirs, next_dir = self.search_for_keyword_in_folder(
                    keyword, sub_root, next_dir, search_sub_folders,
                    search_in_file_text, search_file_names, search_zip_files,
                    case_sensitive)

                if in_sub_dirs:
                    at_least_one_match = True
                    curr_match_dir_obj.sub_folders.append(next_dir)


        if at_least_one_match is True or in_sub_dirs is True:
            return [True, curr_match_dir_obj]
        else:
            return [False, curr_match_dir_obj]


    def print_all_matches(self, curr_match_dir_obj=None):
        """
        Prints all occurances of all the types of keyword matches.
        """
        if curr_match_dir_obj is None:
            curr_match_dir_obj = self.base_search_dir

        print(curr_match_dir_obj.current_dir)
        curr_match_dir_obj.print_contents()

        if curr_match_dir_obj.sub_folders:
            for sub_folder in curr_match_dir_obj.sub_folders:
                self.print_all_matches(sub_folder)
        return


    def return_folder_names(self):
        """
        Returns:
            A list of strings containing all the directory in which either a
            keyword match was found or the directory contained a sub-directory
            that in which a keyword match was found.
        """

        def find_folder_names(curr_match_dir_obj=None):
            nonlocal folder_names

            if curr_match_dir_obj is None:
                curr_match_dir_obj = self.base_search_dir

            folder_names.append(curr_match_dir_obj.folder_name)

            if curr_match_dir_obj.sub_folders:
                for sub_folder in curr_match_dir_obj.sub_folders:
                    find_folder_names(sub_folder)
            return

        folder_names = list()
        find_folder_names(curr_match_dir_obj=None)

        return folder_names



if __name__ == "__main__":

    #print("\n\n\n")

    search_dir = r"Put a path to a directory here"
    keyword = "Happy"

    test_search = KeywordFileSearch(search_dir)

    test_search.search_for_keyword_in_folder(keyword, search_dir,
        search_sub_folders=True, search_in_file_text=True,
        search_file_names=True, search_zip_files=True, case_sensitive=True)

    test_search.print_all_matches()
    #print("\n\n\n\n")



#   python3 deep_keyword_searcher.py
