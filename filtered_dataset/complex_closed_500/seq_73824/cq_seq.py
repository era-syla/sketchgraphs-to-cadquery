import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, -35.0).threePointArc((35.0, 0.0), (-0.0, 35.0)).lineTo(0.0, -35.0).close()
solid=wp_sketch0.add(loop0).extrude(-180.14742668021285)
