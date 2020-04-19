#!/usr/bin/env python3

import json
import subprocess

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main


class RoutinesCharm(CharmBase):
    state = StoredState()

    def __init__(self, framework, parent):
        super().__init__(framework, parent)

        framework.observe(self.on.install, self)
        framework.observe(self.on.upgrade_charm, self)
        framework.observe(self.on.run_action, self)

    def on_install(self, event):
        pass

    def on_upgrade_charm(self, event):
        pass

    def on_config_changed(self, event):
        pass

    def on_run_action(self, event):
        routine_param = event.params["routine"]
        routines = json.loads(self.framework.model.config["routines"])

        event.log("Action triggered: {}".format(routine_param))
        try:
            action = routines[routine_param]
        except KeyError:
            event.fail("No action '{}' configured".format(routine_param))
            return
        event.log("Command to be executed: {}".format(action))

        subprocess.run(action.split())


if __name__ == '__main__':
    main(RoutinesCharm)
