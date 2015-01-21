import sublime, sublime_plugin, re

class makeEngWordbookCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		def uniq(seq):
			# prevents duplicating
			checked = []
			for e in seq:
				if e.strip() not in checked:
					checked.append(e)
			return checked

		def openFileSearch(word_s):

			active_window = sublime.active_window()
			views = active_window.views()
			active_view = active_window.active_view()

			other_views = [v for v in views if v.id != active_view.id]
			view_list = [active_view] + other_views
			
			matched_words = []
			for e in view_list:
				matched_regions = []
				if e.find_all(word_s, sublime.IGNORECASE):
					matched_regions.append(e.find_all(word_s, sublime.IGNORECASE)) 

					for ee in matched_regions:
						for eee in ee:
							each_line_region = e.line(eee)
							each_line_strings = e.substr(each_line_region)
							matched_words.append(each_line_strings)

			return matched_words

		def replace_words(index):
			
			if(index > -1):
				self.view.run_command("replace_words_with_matching_line",{"begin": begin, "end": end, "show_matches_to_quick_panel": show_matches_to_quick_panel, "index": index})

		# region at cursor
		cursor_position = self.view.sel()[0]

		# string in region at cursor position(one word or more)
		# begin and end are the region where searched line is inserted
		if cursor_position.end() - cursor_position.begin() == 0:
			word_region = self.view.word(cursor_position)
			word_s = self.view.substr(word_region).strip()
			begin = word_region.a
			end = word_region.b
		else:
			word_s = self.view.substr(cursor_position).strip()
			begin = cursor_position.begin()
			end = cursor_position.end()

		# preventing too much words from being founded
		word_s = "^" + word_s

		# searching word_s in current window
		# save to show_matches_to_quick_panel
		matched_result = uniq(openFileSearch(word_s))

		# display words in the begining of each line
		show_matches_to_quick_panel = []
		for e in matched_result:
			show_matches_to_quick_panel.append(e[0:80])


		# show quick panel including matching words
		sublime.active_window().show_quick_panel(show_matches_to_quick_panel, replace_words)


class replaceWordsWithMatchingLineCommand(sublime_plugin.TextCommand):
	def run(self, edit, begin, end, show_matches_to_quick_panel, index):
		self.view.replace(edit, sublime.Region(begin, end), show_matches_to_quick_panel[index])

class copyToDicCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		cursor_position = self.view.sel()[0]
		current_line = self.view.line(cursor_position)
		current_string = '\n' + self.view.substr(current_line)

		active_window = sublime.active_window()
		views = active_window.views()
		dic_file_end = ""
		for e in views:
			file_name_plus_path = e.file_name()
			pattern = re.compile("(\/.+\/)(.*)")
			file_name = pattern.sub("\g<2>", file_name_plus_path)

			if file_name == "eng_dic_data.txt":
				dic_file_end = e.size()
				e.insert(edit, dic_file_end, current_string)
				sublime.message_dialog("사전 파일에 추가되었습니다.\nThe words has inserted into the dictionary file.")
		if dic_file_end == "":
			sublime.message_dialog("사전 파일이 열려 있지 않습니다.\n The dictionary file is not opened.")

class moveToDicCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		cursor_position = self.view.sel()[0]
		current_line = self.view.line(cursor_position)
		current_string = self.view.substr(current_line)
		sublime.set_clipboard(current_string)
		
		pattern = re.compile(r'^.+\t')
		keyword_object = pattern.match(current_string)
		keyword = '^' + keyword_object.group()

		active_window = sublime.active_window()
		views = active_window.views()
		dic_file_end = ""
		for e in views:
			file_name_plus_path = e.file_name()
			pattern = re.compile("(\/.+\/)(.*)")
			file_name = pattern.sub("\g<2>", file_name_plus_path)

			if file_name == "eng_dic_data.txt":
				active_window.focus_view(e)
				keyword_position = e.find(keyword, 0)

				if e.find(keyword, 0):
					vector = e.text_to_layout(keyword_position.a)
					e.set_viewport_position(vector)
					e.sel().add(e.line(keyword_position))
				else:
					sublime.message_dialog("찾는 단어가 없습니다.\n The keyword is not found.")
					
				# print("keyword_position is", keyword_position)
				# print("vector position is", vector)

