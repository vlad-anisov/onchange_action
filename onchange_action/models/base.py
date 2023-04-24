import logging
from odoo import models, _

_logger = logging.getLogger(__name__)


class Base(models.AbstractModel):
    _inherit = "base"

    def _onchange_eval(self, field_name, onchange, result):
        """
        OVERWRITE
        Added a return of action
        """
        onchange = onchange.strip()

        def process(res):
            if not res:
                return
            if res.get("value"):
                res["value"].pop("id", None)
                self.update({key: val for key, val in res["value"].items() if key in self._fields})
            if res.get("domain"):
                _logger.warning("onchange method %s returned a domain, this is deprecated", method.__qualname__)
                result.setdefault("domain", {}).update(res["domain"])
            if res.get("warning"):
                result["warnings"].add(
                    (
                        res["warning"].get("title") or _("Warning"),
                        res["warning"].get("message") or "",
                        res["warning"].get("type") or "",
                    )
                )
            if res.get("action"):
                result["action"] = res.get("action")
        if onchange in ("1", "true"):
            for method in self._onchange_methods.get(field_name, ()):
                method_res = method(self)
                process(method_res)
            return
