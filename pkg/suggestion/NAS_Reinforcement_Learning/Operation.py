import itertools
import numpy as np


class Operation(object):
    def __init__(self, opt_id, opt_type, opt_params):
        self.opt_id = opt_id
        self.opt_type = opt_type
        self.opt_params = opt_params

    def print_op(self):
        print("Operation ID: \n\t", self.opt_id)
        print("Operation Type: \n\t", self.opt_type)
        print("Operations Parameters:")
        for ikey in self.opt_params:
            print("\t {}: {}".format(ikey, self.opt_params[ikey]))


class SearchSpace(object):
    def __init__(self, operation_list):
        self.operation_list = operation_list
        self.search_space = list()
        self._parse_operations()
        self.num_operations = len(self.search_space)

    def _parse_operations(self):
        # search_sapce is a list of Operation class

        operation_id = 0

        for operation_dict in self.operation_list:
            opt_type = operation_dict['operationtype']
            opt_spec = operation_dict['spec']
            # avail_space is dict with the format {"spec_nam": [spec feasible values]}
            avail_space = dict()
            avail_space_len = list()
            num_spec = len(opt_spec)

            for ispec in opt_spec:
                spec_name = ispec['name']
                if ispec['parametertype'] == 'categorical':
                    avail_space[spec_name] = ispec['feasible']['list']
                elif ispec['parametertype'] == 'int':
                    spec_min = int(ispec['feasible']['min'])
                    spec_max = int(ispec['feasible']['max'])
                    avail_space[spec_name] = range(int(spec_min)-1, int(spec_max))
                elif ispec['parametertype'] == 'range':
                    spec_min = float(ispec['feasible']['min'])
                    spec_max = float(ispec['feasible']['max'])
                    spec_step = float(ispec['feasible']['step'])
                    avail_space[spec_name] = np.arange(spec_min - spec_step, spec_max, spec_step)

                avail_space_len.append(len(avail_space[spec_name]))

            # generate all the combinations of possible operations
            key_avail_space = list(avail_space.keys())
            val_avail_space = list(avail_space.values())

            for this_opt_vector in itertools.product(*val_avail_space):
                opt_params = dict()
                for i in range(num_spec):
                    opt_params[key_avail_space[i]] = this_opt_vector[i]
                this_opt_class = Operation(operation_id, opt_type, opt_params)
                self.search_space.append(this_opt_class)
                operation_id += 1







