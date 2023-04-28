from electric.logic_gate import LogicGate


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
        result = []
        for index, cur_gate in enumerate(self.input_gates):

            # input gate is a connector, calculate how many gates it uses
            if isinstance(cur_gate, Connector):
                count = self.logical_inputs_count(cur_gate)
                result.append(cur_gate.send_inputs(inputs[:count]))
                inputs = inputs[count:]

            # input gate is a binary.
            elif cur_gate.__name__ in ['OrGate', 'AndGate', 'NandGate', 'XorGate']:
                result.append(cur_gate.output(inputs[0], inputs[1]))
                inputs = inputs[2:]

            # input gate is a unary.
            else:
                result.append(cur_gate.output(inputs[0]))
                inputs = inputs[1:]

        # return the list of output values
        return result

    def logical_inputs_count(self, current):
        """
           Counts the number of logical inputs used in a logic circuit (Connector).

           Args:
               current: The current gate or connector being processed.

           Returns:
               The number of logical inputs used in the circuit.

           """
        if not current:
            return 0

        # current is a gate
        if not isinstance(current, (Connector, list)):
            if current.__name__ == 'NotGate':
                return 1
            else:
                return 2

        # current is a connector
        if isinstance(current, list):
            return self.logical_inputs_count(current[0]) + self.logical_inputs_count(current[1:])
        else:
            return current.logical_inputs_count(current.input_gates[0]) + current.logical_inputs_count(
                current.input_gates[1:])
