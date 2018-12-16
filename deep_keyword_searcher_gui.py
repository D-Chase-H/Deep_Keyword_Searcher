#! /usr/bin/env python3

# This module is part of Deep_Keyword_Searcher and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

#   Author: D-Chase-H

import platform
import pyperclip
from deep_keyword_searcher import KeywordFileSearch
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
import os


class Window(object):
    """docstring for Window."""
    def __init__(self):

        self.root = Tk()
        self.root.title("File Searcher")

        ########## FRAMES ##########

        ### Main Frame ###
        self.content = ttk.Frame(self.root,
                                padding=(5, 5, 12, 0), width=1845, height=40)

        self.content.grid(column=0, row=0, sticky=(N, W, E, S))

        self.text_frame = ttk.Frame(self.content,
                                    borderwidth=5, relief="sunken",
                                    width=1845, height=40)

        self.select_folder = ttk.Frame(self.content,
                                       borderwidth=5, relief="sunken",
                                       width=1845, height=40)

        self.search_button_frame = ttk.Frame(self.content,
                                             borderwidth=5, relief="sunken",
                                             width=1845, height=40)

        self.tree_frame = ttk.Frame(self.content,
                                    borderwidth=5, relief="sunken",
                                    width=1845, height=40)

        self.rules = ttk.Frame(self.content,
                               borderwidth=5,
                               width=1845, height=40)


        ########## Widgets ##########

        ##### rules widgets #####

        self.search_sub_folders = IntVar(value=1)
        self.search_in_file_text = IntVar(value=1)
        self.search_file_names = IntVar(value=1)
        self.search_zip_files = IntVar(value=1)
        self.case_sensitive = IntVar(value=0)

        self.rule_subfold_button = ttk.Checkbutton(
                                               self.rules,
                                               text='Search all sub-folders',
                                               variable=self.search_sub_folders,
                	                           onvalue=1, offvalue=0)

        self.rule_filetext_button = ttk.Checkbutton(
                                              self.rules,
                                              text='Search text in files',
                                              variable=self.search_in_file_text,
                	                          onvalue=1, offvalue=0)

        self.rule_filename_button = ttk.Checkbutton(
                                        self.rules,
                                        text='Search For text in file names',
                                        variable=self.search_file_names,
        	                            onvalue=1, offvalue=0)

        self.rule_zipfile_button = ttk.Checkbutton(
                                       self.rules,
                                       text='Search text files in zipped files',
                                       variable=self.search_zip_files,
        	                           onvalue=1, offvalue=0)
        self.rule_case_button = ttk.Checkbutton(
                                     self.rules,
                                     text='Case Sensitive',
                                     variable=self.case_sensitive,
                    	             onvalue=1, offvalue=0)

        ##### text_frame widgets #####
        search_text = " "*10 + 'Enter text to search for:' + " "*10
        self.term_label = ttk.Label(self.text_frame, text=search_text)

        self.search_term = StringVar()
        self.search_text_entrybox = ttk.Entry(self.text_frame,
                                               textvariable=self.search_term,
                                               width=50)


        ##### select_folder widgets #####
        self.file_path_string = ""
        self.file_select_button = ttk.Button(self.select_folder,
                                             text="Select Folder",
                                             command=self.ask_for_file_path)

        ##### search_button_frame widgets #####
        self.search_button = ttk.Button(self.search_button_frame,
                                        text="Perform search",
                                        command=self.do_search)

        # Tkinter has problems with having a button to stop a function that is
        # initiated by another button and is currently running, due to tkinter
        # being single-threaded. I may not be able to add this functionality
        # to the app, but I will leave this code here jsut in case I figure out
        # a way to do it later on.
        #self.stop_search = False
        #self.stop_search_button = ttk.Button(self.search_button_frame,
                                             #text=" stop search\n(not working)",
                                             #command=self.stop_search,
                                             #state='disabled')

        self.search_progress = "No Search in Progress"
        self.search_progresslabel = ttk.Label(self.search_button_frame,
                                               text=self.search_progress)

        ##### tree_frame widgets #####
        self.ftree = ttk.Treeview(self.tree_frame,
                                  height=40, selectmode="extended")
        self.ftree.heading("#0", text="Folder Path")
        self.ftree.column("#0",minwidth=0,width=1000, stretch=NO)


        ##### File_dialog Ok button functioanlity #####
        self.file_select_button.bind("<Return>", self.on_ok_regular_enter)

        ##### text_frame enter functionality #####
        self.search_text_entrybox.bind("<Return>", self.do_search_enter)

        ##### TreeView click functionality #####
        self.ftree.bind("<Button-3>", self.rightClickMenu)
        self.ftree.bind("<Button-1>", self.leftClickMenu)


        ########## GRID LAYOUT DESIGN ##########
        self.content.grid(column=0, row=0)

        ##### rules grid layout #####
        self.rules.grid(column=8, row=0, columnspan=8, rowspan=5)

        self.rule_case_button.grid(column=8, row=0, columnspan=1, rowspan=1)
        self.rule_filetext_button.grid(column=8, row=1, columnspan=1, rowspan=1)
        self.rule_subfold_button.grid(column=8, row=2, columnspan=1, rowspan=1)
        self.rule_zipfile_button.grid(column=8, row=3, columnspan=1, rowspan=1)
        self.rule_filename_button.grid(column=8, row=4, columnspan=1, rowspan=1)

        ##### select_folder grid layout #####
        self.select_folder.grid(column=2, row=0, columnspan=1, rowspan=1)
        self.file_select_button.grid(column=0, row=0, columnspan=1, rowspan=1)

        ##### text_frame grid layout #####
        self.text_frame.grid(column=0, row=0, columnspan=5, rowspan=2)
        self.term_label.grid(column=0, row=1, columnspan=1, rowspan=1)
        self.search_text_entrybox.grid(column=0, row=2, columnspan=1, rowspan=1)

        ##### search_button_frame grid layout #####
        self.search_button_frame.grid(column=0, row=7, columnspan=8, rowspan=2)
        self.search_button.grid(column=0, row=0, columnspan=1, rowspan=1)
        #self.stop_search_button.grid(column=6, row=0, columnspan=1, rowspan=1)
        self.search_progresslabel.grid(column=0, row=1, columnspan=1, rowspan=1)

        ##### tree_frame grid layout #####
        self.tree_frame.grid(column=0, row=11,
                             columnspan=3, rowspan=1)
        self.ftree.grid(column=2, row=3,
                        columnspan=1, rowspan=1)


        self.root.mainloop()


    def on_ok_regular_enter(self, event):
        return


    def ask_for_file_path(self):
        self.file_path_string = filedialog.askdirectory(initialdir = "/")
        return


    def confirm_search_term_entry(self):
        return self.search_term.get()


    def int_to_bool(self, input_num):
        if input_num == 1:
            return True
        elif input_num == 0:
            return False


    def get_zipped_path(self, path):

        path = list(path)

        while True:
            if ''.join(path[-3:]) == ".7z":
                break
            elif ''.join(path[-4:]) == ".zip":
                break
            elif ''.join(path[-4:]) == ".rar":
                break
            elif ''.join(path[-4:]) == ".tar":
                break
            elif ''.join(path[-7:]) == ".tar.gz":
                break

            path.pop()

        return ''.join(path)


    def is_internal_zip_file(self, temp_row_ID):

        zip_formats = set([".zip", ".7z", ".rar", ".tar", ".tar.gz"])
        from_zip_file = False

        for item in zip_formats:
            if item in temp_row_ID:
                from_zip_file = True
                print("Is inside zipped file.")
                break

        return from_zip_file


    def rightClickMenu(self, event):

        def copy_path_to_clipboard():
            pyperclip.copy(rowID)
            return


        def open_file_or_folder():

            zip_formats = set([".zip", ".7z", ".rar", ".tar", ".tar.gz"])

            temp_row_ID = rowID
            is_inside_zip = self.is_internal_zip_file(temp_row_ID)

            if is_inside_zip is True:
                temp_row_ID = self.get_zipped_path(temp_row_ID)

            if platform.system() == "Windows":
                os.startfile(temp_row_ID)
            else:
                subprocess.call(("xdg-open", temp_row_ID))

            return

        # create a popup menu
        rowID = self.ftree.identify('item', event.x, event.y)

        if rowID:
            self.ftree.selection_set(rowID)
            self.ftree.focus_set()
            self.ftree.focus(rowID)
            #print("rowID: ", rowID, "\n")

            if os.path.exists(rowID) is False:
                return

            menu = Menu(self.tree_frame, tearoff=0)
            menu.add_command(label="Copy File Path to Clipboard",
                             command=copy_path_to_clipboard)
            menu.add_command(label="Open File or Folder",
                             command=open_file_or_folder)
            menu.tk_popup(event.x_root, event.y_root)
        else:
            menu

        return

    def leftClickMenu(self, event):
        try:
            menu.tk_popup(event.x_root, event.y_root)
        except:
            pass

        return


    def do_search_enter(self, event):
        return self.do_search()


    def stop_search(self):
        self.stop_search = True
        return


    def do_search(self):

        def find_folder_names(curr_dir, parent_folder=None, curr_dir_index=0):

            if self.stop_search is True:
                return

            if parent_folder is None:
                self.ftree.insert('', 0, curr_dir.current_dir,
                            text=curr_dir.current_dir)
            else:
                self.ftree.insert(parent_folder, 'end', curr_dir.current_dir,
                             text=curr_dir.folder_name)

            ################### BEGINING OF NESTED FUNCTION ####################
            #### ADD FILES OR TEXT AS SUB-NODES TO CURRENT FOLDER NODE ####

            # Add Any Files with a name that matched the search term.
            for file_name in curr_dir.file_name_match:
                file_id = "{}/{}".format(curr_dir.current_dir, file_name)

                self.ftree.insert(curr_dir.current_dir, 'end', file_id,
                              text=file_id)

                #print(file_name)

            # Add text and line number for any files that had text within
            # them that matched the search term.
            for file_name, text_matches in curr_dir.file_text_match.items():
                file_id = "{}/{}".format(curr_dir.current_dir, file_name)

                self.ftree.insert(curr_dir.current_dir, 'end', file_id,
                              text=file_name)

                #print(file_name)

                for int_text_match in text_matches:
                    line_num = int_text_match.line_num
                    line_txt = int_text_match.line_text
                    line_text = " LINE{}:  {}".format(line_num, line_txt)
                    line_id = file_id + line_text

                    self.ftree.insert(file_id, 'end', line_id,
                                  text=line_text)

                    #print(line_text)

            # Add Any Zipped Files with a name that matched the search term.
            for file_name in curr_dir.zip_file_name_match:
                file_id = "{}/{}".format(curr_dir.current_dir, file_name)

                self.ftree.insert(curr_dir.current_dir, 'end', file_id,
                              text=file_name)

            # Add text and line number for any files within a zipped file
            # that had text within them that matched the search term.
            for item in curr_dir.zip_file_text_match.items():
                file_name, text_matches = item
                file_id = "{}/{}".format(curr_dir.current_dir, file_name)

                self.ftree.insert(curr_dir.current_dir, 'end', file_id,
                              text=file_name)

                for int_text_match in text_matches:
                    line_num = int_text_match.line_num
                    line_txt = int_text_match.line_text
                    line_text = " LINE{}:  {}".format(line_num, line_txt)
                    line_id = file_id + line_text

                    self.ftree.insert(file_id, 'end', line_id,
                                      text=line_text)

            if curr_dir.sub_folders:
                for sub_folder in curr_dir.sub_folders:

                    find_folder_names(sub_folder, curr_dir.current_dir)
            return
        ####################### END OF NESTED FUNCTION #########################

        #################### BEGINNING OF main function's stuff ################


        self.search_progresslabel.config(text="  Search in Progress ")
        #self.stop_search_button.config(state='!disabled')
        self.root.update()

        search_term = str(self.search_term.get())
        file_path_string = self.file_path_string
        search_sub_folders = self.int_to_bool(self.search_sub_folders.get())
        search_in_file_text = self.int_to_bool(self.search_in_file_text.get())
        search_file_names = self.int_to_bool(self.search_file_names.get())
        search_zip_files = self.int_to_bool(self.search_zip_files.get())
        case_sensitive = self.int_to_bool(self.case_sensitive.get())

        # Clear out the contents of the tree before a search
        self.ftree.delete(*self.ftree.get_children())

        test_search = KeywordFileSearch(self.file_path_string)

        #print(search_term)
        #print(search_term == self.search_term.get())
        #print(file_path_string)

        test_search.search_for_keyword_in_folder(
                                        search_term,
                                        file_path_string,
                                        search_sub_folders=search_sub_folders,
                                        search_in_file_text=search_in_file_text,
                                        search_file_names=search_file_names,
                                        search_zip_files=search_zip_files,
                                        case_sensitive=case_sensitive)

        find_folder_names(test_search.base_search_dir)

        self.search_progresslabel.config(text="   Search Complete   ")
        #self.stop_search_button.config(state='disabled')
        #self.stop_search = False
        return


if __name__ == '__main__':
    test = Window()
