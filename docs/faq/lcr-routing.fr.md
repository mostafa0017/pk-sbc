<!---
# P-KISS-SBC documentation © 2007-2024 by Mathias WOLFF 
# is licensed under Attribution-NonCommercial-ShareAlike 4.0 International (see https://creativecommons.org/licenses/by-nc-sa/4.0/)
# SPDX-License-Identifier: CC-BY-NC-SA-4.0
--->

# Est-ce que PKS fait du Least Cost Routing (LCR) ?

PKS ne sait pas faire du routage des appels basés sur les coûts de communications des fournisseurs SIP. Cette fonctionnalité présente dans PyFreeBilling a été supprimée, car elle apportée une plus grande complexité, à la fois dans la partie scripting et donc du debug mais aussi au niveau de l'administration.

Si cette fonctionnalité est nécessaire, d'autres solutions seront alors plus adaptées.

Néanmoins, une [discussion](https://github.com/mwolff44/pyfreebilling/discussions/186) existe sur le forum afin d'intégrer [CGRateS](http://www.cgrates.org/).
