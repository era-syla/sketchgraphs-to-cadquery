import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0055, 0.012).threePointArc((0.012, 0.0185), (0.0185, 0.012)).lineTo(0.0213, 0.012).threePointArc((0.012, 0.0213), (0.0027, 0.012)).lineTo(0.0055, 0.012).close()
solid=wp_sketch0.add(loop0).extrude(-0.022859733465102526)
