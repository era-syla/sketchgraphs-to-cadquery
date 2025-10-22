import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0125, -0.045).lineTo(0.0125, -0.045).lineTo(0.0125, 0.045).threePointArc((0.0, 0.04869), (-0.0125, 0.045)).lineTo(-0.0125, -0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.23402411301376477)
