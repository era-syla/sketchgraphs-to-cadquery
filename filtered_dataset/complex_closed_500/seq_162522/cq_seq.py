import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.05775).threePointArc((0.04022, 0.04022), (0.05775, 0.0)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.11868934418635632)
