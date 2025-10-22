import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.2921).lineTo(0.0889, 0.2921).lineTo(0.0889, 0.1016).lineTo(0.0, 0.1016).lineTo(0.0, 0.2921).close()
solid=wp_sketch0.add(loop0).extrude(0.44267351992642956)
