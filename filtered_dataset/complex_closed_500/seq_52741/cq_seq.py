import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.338, -0.05).lineTo(0.062, -0.05).threePointArc((0.05351, -0.04649), (0.05, -0.038)).lineTo(0.05, 0.038).threePointArc((0.05351, 0.04649), (0.062, 0.05)).lineTo(0.338, 0.05).threePointArc((0.34649, 0.04649), (0.35, 0.038)).lineTo(0.35, -0.038).threePointArc((0.34649, -0.04649), (0.338, -0.05)).close()
solid=wp_sketch0.add(loop0).extrude(-0.34964159423051877)
