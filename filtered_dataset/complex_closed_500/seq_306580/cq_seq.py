import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04031, 0.0).lineTo(-0.0163, 0.0).lineTo(-0.0163, 0.03289).lineTo(-0.04031, 0.03289).lineTo(-0.04031, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.07157096624285426)
