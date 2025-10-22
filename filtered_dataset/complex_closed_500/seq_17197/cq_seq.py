import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.02816).lineTo(0.01143, 0.02816).threePointArc((0.01749, 0.03067), (0.02, 0.03672)).lineTo(0.02, 0.03759).threePointArc((0.01749, 0.04365), (0.01143, 0.04616)).lineTo(-0.0, 0.04616).lineTo(0.0, 0.02816).close()
solid=wp_sketch0.add(loop0).extrude(-0.004385594829300672)
