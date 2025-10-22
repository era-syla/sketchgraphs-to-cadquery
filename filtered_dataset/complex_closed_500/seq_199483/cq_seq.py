import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0775, 0.03496).lineTo(0.0775, 0.02996).lineTo(0.0825, 0.02996).threePointArc((0.08104, 0.0335), (0.0775, 0.03496)).close()
solid=wp_sketch0.add(loop0).extrude(-0.012310317005907793)
