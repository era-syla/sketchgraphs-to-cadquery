import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.007, 0.00802).threePointArc((0.0, 0.00752), (0.007, 0.00802)).lineTo(-0.007, 0.00802).close()
solid=wp_sketch0.add(loop0).extrude(-0.017882403710628072)
