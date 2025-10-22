import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.075).lineTo(0.003, 0.075).threePointArc((0.00512, 0.07412), (0.006, 0.072)).lineTo(0.006, 0.013).threePointArc((0.00805, 0.00805), (0.013, 0.006)).lineTo(0.047, 0.006).threePointArc((0.04912, 0.00512), (0.05, 0.003)).lineTo(0.05, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.18105994958530494)
