
class Connector:
    """
      Connects input gates to a gate that computes a logic operation.

      Attributes:
          gate (LogicGate): The gate that computes a logic operation.
          input_gates (list): The input gates connected to the gate.

      Methods:
          send_inputs: Computes the output of the gate given the inputs.
          calculate_output: Calculates the output of each input gate.
          count_gates: Counts the number of gates in a Connector or list of Connectors.

      """
    def __init__(self, gate, input_gates):
        self.gate = gate
        self.input_gates = input_gates

    def send_inputs(self, inputs):
        """
        Computes the output of the gate given the inputs.

        Args:
            inputs (list): The input values for the gate.

        Returns:
            The output value of the gate.
        """
        return self.gate.output(*self.calculate_input_gates_outputs(inputs))

    def calculate_input_gates_outputs(self, inputs):
        """
         Calculates the output from the input gates of the connector.

         Args:
             inputs (list): The logical input values to the input gates of the connector.

         Returns:
             A list containing the output values from the input gates.
         """
        res = []
        for i, cur_gate in enumerate(self.input_gates):

            # if the input gate is a connector, recursively calculate the output from its input gates
            if isinstance(cur_gate, Connector):
                # count the number of input values needed for the connector
                count = self.logical_inputs_count(cur_gate)
                # calculate the output from the connector's input gates
                res.append(cur_gate.send_inputs(inputs[:count]))
                # remove the used input values from the list
                inputs = inputs[count:]

            # if the input gate is a binary gate, calculate its output using two input values
            elif cur_gate.__name__ in ['OrGate', 'AndGate', 'NandGate', 'XorGate']:
                res.append(cur_gate.output(inputs[0],inputs[1]))
                inputs = inputs[2:]

            # if the input gate is a unary gate, calculate its output using one input value
            else:
                res.append(cur_gate.output(inputs[0]))
                inputs = inputs[1:]

        # return the list of output values
        return res

    def logical_inputs_count(self, current):
        """
           Counts the number of logical inputs used in a logic circuit (Connector).

           Args:
               current: The current gate or connector being processed.

           Returns:
               The number of logical inputs used in the circuit.

           """
        # Base case: if there are no more gates to process, return 0
        if not current:
            return 0

        # If the current element is not a connector or a list of connectors/gates, it must be a gate
        if not isinstance(current, (Connector,list)) :
            if current.__name__  == 'NotGate':
                return 1
            else:
                return 2

        # If the current element is a list of connectors/gates, recurse through each element
        if isinstance(current,list):
            return self.logical_inputs_count(current[0]) + self.logical_inputs_count(current[1:])

        # If the current element is a connector, recurse through each input gate
        else:
            return current.logical_inputs_count(current.input_gates[0]) + current.logical_inputs_count(current.input_gates[1:])



