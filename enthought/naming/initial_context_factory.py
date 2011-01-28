#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought naming package component>
#------------------------------------------------------------------------------
""" The base class for all initial context factories. """


# Enthought library imports.
from enthought.traits.api import HasTraits

# Local imports.
from context import Context


class InitialContextFactory(HasTraits):
    """ The base class for all initial context factories. """

    ###########################################################################
    # 'InitialContextFactory' interface.
    ###########################################################################

    def get_initial_context(self, environment):
        """ Creates an initial context for beginning name resolution. """

        return Context(environment=environment)

#### EOF ######################################################################
