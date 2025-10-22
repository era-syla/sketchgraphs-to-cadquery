import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.026, 0.0).threePointArc((0.03166, 0.00234), (0.034, 0.008)).lineTo(0.034, 0.042).threePointArc((0.03166, 0.04766), (0.026, 0.05)).lineTo(-0.0, 0.05).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.01397592957425228)
