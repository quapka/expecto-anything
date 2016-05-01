import tkinter as tk
import time


class App(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# boolean for checking, whether the stopwatch currently run
		self.running   = False
		# the starting time
		self.startTime = 0
		# StringVar so the text inside self.label is updated on change
		self.timeLabelText = tk.StringVar()
		self.label = tk.Label(textvariable=self.timeLabelText)
		# pack it in the frame
		self.label.pack()
		# similar code for button, added self._runButton when the button is clicked
		self.runButtonText = tk.StringVar()
		self.runButtonText.set("Run")
		self.runButton = tk.Button(textvariable=self.runButtonText,
								   command=self.__runButton)
		self.runButton.pack()
		# array to hold the laps
		self.laps    = []
		self.lapButton = tk.Button(text="Lap",
								   command=self.__lapButton)
		self.lapButton.pack()
		# bind Return with __lapButton function
		self.bind("<Return>", self.__lapButton)

	def __timelabel(self):
		# if running change the time each second
		if self.running:
			seconds = time.time() - self.startTime
			self.timeLabelText.set("%d:%02d:%02d" % seconds_to_time(seconds))
			self.after(1000, self.__timelabel)

	def __runButton(self):
		# if "was" running, set running to false and adjust label
		if self.running:
			self.running = False
			self.runButtonText.set("Run")
		# if "was not" running
		else:
			# get the time
			self.startTime = time.time()
			# change running to True
			self.running = True
			# start stopwatch immediately
			self.after(0, self.__timelabel)
			# change the text on the runButton
			self.runButtonText.set("Stop")
			# clear each lap from previous run
			for lap in self.laps:
				lap.pack_forget()
			# and empty it, maybe use while loop and pop
			self.laps = []

	def __lapButton(self, *args):

		if self.running:
			# get the time as str "HH:MM:SS"
			t = self.timeLabelText.get()
			t = time_to_seconds(t)
			# if there are previous laps
			if self.laps:
				# get their sum
				elapsed = sum([time_to_seconds(self.laps[x].cget("text").split()[1]) for x in range(len(self.laps))])
				# substract that
				t       = t - elapsed
			t = seconds_to_time(t)
			t = ":".join([str(x) for x in t])
			t = "{}. {}".format(len(self.laps)+ 1, t)
			# add new label with text
			self.laps.append(tk.Label(text=t))
			# pack all the label
			for lap in self.laps:
				lap.pack()

# methods for handling time
# probably it would be better to use some precoded method from 
# module time and datetime
def time_to_seconds(time):

	h, m, s = [int(x) for x in time.split(':')]
	return h*3600 + m*60 + s

def seconds_to_time(seconds):

	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	return h, m, s

if __name__ == '__main__':

	App().mainloop()