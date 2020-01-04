import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler(Gtk.Window):

    def onDestroy(self, *args):
        Gtk.main_quit()

    def init_repository_clicked(self, button):

        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_file_repository_clicked(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("minimalist_git_client_ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()