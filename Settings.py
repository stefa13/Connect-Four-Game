from exceptions import SettingsException

class Settings:
    def __init__(self, filename):
        self._filename = filename
        self._load_settings()

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        raise SettingsException(f"No valid '{key}' property was found.")

    def _load_settings(self):
        self._data = {}
        with open(self._filename, "r") as f:
            lines = f.read().split('\n')
            for line in lines:
                if len(line) == 0 or line[0] == '#':
                    continue
                params = line.replace('\"', '').split("=")
                for i in range(len(params)):
                    params[i] = params[i].strip()
                if len(params) != 2:
                    continue
                self._data[params[0]] = params[1]