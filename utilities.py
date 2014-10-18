import io
import os
import sys

from IPython.nbformat import current

def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = current.read(f, 'json')
        if merged is None:
            merged = nb
        else:
            merged.worksheets[0].cells.extend(nb.worksheets[0].cells)
    merged.metadata.name += "_merged"
    print current.writes(merged, 'json')

#if __name__ == '__main__':
 #   merge_notebooks(sys.argv[1:])


class TableFigureCounter:
    def __init__(self, current_tab =-1, current_fig=-1):
        if current_tab == -1:
            self.tab_count = 0
        else:
            self.tab_count = current_tab
        if current_fig == -1:
            self.fig_count = 0
        else:     
            self.fig_count = current_fig
    def get_next_tab(self, chapter=None):
        self.tab_count = self.tab_count + 1
        return 'Table ' + str(chapter) + '.' + str(self.tab_count)        
    def get_next_fig(self, chapter=None):
        self.fig_count = self.fig_count + 1
        return 'Figure ' + str(chapter) + '.' + str(self.fig_count)
    def reset(self):
        self.tab_count = 0
        self.fig_count = 0