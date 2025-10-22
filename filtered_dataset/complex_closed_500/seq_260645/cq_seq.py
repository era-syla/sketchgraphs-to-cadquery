import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03, 0.04).lineTo(0.02, 0.04).lineTo(0.02, -0.04).lineTo(0.03, -0.04).lineTo(0.03, -0.035).lineTo(0.06, -0.035).lineTo(0.06, -0.02499).threePointArc((0.0466, -0.0), (0.06, 0.02499)).lineTo(0.06, 0.035).lineTo(0.03, 0.035).lineTo(0.03, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.06546333177785592)
