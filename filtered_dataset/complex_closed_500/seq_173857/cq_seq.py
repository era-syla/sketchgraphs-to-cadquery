import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.13494, 0.00295).lineTo(0.16846, 0.00295).threePointArc((0.16588, 0.00552), (0.16846, 0.00809)).lineTo(0.13494, 0.00809).threePointArc((0.13237, 0.00552), (0.13494, 0.00295)).close()
solid=wp_sketch0.add(loop0).extrude(-0.07304943494425656)
