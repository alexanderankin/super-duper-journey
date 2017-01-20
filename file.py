from __future__ import print_function

def basic_demo():
  from gi.repository import Gtk

  window = Gtk.Window()
  window.connect("delete-event", Gtk.main_quit)
  window.show_all()

  Gtk.main()

def button_demo():
  from gi.repository import Gtk
  
  class ButtonWindow(Gtk.Window):
    """ButtonWindow"""
    def __init__(self):
      super(ButtonWindow, self).__init__(
        title = "My Button Window"
      )
      # Gtk.Window.__init__(self, title = "My Button Window")

      # Button
      self.button = Gtk.Button(label = "Ok")
      self.button.connect("clicked", self.button_callback)
      self.add(self.button)

    def button_callback(self, widget):
      print ("button was clicked")

  window = ButtonWindow()
  window.connect("delete-event", Gtk.main_quit)
  window.show_all()

  Gtk.main() 

def properties_demo():
  """Properties of widgets"""
  from gi.repository import Gtk

  window = Gtk.Window()
  
  label = Gtk.Label()
  label.set_label("See reference for more details")
  label.set_angle(10)
  # label.set_halign(Gtk.Align.END)
  window.add(label)

  window.connect("delete-event", Gtk.main_quit)
  window.show_all()

  Gtk.main()

def box_demo():
  from gi.repository import Gtk
  class BoxWindow(Gtk.Window):
    """BoxWindow"""
    def __init__(self):
      super(BoxWindow, self).__init__(
        title = ""
      )

      # Box (spacing in px)
      self.box = Gtk.Box(spacing = 10)
      self.add(self.box)

      # Print button
      self.print_button = Gtk.Button(label = "print")
      self.print_button.connect("clicked", lambda w: print ("print"))

      # pack_start vs pack_end: L to R vs R to L
      self.box.pack_start(
        child = self.print_button,
        expand = True,
        fill = True,
        padding = 10)

      # View button
      self.view_button = Gtk.Button(label = "view")
      self.view_button.connect("clicked", lambda w: print ("view"))

      self.box.pack_start(
        child = self.view_button,
        expand = True,
        fill = True,
        padding = 10)



  window = BoxWindow()

  window.connect("delete-event", Gtk.main_quit)
  window.show_all()

  window.move(100, 100)

  Gtk.main()

def grid_demo():
  from gi.repository import Gtk
  class GridWindow(Gtk.Window):
    """GridWindow"""
    def __init__(self):
      super(GridWindow, self).__init__()

      grid = Gtk.Grid()
      self.add(grid)

      # Create 6 buttons
      button1 = Gtk.Button(label = "bt 1")
      button2 = Gtk.Button(label = "bt 2")
      button3 = Gtk.Button(label = "bt 3")
      button4 = Gtk.Button(label = "bt 4")
      button5 = Gtk.Button(label = "bt 5")
      button6 = Gtk.Button(label = "bt 6")

      grid.add(button1)  # default : top left

      grid.attach(
        child = button2,
        left = 1, # column 2
        top = 0, # first row
        width = 2, # "columnspan" # twice as wide
        height = 1, # "rowspan"   # once  as tall
      )
      grid.attach_next_to(
        child = button3,
        sibling = button1,
        side = Gtk.PositionType.BOTTOM,
        width = 1,
        height = 2
      )
      grid.attach(button4, 1, 1, 1, 1)
      grid.attach(button5, 2, 1, 1, 1)
      grid.attach(button6, 1, 2, 2, 1)

  window = GridWindow()

  window.connect("delete-event", Gtk.main_quit)
  window.show_all()

  window.move(100, 100)

  Gtk.main()

"""
next = https://www.youtube.com/watch?v=EwoF6jErb9w
"""

def list_demo():
  from gi.repository import Gtk
  
  class ListWindow(Gtk.Window):
    """ListWindow"""
    def __init__(self):
      super(ListWindow, self).__init__(
        title = "My List Window"
      )

      self.set_border_width(10)
      
      listbox = Gtk.ListBox()
      listbox.set_selection_mode(Gtk.SelectionMode.NONE) # mouse cpy/pst
      self.add(listbox)

      # row
      row_1 = Gtk.ListBoxRow()

      # Checkbox Box
      box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
      row_1.add(box_1)
      
      # Checkbox
      label = Gtk.Label("Do Extra")
      check = Gtk.CheckButton()
      label.set_halign(Gtk.Align.START)
      check.set_halign(Gtk.Align.END)
      box_1.pack_start(label, True, True, 0)
      box_1.pack_start(check, True, True, 0)

      listbox.add(row_1)

      # row
      row_2 = Gtk.ListBoxRow()

      # ToggleSwitch Box
      box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
      row_2.add(box_2)
      
      # ToggleSwitch
      label = Gtk.Label("On/Off")
      switch = Gtk.Switch()
      label.set_halign(Gtk.Align.START)
      switch.set_halign(Gtk.Align.END)
      box_2.pack_start(label, True, True, 0)
      box_2.pack_start(switch, True, True, 0)

      listbox.add(row_2)

  window = ListWindow()
  window.connect("delete-event", Gtk.main_quit)
  window.move(100, 100)
  window.show_all()



  Gtk.main() 

def stack_switcher_demo():
  from gi.repository import Gtk

  class StackWindow(Gtk.Window):
    """docstring for StackWindow"""
    def __init__(self):
      super(StackWindow, self).__init__(title = "Stack Demo")

      self.set_border_width(10)

      box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
      self.add(box)

      # Stack (main area)
      main_area = Gtk.Stack()
      main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
      main_area.set_transition_duration(300)

      # Stack page 1
      listbox = Gtk.ListBox()
      listbox.set_selection_mode(Gtk.SelectionMode.NONE) # mouse cpy/pst
      main_area.add_titled(listbox, "List_box_stack_frame", "List Box")

      # row
      row_1 = Gtk.ListBoxRow()

      # Checkbox Box
      box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
      row_1.add(box_1)
      
      # Checkbox
      label = Gtk.Label("Do Extra")
      check = Gtk.CheckButton()
      label.set_halign(Gtk.Align.START)
      check.set_halign(Gtk.Align.END)
      box_1.pack_start(label, True, True, 0)
      box_1.pack_start(check, True, True, 0)

      listbox.add(row_1)

      # row
      row_2 = Gtk.ListBoxRow()

      # ToggleSwitch Box
      box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
      row_2.add(box_2)
      
      # ToggleSwitch
      label = Gtk.Label("On/Off")
      switch = Gtk.Switch()
      label.set_halign(Gtk.Align.START)
      switch.set_halign(Gtk.Align.END)
      box_2.pack_start(label, True, True, 0)
      box_2.pack_start(switch, True, True, 0)

      listbox.add(row_2)

      # Stack page 2
      label = Gtk.Label()
      # label.set_label()
      label.set_markup("<big>OMG BIG</big>")
      main_area.add_titled(label, "label_name", "Big Label")

      # Stack Switcher
      stack_switcher = Gtk.StackSwitcher()
      stack_switcher.set_stack(main_area)

      box.pack_start(stack_switcher, True, True, 0)
      box.pack_start(main_area, True, True, 0)




  window = StackWindow()
  window.connect("delete-event", Gtk.main_quit)
  window.move(100, 100)
  window.show_all()



  Gtk.main() 

if __name__ == '__main__':
  # box_demo()
  # button_demo()
  # grid_demo()
  # list_demo()
  stack_switcher_demo()
