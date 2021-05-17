from ansible.plugins.inventory import BaseInventoryPlugin

ANSIBLE_METADATA = {
    'metadata_version': '',
    'status': [],
    'supported_by': ''
}

DOCUMENTATION = """
    ---
    module: 'devizo.csv_inventory'
    plugin_type: 'inventory'
    short_description: 'Parse CSV file as host inventory'
    description: 'Parse CSV file as host inventory'
    author: 'Douglas J. Renze'
    version_added: ''
    options:
"""


class InventoryModule(BaseInventoryPlugin):
    """Parse CSV file as host inventory"""

    NAME = "devizo.csv_inventory"

    def verify_file(self, path):
        """Verify that the source file can be processed correctly.

        Args:
            path (str): The path to the file that needs to be verified

        Returns:
            bool: True if the file is valid, else False
        """


    def parse(self, inventory, loader, path, cache=True):
        """Parse and populate the inventory with data about hosts.

        Parameters:
            inventory (str): The inventory to populate
        """
        
        # The following invocation supports Python 2 in case we are
        # still relying on it. Use the more convenient, pure Python 3 syntax
        # if you don't need it.
        super(InventoryModule, self).parse(inventory, loader, path, cache)


    def _sanitize_string(self, s):
        """Sanitize string
        
        Sanitize strings, converting to all-lowercase and replacing all
        non-alphanumeric characters with `_`.
        
        Args:
            s (str): String to sanitize.
            
        Returns:
            str: Sanitized string.
            
        """
        
        return ''.join([c if c.isalnum() else '_' for c in s]).lower()


    def _sanitized_csv(self, infile: str) -> dict:
        with open(infile, 'r') as f:
            for r in csv.DictReader(f):
                yield {self._sanitize_string(k): v for k, v in r.items()}
