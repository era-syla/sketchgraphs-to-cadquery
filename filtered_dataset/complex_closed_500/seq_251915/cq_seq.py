import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02, 0.03122).lineTo(0.00223, 0.03389).threePointArc((-0.0, 0.03405), (-0.00223, 0.03389)).lineTo(-0.02, 0.03122).lineTo(0.02, 0.03122).close()
solid=wp_sketch0.add(loop0).extrude(0.08800953903574996)
