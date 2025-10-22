import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00889, 0.0762).lineTo(0.00889, 0.06131).threePointArc((0.00916, 0.05719), (0.00996, 0.05313)).lineTo(0.01798, 0.02307).threePointArc((0.01878, 0.01901), (0.01905, 0.01489)).lineTo(0.01905, 0.0).lineTo(0.02025, 0.0).lineTo(0.02025, 0.01489).threePointArc((0.01998, 0.01901), (0.01918, 0.02307)).lineTo(0.01116, 0.05313).threePointArc((0.01036, 0.05719), (0.01009, 0.06131)).lineTo(0.01009, 0.0762).lineTo(0.00889, 0.0762).close()
solid=wp_sketch0.add(loop0).extrude(0.09527958015817242)
