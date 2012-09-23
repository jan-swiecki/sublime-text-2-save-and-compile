import sublime, sublime_plugin
import sys, subprocess
import re

class SaveAndCompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("save")

		filename = self.view.file_name()

		if filename.endswith('.less'):

			out_filename = re.sub(".less$",".css",filename)

			print "lessc",filename,out_filename

			self.view.window().run_command('my_exec',{
				"cmd": ["lessc",filename,out_filename],
				"shell": True,
				"quiet": True
			})

		elif filename.endswith('.co'):
			self.view.window().run_command('my_exec',{
				"cmd": ["coco","-c",filename],
				"shell": True,
				"quiet": True
			})
