import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(148.2881, -1.79325).lineTo(156.30173, 2.57781).lineTo(170.10699, 5.74683).lineTo(169.08708, -3.06815).lineTo(148.2881, -1.79325).close()
solid=wp_sketch0.add(loop0).extrude(-58.468798172185146)
