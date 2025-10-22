import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0762, 0.1016).lineTo(0.05786, 0.1016).lineTo(0.05786, -0.1016).lineTo(0.0762, -0.1016).lineTo(0.0762, 0.1016).close()
solid=wp_sketch0.add(loop0).extrude(0.23516255719502902)
