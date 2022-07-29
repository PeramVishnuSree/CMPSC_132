 

    def __delitem__(self, value):
        self._deleteHelper(None, self.root, value)
        return self.printInorder
    

    def _deleteHelper(self, parent, current, value):
        if current is None:
            return None 
        if current.value>value:
            _____________________________________________ #[1]
        elif current.value<value:
            _____________________________________________ #[2]
        else:

            node_children=self.numChildren(current)

            if node_children==0 or node_children==1:

                if current.left is not None:
                    child = ______________________ #[3]
                else:
                    child = ______________________ #[4]


                if (parent is not None) and (parent.left is current):

                    _____________________________________________ #[5]
                elif (parent is not None) and (parent.right is current):
                    _____________________________________________ #[6]
                else:
                    _____________________________________________ #[7]
            else:

                temp = current.right
                parent = current
                while temp.left is not None: 
                    _____________________________________________ #[8]
                    _____________________________________________ #[9]

                current.value=_____________________________________________ #[10]
                self._deleteHelper(______________, _____________, _____________) #[11]
    
