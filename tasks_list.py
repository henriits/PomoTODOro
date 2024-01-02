from PyQt6.QtWidgets import QListWidget, QListWidgetItem

from task_widget import TaskWidget


class TasksList(QListWidget):
    def add_task(self, task_text):
        if task_text:
            task_widget = TaskWidget(task_text)
            item = QListWidgetItem()
            item.setSizeHint(task_widget.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, task_widget)

    def remove_checked_tasks(self):
        for i in reversed(range(self.count())):
            item = self.item(i)
            task_widget = self.itemWidget(item)
            if isinstance(task_widget, TaskWidget) and task_widget.isChecked():
                self.takeItem(i)
