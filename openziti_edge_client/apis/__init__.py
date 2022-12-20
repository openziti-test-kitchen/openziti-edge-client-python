
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from openziti_edge_client.api.authentication_api import AuthenticationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openziti_edge_client.api.authentication_api import AuthenticationApi
from openziti_edge_client.api.current_api_session_api import CurrentAPISessionApi
from openziti_edge_client.api.current_identity_api import CurrentIdentityApi
from openziti_edge_client.api.edge_router_api import EdgeRouterApi
from openziti_edge_client.api.enroll_api import EnrollApi
from openziti_edge_client.api.extend_enrollment_api import ExtendEnrollmentApi
from openziti_edge_client.api.external_jwt_signer_api import ExternalJWTSignerApi
from openziti_edge_client.api.informational_api import InformationalApi
from openziti_edge_client.api.mfa_api import MFAApi
from openziti_edge_client.api.posture_checks_api import PostureChecksApi
from openziti_edge_client.api.service_api import ServiceApi
from openziti_edge_client.api.services_api import ServicesApi
from openziti_edge_client.api.session_api import SessionApi
from openziti_edge_client.api.well_known_api import WellKnownApi
