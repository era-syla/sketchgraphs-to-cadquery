import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00635, 0.01613).lineTo(0.01905, 0.01613).threePointArc((0.0213, 0.0152), (0.02223, 0.01295)).lineTo(0.00318, 0.01295).threePointArc((0.0041, 0.0152), (0.00635, 0.01613)).close()
solid=wp_sketch0.add(loop0).extrude(-0.03584300108143957)
