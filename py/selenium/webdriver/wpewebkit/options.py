# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import typing

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.options import ArgOptions


class Options(ArgOptions):
    KEY = "wpe:browserOptions"

    def __init__(self) -> None:
        super().__init__()
        self._binary_location = ""
        self._taget_address = None

    @property
    def binary_location(self) -> str:
        """Returns the location of the browser binary otherwise an empty
        string."""
        return self._binary_location

    @binary_location.setter
    def binary_location(self, value: str) -> None:
        """Allows you to set the browser binary to launch.

        :Args:
         - value : path to the browser binary
        """
        if not isinstance(value, str):
            raise TypeError(self.BINARY_LOCATION_ERROR)
        self._binary_location = value

    property
    def taget_address(self) -> str:
        """:Returns: The address of the remote inspector instance."""
        return self._taget_address

    @taget_address.setter
    def taget_address(self, value: str) -> None:
        """Allows you to set the address of the remote inspector instance that
        the WPEWebDriver instance will try to connect to during an active wait.

        :Args:
         - value: address of remote inspector instance if any (hostname[:port])
        """
        if not isinstance(value, str):
            raise TypeError("Target Address must be a string")
        self._taget_address = value

    def to_capabilities(self):
        """Creates a capabilities with all the options that have been set and
        returns a dictionary with everything."""
        caps = self._caps

        browser_options = {}
        if self.binary_location:
            browser_options["binary"] = self.binary_location
        if self.arguments:
            browser_options["args"] = self.arguments
        if self.taget_address:
            browser_options["targetAddress"] = self.taget_address

        caps[Options.KEY] = browser_options

        return caps

    @property
    def default_capabilities(self) -> typing.Dict[str, str]:
        return DesiredCapabilities.WPEWEBKIT.copy()
