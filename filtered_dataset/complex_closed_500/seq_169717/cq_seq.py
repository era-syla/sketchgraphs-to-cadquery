import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04128, 0.0127).lineTo(0.04569, 0.03771).lineTo(0.05204, 0.03771).lineTo(0.04763, 0.0127).threePointArc((0.04499, 0.00898), (0.04128, 0.00635)).lineTo(0.04128, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.041819650208840216)
