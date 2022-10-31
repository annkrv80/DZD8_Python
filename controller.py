import view
import model


def run():
    start = view.show_menu()
    if start == 1:
        res = model.data_open()
        view.show_data(res)
    elif start == 2:
        in_info = view.add_info()
        model.add_info(in_info)
    elif start == 3:
        res = model.data_open()
        view.show_data(res)
        index = view.del_note()
        model.del_info(index)
    elif start == 4:
        res = model.data_open()
        view.show_data(res)
        index, tel = view.change_tel()
        model.update_info(index, tel)
    elif start == 5:
        model.inport_export()
