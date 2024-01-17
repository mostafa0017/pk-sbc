# Connecting an IPBX to more than one operator

In order to save money on subscriptions and telephone communications, it may be advisable to use different operators depending on the destinations or numbers required, particularly for international calls. P-KISS-SBC makes it possible to connect several operators to an IPBX and to route incoming calls to the IPBX, whatever the original operator, and to route outgoing calls to the desired operator. Although it is possible to connect several operators directly to an IPBX, it is complex to route calls to the desired operator while integrating a failover function. P-KISS-SBC incorporates a function that allows you to attempt to route the call to a preferred operator and, if this fails, to attempt to terminate the call on a second operator.

SIP PROVIDER 1
              ===== P-KISS-SBC ==== IPBX
SIP PROVIDER 2                            
