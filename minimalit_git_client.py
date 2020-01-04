import gi
import git
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler(Gtk.Window):

    _path_selected = ""
    _repo_obj = None

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

            Handler._path_selected = dialog.get_filename()
            Handler._repo_obj = git.Repo.init(Handler._path_selected)

        elif response == Gtk.ResponseType.CANCEL:

            pass

        dialog.destroy()

    def add_file_repository_clicked(self, button):

        Handler._repo_obj.git.add(all = True)

builder = Gtk.Builder()
builder.add_from_file("minimalist_git_client_ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()