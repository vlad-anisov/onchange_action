
Onchange actions
=====

This module allows you to return an action (``ir.actions.*``) from an onchange handler.

This way, you can have much more elaborate message boxes or simply show a whole wizard or do whatever else is possible with actions on the client side.

Usage
=====

Depend on this module and in your onchange handler, add a key ``action`` to the dictionary of the result which contains the definition of an action to execute:

```python

    {
        'value': ....,
        'domain': ....,
        'action': {
            'type': 'ir.actions.act_window',
            'res_model': 'my.wizard',
            ...
        },
    }
```
