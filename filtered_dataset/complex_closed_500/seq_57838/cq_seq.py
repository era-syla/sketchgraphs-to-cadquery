import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1425, -0.065).lineTo(-0.1425, -0.065).threePointArc((-0.14604, -0.06354), (-0.1475, -0.06)).lineTo(-0.1475, 0.06).threePointArc((-0.14604, 0.06354), (-0.1425, 0.065)).lineTo(0.1425, 0.065).threePointArc((0.14604, 0.06354), (0.1475, 0.06)).lineTo(0.1475, -0.06).threePointArc((0.14604, -0.06354), (0.1425, -0.065)).close()
solid=wp_sketch0.add(loop0).extrude(-0.4714470683282886)
