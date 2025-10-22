import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.04763).threePointArc((0.04763, 0.0), (0.0, 0.04763)).lineTo(0.0, -0.04763).close()
solid=wp_sketch0.add(loop0).extrude(0.11901502888808987)
