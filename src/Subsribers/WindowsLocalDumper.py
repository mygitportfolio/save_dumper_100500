import errno
import shutil


class LocalDumper:
    @staticmethod
    def _copy(src, dest):
        try:
            shutil.copytree(src, dest)
        except OSError as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
            else:
                print('Directory not copied. Error: %s' % e)

    def dump_saves(self, state) -> None:
        self._copy(state['watched_dir'], state['dump_dir'])
