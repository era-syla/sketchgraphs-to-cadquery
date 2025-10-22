import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0035).lineTo(-0.0213, 0.0035).threePointArc((-0.026, 0.00236), (-0.03083, 0.00197)).lineTo(-0.03083, 0.00375).lineTo(-0.034, 0.00375).lineTo(-0.034, 0.0).lineTo(0.0, 0.0).lineTo(0.012, 0.0).lineTo(0.012, 0.0025).lineTo(0.0, 0.0025).lineTo(0.0, 0.0035).close()
solid=wp_sketch0.add(loop0).extrude(-0.025606165240701077)
