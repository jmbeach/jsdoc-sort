import vim
import re;

class JsdocSorter(object):
    def __init__(self, vim):
        self._vim = vim

    def parse_doc(self, i):
        properties = {}
        params = {}
        typedef = None
        start_i = i
        while True:
            line = self._vim.current.buffer[i]
            stripped = line.strip()
            property_param_match = re.search('@(property|param)( [{].*[}] )([a-zA-Z0-9]+)', stripped)
            if stripped == '*/':
                sorted_properties = sorted(properties.keys())
                sorted_params = sorted(params.keys())
                current_line = start_i
                if typedef is not None:
                    self._vim.current.buffer[current_line] = typedef
                    current_line += 1
                
                for key in sorted_properties:
                    current = properties[key]
                    self._vim.current.buffer[current_line] = current
                    current_line += 1
                
                for key in sorted_params:
                    current = params[key]
                    self._vim.current.buffer[current_line] = current
                    current_line += 1

                return
            if '@typedef' in stripped:
                typedef = line
            elif property_param_match is not None:
                prop_or_param = property_param_match.groups(0)[0]
                name = property_param_match.groups(0)[2]
                if prop_or_param == 'property':
                    properties[name] = line
                else:
                    params[name] = line
            i += 1

    def sort(self):
        for i in range(0, len(self._vim.current.buffer)):
            line = self._vim.current.buffer[i]
            if '/**' == line.strip():
                self.parse_doc(i + 1)

JsdocSorter(vim).sort()
